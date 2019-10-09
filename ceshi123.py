import requests
html=requests.get(url="https://www.haoyunbb.com/40weeks/122116407.html",verify=False).content.decode()
print(html)