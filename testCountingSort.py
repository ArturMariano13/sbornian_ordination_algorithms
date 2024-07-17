import json
import time

def counting_sort_logs(logs):
    meses_ordem = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Função para extrair o mês e o número do log no mês
    def get_month_and_log_number(log):
        return meses_ordem.index(log['month']), log['log']

    # Encontre o maior número de log e índice de mês
    max_month_index = len(meses_ordem) - 1
    max_log_number = max(log['log'] for log in logs)

    # Contagem de ocorrências para o número de log e para o mês
    count_log = [0] * (max_log_number + 1)
    count_month = [0] * len(meses_ordem)

    for log in logs:
        count_log[log['log']] += 1
        count_month[meses_ordem.index(log['month'])] += 1

    # Atualize as contagens para as posições corretas
    for i in range(1, len(count_log)):
        count_log[i] += count_log[i - 1]

    for i in range(1, len(count_month)):
        count_month[i] += count_month[i - 1]

    # Ordenar os logs
    sorted_logs = [None] * len(logs)
    for log in reversed(logs):
        month_index, log_number = get_month_and_log_number(log)
        sorted_index = count_month[month_index] - 1
        sorted_logs[sorted_index] = log
        count_month[month_index] -= 1

    return sorted_logs

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

# Ordenar os logs usando Counting Sort
start_time = time.time()
logs_ordenados = counting_sort_logs(logs)
end_time = time.time()

print("Counting Sort concluído!")
print("\nTempo Counting Sort: %s seconds" % (end_time - start_time))

# Salvar os logs ordenados em um novo arquivo JSON
filename_ordenado = 'logs_ordenados.json'  # Nome do arquivo para os logs ordenados
save_logs_to_json(logs_ordenados, filename_ordenado)
print("Arquivo ordenado salvo com sucesso!")
