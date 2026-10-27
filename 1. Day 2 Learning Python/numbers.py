# penjumlahan hardcode
# melakukan deklarasi variable z dan y dalam type data integer
z = 1
y = 2

# melakukan aritmatika sederhana dengan menjumlahkan variable z dan y
x = z + y

# lalu print hasil dari penjumlahan variable z dan y yang tersimpan dalam variable x
print("Hasil dari z + y adalah:",x)

# Membuat function untuk menggunakan calculator sederhana dengan input int untuk menghitung angka bulat
def calculator_non_float():
    # penjumlahan dengan input()
    # melakukan deklarasi variable z dan y dalam type data integer dengan menggunakan input()
    z = int(input("Masukkan angka pertama: ")) # int() digunakan untuk mengubah inputan yang defaultnya adalah str/ string menjadi integer
    y = int(input("Masukkan angka kedua: "))
    x = z + y
    print("Hasil dari z + y adalah:",x)

    # sistem calculator sederhana dengan menggunakan if dan else
    z = int(input("Masukan angka pertama: "))
    y = int(input("Masukan angka kedua: "))

    # memberikan pilihan untuk operasi aritmatika yang ingin dilakukan
    print("Pilih operasi aritmatika yang ingin dilakukan:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    # mendeklarasikan variable untuk menyimpan pilihan operasai yang akan digunakan untuk di masukan pada if dan else
    operasi = int(input("Masukan pilihan operasi (1/2/3/4): "))

    # membuat percabangan if dan else untuk setiap operasi aritmatika yang dipilih
    if operasi == 1:
        x = z + y
        print("Hasil penjumlahan dari", z, "+", y, "=", x)
    elif operasi == 2:
        x = z- y
        print("Hasil pengurangan dari", z, "-", y, "=", x)
    elif operasi == 3:
        x = z * y
        print("Hasil perkalian dari", z, "*", y, "=", x)
    elif operasi == 4:
        if y == 0:
            print("Error: Pembagian dengan nilai nol tidak diperbolehkan.")
        else:
            x = z / y
            print("Hasil pembagian dari", z, "/", y, "=", x)
    else:
        print("Pilihan yang dimasukkan tidak valid. Silahkan pilih antara 1,2,3, atau 4.")

# Membuat function untuk menggunakan calculator sederhana dengan input float untuk menghitung angka desimal
def calculator_float():
    # penjumlahan dengan input()
    # melakukan deklarasi variable z dan y dalam type data integer dengan menggunakan input()
    z = float(input("Masukkan angka pertama: ")) # float() digunakan untuk mengubah inputan yang defaultnya adalah str/ string menjadi float
    y = float(input("Masukkan angka kedua: "))
    x = z + y
    print("Hasil dari z + y adalah:",x)

    # sistem calculator sederhana dengan menggunakan if dan else
    z = float(input("Masukan angka pertama: "))
    y = float(input("Masukan angka kedua: "))

    # memberikan pilihan untuk operasi aritmatika yang ingin dilakukan
    print("Pilih operasi aritmatika yang ingin dilakukan:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    # mendeklarasikan variable untuk menyimpan pilihan operasai yang akan digunakan untuk di masukan pada if dan else
    operasi = int(input("Masukan pilihan operasi (1/2/3/4): "))

    # Memberikan pilihan untuk membulatkan hasil atau tetap menjadikannya desimal
    print("Pilih cara menampilkan hasil:")
    print("1. Tampilkan sebagai desimal")
    print("2. Bulatkan hasil")
    pilihan_tampilan = int(input("Masukan pilihan (1/2): "))

    # Pengamanan agar tidak memasukan input selain 1 dan 2
    if pilihan_tampilan not in [1, 2]:
        print("Pilihan yang dimasukkan tidak valid. Silahkan pilih antara 1 atau 2.")
        return  # Keluar dari fungsi jika input tidak valid

    # membuat percabangan if dan else untuk setiap operasi aritmatika yang dipilih
    if operasi == 1:
        x = z + y
        if pilihan_tampilan == 2:
            x = round(x)
        print("Hasil penjumlahan dari", z, "+", y, "=", x)
    elif operasi == 2:
        x = z- y
        if pilihan_tampilan == 2:
            x = round(x)
        print("Hasil pengurangan dari", z, "-", y, "=", x)
    elif operasi == 3:
        x = z * y
        if pilihan_tampilan == 2:
            x = round(x)
        print("Hasil perkalian dari", z, "*", y, "=", x)
    elif operasi == 4:
        if y == 0:
            print("Error: Pembagian dengan nilai nol tidak diperbolehkan.")
        else:
            x = z / y
            if pilihan_tampilan == 2:
                x = round(x)
            print("Hasil pembagian dari", z, "/", y, "=", x)
    else:
        print("Pilihan yang dimasukkan tidak valid. Silahkan pilih antara 1,2,3, atau 4.")

# Membuat menu pilihan antara calculator int atau float
print("Pilih jenis calculator yang ingin digunakan:")
print("1. Calculator untuk angka bulat (int)")
print("2. Calculator untuk angka desimal (float)")
pilihan_calculator = int(input("Masukan pilihan (1/2): "))

# Membuat if dan else untuk memilih calculator int atau float
if pilihan_calculator == 1:
    calculator_non_float()
elif pilihan_calculator == 2:
    calculator_float()
else:
    print("Pilihan yang dimasukkan tidak valid. Silahkan pilih antara 1 atau 2.")