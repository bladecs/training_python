import random
from pprint import pprint

# List python

# List python merupakan type array yang akan menyimpan banyak data dalam satu variable dengan menggunakan
# [] sebagai wadah penyimpanan datanya

my_student = ["Hafizh", "Adhwa", "Vicky"]
print(my_student) # ini akan print semua listnya
print(my_student[1]) # ini akan print index 1 yaitu "Adhwa"
print(len(my_student)) # ini akan print panjang dari list yang dibuat
print(type(my_student)) # ini akan print typenya yaitu "list"

# Tuples python

# Tuples python merupakan type array yang akan menyimpan banyak data dalam satu variable dengan menggunakan
# () sebagai wadah penyimpanan datanya, perbedaannya dengan list adalah apa bila sudah jadi maka tuples
# tidak lagi bisa diubah

my_book = ("Novel", "Comic", "Magazine")
print(my_book) # ini akan print semua tuplesnya
print(my_book[1]) # ini akan print index 1 yaitu "Comic"
print(len(my_book)) # ini akan print panjang tuples yang dibuat
print(type(my_book)) # ini akan print typenya yaitu "tuples"

# Dist python

# Dist python merupakan type array yang akan menyimpan banyak data dalam setiap variable yang dibungkus oleh
# {} dan dapat dipanggil menggunakan setiap variablenya, tidak boleh ada duplikasi data

my_profile = {
    "name" : "Hafizh Ahmad Al Mushoffi",
    "born" : "Bandung",
    "hobby" : ("basket","gaming","cycling"),
    "age" : 22
}
print(my_profile) # ini akan print semua distnya
print(my_profile["hobby"]) # ini akan print dist dengan variable "hobby"
print(len(my_profile)) # ini akan print panjang dist yang dibuat
print(type(my_profile)) # ini akan print typenya yaitu "dist"

# Sets python

# Set python merupakan type array yang akan menyimpan banyak data dalam satu variable yang tidak di ubah
# tidak boleh ada duplikasi, dan tidak bisa di order (not ordered)

my_food = {"Burger", "Pizza", "Meat Ball"}
print(my_food) # ini akan print semua setsnya
print(len(my_food)) # ini akan print panjang set yang dibuat
print(type(my_food)) # ini akan print typenya yaitu "sets"

# Membuat invetory counter menggunakan list, tuples, set, dan dist

def main():
    my_inventory = ["Susu Kotak", "Tahu Putih", "Sosis Sapi", "Sosis Ayam", "Bakso Sapi"]
    my_stock = []
    for i in my_inventory:
        my_data = {
            "name" : i,
            "stock" : int(random.randrange(1,10))
        }
        my_stock.append(my_data)
    pprint(my_stock)
    count_invetory = len(my_inventory)
    print("Barang yang ada di inventory berjumlah:",count_invetory)
    count_stock_all = 0
    for x in my_stock:
        count_stock_all += x["stock"]
    print("Jumlah semua stock di inventory berjumlah:",count_stock_all)

main()