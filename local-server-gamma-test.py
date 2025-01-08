import requests 
import json

def chat(messages):
    r = requests.post(
        "http://localhost:11434/api/generate",  # 추후 변경됨
        json={
            "model": "gemma:7b",
            "prompt": messages[-1]["content"],
            "stream": True,
            "options": {
                "temperature": 0.7,    # 응답의 창의성 조절
                "top_k": 50,          # 토큰 선택의 다양성
                "top_p": 0.95,        # 누적 확률 임계값
                "num_ctx": 4096       # 컨텍스트 윈도우 크기
            }
        },
    )
    r.raise_for_status()
    
    output = ""
    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
            
        if body.get("done") is False:
            chunk = body.get("response", "")
            output += chunk
            print(chunk, end="", flush=True)
            
        if body.get("done", False):
            return {"role": "assistant", "content": output}
            
def main():
    print("Gemma 7B 모델과 대화를 시작합니다.")
    print("대화를 종료하려면 빈 프롬프트를 입력하세요.\n")
    
    messages = []
    while True:
        user_input = input("\n프롬프트 입력: ")
        if not user_input:
            print("대화를 종료합니다.")
            exit()
        print()
        
        messages.append({"role": "user", "content": user_input})
        response_message = chat(messages)
        messages.append(response_message)
        print("\n")

if __name__ == "__main__":
    main()
