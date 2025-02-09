import requests
import time

# API Anahtarları
API_KEYS = {
    "agent-1": "apikey",
    "agent-2": "apikey",
}

API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key="

# Google Gemini API'ye mesaj gönderme fonksiyonu
def get_gemini_response(agent, message):
    url = API_URL + API_KEYS[agent]
    
    payload = {
        "contents": [{"role": "user", "parts": [{"text": message}]}]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        return response_data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print(f"❌ {agent} API Hatası: {response.status_code} - {response.text}")
        return None

# Sohbet Başlatma
print("🤖 Agent-1 ve Agent-2 Sohbet Ortamına Hoş Geldiniz!")
print("İlk mesajı Agent-1 adına yazın. Çıkmak için 'exit' yazın.\n")

agent_1_message = input("👤 Agent-1: ")
if agent_1_message.lower() == "exit":
    print("Sohbet sonlandırıldı.")
else:
    while True:
        # Agent-1 mesajı Agent-2'ye gönderiyor
        agent_2_response = get_gemini_response("agent-2", agent_1_message)
        if not agent_2_response or agent_2_response.lower() == "exit":
            print("Sohbet sonlandırıldı.")
            break
        print(f"🤖 Agent-2: {agent_2_response}")

        time.sleep(1)  # Yanıtlar arasında küçük bir bekleme süresi

        # Agent-2 mesajı Agent-1'e gönderiyor
        agent_1_message = get_gemini_response("agent-1", agent_2_response)
        if not agent_1_message or agent_1_message.lower() == "exit":
            print("Sohbet sonlandırıldı.")
            break
        print(f"🤖 Agent-1: {agent_1_message}")

        time.sleep(1)  # Yanıtlar arasında küçük bir bekleme süresi
