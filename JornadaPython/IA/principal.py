# Objetivo - Treinar uma IA para que ela possa fazer uma previsão do score de alguns clientes de teste
#1 - Importar a base de dados
import pandas as pd

tabela = pd.read_csv("clientes.csv")

""" print(tabela)
print(tabela.info()) """

#2 - Preparar a base de dados - Tudo precisa estar em número para treinar a IA utilizando Label Encoder
#As colunas "profissao", "mix_credito", "comportamento_pagamento" são do tipo object, logo, precisam ser codificadas para números
#Score credito nao precisa ser codificado, pois é o objetivo de previsão

from sklearn.preprocessing import LabelEncoder

#Criar Label Encoder
codificador = LabelEncoder()

#Aplicar o Labem encoder nas colunas necessárias
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

#3 - Aprendizado da IA
#Quem é necessário prever(y): Score de credito do cliente
#Quem é usado para fazer as previsões(x): Dados importantes, ID ou nome não são importantes

y = tabela["score_credito"]
x = tabela.drop(columns=["score_credito", "id_cliente"])

#Treino e teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)


#4 - Criar a IA
#Dois modelos de aprendizado, de árvore de decisão e KNN (vizinhos próximos)

#Importar IA
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

#Criar IA
modelo_arvore = RandomForestClassifier()
modelo_vizinho = KNeighborsClassifier()

#Treino da IA
modelo_arvore.fit(x_treino, y_treino)
modelo_vizinho.fit(x_treino, y_treino)

#Previsão dos modelos 
previsao_arvore = modelo_arvore.predict(x_teste)
previsao_vizinho = modelo_vizinho.predict(x_teste)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_teste, previsao_arvore))
print(accuracy_score(y_teste, previsao_vizinho))

#Utilizando em outra base de dados
tabela_nova = pd.read_csv("novos_clientes.csv")

tabela_nova["profissao"] = codificador.fit_transform(tabela_nova["profissao"])
tabela_nova["mix_credito"] = codificador.fit_transform(tabela_nova["mix_credito"])
tabela_nova["comportamento_pagamento"] = codificador.fit_transform(tabela_nova["comportamento_pagamento"])

previsoes = modelo_arvore.predict(tabela_nova)
print(previsoes)