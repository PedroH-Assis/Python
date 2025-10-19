var = 1

print (var == 0)

var = 3                 # == quer dizer igual em comparação, porém o = é somente atribuição

print(var == 3)

var = 5

print(var != 5)

var = 6                 # != quer dizer diferente

print(var != 8)

var = 9

print (var > 10)

var = 11                # > maior que

print(var > 6)

var = 12

print(var >= 12)

var = 13                # >= maior ou igual

print(var >=5)


var1 = 14

print(var1 <= 14)

var = 15                # <= menor ou igual

print(var <= 45 )

teste = var >= var1


# +-------------+------------------------------+-----------+
# | Prioridade  | Operadores                   | Tipo      |
# +-------------+------------------------------+-----------+
# | 1           | +,   -,                      | unário    |
# | 2           | **                           |           |
# | 3           | *   /   //   %               |           |
# | 4           | +   -                        | binário   |
# | 5           | <   <=   >   >=              |           |
# | 6           | ==   !=                      |           |
# +-------------+------------------------------+-----------+


n = int(input("Digite um número: ")) 

print(n >= 100) 