pip install llama-index-llms-groq
pip install llama-index
from llama_index.llms.groq import Groq as g
GROQ_API_KEY="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"
!pip install --upgrade llama-index-llms-groq

## First Code
llm=g(model="llama3-70b-8192", api_key="your key")

response=llm.complete("Explain Something")

print(response)

## Second Code
from llama_index.core.llms import ChatMessage
message=[
    ChatMessage(
        role="system", content="You are my Best Friend, my name is Sana"
    ),
    ChatMessage(role="user", content="what is your name? and from where you are taking that name? is it random?"),
]
resp=llm.chat(message)

print(resp)
