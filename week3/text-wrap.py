def wrap(string, max_width):
    i = 0
    sol = ""
    for x in range(0, len(string)):
        sol = sol + string[x]
        i = i + 1
        if i % max_width == 0:
            sol = sol + "\n"
    return sol

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

