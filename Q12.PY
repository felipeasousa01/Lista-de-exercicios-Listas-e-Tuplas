# 12- Explique o que acontece ao tentar alterar um elemento de uma tupla. Faça o teste no código.
tupla = ("1", "2", "3", "4", "5")
tupla.remove("3")  # Isso causará um erro, pois tuplas são imutáveis.
print(tupla)

