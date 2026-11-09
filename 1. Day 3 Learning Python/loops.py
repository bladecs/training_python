import random

def menu():
    print("-"*22)
    print("|"," "*((10//2)-3),"1"," "*((10//2)-3),"|","DIAMON"," ","|")
    print("|"," "*((10//2)-3),"2"," "*((10//2)-3),"|","SQUARE"," ","|")
    print("|"," "*((10//2)-3),"3"," "*((10//2)-3),"|","TRIANGLE","|")
    print("-"*22)
    print("|"," "*3,"Menu Bentuk"," "*2,"|")
    print("-"*22)

def forloops_apps():
    menu()
    bentuk = int(input("Pilih Bentuk Yang Ingin Di Buat: "))
    if bentuk == 1:
        diamon()
    elif bentuk == 2:
        square()
    elif bentuk == 3:
        triangle()
    else:
        print("Menu yang dinputkan tidak ada!")
        exit()

def nestedloops_apps():
    # Fizzbuzz script
    n = int(input("Masukan jumlah panjang loops pertama: "))

    result = []

    for i in range(n):
        if i % 1 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 1 == 0:
            print("Fizz")
        elif i % 3 == 0:
            print("Buzz")
        else:
            print(i)
        for y in range(n):
            if y % 3 == 0 and y % 5 == 0:
                print("FizzBuzz")
            elif y % 3 == 0:
                print("Fizz")
            elif y % 5 == 0:
                print("Buzz")
            else:
                print(i)

def random_number_guessing():
    numbers = []
    for i in range(5):
        number = int(input("Masukan angka acak: "))
        numbers.append(number)
    
    random_number = random.choice(numbers)

    for i in range(3):
        geussing_number = int(input("Masukan angka tebakan anda: "))
        if geussing_number == random_number:
            print("Tebakan Anda Benar!!!")
            break
        else:
            print("Tebakan anda Salah, Silahkan Coba Lagi")
    

def main():
    print("1. Forloops Apps")
    print("2. Nestedloops Apps")
    print("3. Random Number Guessing Apps")
    apps = int(input("Pilih Aplikasi Yang Ingin Digunakan: "))
    if apps == 1:
        forloops_apps()
    elif apps == 2:
        nestedloops_apps()
    elif apps == 3:
        random_number_guessing()
    else:
        print("Input tidak valid! Pilih (1/2)")

# Penggunaan For Loops untuk membuat sebuah bentuk bidang datar
def diamon():
    # Inisiasi panjang loop yg akan di lakukan
    n = 5
    for i in range(n): # for akan berjalan dalam range n sebagai panjang loopnya ya itu sampai (0,1,2,3,4)
        print(" "*(n-i-1)+"*"*(2*i-1)) # ini akan menciptakan bentuk segitiga sama sisi
    for i in range(n-2,-1,-1): # for ini akan berjalan mundur dari range yang telah di tentukan -1 pertama berfungsi sebagai limit sedangkan -1 kedua berfungsi untuk mengurangi index loopsnya
        print(" "*(n-i-1)+"*"*(2*i-1)) # ini akan menciptakan bentuk segitiga sama sisi terbalik

def square():
    n = 5
    for i in range(n):
        if i == 0 or i == n-1:
            print("* "*n)
        else:
            print("*"," "*(n),"*")

def triangle():
    n = 5
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i-1))

main()