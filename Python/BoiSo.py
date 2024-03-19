def test(n):
    if n%7==0 and n%5!=0: return True
    else: return False
for i in range (1999, 3201):
    if test(i)==True: print(i, end=", ")
