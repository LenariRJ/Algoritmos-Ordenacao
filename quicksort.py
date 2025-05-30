# QUICK SORT 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return quick_sort(menores) + iguais + quick_sort(maiores)

# Vantagens:
# Muito rápido na prática
# Complexidade média O(n log n)

# Desvantagens:
# Pior caso O(n²)
# Não é estável
# Requer uso de pilha (recursão)
