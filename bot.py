import json
from config import *
from tools import function_list
from utils import *
from prompts import *


class ChatBot():
    def __init__(self) -> None:
        self.knowledge_base = pinecone.Index(PINECONE_INDEX)
        self.history = []
        self.initialize()

    def initialize(self):
        self.start_prompt = get_assistant_start()
        self.system_prompt = get_system_prompt()
        self.vision_prompt = get_vision_prompt()
        self.summarize_prompt = get_summarization_prompt()
        self.unfamiliar_prompt = get_unfamiliar_prompt()

        self.history = [self.system_prompt, self.start_prompt]
        print('Bot:', self.start_prompt['content'])

    def get_knowledge(self, query, top_k=7):
        query_vector = get_embedding(query)
        result = self.knowledge_base.query(vector=query_vector, top_k=top_k)
        matches = result.to_dict()['matches']
        ids = [match["id"] for match in matches]
        data = self.knowledge_base.fetch(ids).to_dict()['vectors']
        descriptions = []
        for id in ids:
            descriptions.append(data[id]["metadata"])
        knowledge_text = get_knowledge_text(descriptions)
        return knowledge_text

    def chat(self, user_query, img=''):
        if img != '':
            vision_query = [
                {"type": "text", "text": user_query},
                {
                    "type": "image_url",
                    "image_url": img
                }
            ]

            messages = [self.vision_prompt, {"role": "user", "content": vision_query}]

            response = client.chat.completions.create(
                model='gpt-3.5-turbo-1106',
                messages=messages,
                temperature=0.5,
                max_tokens=800,
                stream=True
            )
            text = ''
            for chunk in response:
                data = chunk.choices[0].delta
                if hasattr(data, 'content'):
                    text += data.content
                    yield f"data: {json.dumps({'token': data.content})}\n\n".encode("utf-8")
            self.history.append({"role": "user", "content": user_query})
            self.history.append({"role": "assistant", "content": text})

        else:
            self.history.append({"role": "user", "content": user_query})
            if len(self.history) <= 7:
                messages = self.history
            else:
                messages = [self.system_prompt] + self.history[-6:]
            
            function_response = client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages[1:],
                temperature=0,
                functions=function_list,
                function_call='auto'
            )

            print(function_response.choices[0].finish_reason)

            if function_response.choices[0].finish_reason == "function_call":
                params = function_response.choices[0].message.function_call
                print(params.name)
                if params.name == 'get_knowledge':
                    knowledge_prompt = get_knowledge_prompt(self.get_knowledge(user_query))
                    print('get_knowledge')
                    messages.append(knowledge_prompt)
                elif params.name == 'unfamiliar_question':
                    messages.append(self.unfamiliar_prompt)
            
            response = client.chat.completions.create(
                model=LLM_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=800,
                stream=True
            )
            output = ''
            for chunk in response:
                data = chunk.choices[0].delta
                if hasattr(data, 'content'):
                    if data.content is not None:
                        output += data.content 
                    # yield f"data: {json.dumps({'token': data.content})}\n\n".encode("utf-8")
                    yield data.content
            self.history.append({"role": "assistant", "content": output})
            print('ok')


bot = ChatBot()
while True:
    user = input('Pul: ')
    answer = bot.chat(user)
    for chunk in answer:
        print(chunk, end='', flush=True)
    print()
    # print('Bot:', answer)
        