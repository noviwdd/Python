import math
import sys

def lingkaran():
    print("\n---------------------------")
    print(" Menghitung Luas Lingkaran")
    print("---------------------------")
    r = int(input("Masukkan jari-jari : "))
    luas = 22/7 * r * r
    print("Luas Lingkaran : ", luas)
    tanya()

def persegi():
    print("\n---------------------------")
    print(" Menghitung Luas Persegi")
    print("---------------------------")
    s = int(input("Masukkan panjang sisi : "))
    luas = s * s
    print("Luas Persegi : ", luas)
    tanya()

def segitiga():
    print("\n---------------------------")
    print(" Menghitung Luas Segitiga")
    print("---------------------------")
    a = int(input("Masukkan alas : "))
    t = int(input("Masukkan tinggi : "))
    luas = 0.5 * a * t
    print("Luas Segitiga : ", luas)
    tanya()

def fibonacci():
    print("\n---------------------------")
    print(" Segitiga Fibonacci")
    print("---------------------------")
    un = int(input("Masukkan suku : "))
    hasil = (un-1)+(un-2)
    print("Hasilnya Adalah :", hasil)
    tanya()

def siku():
    print("\n---------------------------")
    print(" Segitiga Siku-Siku")
    print("---------------------------")
    sisi = input("Sisi yang ingin di cari [a, b, c] : ")
    if sisi == "a":
        b = int(input("Masukkan panjang sisi b : "))
        c = int(input("Masukkan panjang sisi c : "))
        a = math.sqrt((c*c)-(b*b))
        print("Panjang sisi a adalah : " , a)
        tanya()
    elif sisi == 'b':
        a = int(input("Masukkan panjang sisi a : "))
        c = int(input("Masukkan panjang sisi c : "))
        b = math.sqrt((c*c)-(a*a))
        print("Panjang sisi b adalah : " , b)
        tanya()
    elif sisi == 'c':
        a = int(input("Masukkan panjang sisi a : "))
        b = int(input("Masukkan panjang sisi b : "))
        c = math.sqrt((a*a)+(b*b))
        print("Panjang sisi c adalah : " , c)
        tanya()
    else:
        print("\nPilihan yang anda masukkan salah!")
        siku()
        


def menu():
    print("\nPilih Program :")
    print("	1. Menghitung Luas Lingkaran")
    print("	2. Menghitung Luas Persegi")
    print("	3. Menghitung Luas Segitiga")
    print("	4. Segitiga Fibonacci")
    print("	5. Segitiga Siku-Siku")
    print("	6. Exit")

    pilih = int(input("Masukkan pilihan [1-6] : "))

    if pilih == 1:
        lingkaran()
    elif pilih == 2:
        persegi()
    elif pilih == 3:
        segitiga()
    elif pilih == 4:
        fibonacci()
    elif pilih == 5:
        siku()
    elif pilih == 6:
        print("Terima kasih sudah menggunakan aplikasi ini!")
        sys.exit()
    else:
        print("\nPilihan yang anda masukkan salah!")
        menu()

def tanya():
    print("\n-----------------------------------------")
    tanya = input(" Ingin mengulang aplikasi lagi? [y/t] : ")
    print("-----------------------------------------")
    if tanya == "y":
        menu()
    elif tanya == "t":
        sys.exit()
    else:
        print("Pilihan yang anda masukan salah!")

menu()
