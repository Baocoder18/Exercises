# # Truyen du lieu
# print("Ten = {0}, Ho = {1}".format("titv", "vn"))
 
# a = input("Nhap vao a: ")
# print("a = {0}".format(a))
# # Nhap du lieu 
# ho = input("Nhap vao ho: ")
# ten = input("Nhap vao ten: ")
# print("Xin chao", ho, ten)

# #In ra kieu du lieu
# x = 1
# print(type(x))
# x = 1.0
# print(type(x))
# x = 1 + 2j
# print(type(x))
# x = 'abc'
# print(type(x))
# x = True
# print(type(x))
# e =  2.72
# pi = "3.14"
# text = "Hello World"
# print("Kieu du lieu bien e:", type(e), "Kieu du lieu bien pi:", type(pi), "Kieu du lieu text:", type(text))

# #Ep kieu du lieu
# a = 5
# b = 2.0
# c = a/b
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))

# n = 100
# m = "200"
# print(n+ int(m))
# print(str(n)+ m)

# #Cac phep toan so hoc
# a = int(input("Nhap vao so a: "))
# b = int(input("Nhap vao so b: "))
# print("{0}+{1}={2}".format(a, b, a+b))
# print("{0}-{1}={2}".format(a, b, a-b))
# print("{0}*{1}={2}".format(a, b, a*b))
# print("{0}/{1}={2}".format(a, b, a/b))
# print("{0}**{1}={2}".format(a, b, a**b))
# print("{0}%{1}={2}".format(a, b, a%b))
# print("{0}//{1}={2}".format(a, b, a//b))  

# # Cac toan tu so sanh va logic
# x = int(input("x = "))
# y = int(input("y = "))
# print("{0} < {1} la {2}". format(x, y, x<y))
# print("{0} > {1} la {2}". format(x, y, x>y))
# print("{0} == {1} la {2}". format(x, y, x==y))
# print("{0} <= {1} la {2}". format(x, y, x<=y))
# print("{0} >= {1} la {2}". format(x, y, x>=y))
# print("{0} != {1} la {2}". format(x, y, x!=y))

# z = int(input("Nhap z: "))
# print("{0} < {1} and {2} < {3} = {4}".format(x, y, y, z, (x <y) and (y<z)))
# print("{0} < {1} or {2} < {3} = {4}".format(x, y, y, z, (x < y) or (y < z)))
# print("not {0} > {1} = {2}".format(x, z, not(x > z)))

# # Thu vien toan hoc 
# import math
# x = float(input("Nhap x: "))
# print("|x| = ", math.fabs(x))
# print("pi = ", math.pi)
# print("e = ", math.e)
# print("sqrt(x) = ", math.sqrt(x))
# print("ceil(x) = ", math.ceil(x)) #Lam tron len
# print("floor(x) = ", math.floor(x)) #Lam tron xuong
# print("pow(x) = ", math.pow(x,2))

# #Toan tu dieu kien
# x = int(input("Nhap x: "))
# y = int(input("Nhap y: "))
# kq = "x lon hon y" if(x > y) else "x be hon y"
# print(kq)

# # Cau lenh re nhanh if else
# x = int(input("Nhap x: "))
# if x >= 0: 
#     print(x, "la so duong")
# else: 
#     print(x, "la so am")
# if x >= 9:
#     print("Ban la hoc sinh gioi")
# elif x <= 5: 
#     print("Ban la hoc sinh kem")

# # Kieu du lieu List
# # In ra toan bo gia tri 
# colors = ["red", "green", "blue"]
# print(colors)
# # List co thu tu, vi tri duoc danh dau tu 0, tu trai sang phai
# studentList = ["An", "Binh", "Ngan", "Vy"]
# print(studentList[2])
# #studentList[x:y] => Lay ra [x:y)
# print(studentList[0:1])
# print(studentList[0:2])
# print(studentList[0:3])
# #Them 1 phan tu vao list
# studentList.append("Thien")
# print(studentList)
# #Chen 1 phan tu vao list
# studentList.insert(2, "Ngoc")
# print(studentList)
# #Them phan tu vao cuoi list
# studentList[len(studentList):] = ["Thanh"]
# print(studentList)
# #Dem so luong phan tu thoa man dieu kien
# print("Dem Ngoc:", studentList.count("Ngoc"))
# #Xoa phan tu
# studentList.remove("Thanh")
# print(studentList)
# #Xoa phan tu theo vi tri
# studentList.pop(1)
# print(studentList)
# #Dao nguoc list
# studentList.reverse()
# print(studentList)
# #Sap xep
# numbers = [7,4,5,2,3,1]
# numbers.sort()
# print(numbers)

