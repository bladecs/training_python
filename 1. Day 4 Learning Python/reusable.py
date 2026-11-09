def list_barang(data_barang):
    total_belanja = 0
    for i in data_barang:
        total_belanja = data_barang["harga"] * data_barang["jumlah"]
    
    print(diskon_generate(total_belanja))
    
def diskon_generate(harga_total):
    persen_diskon = 10
    diskon = harga_total * (persen_diskon / 100)        
    return(diskon,harga_total-diskon)

def add_barang(nama,harga,stok):
    data_menu = {
        "nama":nama,
        "harga":harga,
        "stok":stok
    }
    menu_barang(data_menu)

def menu_barang(data_menu):
    print("*"*20)
    for menu in data_menu:
        print(data_menu[menu])

def belanja():
    nama_barang = input("Masukan Barang Yang Ingin Dibeli : ")
    harga = int(input("Masukann Harga Yang Tertera: "))
    jumlah = int(input("Jumlah Yang Ingin Dibeli: "))
    data_barang = {
        "nama_barang" : nama_barang,
        "harga" : harga,
        "jumlah" : jumlah
    }
    list_barang(data_barang)


def main():
    add_barang("Kopi Box",10000,10)
    add_barang("Tahu Krispi",8500,10)
    add_barang("Teh Box",2000,10)
    add_barang("Roko Box",15000,10)
    belanja()

main()