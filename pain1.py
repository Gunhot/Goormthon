# bandage : 1
# medicine : 7
# painkiller : 14
n = int(input())
count = 0

t = n // 14
n %= 14
count += t

t = n // 7
n %= 7
count += t

t = n // 1
n %= 1
count += t
print(count)