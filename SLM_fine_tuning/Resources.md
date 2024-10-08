\#References and resources used  
Tao Lin

\_Note: some topics came from my my early brainstorming, but I didn’t actually use them\_

\#\#Similar use case (email classification)

\#\#Fine-tuning strategies and guides  
A ppt from Chang et al 2023 \=\> I got a lot of direction from their comparative study  
[https://github.com/neelblabla/large\_language\_models\_for\_processing\_emails/blob/main/LLMs%20for%20Email%20Classification.pdf](https://github.com/neelblabla/large_language_models_for_processing_emails/blob/main/LLMs%20for%20Email%20Classification.pdf)

BERT [https://medium.com/@khang.pham.exxact/text-classification-with-bert-7afaacc5e49b](https://medium.com/@khang.pham.exxact/text-classification-with-bert-7afaacc5e49b)  
A collection on LLM on colab [https://github.com/mlabonne/llm-course](https://github.com/mlabonne/llm-course)

Bigbird doc [https://huggingface.co/docs/transformers/model\_doc/big\_bird](https://huggingface.co/docs/transformers/model_doc/big_bird)

Bigbird fine-tuning [https://github.com/jlealtru/website\_tutorials/blob/main/notebooks/BigBird%20text%20classification.ipynb](https://github.com/jlealtru/website_tutorials/blob/main/notebooks/BigBird%20text%20classification.ipynb)

This paper talks about overfitting  
[https://stackoverflow.com/questions/73527846/how-to-improve-an-accuracy-of-validation-and-test-of-my-model-of-transfer-learni](https://stackoverflow.com/questions/73527846/how-to-improve-an-accuracy-of-validation-and-test-of-my-model-of-transfer-learni)

Another way to fine-tune BERT-level models \> ONLY trained the final classifier  
https://github.com/huggingface/transformers/issues/400

\#\#LLM local servers  
Ollama [https://github.com/ollama/ollama](https://github.com/ollama/ollama)  
Hosting on Colab \> an interesting idea, but may run into many issues such as authentication https://shiv248.medium.com/hosting-open-source-llm-model-on-google-colaboratory-cc14a42d4053

\#\#EDA  
Bertopic [https://maartengr.github.io/BERTopic/getting\_started/quickstart/quickstart.html](https://maartengr.github.io/BERTopic/getting_started/quickstart/quickstart.html)  
Kmeans on clustering https://scikit-learn.org/dev/auto\_examples/text/plot\_document\_clustering.html  
Textblob sentiment https://textblob.readthedocs.io/en/dev/quickstart.html  
My previous work on NLP feature engineering [https://github.com/daywatch/Python](https://github.com/daywatch/Python)

\#\# LLAMA2 fine-tuning (I thought about it, but it’s circular to fine-tune LLAMA with LLAMA data)  
Loss is not reliable when you use LoRA methods  
[https://www.reddit.com/r/LocalLLaMA/comments/17zwh3z/training\_and\_validation\_loss\_behavior\_while/](https://www.reddit.com/r/LocalLLaMA/comments/17zwh3z/training_and_validation_loss_behavior_while/)

\#\#Commercial LLM APIs for LLAMA3   
AWAN [https://www.awanllm.com/](https://www.awanllm.com/)  
Groq [https://console.groq.com/docs/quickstart](https://console.groq.com/docs/quickstart)  
Perplexity [https://docs.perplexity.ai/guides/pricing](https://docs.perplexity.ai/guides/pricing)  
Novita [https://novita.ai/user/login?\&redirect=/model-api/pricing?\&utm\_source=model-api-pricing--Header\_Login\_Button](https://novita.ai/user/login?&redirect=/model-api/pricing?&utm_source=model-api-pricing--Header_Login_Button)  
GLHF  [https://glhf.chat/chat/create](https://glhf.chat/chat/create)  
Free LLM APIs [https://github.com/cheahjs/free-llm-api-resources?tab=readme-ov-file](https://github.com/cheahjs/free-llm-api-resources?tab=readme-ov-file)

