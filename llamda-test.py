import requests 
import json

def chat(messages):
    r = requests.post(
#        "http://localhost:11434/api/generate",
        "https://5453-115-94-132-50.ngrok-free.app/api/generate",
        json={
            "model": "llama2:latest", 
            "prompt": messages[-1]["content"],  # 마지막 메시지의 내용만 전송
            "stream": True
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
            # 응답 완료시 메시지 생성
            return {"role": "assistant", "content": output}
            
def main():
    messages = []
    while True:
        user_input = input("\n프롬프트 입력: ")
        if not user_input:
            exit()
        print()
        
        messages.append({"role": "user", "content": user_input})
        response_message = chat(messages)
        messages.append(response_message)
        print("\n")

if __name__ == "__main__":
    main()