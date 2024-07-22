from langfuse import Langfuse
import os
from dotenv import load_dotenv
from langfuse.decorators import observe, langfuse_context
from groq import Groq
from PyPDF2 import PdfReader

load_dotenv()
SECRET_KEY = os.getenv('LANGFUSE_SECRET_KEY')
PUBLIC_KEY= os.getenv("LANGFUSE_PUBLIC_KEY")
GROQ_KEY = os.getenv("GROQ_API_KEY")

langfuse = Langfuse(
  secret_key= SECRET_KEY,
  public_key= PUBLIC_KEY,
  host="https://us.cloud.langfuse.com"
)
 
client = Groq(
    api_key=GROQ_KEY,
)

reader = PdfReader('esume.pdf')
page = reader.pages[0]

# extracting text from page
resume_text = page.extract_text()

test_prompt = f"""Extract the following information from this resume: Name, Email, Phone, LinkedIn. If any information is not found, use 'Not provided' as the value. Resume: {{resume_text}}"""

# register test_prompt
langfuse.create_prompt(
    name="entity extraction",
    prompt="""Extract the following information from this resume: Name, Email, Phone, LinkedIn. Format the output exactly as follows (include all fields even if information is not found):\nName: [name]\nEmail: [email]\nPhone: [phone]\nLinkedIn: [linkedin]\nIf any information is not found, use 'Not provided' as the value. 
Resume: {{resume_txt}}. Return the output in a list format, e.g., ["Name": TEXT, "Email": TEXT, ...].""",
    config={
        "model":"llama3-70b",
        "temperature": 0,
        "json_schema":{
            "main_character": "string (name of protagonist)",
            "key_content": "string (1 sentence)",
            "keywords": "array of strings",
            "genre": "string (genre of story)",
            "critic_review_comment": "string (write similar to a new york times critic)",
            "critic_score": "number (between 0 bad and 10 exceptional)"
        }
    },
    labels=["production"]
)

prompt = langfuse.get_prompt("entity extraction", version=2)

# Wrap LLM function with decorator
@observe(as_type="generation")
def groq_completion(**kwargs):
  # optional, extract some fields from kwargs
  kwargs_clone = kwargs.copy()
  #print(kwargs_clone)
  input = kwargs_clone.pop('messages', None)
  #print(input)
  model = kwargs_clone.pop('model', None)
  #print(model)
  #print("\n\n")
  langfuse_context.update_current_observation(
      input=str(input),
      model=model,
      metadata=kwargs_clone,
      prompt=prompt
  )
  # return result
  return client.chat.completions.create(**kwargs).choices[0].message.content

@observe()
def running_prompts():
  return groq_completion(
      messages=[
          {"role": "system", "content": "You are a professional career advisor."},
          {"role": "user","content": test_prompt}
      ],
      model="llama3-70b-8192",
  )

# create a dataset for testing
langfuse.create_dataset(
    name="testing_dataset",
    # optional description
    description="My first dataset",
    # optional metadata
    metadata={
        "author": "TL",
        "date": "2022-01-01",
        "type": "benchmark"
    }
)

langfuse.create_dataset_item(
    dataset_name="testing_dataset",
    # any python object or value, optional
    input={
        "text": "1+1=?"
    },
    # any python object or value, optional
    expected_output={
        "text": "2"
    },
    # metadata, optional
    #metadata={
    #    "model": "llama3",
    #}
)



def main():
    t =running_prompts()
    return t
 
for _ in range(5):
    main()


"""
  langfuse_context.update_current_trace(
    name=model,
    session_id="1234",
    user_id="5678",
    tags=["tag1", "tag2"],
    public=True,
    metadata=kwargs_clone
)
"""
