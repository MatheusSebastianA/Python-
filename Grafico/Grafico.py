import matplotlib.pyplot as plt 
from numpy import log as ln


#Pegando os valores do primeiro arquivo.txt e salvando em valores
with open("teste.txt", "r") as arquivo:
    valores = arquivo.readlines()

#Convertendo os valores para o log natural
vetor_logaritmico1 = []
for elemento in valores:
    valor_float = ln(float(elemento))
    vetor_logaritmico1.append(valor_float)

#Pegando os valores do segundo arquivo.txt e salvando em valores
with open("valoresTeste.txt", "r") as arquivo:
    valores = arquivo.readlines()

#Convertendo os valores para o log natural
vetor_logaritmico2 = []
for elemento in valores:
    valor_float = ln(float(elemento))
    vetor_logaritmico2.append(valor_float)

K_pontos = [64, 128, 200, 256, 512, 600, 800, 1024, 2000, 3000, 4096, 6000, 7000, 10000, 50000, 10**5, 10**6, 10**7, 10**8]


x = []
#Convertendo a quantidade de k pontos do sistema para log natural
for elemento in K_pontos:
    valor_float = ln(float(elemento))
    x.append(valor_float)

#Primeira linha do gráfico
y1 = vetor_logaritmico1

#Segunda linha do gráfico
y2 = vetor_logaritmico2

plt.plot(x,y1)
plt.plot(x, y1, label="dados1", color="orange")
plt.plot(x, y2)
plt.plot(x, y1, label="dados2", color="blue")
plt.legend()

plt.ylabel("Ln (medida)")
plt.xlabel("Ln(número de pontos)")
plt.title("Medida")

plt.show()
