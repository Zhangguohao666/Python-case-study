def merge(left, right):
    merged = []
    i, j = 0, 0
    left_len, right_len = len(left), len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    return merge(left, right)

def main():
    a = [59, 12, 77, 64, 72, 69, 46, 89, 31, 9]
    print(mergeSort(a))

if __name__ == '__main__':main()
