def selectionSort(a):
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if(a[j] < a[i]):
                a[i],a[j] = a[j],a[i]

def main():
    a = [2, 97, 86, 64, 50, 80, 3, 71, 8, 76]
    selectionSort(a)
    print(a)

if __name__ == '__main__':main()
