# Membuat fungsi untuk menentukan grade dari score yang diinputkan
def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Membuat tampilan untuk input nama dan score
    nama = input("Masukan Nama Mahasiswa: ")
    if nama == "":
        print("Nama tidak boleh kosong!")
        exit()

    # Mengunakan try-except untuk menangain error jika score yg dimasukan bukan berupa angka atau kosong
    try:
        score = float(input("Masukan Score Mahasiswa: "))
        # Memeriksa apakah score yg dimasukan berada pada rentang 0 hingga 100
        if score < 0 or score > 100:
            print("Score harus antara 0 hingga 100!")
            exit()
        # Memanggil fungsi grade dan menampilkan hasilnya
        hasil_grade = grade(score)
        print(f"Nama Mahasiswa: {nama}")
        print(f"Score Mahasiswa: {score}")
        print(f"Grade Mahasiswa: {hasil_grade}")
    except ValueError:
        print("Score harus berupa angka!")

main()
