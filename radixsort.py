# RADIX SORT

def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in reversed(arr):
        index = (i // exp) % 10
        output[count[index] - 1] = i
        count[index] -= 1
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_exp(arr, exp)
        exp *= 10
    return arr

# Vantagens:
# Complexidade linear para inteiros com número limitado de dígitos
# Estável

# Desvantagens:
# Requer estrutura auxiliar (counting sort)
# Só funciona com inteiros
