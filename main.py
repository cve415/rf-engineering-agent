import os
import requests
from dotenv import load_dotenv

# Note: Your RF Agent was looking for .env in the /docs folder
env_path = os.path.join("docs", ".env")
load_dotenv(dotenv_path=env_path)

def start_agent():
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        print("❌ ERROR: RF Agent couldn't find the key in docs/.env")
        return

    print("📡 RF Engineering Agent: INITIALIZING...")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "moonshotai/kimi-free",
        "messages": [{"role": "user", "content": "RF Agent check: System Live?"}]
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("✅ SUCCESS! Kimi is connected.")
        print(f"🤖 Response: {response.json()['choices'][0]['message']['content']}")
    else:
        print(f"❌ Connection Failed: {response.status_code}")

if __name__ == "__main__":
    start_agent()