if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique = set(arr)
    array  = list(unique)
    array.sort(reverse=True)
    print(array[1])