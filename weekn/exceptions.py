n = int(input())

for i in range(0, n):
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

