import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(res.text[:500])

lalleFile = open('Story_1.txt','wb')
for chunk in res.iter_content(100000):
    lalleFile.write(chunk)

lalleFile.close()