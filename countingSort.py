import ijson
import json
import time
from Log import Log 

dados_json = []

def ler_json_grande(path):
    with open(path, 'rb') as f:
        objetos = ijson.items(f, 'item')
        for objeto in objetos:
            log = Log(objeto['month'], objeto['log'], objeto['msg'], objeto['user'])
            dados_json.append(log)


def countingSort(dados_json):
    size = len(dados_json)
    output = [0] * size

    # Ordenar pelo número do log usando countingSort
    max_log_number = max(log.number for log in dados_json)
    count = [0] * (max_log_number + 1)

    for log in dados_json:
        count[log.number] += 1

    for i in range(1, max_log_number + 1):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        output[count[dados_json[i].number] - 1] = dados_json[i]
        count[dados_json[i].number] -= 1

    max_month_index = max(log.get_month_index() for log in dados_json)
    count = [0] * (max_month_index + 1)

    for log in output:
        count[log.get_month_index()] += 1

    for i in range(1, max_month_index + 1):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        dados_json[count[output[i].get_month_index()] - 1] = output[i]
        count[output[i].get_month_index()] -= 1
	
def salvarLogsJSON(dados_json, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados_json, f, default=lambda x: vars(x), indent=4)

def removerMonthIndex(log):
    return {key: value for key, value in vars(log).items() if key != 'monthIndex'}

ler_json_grande('data100.json')
print("Terminou leitura")


start_time = time.time()
countingSort(dados_json)
end_time = time.time()
print("Tempo de Ordenação: %s seconds" % (end_time - start_time))

file = 'logs_ordenados.json'

try:
    salvarLogsJSON(dados_json, 'logs_ordenados.json')
    print(f"Salvou no arquivo " + file)
except Exception as e:
    print(e)

