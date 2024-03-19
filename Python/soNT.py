n = int(input("Nhap n: "))
def ktraSNT(n): 
    if n < 2: return False
    for i in range(2,n):
        if n % i == 0: return False
    return True
print(ktraSNT(n))
for i in range(2,n): 
    if ktraSNT(i): print(i)