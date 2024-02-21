# CAPSTONE Modul 1 : YUNELLA AMELIA SIAGIAN (JCDSOL-013 Group 1) Februari 2024

# Penjualan Barang Toko Peralatan Sekolah

#import library yang digunakan
from tabulate import tabulate
import regex as re

# Dummy Data Penjualan Barang Toko Peralatan Sekolah Januari 2024
data = [
    {'No':1, 'Barang':'Buku', 'Kode':'BK04','Harga':8000, 'Stock_Awal':500, 'Terjual':423},
    {'No':2, 'Barang':'Pulpen', 'Kode':'PN03','Harga':7000, 'Stock_Awal':500, 'Terjual':408},
    {'No':3, 'Barang':'Pensil', 'Kode':'PL06','Harga':3000, 'Stock_Awal':500, 'Terjual':417},
    {'No':4, 'Barang':'Rautan', 'Kode':'SR09','Harga':2000, 'Stock_Awal':300, 'Terjual':120},
    {'No':5, 'Barang':'Tas', 'Kode':'BG03','Harga':58000, 'Stock_Awal':200, 'Terjual':40},
    {'No':6, 'Barang':'Crayon', 'Kode':'CN06','Harga':23000, 'Stock_Awal':300, 'Terjual':218},
    {'No':7, 'Barang':'Penghapus', 'Kode':'ER06','Harga':2500, 'Stock_Awal':300, 'Terjual':289},
    {'No':8, 'Barang':'Penggaris', 'Kode':'RR05','Harga':5000, 'Stock_Awal':275, 'Terjual':75},
    {'No':9, 'Barang':'Spidol', 'Kode':'SL06','Harga':8000, 'Stock_Awal':200, 'Terjual':80},
    {'No':10, 'Barang':'Kalkulator', 'Kode':'CL10','Harga':85000, 'Stock_Awal':120, 'Terjual':68}]

# 1. Fungsi untuk membaca dan menampilkan data dalam tabulate ----
def read_data():
    for i in range(len(data)):
        data[i]['No'] = i+1
    print(tabulate(data, headers='keys',tablefmt='pretty'))

# ----- Fungsi untuk membaca data -------
def menu_utama():
    read_opsi = input("Ingin kembali ke menu utama? (Y/N) -- ")
    if read_opsi == 'y' or read_opsi == 'Y':
        land_page()
    else:
        print("Berikut data ditampilkan kembali.")
        read_data()

# 2. Fungsi untuk mencari suatu barang tertentu ----------------------
def filter_by_barang():
    produk = input("Masukkan nama barang yang anda cari: ").title()
    for item in data:
        if item["Barang"] == produk:
            filtered_barang = [item for item in data if item["Barang"] == produk]
            table = tabulate(filtered_barang, headers="keys", tablefmt="pretty")
            print(table)
            break
    else:
        print("Maaf, produk yang anda cari tidak tersedia di toko kami.")

# 3. Fungsi untuk membuat data baru ---------------------------------
def create_data():
    No = (len(data))+1

    while True:
        Barang1 = input("Masukkan nama barang baru : ")
        if re.fullmatch(r"[A-Za-z]{3,}", Barang1):
                Barang = Barang1.capitalize()
                break
        else:
            print("Nama barang minimal berisi 3 karakter (hanya huruf).")
    
    
    while True:
        Kode1 = input("Masukkan kode barang baru : ")
        if re.fullmatch(r"[A-Za-z]{2}\d{2}", Kode1):
                Kode = Kode1.upper()
                break
        else:
            print("Kode terdiri dari 4 karakter(2 huruf dan 2 angka).")

    while True:
        try:
            Harga = int(input("Masukkan harga barang baru : ")) 
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Invalid! Yang Anda masukkan adalah karakter. Silahkan input angka.')

    while True:
        try:
            Stock_Awal = int(input("Masukkan stock awal barang baru : "))
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Invalid! Yang Anda masukkan adalah karakter. Silahkan input angka.')

    while True:
        try:
            Terjual = int(input("Masukkan jumlah barang baru yang terjual : "))
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Invalid! Yang Anda masukkan adalah karakter. Silahkan input angka.')

    new_data = {"No": No, "Barang": Barang, "Kode": Kode, "Harga": Harga, "Stock_Awal" : Stock_Awal, "Terjual" : Terjual}
    data.append(new_data)
    print("\n  Data sudah berhasil diinput, perhatikan tabel berikut ini. \n  Apabila ada data yang ingin diperbaiki dapat menggunakan fitur update.")
    read_data()
    menu_utama()

