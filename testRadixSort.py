import json
import time

def radix_sort_logs(logs):
    # Lista ordenada de meses
    meses_ordem = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Função para extrair o mês e o número do log no mês
    def get_month_and_log_number(log):
        return meses_ordem.index(log['month']), log['log']

    # Função de ordenação estável por mês e número do log no mês
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

    # Ordenar primeiro por número do log no mês, depois por mês
    logs_sorted_by_log_number = stable_sort(logs, lambda x: x['log'])
    logs_sorted = stable_sort(logs_sorted_by_log_number, lambda x: (meses_ordem.index(x['month']), x['log']))
    
    return logs_sorted

# Função para carregar os dados do arquivo JSON
def load_logs_from_json(filename):
    with open(filename, 'r') as file:
        logs = json.load(file)
    return logs

# Função para salvar os logs ordenados em um arquivo JSON
def save_logs_to_json(logs, filename):
    with open(filename, 'w') as file:
        json.dump(logs, file)

# Exemplo de uso
filename = 'data.json'  # Nome do arquivo com os registros de log em formato JSON
logs = load_logs_from_json(filename)

# Ordenar os logs usando Radix Sort
start_time = time.time()
logs_ordenados = radix_sort_logs(logs)
end_time = time.time()
print("\nTempo Radix Sort: %s seconds" % (end_time - start_time))
print("Ordenação concluída")

# Salvar os logs ordenados em um novo arquivo JSON
filename_ordenado = 'logs_ordenados.json'  # Nome do arquivo para os logs ordenados
save_logs_to_json(logs_ordenados, filename_ordenado)
print("Programa finalizado!")