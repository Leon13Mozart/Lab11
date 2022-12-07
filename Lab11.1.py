import csv
a=str(input("Введіть прізвище "))
b=str(input("Введіть рік народження "))
sec=a+b
with open("D:\\ДЗ\\R\\div.csv",'w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(sec)
