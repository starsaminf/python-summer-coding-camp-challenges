import datetime

date = input()

month, day, year = (int(x) for x in date.split(' '))    

ans = datetime.date(year, month, day)

print (ans.strftime("%A").upper())

