# deklarasi variable nama
nama = "Hafizh Ahmad Al Mushoffi"
# lalu print variable nama dengan memanggil variable nama di print()
print(nama)

# deklarasi variable nama menggunakan input()
nama = input("Siapa nama kamu? ")

# deklarasi variable nama menggunakan input() yang berisi whitespace
nama_whitespace = input("Siapa nama kamu? (whitespace) ").strip() # menggunakan method strip() untuk menghapus whitespace di awal dan akhir string
# strip() hanya bisa berfungsi pada kalimat maupun kata namun pada kalimat whitespace hanya dihapus di awal dan di akhir kalimat.

# deklarasi variable nama menggunakan input() yang berisi hurung kecil semua untuk di besarkan
nama_lowercase = input("Siapa nama kamu? (lowercase) ").capitalize() # menggunakan method capitalize() untuk mengubah huruf pertama menjadi huruf besar dan huruf lainnya menjadi huruf kecil

# deklarasi variable nama menggunakan input() yang berisi huruf besar semua untuk di kecilkan
nama_uppercase = input("Siapa nama kamu? (uppercase) ").lower() # menggunakan method lower()

#deklarasi variable buku
buku = input("Apa judul buku favorit kamu? (buku) ")

# lalu print variable nama dengan memaanggil variable nama di print()
print("Hallo, " + nama + " Selamat datang di pembelajaran python.")
print("Hallo,", nama, "Selamat datang di pembelajaran python. bukan menggunakan + tapi menggunakan syntax koma (,)")
print(f"Hallo, {nama}","Selamat datang di pembelajaran python. menggunakan f-string untuk memeberitahukan bahwa ini string khusus")

# melakukan print variable name_whitespace dengan menggunakan 3 jenis syntax print() yang sebelumnya telah digunakan
print("Hallo Whitespace, " + nama_whitespace + " Selamat datang di pembelajaran python.")
print("Hallo Whitespace,", nama_whitespace, "Selamat datang di pembelajaran python. bukan menggunakan + tapi menggunakan syntax koma (,)")
print(f"Hallo Whitespace, {nama_whitespace}","Selamat datang di pembelajaran python. menggunakan f-string untuk memeberitahukan bahwa ini string khusus")

# melakukan print variable name_lowercase dengan menggunakan 3 jenis syntax print() yang sebelumnya telah digunakan
print("Hallo Lowercase, " + nama_lowercase + " Selamat datang di pembelajaran python.")
print("Hallo Lowercase,", nama_lowercase, "Selamat datang di pembelajaran python. bukan menggunakan + tapi menggunakan syntax koma (,)")
print(f"Hallo Lowercase, {nama_lowercase}","Selamat datang di pembelajaran python. menggunakan f-string untuk memeberitahukan bahwa ini string khusus")

# melakukan print variable name_uppercase dengan menggunakan 3 jenis syntax print() yang sebelumnya telah digunakan
print("Hallo Uppercase, " + nama_uppercase + " Selamat datang di pembelajaran python.")
print("Hallo Uppercase,", nama_uppercase, "Selamat datang di pembelajaran python. bukan menggunakan + tapi menggunakan syntax koma (,)")
print(f"Hallo Uppercase, {nama_uppercase}","Selamat datang di pembelajaran python. menggunakan f-string untuk memeberitahukan bahwa ini string khusus")

# melakukan print variable buku dengan menggunakan title() untuk mengubah semua huruf awalan jadi kapital
print("Buku favorit kamu adalah " + buku.title() + " Selamat datang di pembelajaran python.")