*Skills and projects covered in LLM and ChatGPT folders*:
<br>

## Section 1: *Large Language Models: Application through Production (EdX)*

## [LM1](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2001%20-%20LLMs%20with%20Hugging%20Face.ipynb)
Use Hugging Face datasets and large models; set up tokenizer config

## [LM2](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2002%20-%20Embeddings%2C%20Vector%20Databases%2C%20and%20Search.ipynb)
Build a **knowledge-based question answering / search system** 

 - Convert a dataset to vectors and save them in a vector library (FAISS) or database (Chroma)
 - Vectorize a query (with filters in it) and saved the output as *context*
 - Combine *context* with *original prompt* as new prompts to generate search results
 
 This module also has tutorials on [Pinecone](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2002a%20-%20Pinecone%20%5BOPTIONAL%5D.ipynb) and [Weaviate](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2002b%20-%20Weaviate%20%5BOPTIONAL%5D.ipynb)
 
## [LM3](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2003%20-%20Building%20LLM%20Chains.ipynb)
Build tree LLM-chain-based models
 - LLM1 moderates the comments generated by LLM2
 - Use LLM with LangChain agents (Wiki, Google, Python REPL) to do automatic data analyses
 - An LLM agent that allows user to have free chat with documents (e.g., Shakespeare's books)

## [LM4](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2004a%20-%20Fine-tuning%20LLMs.ipynb)
Fine-tune LLMs with Hugging Face, Tensorboard, and DeepSpeed (multiple GPU cluster support) on a traditional IMDB classification; evaluate summarization performance with NLTK and ROUGE

## [LM5](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2005%20-%20LLMs%20and%20Society.ipynb)
Hugging Face Disaggregator (for q quick demographic analysis) and evaluate (for toxicity), gender expression generation, and SHAP (for interpretability, i.e., token-level contribution for the final generated output)

## [LM6](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM%2006%20-%20LLMOps.ipynb)
MLOps of a sample model with MLFlow, focusing on model registeration, versioning, monitoring/performance Tracking, and pushing to the production
<br>

## Section 2: my fine-tuning practices:
- [use QLoRa and hf PEFT to tune GPT-neo model on casual language modeling](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Fine_tuning_GPT_neo_with_QLoRa_and_PEFT.ipynb)
- [use deepspeed to tune mpt model on instruction data](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Fine_tuning_instruction_LLM_with_deepspeed.ipynb)
- [use XTurning on LLaMA 7b on question answering](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/fine_tuning_LLaMA7b_lora_int8.ipynb)
<br>

## Section 3: *Generative AI and Large Language Models (Coursera)*
### [Lab1: prompt-engineering](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Lab_1_summarize_dialogue.ipynb)
### [Lab2: fine-tune with LoRA](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Lab_2_fine_tune_generative_ai_model.ipynb)
### [Lab3: reinforcement learning with human feedback (**RLHF-PPO & KL**)](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Lab_3_fine_tune_model_to_detoxify_summaries.ipynb)
<br>

## Section 4: *openai_api_ and prompt dev*
- [prompt engineering demos and guideline](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/openai_api/chatgpt_prompt_engineering_guideline.ipynb)
- [use of langchain, including prompt management, external agents, and evaluation tools](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/openai_api/langchain_chatgpt.ipynb)
- [**fine-tuning service on chatgpt with generated data from gpt4**](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/openai_api/fine-tuning%20chatgpt%20with%20gpt4%20generated%20data.ipynb)
- [A tutotial of AutoGen, a multi-agent LLM package](https://github.com/daywatch/LLM_and_ChatGPT/tree/main/openai_api/autogen)
<br>

## Section 5: *Foundation Models from the Ground Up (EdX)*
- [transformer algorithm in torch](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2001L%20-%20Transformer%20Architecture%20Lab.ipynb)
- [fine-tuning with LORA and PEFT](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2002L%20-%20LoRA%20with%20PEFT.ipynb)
- [fine-tuning with prompt-tuning and PEFT](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2002%20-%20Prompt%20Tuning%20with%20PEFT.ipynb)
- [quantization and deploylment](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2003%20-%20Deployment%20of%20LLMs.ipynb)
<br>

## Section 6: *Apply LLMOps using VetexAI(DeepLearningAI - GCP)*
[course notes](https://docs.google.com/document/d/1XGCWNAYrCKaxr6WF5YshBOhWf5r272hZjJtZ_soNGug/edit?usp=sharing)
- [L2: data ingestion using SQL and storage on GCP](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/vertexAI_LLMOps/vertexAI_L2_dataipynb)
- [L3: use kubeflow for automation orchestratian + fine-tuning on vetexAI with QLoRA](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/vertexAI_LLMOps/vertexAI_L3_automation.ipynb)
- [L4: make predictions and pull out metrics on safety scores, such as harassment and severity](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/vertexAI_LLMOps/vertexAI_L4_predictions_prompts_safety.ipynb)
<br>

## Section 7: *Azure AI APIs*
This section includes several cases of Azure AI services, including Azure OpenAI, AI Studio, Speech (TTS & STT), AI Search, Document Intelligence, Storage, Vision, Language Service (translation, sentiment analysis, lang detection, intent & entity), and Semantic Kernel (similar to LangChain)

### other resources
- A sample of my [reserach links](https://docs.google.com/document/d/1v62l0hC4MBPpnCHBsVGJ8Tr3KzCCpMx23fIqmA8hTak/edit?usp=sharing) on LLM topics working as an Applied Scientist (NLP), including latest model update, prompt engineering, practice on fine-tuning and alignment, literatures, and downstream tasks and so on
- [Fine-tuning huggingface LLMs on AWS SageMaker](https://github.com/huggingface/notebooks/blob/main/sagemaker/01_getting_started_pytorch/sagemaker-notebook.ipynb)
- [Fine_tuning huggingface LLMs within azureml](https://balabala76.medium.com/azure-machine-learning-fine-tuning-large-language-models-q-a-and-summarization-comparing-various-2cb8b9a1681)
<br>
	
