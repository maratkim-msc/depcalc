vinput=input("Введите сумму вклада")
minput=input("Количество месяцев вклада")
pinput=input("Годовая процентная ставка")
reinvestinput=int(input())
# v- сумма начального вклада
v=float(vinput)
# m - количество месяцев вклада
m=int(minput)
# p - годовая процентная ставка
p=float(pinput)
# так как нормальную формулу для капитализации не нашёл, напишу ручками на каждый месяц
m1=round(((v*p)/12/100), 3)
m2=round(((v+m1)*p/12/100), 3)
m3=round(((v+m2+m1)*p/12/100), 3)
m4=round(((v+m3+m2+m1)*p/12/100), 3)
m5=round(((v+m4+m3+m2+m1)*p/12/100), 3)
m6=round(((v+m5+m4+m3+m2+m1)*p/12/100), 3)
m7=round(((v+m6+m5+m4+m3+m2+m1)*p/12/100), 3)
m8=round(((v+m7+m6+m5+m4+m3+m2+m1)*p/12/100), 3)
m9=round(((v+m8+m7+m6+m5+m4+m3+m2+m1)*p/12/100), 3)
m10=round(((v+m9+m8+m7+m6+m5+m4+m3+m2+m1)*p/12/100), 3)
m11=round(((v+m10+m9+m8+m7+m6+m5+m4+m3+m2+m1)*p/12/100), 3)
m12=round(((v+m11+m10+m9+m8+m7+m6+m5+m4+m3+m2+m1)*p/12/100), 3)
#капитализация
if reinvestinput!=0:
    reinvest=round((v+m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12),2)
print(str(m1,m2,m3,m4))