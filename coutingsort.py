# COUNTING SORT

def counting_sort(arr):
    if not arr:
        return arr
    maior = max(arr)
    menor = min(arr)
    faixa = maior - menor + 1
    count = [0] * faixa
    output = [0] * len(arr)

    for num in arr:
        count[num - menor] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - menor] - 1] = num
        count[num - menor] -= 1

    return output

# Vantagens:
# Muito rápido para valores inteiros pequenos
# Estável

# Desvantagens:
# Ineficiente para dados com intervalo grande
# Só funciona com inteiros
