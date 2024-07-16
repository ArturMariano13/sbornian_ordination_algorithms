import ijson
import time
from Log import Log

dados_json = []

def radix_sort_logs(logs, key_func):
    # Função de ordenação estável
    def stable_sort(arr, key_func):
        buckets = {}
        for item in arr:
            key = key_func(item)
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(item)
        result = []
        for key in sorted(buckets.keys()):
            result.extend(buckets[key])
        return result

    return stable_sort(logs, key_func)

def ler_json_grande(path):
    with open(path, 'rb') as f:
        objetos = ijson.items(f, 'item')
        for objeto in objetos:
            log = Log(objeto['month'], objeto['log'], objeto['msg'], objeto['user'])
            dados_json.append(log)

def buscar_registro_por_posicao(logs, posicao):
    if posicao < 0 or posicao >= len(logs):
        return None
    return logs[posicao]

# Exemplo de uso
filename = 'data.json'  # Nome do arquivo com os registros de log em formato JSON
ler_json_grande(filename)

# Lista ordenada de meses
meses_ordem = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Ordenar os logs primeiro pelos meses
start_time = time.time()
logs_ordenados_por_mes = radix_sort_logs(dados_json, lambda x: meses_ordem.index(x.month))
end_time = time.time()
print("\nTempo de Ordenação por Mês: %s seconds" % (end_time - start_time))
print("Ordenação por mês concluída")

# Suponha que você tenha um índice aproximado do impostor
indice_impostor = 1000000  # Exemplo de índice

# Localizar o mês do impostor com base na posição
impostor_log = buscar_registro_por_posicao(logs_ordenados_por_mes, indice_impostor)
if impostor_log:
    impostor_mes = impostor_log.month
    print(f"Impostor encontrado no mês: {impostor_mes}")

    # Filtrar os logs para o mês do impostor
    logs_mes_impostor = [log for log in logs_ordenados_por_mes if log.month == impostor_mes]

    # Ordenar os logs dentro desse mês específico pelos números dos logs
    start_time = time.time()
    logs_mes_impostor_ordenados = radix_sort_logs(logs_mes_impostor, lambda x: x.number)
    end_time = time.time()
    print("\nTempo de Ordenação dentro do Mês do Impostor: %s seconds" % (end_time - start_time))
    print("Ordenação dentro do mês concluída")

    # Localizar a posição do impostor dentro do mês ordenado
    impostor_final = buscar_registro_por_posicao(logs_mes_impostor_ordenados, indice_impostor - logs_ordenados_por_mes.index(impostor_log))
    if impostor_final:
        print(f"Impostor final encontrado: {impostor_final}")
    else:
        print(f"Impostor não encontrado após a ordenação dentro do mês")
else:
    print(f"Impostor não encontrado na posição {indice_impostor}")

print("Programa finalizado!")
