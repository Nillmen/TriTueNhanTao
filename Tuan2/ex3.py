import numpy as np

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def PhanLoaiPhuongTrinh(heSo):
    if heSo[2] == "":
        for i in range(len(heSo) - 1, 0, -1):
            heSo[i] = heSo[i - 1]
        heSo[0] = 0
        return "Phuong trinh bac nhat", heSo
    else:
        return "Phuong trinh bac hai", heSo

def GiaiPhuongTrinh(heSo):
    if heSo[0] == 0:
        if heSo[1] == 0:
            if heSo[2] == 0:
                return "Phuong trinh vo so nghiem"
            else:
                return "Phuong trinh vo nghiem"
        else:
            return "Phuong trinh co nghiem duy nhat: x = " + str(-heSo[2] / heSo[1])
    else:
        delta = heSo[1] ** 2 - 4 * heSo[0] * heSo[2]
        if delta < 0:
            return "Phuong trinh vo nghiem"
        elif delta == 0:
            return "Phuong trinh co nghiem kep: x1 = x2 = " + str(-heSo[1] / (2 * heSo[0]))
        else:
            return "Phuong trinh co hai nghiem phan biet: x1 = " + str((-heSo[1] + delta ** 0.5) / (2 * heSo[0])) + ", x2 = " + str((-heSo[1] - delta ** 0.5) / (2 * heSo[0]))

def main():
    a = input("Nhap he so a: ")
    while a == "" or not is_number(a):
        print("He so a khong duoc de trong hoac không phai la so!\n")
        a = input("Nhap he so a: ")
    b = input("Nhap he so b: ")
    while b == "" or not is_number(b):
        print("He so b khong duoc de trong hoac không phai la so!\n")
        print("he so a đã nhập: " + a)
        b = input("Nhap he so b: ")
    c = input("Nhap he so c (de trong neu la phuong trinh bac nhat): ")
    while not is_number(c) and c != "":
        print("He so c khong phai la so!\n")
        print("he so a đã nhập: " + a)
        print("he so b đã nhập: " + b)
        c = input("Nhap he so c (de trong neu la phuong trinh bac nhat): ")
    heSo = np.array([a, b, c])
    loaiPhuongTrinh, heSo = PhanLoaiPhuongTrinh(heSo)
    print("Phuong trinh da nhap la: " + loaiPhuongTrinh)
    heSo = heSo.astype(float)
    print(GiaiPhuongTrinh(heSo))

if __name__ == "__main__":
    main()