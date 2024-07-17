import ijson
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

def radix_sort(input_array):
    # Encontrar o valor máximo de monthIndex (0 a 11) e log number
    max_month = 11
    max_log_number = max(log.number for log in input_array)

    # Ordenar pelos meses (mais significativo)
    input_array = counting_sort(input_array, lambda log: log.monthIndex, max_month)


    return input_array

def ler_json_grande(path):
    with open(path, 'rb') as f:
        objetos = ijson.items(f, 'item')
        for objeto in objetos:
            log = Log(objeto['month'], objeto['log'], objeto['msg'], objeto['user'])
            dados_json.append(log)

# Exemplo de uso
filename = 'data.json'  # Nome do arquivo com os registros de log em formato JSON
ler_json_grande(filename)



start_time = time.time()
dados_json = radix_sort(dados_json)
end_time = time.time()

print("\nTempo de Ordenação: %s segundos" % (end_time - start_time))
print("Ordenação por mês e número do log concluída")

# Printando alguns logs para verificação (opcional)
# Ordenar os logs usando radix sort
for log in dados_json[:10]:  # Print the first 10 logs for verification
    print(log)

print("Programa finalizado!")

"""
    # Ordenar pelos números dos logs (menos significativo)
    input_array = counting_sort(input_array, lambda log: log.number, max_log_number)
"""