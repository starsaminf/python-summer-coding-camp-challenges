if __name__ == '__main__':
    list = []
    unique = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
        unique.add(score)
    list.sort(key=lambda x:x[0])
    unique_sort = sorted(unique)
    for x in list :
        if x[1] == unique_sort[1]:
            print(x[0])