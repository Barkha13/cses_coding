n =  int(input())
ls = [int(i) for i in input().split()]

count = 0
prev = ls[0]
for i in range(1, n):
    if ls[i] < prev:
        diff = prev - ls[i]
        ls[i] += diff
        count += diff
    prev = ls[i]
print(count)