def insertSort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if(a[j-1] > a[j]):
                a[j-1],a[j] = a[j],a[j-1]

def main():
    a = [2, 97, 86, 64, 50, 80, 3, 71, 8, 76]
    insertSort(a)
    print(a)

if __name__ == '__main__':main()
