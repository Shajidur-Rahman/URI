selary = float(input())
def selearyper(amount, per):
    res = (amount * per) / 100
    return res
if selary > 0 and selary < 400:
    fi = f"""Novo salario: {format(selearyper(selary, 15) + selary)}
Reajuste ganho: {selearyper(selary, 15)}
Em percentual: 15 %"""
    print(fi)
# second 
elif selary > 400.01 and selary < 800:
    fi = f"""Novo salario: {selearyper(selary, 12) + selary}
Reajuste ganho: {selearyper(selary, 12)}
Em percentual: 12 %"""
    print(fi)
# third
elif selary > 1200.01 and selary < 2000:
    fi = f"""Novo salario: {selearyper(selary, 7) + selary}
Reajuste ganho: {selearyper(selary, 7)}
Em percentual: 7 %"""
    print(fi)
else:
    fi = f"""Novo salario: {selearyper(selary, 4) + selary}
Reajuste ganho: {selearyper(selary, 4)}
Em percentual: 4 %"""
    print(fi)