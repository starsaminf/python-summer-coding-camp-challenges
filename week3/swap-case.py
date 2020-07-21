def swap_case(s):
    ans = ""
    for x in(s):
        if x >= 'a' and x <= 'z':
            ans = ans + x.upper()
        elif x >= 'A' and x <= 'Z':
            ans = ans + x.lower()
        else:
            ans = ans + x

    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

