seleary = float(input())
def selearyper(amount, per):
    res = (amount * per) / 100
    add = format(res + amount, '.2f')
    res = format(res, '.2f')
    result = f"""Novo salario: {add}
Reajuste ganho: {res}
Em percentual: {per} %"""
    return result


if seleary >= 0 and seleary <= 400:
    print(selearyper(seleary, 15))
elif seleary >= 400.01 and seleary <= 800:
    print(selearyper(seleary, 12))
elif seleary >= 800.01 and seleary <= 1200:
    print(selearyper(seleary, 10))
elif seleary >= 1200.01 and seleary <= 2000:
    print(selearyper(seleary, 7))
else:
    print(selearyper(seleary, 4))
