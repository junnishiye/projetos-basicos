
np=input("coloque o nome do produto: ")
pu=float(input("coloque o preço unitário do produto: "))
q=int(input("coloque a quantidade do produto: "))
d=float(input("coloque o desconto do produto: "))/100
print("o valor bruto da compra do item",np,"é:",pu*q)
print("o valor do desconto do item",np,"é:",pu*q*d)
print("o valor líquido da compra do item",np,"é:",pu*q-pu*q*d)

nc=input('coloque o nome do colaborador: ')
vh=float(input('coloque o valor da hora trabalhada: '))
ht=float(input('coloque as horas trabalhadas: '))
vb=float(input('coloque o valor do bônus fixo do mês: '))
print("colaborador",nc,"recebe um valor bruto de:",vh*ht,"e um valor liquido de:",vh*ht+vb)


