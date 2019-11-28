import requests as re
result=re.get("http://127.0.0.1:8000/class/")
jd=result.json()
print(jd)
print("-------------")
result=re.post("http://127.0.0.1:8000/class/")
jd=result.json()
print(jd)
print("-------------------------")

result=re.put("http://127.0.0.1:8000/class/")
jd=result.json()
print(jd)
print("-------------------------")

result=re.delete("http://127.0.0.1:8000/class/")
jd=result.json()
print(jd)
print("-------------------------")


