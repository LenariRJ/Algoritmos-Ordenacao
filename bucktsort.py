# BUCKET SORT

def insertion_sort_bucket(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    num_buckets = 10
    max_val = max(arr)
    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        index = int(num / max_val * (num_buckets - 1))
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(insertion_sort_bucket(bucket))
    return sorted_arr

# Vantagens:
# Muito eficiente quando os dados são uniformemente distribuídos
# Pode ter desempenho linear

# Desvantagens:
# Desempenho depende da distribuição dos dados
# Pode exigir muita memória
