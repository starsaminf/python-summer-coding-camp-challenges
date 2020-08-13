n = int(input())
array = list(map(int, input().split()))

if all([x >= 0 for x in array]):
    sw = False
    for element in array:
        aux = list(str(element))
        original = list(str(element))
        aux.reverse()
        if aux == original:
            print(True)
            sw = True
            break
    if sw == False:
        print(False)
else:
    print(False)


## sol2
n = int(input())
array = list(map(int, input().split()))

if all([x >= 0 for x in array]):
        print(any([str(element) == str(element)[::-1] for element in array]))
else:
    print(False)

## sol3

n = int(input())
array = list(map(int, input().split()))
print(all([x >= 0 for x in array]) and any([str(element) == str(element)[::-1] for element in array]))