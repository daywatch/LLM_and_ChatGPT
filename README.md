*Skills and projects covered in LLM and ChatGPT folders*:
<br>

## Section 1: *Large Language Models: Application through Production (EdX)*

## LM1
Use Hugging Face datasets and large models; set up tokenizer config

## LM2
Build a **knowledge-based question answering / search system** 

 - Convert a dataset to vectors and save them in a vector library (FAISS) or database (Chroma/Pinecone/Weaviate)
 - Vectorize a query (with filters in it) and saved the output as *context*
 - Combine *context* with *original prompt* as new prompts to generate search results
 
## LM3
Build tree LLM-chain-based models
 - LLM1 moderates the comments generated by LLM2
 - Use LLM with LangChain agents (Wiki, Google, Python REPL) to do automatic data analyses
 - An LLM agent that allows user to have free chat with documents (e.g., Shakespeare's books)

## LM4
Fine-tune LLMs with Hugging Face, Tensorboard, and DeepSpeed (multiple GPU cluster support) on a traditional IMDB classification; evaluate summarization performance with NLTK and ROUGE

## LM5
Hugging Face Disaggregator (for q quick demographic analysis) and evaluate (for toxicity), gender expression generation, and SHAP (for interpretability, i.e., token-level contribution for the final generated output)

## LM6
MLOps of a sample model with mlFlow 

## Section 2: my fine-tuning practices:
- [use QLoRa and hf PEFT to tune GPT-neo model on casual language modeling](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Fine_tuning_GPT_neo_with_QLoRa_and_PEFT.ipynb)
- [use deepspeed to tune mpt model on instruction data](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/Fine_tuning_instruction_LLM_with_deepspeed.ipynb)
- [use XTurning on LLaMA 7b on question answering](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/fine_tuning_LLaMA7b_lora_int8.ipynb)
<br>

## Section 3: *Generative AI and Large Language Models (Coursera)*
### Lab1: prompt-engineering
### Lab2: fine-tune with LoRA
### Lab3: reinforcement learning with human feedback (**RLHF-PPO & KL**) 
<br>

## Section 4: *openai_api_ and prompt dev*
- prompt engineering demos and guideline
- use of langchain, including prompt management, external agents, and evaluation tools
- **fine-tuning service on chatgpt with generated data from gpt4**
<br>

## Section 5: *Foundation Models from the Ground Up (EdX)*
- [transformer algorithm in torch] (https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2001L%20-%20Transformer%20Architecture%20Lab.ipynb)
- [fine-tuning with LORA and PEFT](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2002L%20-%20LoRA%20with%20PEFT.ipynb)
- [fine-tuning with prompt-tuning and PEFT](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2002%20-%20Prompt%20Tuning%20with%20PEFT.ipynb)
- [quantization and deploylment](https://github.com/daywatch/LLM_and_ChatGPT/blob/main/LLMs_course_and_practice/LLM2%2003%20-%20Deployment%20of%20LLMs.ipynb)

## Section 6: * Apply LLMOps using VetexAI(DeepLearningAI - GCP)*
[course notes](https://docs.google.com/document/d/1XGCWNAYrCKaxr6WF5YshBOhWf5r272hZjJtZ_soNGug/edit?usp=sharing)
- L2: data ingestion using SQL and storage on GCP
- L3: use kubeflow for automation orchestratian + fine-tuning on vetexAI with QLoRA
- L4: make predictions and pull out metrics on safety scores, such as harassment and severity

### other resources
A sample of my [reserach links](https://docs.google.com/document/d/1v62l0hC4MBPpnCHBsVGJ8Tr3KzCCpMx23fIqmA8hTak/edit?usp=sharing) on LLM topics

<br>
	
