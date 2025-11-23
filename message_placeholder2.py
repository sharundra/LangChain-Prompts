from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


#load_chat_history
chat_history = []
with open('chat_history2.txt') as f:
    chat_history.extend(f.readlines())

#create chat template
chat_template = ChatPromptTemplate([
                                        ('system', 'you are a {domain} expert'),
                                        MessagesPlaceholder(variable_name = 'chat_history'),
                                        ('human', '{query}')
                                    ])

#create prompt
prompt = chat_template.invoke({'domain': 'history', 'chat_history':chat_history,'query':'When and why was it fought?'}) 

print(prompt)

model = ChatOpenAI()
response = model.invoke(prompt)
print(response)