s = input()

count = 1
count_so_far = 1
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        count_so_far += 1
    else:
        count_so_far = 1
    count = max(count, count_so_far)

print(count)