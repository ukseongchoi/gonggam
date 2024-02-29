import datetime
import requests
import socket
import time

time.sleep(10)
discord_url = "https://discord.com/api/webhooks/1210639626751180810/pRCB-WaDH1czR5iYTtVkWpoK4N8QyF6iC0BRdSPkgZ8B1bO3-6RXKI7aG3N8mQIp-Mau"
#디스코드 채널로 메세지 전송
def discord_send_message(text):
    now = datetime.datetime.now()
    message = {"content": f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {str(text)}"}
    requests.post(discord_url, data=message)
    print(message)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
a = sock.getsockname()[0]
discord_send_message(a)