# #Vong lap for
# n = int(input("Nhap n: "))
# sum = 0
# for i in range(n+1):
#     sum += i
# print("Tong =", sum)
# #Vong lap for co buoc tang tuy chinh
# for i in range(0,10,2):   #Chay tu 0 -> 10, moi lan tang len 2 don vi
#     print(i)
# colors = ["red", "green", "yellow"]
# for color in colors:
#     print(color)
# #Vong lap for duyet phan tu theo vi tri
# for i in range(len(colors)):
#     print(colors[i])

# #In bang cuu chuong
# for j in range(2,10):   
#     print("Bang cuu chuong", j)
#     for i in range(1,11):
#         print("{0} x {1} = {2}".format(j, i, i*j))

# #Kieu du lieu String
# #Cong chuoi
# s1 = "Xin chao"
# s2 = " Bao Coder"
# print(s1 + s2)
# #Chuoi nhieu dong
# chuoi_nhieu_dong = '''
# Dong 1
# Dong 2
# Dong 3
# '''
# print(chuoi_nhieu_dong)
# #Lap lai chuoi
# chep_phat = "Em hua lam bai day du\n"
# chep_phat_10 = chep_phat * 10
# print(chep_phat_10)
# #Viet hoa chu dau cua chuoi
# s = "hom nay troi dep qua!"
# s = str.capitalize(s)
# print(s)
# #Viet hoa toan bo chuoi
# s = s.upper()
# print(s)
# #Viet thuong toan bo chuoi
# s = s.lower()
# print(s)
# #Tim va dem so luong chuoi con
# s = "Lap trinh python"
# print(s.find("python"))
# print(s.count("python"))
# #Cat chuoi thanh mot list
# list1 = s.split(" ")
# print(list1)
# #Thay the chuoi
# s = s.replace("python", "java")
# print(s)
# #Lay chuoi con
# print(s[0:10])

# # Vong lap while
# n = -1
# while(n <= 0):
#     n = int(input("Nhap n: "))
# i = 0
# tong = 0
# while(i<=n):
#     tong += i
#     i += 1
# print(tong)
# print(i)
# j = 0
# while(j <= 10):
#     print(j, "ben trong vong lap")
#     j += 1
#     if(j >= 5): break
# else: 
#     print(j, "ben ngoai vong lap")

# # Chuyen so thap phan sang nhi phan
# n = -1
# while(n <= 0):
#     n = int(input("Nhap n > 0: "))
    
# ketqua = ""
# while(n>0):
#     ketqua = str(n%2) + ketqua
#     print("n%2 = ", n%2)
#     n //= 2
#     print("n = ", n//2)
# print("Ket qua: ", ketqua)

# # Cau lenh break va continue
# for i in range(0,10):
#     print(i)
#     if(i > 5): 
#         break

# n = 100
# while (n > 0):
#     print(n)
#     n = n//2
#     if(n<50):
#         break

# for i in range(2,10):
#     for j in range(1,11):
#         print("{0} x {1} = {2}".format(i, j, i*j))
#         if(j > 5):
#             break
#     print("\n")

# for i in range(0,10):
#     if(i%2==1): 
#         continue
#     print(i)

# # Tuple => Gia tri cua Tuple khong the thay doi
# gioiTinh = ("nam", "nu")
# lopHoc = (1,2,3,4,5,6,7,8,9)
# traiCay = ("Tao", "Chuoi", "Cam", "Tao", "Dua hau")
# print(gioiTinh[0])
# print(traiCay[0:2])
# for i in traiCay:
#     print(i)
# # Cong Tuple
# y = (1,2,3) + (4,5,6)
# print(y)
# # Nhan Tuple
# y = (1,2,3)*2
# print(y)
# # Kiem tra phan tu co trong Tuple hay khong
# print("Tao" in traiCay)
# # Lay so luong phan tu cua Tuple
# x = len(traiCay)
# print(x)
# #Dem so luot xuat hien
# print(traiCay.count("Tao"))
# # Tim min, max va tinh sum
# print("Min: ", min(lopHoc))
# print("Max: ", max(traiCay))
# print("Tong: ", sum(lopHoc))
# #Sap xep va chuyen ve List
# listTC = sorted(traiCay)
# print(listTC)

