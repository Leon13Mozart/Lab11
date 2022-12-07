import json
n=str(input("Введіть дані про автора "))
s=str(input("Введіть дані про книгу"))
wer=n+' '+s
with open("D:\\ДЗ\\R\\i.json",'a') as f:
  json.dump(wer,f)
