# INSERTION SORT

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

# Vantagens:
# Bom desempenho com listas pequenas ou quase ordenadas
# Estável
# In-place

# Desvantagens:
# Complexidade O(n²) no pior caso
