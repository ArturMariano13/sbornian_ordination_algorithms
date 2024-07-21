import json
import time
from Log import Log

dados_json = []

def counting_sort(input_array, key_func, max_value):
    count_array = [0] * (max_value + 1)
    output_array = [None] * len(input_array)

    for item in input_array:
        key = key_func(item)
        count_array[key] += 1

    for i in range(1, max_value + 1):
        count_array[i] += count_array[i - 1]

    for item in reversed(input_array):
        key = key_func(item)
        output_array[count_array[key] - 1] = item
        count_array[key] -= 1

    return output_array

def radix_sort(input_array, key_funcs, max_values):
    total_sort_time = 0
    for key_func, max_value in zip(key_funcs, max_values):
        start_time = time.time()
        input_array = counting_sort(input_array, key_func, max_value)
        end_time = time.time()
        total_sort_time += (end_time - start_time)
    return input_array, total_sort_time

def ler_json_grande(path):
    with open(path, 'r') as f:
        objetos = json.load(f)
        for objeto in objetos:
            log = Log(objeto['month'], objeto['log'], objeto['msg'], objeto['user'])
            dados_json.append(log)

def buscar_registro_por_posicao(logs, posicao):
    if posicao < 1 or posicao > len(logs):
        return None
    return logs[posicao - 1] 

filename = 'data.json'  
ler_json_grande(filename)

meses_ordem = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for log in dados_json:
    log.monthIndex = meses_ordem.index(log.month)


dados_json, tempo_ordenacao_meses = radix_sort(dados_json, [lambda log: log.monthIndex], [11])

indice_impostor = 1000001  

impostor_log = buscar_registro_por_posicao(dados_json, indice_impostor)
if impostor_log:
    impostor_mes = impostor_log.month

    logs_mes_impostor = [log for log in dados_json if log.month == impostor_mes]

    logs_mes_impostor_ordenados, tempo_ordenacao_mes_impostor = radix_sort(logs_mes_impostor, [lambda x: x.number], [max(log.number for log in logs_mes_impostor)])

    inicio_mes = dados_json.index(logs_mes_impostor[0])
    dados_json[inicio_mes:inicio_mes+len(logs_mes_impostor)] = logs_mes_impostor_ordenados

    impostor_final = buscar_registro_por_posicao(dados_json, indice_impostor)
    if impostor_final:
        print(f"Impostor final encontrado: {impostor_final}")
    else:
        print(f"Impostor não encontrado após a ordenação dentro do mês")
else:
    print(f"Impostor não encontrado na posição {indice_impostor}")

tempo_total_ordenacao = tempo_ordenacao_meses + tempo_ordenacao_mes_impostor
print("\nTempo Total de Ordenação: %s segundos" % tempo_total_ordenacao)

print("Programa finalizado!")