# 4. Fungsi untuk mengupdate data ------------------------
def update_barang():
    while True:
        try:
            old_no = int(input("Masukkan No. Barang : "))
            new_barang = input("Masukkan Nama Barang Baru : ")

            data[old_no-1]["Barang"] = new_barang.title()  #indeks dikurang 1 agar sesuai no urut
            print("Data nama barang berhasil diupdate.")
            read_data()
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Invalid! Yang Anda masukkan adalah karakter!')

def update_harga():
    while True:
        try:
            old_no = int(input("Masukkan No. Barang : "))
            new_harga = int(input("Masukkan Harga Baru : "))

            data[old_no-1]["Harga"] = new_harga  #indeks dikurang 1 agar sesuai no urut
            print("Data harga berhasil diupdate.")
            read_data()
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Yang Anda masukkan adalah karakter!')

def update_stock():
    while True:
        try:
            old_no = int(input("Input No. Barang : "))
            new_stock = int(input("Input Jumlah Stock Terbaru : "))

            data[old_no-1]["Stock_Awal"] = new_stock
            print("Data stock awal berhasil diupdate.")
            read_data()
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Yang Anda masukkan adalah karakter!')

def update_terjual():
    while True:
        try:
            old_no = int(input("Input No. Barang : "))
            new_terjual = int(input("Masukkan data terjual terbaru : "))

            data[old_no-1]["Terjual"] = new_terjual
            print("Data jumlah terjual berhasil diupdate.")
            read_data()
            break
        except ValueError:  #mengantisipasi apabila terjadi error jadi akan keluar print-an dibawah
            print('Yang Anda masukkan adalah karakter!')

#---- Fungsi untuk menampilkan beberapa pilihan update -----
def update():
    while True:
        print('''
        Data apakah yang ingin Anda update?
        1. Update Nama Barang
        2. Update Harga
        3. Update Stock Awal
        4. Update Terjual
        5. Kembali
        ''')
    
        opsi_update = input("Data apakah yang ingin diupdate? ")
    
        if opsi_update == '1':
            update_barang()
        elif opsi_update == '2':
            update_harga()
        elif opsi_update == '3':
            update_stock()
        elif opsi_update == '4':
            update_terjual()
        elif opsi_update == '5':
            break
        else:
            print('Input Anda invalid! Pilihan menu update 1-5.')

# 5. Fungsi untuk menghapus berdasarkan nama_barang -----------------------------
def delete_by_name():
    nama = input("Masukkan Nama Barang yang ingin dihapus: ").title()
    global data
    data = [item for item in data]
    print("Data telah berhasil dihapus.")

    restore_opsi = input("Anda yakin tetap ingin menghapus? Jika tidak, data awal akan ditampilkan. (Y/N) --> ")

    if restore_opsi == 'y' or restore_opsi == 'Y':
        data = [item for item in data if item["Barang"] != nama]
        print("Data telah berhasil dihapus.")
        read_data()
    else:
        data = [item for item in data]
        read_data()

# 6. Fungsi untuk melakukan Sort Data ------------------

def sort_barang():                  # sort by barang secara alfabet
    urut_barang = sorted(data, key=lambda Barang: Barang["Barang"])
    for i in range(len(urut_barang)):
        urut_barang[i]['No'] = i+1
    table = tabulate(urut_barang, headers="keys", tablefmt="pretty")
    print(table)
    print("Data telah ditampilkan berurutan berdasarkan nama barang menurut abjad.")

