"""O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.

Determine o maior lucro dado esse array K de preços.

Exemplo 1:


Input: [7,1,5,3,6,4]

Output: 5

Explicação: Este valor acontece quando compramos a ação no 2o dia e a vendemos no 5o dia (6 - 1)




Exemplo 2:

Input: [7,6,4,3,1]

Output: 0

Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro."""

from random import randint

valores = []
while len(valores) != 5:
    r = randint(0, 100)
    valores.append(r)

print(valores)

b = valores.copy()
b.sort(reverse=True)
if valores == b:
    print(0)
    exit()

result = []
for i in range(len(valores)):
    for j in range(len(valores)):
        if ( j < i):
            total = valores[i] - valores[j]
            result.append(total)

print(max(result))

    