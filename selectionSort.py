import ijson
import time
from Log import Log 

dados_json = []

def ler_json_grande(path):
    with open(path, 'rb') as f:
        objetos = ijson.items(f, 'item')
        for objeto in objetos:
            log = Log(objeto['month'], objeto['log'], objeto['msg'], objeto['user'])
            dados_json.append(log)

def selectionSort(dados_json):
    print("Iniciando ordenação")
    tamanho = len(dados_json)

    for i in range(tamanho - 1):
        indice_menor = i
        for j in range(i + 1, tamanho):
            if dados_json[j].monthIndex < dados_json[indice_menor].monthIndex:
                indice_menor = j
            elif dados_json[j].monthIndex == dados_json[indice_menor].monthIndex:
                if dados_json[j].number < dados_json[indice_menor].number:
                    indice_menor = j    

        dados_json[i], dados_json[indice_menor] = dados_json[indice_menor], dados_json[i]


ler_json_grande('data.json')
print("Terminou leitura")

start_time = time.time()
selectionSort(dados_json)
end_time = time.time()

tamanho = len(dados_json)

print("Tempo de Ordenação: %s seconds" % (end_time - start_time))