def sort_harga():                   # sort by harga dari yang termurah
    urut_harga = sorted(data, key=lambda Harga: Harga["Harga"])
    for i in range(len(urut_harga)):
        urut_harga[i]['No'] = i+1
    table = tabulate(urut_harga, headers="keys", tablefmt="pretty")
    print(table)
    print("Data telah ditampilkan dari harga terendah.")

def sort_terjual():             # sort by jumlah terjual
    urut_jual = sorted(data, key=lambda Terjual: Terjual["Terjual"])
    for i in range(len(urut_jual)):
        urut_jual[i]['No'] = i+1
    table = tabulate(urut_jual, headers="keys", tablefmt="pretty")
    print(table)
    print("Data telah ditampilkan berdasarkan jumlah terjual.")

# ---- Fungsi untuk menampilkan beberapa pilihan sort ------
def sort():
    while True:
        print('''
        Pilihan Sort Data :
        1. Nama Barang
        2. Harga
        3. Jumlah Terjual
        4. Kembali
        ''')
    
        opsi_sort = input("Data ingin diurutkan berdasarkan apa? ")
    
        if opsi_sort == '1':
            sort_barang()
        elif opsi_sort == '2':
            sort_harga()
        elif opsi_sort == '3':
            sort_terjual()
        elif opsi_sort == '4':
            break
        else:
            print('Input Anda invalid! Pilihan menu sort 1-4.')

# ---- Fungsi-fungsi untuk pilihan user dan halaman utama ---------

def land_page():
    while True:
        print('''
    ==========================================
     SELAMAT DATANG DI TOKO PERALATAN SEKOLAH
    ==========================================
    Silahkan Pilih Menu :
    1. Lihat Data Barang
    2. Filter Data
    3. Input Barang Baru 
    4. Update Data
    5. Hapus Data
    6. Sort Data
    7. Keluar
     ''')

        opsi = input("Masukkan Pilihan Menu : ")
        
        if opsi == "1":
            read_data()
            menu_utama()
        elif opsi == "2":
            filter_by_barang()
        elif opsi == '3':
            create_data()
        elif opsi == "4":
            read_data()
            update()
        elif opsi == '5':
            read_data()
            delete_by_name()
        elif opsi == '6':
            sort()
        elif opsi == '7':
            print('Terima kasih!')
            exit()
        else:
            print('Input Anda invalid! Input menu 1-7.')

# Fungsi apabila pilihan user adalah pegawai.
def pegawai():
    while True:
        password = input("Masukkan kata sandi : ")
        if password == "science70store":   # Password sebagai pegawai
            land_page()
        else:
            print('Password salah ! ')
            user()

# Fungsi apabila pilihan user adalah customer. Customer hanya boleh melihat data saja.
def customer():
    while True:
        print('''
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        SELAMAT DATANG PELANGGAN KAMI 
    SILAHKAN AKSES DATA BARANG DI TOKO INI
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    Silahkan Pilih Menu :
    1. Lihat Data Barang
    2. Filter Data
    3. Sort Data
    4. Kembali
     ''')

        option = input("Masukkan Pilihan Menu : ")
        
        if option == "1":
            print(tabulate(data, headers='keys',tablefmt='pretty'))
            print("Berikut ini data barang yang tersedia di toko kami.")
        elif option == "2":
            filter_by_barang()
        elif option == '3':
            sort()
        elif option == '4':
            print('Terima kasih!')
            user()
        else:
            print('Input Anda invalid! Input menu 1-3.')


# Fungsi untuk memilih sebagai user
def user():
    while True:
        print('''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     SELAMAT DATANG DI TOKO PERALATAN SEKOLAH
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Anda merupakan :
    1. Customer
    2. Pegawai
    3. Keluar
     ''')

        opsi = input("Masukkan pilihan user : ")
        
        if opsi == "1":
            customer()
        elif opsi == "2":
            pegawai()
        elif opsi == '3':
            print('Terima kasih!')
            exit()
        else:
            print('Input Anda invalid! Input pilihan menu 1-3.')


user()