n = int(input("Enter: "))
a = 0
b = 1
list = []
for i in range(n+1):
    c = a+b
    list.append(c)
    print(c)
    a = b
    b = c

print("total sum is: ", sum(list))


