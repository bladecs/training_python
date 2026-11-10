import json
import os

# Membuat konstanta untuk nama file yang akan digunakan
FILE_NAME = "todo_data.json"

def muat_data():
    # Membaca data tugas dari file JSON jika filenya tersedia
    if not os.path.exists(FILE_NAME):
        return [] # Mengembalikan list kosong jika file belum dibuat

    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # jika file rusak, list dimulai dalam keadaan kosong
        return []

def simpan_data(tugas):
    # Menggunakan library os dengan syntax 'w' sebagai write untuk menulis kedalam json
    with open(FILE_NAME, 'w') as file:
        json.dump(tugas, file, indent=4)

def tampilkan_tugas(tugas):
    # Menampilkan tugas yang sudah tersimpan di file json
    print("\n" + "="*30)
    print(" Daftar Tugas Saya ")
    print("="*30)

    if not tugas:
        print("Belum ada tugas. silahkan tambahkan")
    else:
        for index, item in enumerate(tugas):
            # Menentukan simbol berdasarkan status 'selesai'
            simbol = "[x]" if item["selesai"] else "[ ]"
            print(f"{index + 1}.{simbol} {item['nama']}")
    print("="*30)

def main():
    # 1. Memuat data ke memori ram dalam bentuk list
    daftar_tugas = muat_data()

    while True:
        tampilkan_tugas(daftar_tugas)
        print("Menu : [1] Tambah   [2] Tandai Selesai  [3] Hapus  [4] Keluar")
        menu = int(input("Masukan pilihan menu: "))

        # 2. Membaca menu yg dipilih dan melakukan ubah data pada memori
        if menu == 1:
            nama_tugas = input("Masukan nama tugas baru: ")
            daftar_tugas.append({
                "nama" : nama_tugas,
                "selesai" : False
            }) # Menambahkan data ke list yg ada dalam memori ram
            simpan_data(daftar_tugas) # Lalu disimpan di hard filenya
            print(f" '{nama_tugas}' berhasil ditambahkan! ")

        elif menu == 2:
            try:
                nomor = int(input("Nomor tugas yang sudah selesai: "))
                if 1 <= nomor <= len(daftar_tugas):
                    daftar_tugas[nomor-1]["selesai"] = True
                    simpan_data(daftar_tugas)
                    print("Status tugas telah diperbarui!")
                else:
                    print("Nomor tugas tidak ditemukan.")
            except ValueError:
                print("Harap masukan angka yg valid")

        elif menu == 3:
            try:
                nomor = int(input("Nomor tugas yang ingin dihapus: "))
                if 1 <= nomor <= len(daftar_tugas):
                    tugas_terhapus = daftar_tugas.pop(nomor - 1)
                    simpan_data(daftar_tugas)
                    print(f"'{tugas_terhapus['nama']}' telah dihapus")
                else:
                    print("Nomor tugas tidak ditemukan.")
            except ValueError:
                print("Masukan angka yang valid.")

        elif menu == 4:
            print("Aplikasi ditutup, Selamat berjumpa kembali")
            break

        else:
            print("Perintah tidak dikenali, silahkan coba lagi.")

# Menjalankan program main
main() 