# # Kieu du lieu Set
# monHoc = {"Toan", "Ly", "Hoa"}
# print(monHoc)
# #Duyet cac phan tu ben trong Set
# for i in monHoc:
#     print(i)
# #Them phan tu vao trong Set
# monHoc.add("Lich su")
# print(monHoc)
# hocThem = {"Anh Van", "Dan Guitar"}
# monHoc.update(hocThem)
# print(monHoc)
# #Them list vao Set
# hocPhuDao = ["Vo thuat", "Mua", "Vo thuat"]
# print(hocPhuDao)
# monHoc.update(hocPhuDao)
# print(monHoc)
# #Xoa 
# monHoc.remove("Vo thuat")
# print(monHoc)   
# monHoc.discard("Vo thuat")
# print(monHoc)
# monHoc.pop()
# print(monHoc)
# monHoc.clear()
# print(monHoc)

# # Bai tap rut tham trung thuong
# import random
# thungPhieu = set()

# while(True):
#     print("-----MENU-----")
#     print("Vui long lua chon chuc nang: ")
#     print("1 - Them mot so dien thoai vao thung phieu du thuong")
#     print("2 - Xoa mot so dien thoai tu thung phieu trung thuong")
#     print("3 - Quay so ngau nhien lay ra mot so dien thoai trung thuong")
#     print("4 - Ket thuc")
    
#     print("Thung phieu hien tai: ")
#     print(thungPhieu)
#     luaChon = int(input("Lua chon: "))
#     if(luaChon == 1):
#         soDienThoai = input("Nhap vao so dien thoai du thuong: ")
#         thungPhieu.add(soDienThoai)
#     elif (luaChon == 2):
#         soDienThoai = input("Nhap vao so dien thoai can xoa: ")
#     elif (luaChon == 3): 
#         index = random.randint(0, len(thungPhieu))
#         print("Vi tri trung thuong: " + str(index))
        
#         i = 0
#         for x in thungPhieu:
#             if(i==index):
#                 break
#             i = i+1
#         print("Chuc mung so dien thoai: " + x + " da trung thuong")
#         thungPhieu.discard(x)
#     else: 
#         break;
#     x = input("Nhap phim bat ky de tiep tuc:    ")

# # Kieu du lieu Dictionary
# sinhVien = {
#     "hoVaTen" : "Nguyen Van A",
#     "maLop" : "DH01",
#     "diemTB" : 8.5
# }
# print(sinhVien)

# print(sinhVien["hoVaTen"])
# #Su dung get de lay gia tri
# print(sinhVien.get("maLop"))

# #Cap nhat gia tri
# sinhVien["maLop"] = "DH02"
# print(sinhVien)
# sinhVien.update({"maLop" : "DH03", "diemTB" : 8.6})
# print(sinhVien)

# #Them cap key:value
# sinhVien["namHoc"] = "2025"
# print(sinhVien)
# sinhVien.update({"noiSinh" : "Hanoi"})
# print(sinhVien)

# #Loai bo muc
# sinhVien.pop("noiSinh")
# print(sinhVien)
# sinhVien.popitem()
# print(sinhVien)
# del sinhVien["hoVaTen"]
# print(sinhVien)

# # Clear
# sinhVien.clear()
# print(sinhVien)

# # Duyet cac gia tri
# for i in sinhVien:
#     print(i)

# # Duyet cac khoa
# for i in sinhVien.values():
#     print(i)
# # Duyet cac cap khoa - gia tri
# for x, y in sinhVien.items():
#     print(x, y)

