# Overview of my project

We don't always have to choose LLMs for downstream tasks. In this repo, I used LLAMA3-8b data to fine-tune a BigBird model (or you can call it knowledge distillation) for a simple classification task

<br>

In this email classification task, I used a fine-tuned BigBird model on almost all the train.csv data. The performance on my own testing data is `{'accuracy': 0.8932926829268293, 'precision': 0.8876199353523544, 'recall': 0.8932926829268293, 'f1': 0.8859254676520414}` 

## 1.Data labeling
- I applied some data cleaning logic and used LLAMA3-8b to generate the labels on about 5k inputs with a few-shot prompt; after that I manually trimmed some unwanted data based on LLAMA3 hallucination

## 2.Fine-tuning and model saving
- I applied the common BERT receipt but the model fine-tuning showed some overfitting effect in the last epoch
- The model checkpoint can be found [here](https://drive.google.com/drive/folders/18v2LV6kKhohGrAkIJfridzETfKF0J2RI?usp=sharing)

### Resources/references can be found in the resources.md