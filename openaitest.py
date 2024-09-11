# Send a POST message to https://openaiproxy-hw.unipus.cn/v1/completions with header X-HMAC-ACCESS-KEY as developer
import requests
import datetime
import hmac, hashlib, base64

url = "https://openaiproxy-hw.unipus.cn/v1/chat/completions"
#v1/engines/davinci-codex/completions v1/embeddings
ak = "chatRobot"
sk = "j57kq7vjemd6uu0kg2yxc4pdf28or0gjekrm52ir"
# ak = "fengjin"
# sk = "OkpzWgUXLnlUZQMyuxPyRJha5JP7RnIp8PoJCbmm"

#date_string = datetime.datetime.now().strftime("%a, %-d, %b %Y %H:%M:%S GMT")

date_string = "Sun, 18 Jun 2023 18:54:43 GMT"
print(date_string)

#message = "POST\n/v1/embeddings\n\n" + ak + "\n" + date_string + "\n"
message = "POST\n/v1/chat/completions\n\n" + ak + "\n" + date_string + "\n"
print(message, len(message))
hasher = hmac.new(sk.encode(), message.encode(), hashlib.sha256)
signature = base64.b64encode(hasher.digest())
print(signature)

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "X-HMAC-ACCESS-KEY": ak,
    "X-HMAC-ALGORITHM": "hmac-sha256",
    "X-HMAC-SIGNATURE": signature,
    "Date": date_string
}

# data = {
#    "input": "Your text string goes here,hello unipus",
#    "model": "text-embedding-ada-002"
#}

data = {
    #"prompt": "can you tell me where i am now",
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "messages": [{"role": "user", "content": "原子核中的强相互作用力是存在于质子和中子间还是在质子中子内部"}]
}

response = requests.post(url, headers=headers, json=data)

#print("Status Code", response.status_code)
print("JSON Response ", response.json())
content = response.json()['choices'][0] #['message'] #['content']

print(content['message']['content']) #.choices[0].message["content"]