# #Xay dung mot tu dien
# tuDien = {}
# while(True):
#     print("Vui long lua chon chuc nang: ")
#     print("""
#         1. Them mot tu vung moi (kem nghia cua tu vung) vao tu dien)\n
#         2. Tra cuu y nghia cua mot tu vung\n
#         3. Cap nhat y nghia cho mot tu vung\n
#         4. Cho phep nguoi dung xoa di 1 tu vung trong tu dien\n
#         5. Cho phep nguoi dung xoa toan bo tu vung\n
#         6. Cho phep nguoi dung in ra toan bo tu vung\n
#         7. Cho phep nguoi dung in ra toan bo tu dien theo cau truc:  "Tu vung" : "Y nghia"\n
#         8. Ket thuc chuong trinh\n
#     """)
#     luaChon = int(input("Nhap vao lua chon cua ban: "))
#     if(luaChon == 1 or luaChon == 3):
#         tuVung = input("Nhap vao tu vung: ")
#         yNghia = input("Nhap vao y nghia: ")
#         tuDien[tuVung] = yNghia
#         print("Da them hoac cap nhat du lieu")
#     elif(luaChon == 2): 
#         tuVung = input("Nhap vao tu vung: ")
#         print("Y nghia: ", tuDien[tuVung])
        
#     elif(luaChon == 4): 
#         tuVung = input("Nhap vao tu vung can xoa: ")
#         tuDien.pop(tuVung)
#         print("Da xoa du lieu")
#     elif(luaChon == 5): 
#         tuDien.clear()
#         print("Da xoa toan bo du lieu")
#     elif(luaChon == 6): 
#         print("Danh sach cac tu vung co trong tu dien: ")
#         for x in tuDien.keys():
#             print(x)
#     elif(luaChon == 7): 
#         print("Danh sach cac tu vung co trong tu dien: ")
#         for x, y in tuDien.items():
#             print(x, ":", y)
#     elif(luaChon == 8): 
#         break
#     else:
#         print("Nhap lua chon khong dung")

# #Function
# def xinChao():
#     print("Hello Friend")
# xinChao()

# def xinChao(hoVaTen):
#     print("Xin chao: " + hoVaTen)
# xinChao("BaoCoder")

# def xinChao(ho, chuLot, ten):
#     print("Xin chao ban: " + ho + chuLot + ten)
# xinChao("Bao", " Coder", " Kim")

# #Khi khong xac dinh duoc doi so, ta co the su dung dau *
# def thoiKhoaBieu(*monHoc):
#     print("Mon 1: " + monHoc[0])
#     print("Mon 2: " + monHoc[1])
#     print("Mon 3: " + monHoc[2])
# thoiKhoaBieu("Toan", "Ly", "Hoa", "Su", "Dia")

# def tinhTong(*giaTri):
#     sum = 0
#     for x in giaTri:
#         sum = sum + x
#     print(sum)
# tinhTong(1,2)
# tinhTong(1,4,7,8,9,5)

# def xinChao(**ten):
#     print("Xin chao: " + ten["ho"])
# xinChao(ten = "Bao", chuLot = "Coder", ho = "Kim")

# def tinhTich(*giaTri):
#     tich = 1
#     for x in giaTri:
#         tich = tich*x
#     return tich
# tich1 = tinhTich(1, 4, 6)
# tich2 = tinhTich(7, 4, 6)   
# tong = tich1 + tich2
# print(tong)

# #Bai tap tim USCLN
# def gcd(a,b):
#     while(a!=b):
#         if(a>b):
#             a = a - b
#         else:
#             b = b - a
#     return a
# print(gcd(11,121))

# #Bai tap nhap vao 1 day (n) so tu ban phim, sau do tinh tong
# list_number = []
# while(True):
#     try: 
#         n = int(input("Nhap vao so luong: "))
#     except: 
#         print("Vui long nhap n >= 1")
#     if(n >= 1):
#         break
# def nhap(n, list_number):
#     for i in range(n):
#         list_number.append(int(input("Nhap vao gia tri thu " + str(i) + ": ")))
# def tinhTong(list_number):
#     tong = 0
#     for x in list_number:
#         tong += x
#     return tong
# nhap(n, list_number)
# print("Tong = " + str(tinhTong(list_number)))

# # Lambda Function
# kiemTraSoChan = lambda a : (a%2==0)
# print(kiemTraSoChan(4))
# print(kiemTraSoChan(5))

# tinhTong = lambda a, b : a + b
# print(tinhTong(5,10))

# def hamMu(n):
#     return lambda x : x**n
# hamMu2 = hamMu(2)
# hamMu3 = hamMu(3)
# hamMu4 = hamMu(4)
# print(hamMu2(3))
# print(hamMu3(3))
# print(hamMu4(3))
