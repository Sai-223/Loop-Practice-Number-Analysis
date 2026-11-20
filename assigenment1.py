n = int(input("Enter n: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

n = int(input("Enter n: "))
m = int(input("Enter m: "))
count = 0
for i in range(n, m + 1):
    if i % 2 == 0:
        count = count + 1
print(count)

n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i)
    i = i + 2

n = int(input("Enter n: "))
m = int(input("Enter m: "))
div2 = 0
div3 = 0
for i in range(n, m + 1):
    if i % 2 == 0:
        div2 = div2 + 1
    if i % 3 == 0:
        div3 = div3 + 1
print(div2)
print(div3)