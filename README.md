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
- fine-tuning service on chatgpt with generated data from gpt4
<br>

### Other resources
Debugging tools \
	1.[Weights & Biases](https://wandb.ai/site/prompts) \
	2.[Galileo](https://www.rungalileo.io/llm-studio/#join-waitlist) \
	3.[Allen NLP's LM tool](https://github.com/mega002/lm-debugger) \
	4.[Aim for LangChain](https://dev.to/tatyana/langchain-aim-building-and-debugging-ai-systems-made-easy-1bk0) \
	5.[LangChain Visualizer](https://github.com/amosjyng/langchain-visualizer) \
	6.LLM-debugging papers \
	[Explainable Automated Debugging via Large Language Model-driven Scientific Debugging](https://arxiv.org/abs/2304.02195) \
	[Teach LLMs to do self-debugging](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://arxiv.org/pdf/2304.05128.pdf) 

<br>

More about fine-tuning \
  1.[eight major methods for fine-tuning LLMs](https://dr-bruce-cottman.medium.com/part-1-eight-major-methods-for-finetuning-an-llm-6f746c7259ee)

	


