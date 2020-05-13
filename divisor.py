num = int(input("num is"))
number = num + 1
print("num+1 is",number)
div = []
for i in range(1, number):
    if num % i == 0:
        div.append(i)

print(div)
