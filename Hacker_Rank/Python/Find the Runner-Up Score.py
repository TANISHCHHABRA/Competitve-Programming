if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = max(arr)
    while True:
        if a in arr:
            arr.remove(a)
        else:
            break
    print(max(arr))
