#!/bin/python
# Importa os processos necessário
import subprocess

PlacasDeRede = list() # Para obter placas de rede para obter mais infromações
Informacoes = list() # Obtem IP e concatena com o nome da placa
EnderecoMAC = list() # Obterm o endereço MAC
PlacasComConexao = list()



# Executa comando para obter informações de ip usando utilitátio do IpRoute
# Filtra por : e troca tudo depois de ': ' por '\\n' e depois deleta tudo que está depois de '<' depois substitui ':' por '==' 
RetornoIpAll = subprocess.Popen("ip a | grep ': ' | sed 's/: /\\n /' | sed 's/ <.*//' | sed 's/:/ == /'", shell=True, stdout=subprocess.PIPE)
RetornoIpAll = RetornoIpAll.communicate()
# Transforma a saída do comando em um lista dividida por ' '
RetornoIpAll = str(RetornoIpAll).split(' ')

# Obtem o nome de cada adptador de rede conectado, Up ou Down
# Percorre toda a lista gerada anteriormente
for x, y in enumerate(RetornoIpAll):
    # Executa a condição para obter os nomes dos adaptadores de rede
    if(RetornoIpAll[x] == "==" and x < len(RetornoIpAll)):
        # Cria a lista de nome de placa de rede
        PlacasDeRede.append(RetornoIpAll[x-1])

# Obtem o IP e MAC de cada adaptador ativo
# Percorre a lista de nome de adaptadores
for Placa in PlacasDeRede:
    # Executa comando para obter informações sobre uma placa de rede
    # A variavel Placa contem o nome da placa procurada 
    RetornoShowPlaca = subprocess.Popen("ip addr show " + Placa, shell=True, stdout=subprocess.PIPE)
    RetornoShowPlaca = RetornoShowPlaca.communicate()
    # Transforma a saída do comando em um lista dividida por ' '
    RetornoShowPlaca = str(RetornoShowPlaca).split(' ')

    # Percorre a lista com as informações do adaptador buscado
    for Posicao, Valor in enumerate(RetornoShowPlaca):
        # Executa a condição para obter os IP dos adaptadores de rede
        if(Valor == "inet" and Posicao < len(RetornoShowPlaca)):
            # Cria uma lista concatenando o nome do adaptador e o IP
            Informacoes.append("Nome do Adaptador: " + Placa + (' ' * (10-len(Placa))) + " IPv4: " + RetornoShowPlaca[Posicao+1] + (' ' * (19-len(RetornoShowPlaca[Posicao+1]))))
            PlacasComConexao.append(Placa)
        # Executa a condição para obter os MACs dos adaptadores de rede
        if(Valor.startswith("link/") and Posicao < len(RetornoShowPlaca)):
            # Cria uma lista com os endereços MAC
            EnderecoMAC.append(RetornoShowPlaca[Posicao+1])

print("Todos os adaptadores de rede")
# Mostra os nomes dos adaptadore de rede unindo com '==' e depois concatenando um '\n'
print(" --- ".join(PlacasDeRede)+ "\n")

if(len(PlacasDeRede) > 0):
    print("\nPlacas com conexão")
    # Percorre a lista de informações geradas anteriormente
    for x in range(len(Informacoes)):
        # Mostra o Nome - IP e MAC de cada adaptador
        print(Informacoes[x] + " Endereço MAC: " + EnderecoMAC[x])

for item in PlacasComConexao:
    for item2 in PlacasDeRede:
        if(item == item2):
            PlacasDeRede.remove(item)

if(len(PlacasDeRede) > 0):
    print("\nPlacas sem conexão")
    for i in PlacasDeRede:
        print(i)