import math as m

def Cosin(x):
    x = m.fabs(x) % (2 * m.pi)
    n = 0
    c = 0
    step = 1
    while m.fabs(step) > 0.0001:
        step = ((-1) ** n) * (x ** (2 * n)) / m.factorial(2 * n)
        c += step
        n += 1
    return c

def main():
    x = float(input("Nhap x: "))
    print("Gia tri gan dung cua cos(x) theo Taylor la: " + str(Cosin(x)))
    print("Gia tri cos(x) theo thu vien math la: " + str(m.cos(x)))

if __name__ == "__main__":
    main()