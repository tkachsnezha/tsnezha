def rec(a, b):
    if a == b:
        print(a)
    elif a < b:
        print(a)
        rec(a + 1, b)
    else:
        print(a)
        rec(a - 1, b)

        
rec(int(input()), int(input()))