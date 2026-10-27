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
    

def main():
    print("1. Forloops Apps")
    print("2. Nestedloops Apps")
    apps = int(input("Pilih Aplikasi Yang Ingin Digunakan: "))
    if apps == 1:
        forloops_apps()
    elif apps == 2:
        nestedloops_apps()
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