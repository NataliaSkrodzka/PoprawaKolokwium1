import math

wynik=0
for i in range(4,11):
    wynik+=pow(math.exp(i)+math.log(24,2),1/4)
print(round(wynik,2))