num = (1, 2, 3, 4)
fruits = ["orange", "apple", "kiwi"]
for num in num: 
    print(num)
print("-------")
for fruits in fruits:
    print(fruits)
tong = 0

for i in range(1,101,1):
    tong = tong + i
    print(i)
print("Tong tu 1 den 100: ", tong)
print("----------------------")
n = int(input("Nhap n: "))
tong = 0
i = 0
while i <= n:
    tong = tong + i
    i = i + 1
print("Tong: ", tong)