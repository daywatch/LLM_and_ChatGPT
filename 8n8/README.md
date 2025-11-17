## LLM and automation with 8n8

<br>

This folder contains two RAG-related workflows: 

<br>

1.In the first flow, after clicking, emails from google docs are indexed on Pinecone (with OpenAI embedding and recursive character splitter)

<br>

2.In the second use case, the user can prompt what message to send to the email: GPT will finish an email draft and pinecone returns with a matching email address. The email content and address will be submitted to a gmail sending node

<br>
Other topics with 8n8:
- [Remote host options (AWS)](https://docs.n8n.io/hosting/installation/server-setups/aws/)
- [Scaling settings](https://docs.n8n.io/hosting/scaling/overview/) 