
import os
import subprocess

Vetor = list()
Resultado = list()
NomePlacas = list()
VetorPlacas = list()
ResultadoSaida = list()

RespostaIpAll = subprocess.Popen('ip a', shell=True, stdout=subprocess.PIPE)
Saida = RespostaIpAll.communicate()
Saida = str(Saida).split(" ")

RespostaIpToken = subprocess.Popen('ip token', shell=True, stdout=subprocess.PIPE)
Placas = RespostaIpToken.communicate()
Placas = str(Placas).split(" ")

for x,y in enumerate(Placas):
    if y == "dev":
        VetorPlacas.append(Placas[x+1])

VetorPlacas = str(VetorPlacas).split("\\")
VetorPlacas = str(VetorPlacas).split(",")

VetorPlacas = [item.replace("'", '') for item in VetorPlacas]
VetorPlacas = [item.replace('"', '') for item in VetorPlacas]
VetorPlacas = [item.replace('[', '') for item in VetorPlacas]

for x, y in enumerate(VetorPlacas):
    if " " == y:
        NomePlacas.append(VetorPlacas[x-1])

for x, y in enumerate(NomePlacas):
    NomePlacas[x] = (y.strip() + ":")

Saida = [item.replace('\\n', '') for item in Saida]
Saida = [item.replace(Saida[0], '1:') for item in Saida]
Saida = [item.replace("'", '') for item in Saida]
Saida = [item.replace(",", '') for item in Saida]

for a in range(0,10):
    for x, y in enumerate(Saida):
        if y == '':
            Saida.pop(x)

Saida.pop(-1)

cont = 1
cont2 = -2

for x , y in enumerate(Saida):
    cont+=1
    if y == "qlen" or y =="brd":
        Saida.insert(cont, "\n     ")

for x , y in enumerate(Saida):
    if NomePlacas[0] in y or NomePlacas[1] in y or NomePlacas[2] in y:
        ResultadoSaida.append("\n" + "\n" + y)
    else:
        ResultadoSaida.append(y)

Saida = list()

for x , y in enumerate(ResultadoSaida):
    a = x - 2
    if "inet6" in y or "noprefixroute" in y:
        Saida.append("\n      " + y)
    else:
        Saida.append(y)

Saida = " ".join(str(x) for x in Saida)

for x , y in enumerate(Saida):
    for w, z in enumerate(y):
        if z == ">":
            Resultado.append(z + "\n     ")
        else:
            Resultado.append(z)

Resultado = "".join(str(x) for x in Resultado)

print(Resultado)
