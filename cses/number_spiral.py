n = int(input())

while n > 0:
    ls = [int(i) for i in input().split()]
    x = ls[0]
    y = ls[1]
    ans = 0
    if x > y:
        if x % 2 == 0:
            ans  = (x * x) - y + 1
        else:
            ans = ((x-1) * (x-1)) + y
    else:
        if y % 2 != 0:
            ans = (y * y) - x + 1
        else:
            ans = ((y-1) * (y-1)) + x
    print(ans)
    n -= 1