import logging
import os
import streamlit as st
import json
import streamlit as st
import streamlit_antd_components as sac
import re
from call_endpoint import *
from st_elements_and_styles import *
import traceback
import yaml
from databricks.sdk import WorkspaceClient
from history_and_feedback_management import *
from streamlit_feedback import streamlit_feedback
from streamlit_float import *
import datetime

# IMPORTANT: TURN ON FOR LOCAL DEV; NEED .env TO RUN LOCALLY
from dotenv import load_dotenv
load_dotenv()

serving_endpoint_index = os.getenv("SERVING_ENDPOINT_INDEX")
serving_endpoint_llm = os.getenv("SERVING_ENDPOINT_LLM")

with open("RAG_config.yaml") as file:
    rag_config = yaml.safe_load(file)

sys_prompt = rag_config["llm_config"]["llm_system_prompt_template"]
max_tokens = rag_config["llm_config"]["llm_parameters"]["max_tokens"]
k = rag_config["retriever_config"]["parameters"]["k"]
history_path = rag_config["history_file"]["path"]
host = os.getenv("HOST")
token = os.getenv("TOKEN")


w = WorkspaceClient()

with open('menu_list.json', 'r') as file:
    file_list = json.load(file)
file_list = [re.sub("/dbfs/FileStore/RAG/","",item) for item in file_list] # TO DO: call dbfs instead of local

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_user_info():
    headers = st.context.headers
    return dict(
        user_name=headers.get("X-Forwarded-Preferred-Username"),
        user_email=headers.get("X-Forwarded-Email"),
        user_id=headers.get("X-Forwarded-User"),
    )

user_info = get_user_info()

# Streamlit app
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

# # Set page configuration to wide mode
# st.set_page_config(
#     page_title="Chatbot App",
#     page_icon="🧱",
#     layout="wide",  # This makes the app use more screen width
#     initial_sidebar_state="collapsed"
# )

# Custom CSS to further adjust width and padding
st.markdown(whole_page_css, unsafe_allow_html=True)

# title_col, logo_col = st.columns([3, 1])

# with title_col:
st.title("Chatbot Assistant")
st.write("Welcome to BBYH constract chatbot")

# with logo_col:
#     # Align the image to the right and center vertically
#     st.markdown(logo_css, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Create a two-column layout
left_col, right_col = st.columns([3, 7])
left_col.float()

# Create an error placeholder in the right column
with right_col:
    error_placeholder = st.empty()

try:
    with left_col:
        
        float_init()
        # Now add all your content
        st.subheader("Contract filter")

        # # Convert URIs to tree structure
        tree_items = uris_to_tree_structure(file_list)

        selected_items = sac.tree(
                    items=tree_items,
                    label="Contracts",
                    format_func="title",
                    icon="document",  # Using folder icon instead of bell
                    width=500,
                    height=500,  # Reduced height to fit the content
                    open_all=True,
                    checkbox=True,
                    show_line=True,
                    key="subject_tree",
                )
            
        # Display selected items
        if selected_items:
            selected_item_cleaned = [item for item in selected_items if "." in item]
        else:
            selected_item_cleaned=None
            st.write("Don't forget to set up your filter before chat!")

        float_parent()


    # Right column - Chat interface
    with right_col:
        # Create a container with matching height

        st.subheader("Chat")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        # Create a container for the chat history
        chat_container = st.container()

        # create an error container for positioning
        error_container = st.container()

        # Initialize a conversation ID tracker
        if "current_conversation_id" not in st.session_state:
            st.session_state.current_conversation_id = generate_uuid()

        # Display chat messages from history on app rerun
        with chat_container:
            messages = st.session_state.messages
            for n,msg in enumerate(messages):
                # Skip feedback messages when displaying
                if msg["role"] == "user_feedback":
                    continue
                st.chat_message(msg["role"]).write(msg["content"])

                # Add feedback only after assistant messages (except intro)
                if msg["role"] == "assistant":
                    message_id = msg.get("id")
                    if message_id:  # Only add feedback if there's a valid ID

                        streamlit_feedback(
                            feedback_type="thumbs",
                            optional_text_label="Please provide extra information",
                            on_submit= lambda user_response: submit_feedback(user_response, message_id=message_id),
                            key=message_id,
                        )

        # Accept user input
        if prompt := st.chat_input("Please ask your question here"):

            conversation_id = st.session_state.current_conversation_id

            # Add user message to chat history
            st.session_state.messages.append({
                "role": "user", 
                "timestamp": datetime.datetime.now().isoformat(),
                "content": prompt,
                "id": conversation_id})

            # Display user message in chat message container
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(prompt)

                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    # Query the Databricks serving endpoint
                    try:
                        context,references = call_index_endpoint(w,serving_endpoint_index,prompt,k,selected_item_cleaned)
                        response = call_llm_endpoint(w,serving_endpoint_llm,context,sys_prompt,prompt,max_tokens)

                        if references != "NA" and response["is_relevant"] in ["YES","yes"] and response["answer"] != "":
                            ref_text = "\nReferences:\n"
                            i = 1
                            for ref in references:
                                ref_text += f"{i}. {ref[0]}, Page: {ref[1]} \n"
                                i += 1
                            final_answer = response["answer"] + "\n" + ref_text
                            st.write(final_answer + ref_text)

                            # Update session state
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "timestamp":datetime.datetime.now().isoformat(),
                                "content": final_answer,
                                "id": conversation_id
                            })
                        
                        else:
                            final_answer = response["answer"]
                            st.write(final_answer)

                            # Update session state
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "timestamp":datetime.datetime.now().isoformat(),
                                "content": final_answer,
                                "id": conversation_id
                            })
                            
                    except Exception as e:

                        with error_container:

                            st.error(f"Error querying model: {e}")

                # renew the conversation id for the next possible pair
                st.session_state.current_conversation_id = generate_uuid()

                # Save after every turn
                save_chat_history(st.session_state.messages,history_path,w)

                st.rerun()
        
        #logger.info(f"History {st.session_state}")
        #w.dbutils.fs.put(history_path, json.dumps(st.session_state.messages), overwrite=True)
        #logger.info(f'number ### {w.dbfs.exists("dbfs:/FileStore/RAG/test")}')


except Exception as e:
    # Any unhandled exception will end up here and be displayed only in the right column
    with error_placeholder:
        st.error(f"An error occurred: {str(e)}")
        st.code(traceback.format_exc())