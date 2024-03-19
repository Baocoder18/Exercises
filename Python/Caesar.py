#Ma hoa
def maHoa(text, k):
    kq = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isspace()):
            kq += " "
        else:    
            if(char.isupper()):
                kq += chr((ord(char) + k - 65) % 26 + 65)
            else: 
                kq += chr((ord(char) + k - 97) % 26 + 97)
    return kq
text = str(input("Nhap text: "))
k = int(input("Nhap so k: "))
print("Thong tin duoc ma hoa: " + maHoa(text, k))

#Giai ma
def giaiMa(text, k):
    kq = ""
    for i in range(len(text)):
        char = text[i]
        if(char.isspace()):
            kq += " "
        else:
            if(char.isupper()):
                kq += chr((ord(char) - k - 65) % 26 + 65)
            else: 
                kq += chr((ord(char) - k - 97) % 26 + 97)
    return kq
text = str(input("Nhap text: "))
k = int(input("Nhap so k: "))
print("Thong tin duoc giai ma: " + giaiMa(text, k))