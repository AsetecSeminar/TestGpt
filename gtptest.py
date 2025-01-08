import openai

from openai import OpenAI

openai.api_key = "yKCx1jIA"  # 새로 복사한 API 키


def ask_to_gpt_35_turbo(user_input):  
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        top_p=0.1,
        temperature=0.1,
        messages=[
            {"role": "system", "content":"You are a helpful assistant."},  
            {"role":"user", "content": user_input}
        ]  
    )  
    
    return response.choices[0].message.content 

users_request = '''
최근 가장 인기있는 프로그래밍 언어를 비교해줘 
'''
r = ask_to_gpt_35_turbo(users_request)
print(r)
