from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="AZURE_OPENAI_KEY",
    api_version="2024-02-15-preview",
    azure_endpoint="https://<your-endpoint>.openai.azure.com"
)

def ask_question(question):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content
