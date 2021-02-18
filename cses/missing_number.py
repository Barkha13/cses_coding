n = int(input())
ls = [int(i) for i in input().split()]

total = 0
for i in range(1, n+1):
    total += i

for num in ls:
    total -= num

print(total)