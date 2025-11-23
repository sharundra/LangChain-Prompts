from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#load_chat_history
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

#create chat template
chat_template = ChatPromptTemplate([
                                        ('system', 'you are a helpful customer support agent'),
                                        MessagesPlaceholder(variable_name = 'chat_history'),
                                        ('human', '{query}')
                                    ])

#create prompt
prompt = chat_template.invoke({'chat_history':chat_history,'query':'Why is my order delayed?'}) 

print(prompt)

