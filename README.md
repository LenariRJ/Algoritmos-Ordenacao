# BUBBLE SORT

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Vantagens:
# Muito simples de entender
# Estável

# Desvantagens:
# Extremamente ineficiente (O(n²))
# Pouco prático para listas grandes
