per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
a = list(per_cent.values())
max_deposit = 0
deposit = []
for i in range(0, len(a)):
    income = round(money * (a[i]/100))
    deposit.append(income)
    i += 1
    if income >= max_deposit:
        max_deposit = income
print(deposit)
print(max_deposit)
