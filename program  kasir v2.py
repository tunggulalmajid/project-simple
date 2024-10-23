import os
import getpass
import time

#ini adalah list kosong
pesanan = []
jumlah = []
atasnama = []




def daftar():
    cover ()
    print (f"""
daftar menu :
           1. Ayam Goreng   : Rp 15000
           2. Bebek Goreng  : Rp 17000
           3. Tempe Penyet  : Rp 12000
           4. Lalapan Telur : Rp 12000
""")
    garis()

def clear ():
    os.system('cls')

def garis ():
    print ("="* 50)

def cover ():
    garis ()
    print ("\t\tprogram kasir")
    garis ()

def enter():
    enter = input("tekan [ENTER] untuk melanjutkan")

def login ():
    clear()
    cover()
    username = "kasir"
    password = "kasir123"
    inputUser = input("masukkan username :\t")
    inputPasword = getpass.getpass("masukkan password :\t")
    if inputUser == username:
        if inputPasword == password:
            enter()
            main()
        else:
            print ("password yang anda masukkan salah")
            login()
    else :
        print ("username dan psaword yang anda masukkan salah")
        login()

def main ():
    clear()
    cover()
    print ("""
menu layanan :
           1. Pesan
           2. Hapus Pesanan 
           3. Keranjang Pesanan
           4. Pembayaran 
           5. log out 
""")
    pilihan = int (input("silahkan pilih opsi (masukkan angka saja) :\t"))
    if pilihan == 1:
        pesan ()
    elif pilihan == 2:
        hapus()
    elif pilihan == 3:
        keranjang()
    elif pilihan == 4:
        pembayaran(pesanan)
    elif pilihan == 5:
        print ("terimakasih telah menggunakan program ini")
    else :
        kembali = input ("opsi tidak tersedia, [ENTER] untuk melanjutkan")
        main()
    
"""
            1. Ayam Goreng   : Rp 15000
           2. Bebek Goreng  : Rp 17000
           3. Tempe Penyet  : Rp 12000
           4. Lalapan Telur : Rp 12000
"""


def pesan ():
    global pesanan,atasnama,inputpesanan,jumlah
    clear()
    cover()
    atasnama = input ("pesanan atas nama :\t")
    clear()
    cover()
    daftar()
    no = input ("pesanan ke berapa ? >>")
    inputpesanan = int(input("silahkan masukkan angka untuk memilih makanan >>"))
    if inputpesanan == 1 :
        makanan = "Ayam Goreng"
        pesanan.append(makanan)
        jumlah = int(input("masukkan jumlah yang diinginkan >>"))
        print(f"pesanan atas nama : {atasnama} telah masuk ke keranjang\nsilahkan lanjut ke menu pembayaran")
        enter()
        main()
    elif inputpesanan == 2 :
        makanan = "Bebek Goreng"
        pesanan.append(makanan)
        jumlah = int(input("masukkan jumlah yang diinginkan >>"))
        print(f"pesanan atas nama : {atasnama} telah masuk ke keranjang\nsilahkan lanjut ke menu pembayaran")
        enter()
        main()
    elif inputpesanan == 3 :
        makanan = "Tempe Penyet"
        pesanan.append(makanan)
        jumlah = int(input("masukkan jumlah yang diinginkan >>"))
        print(f"pesanan atas nama : {atasnama} telah masuk ke keranjang\nsilahkan lanjut ke menu pembayaran")
        enter()
        main()
    elif inputpesanan == 4 :
        makanan = "Lalapan Telur"
        jumlah = int(input("masukkan jumlah yang diinginkan >>"))
        print(f"pesanan atas nama : {atasnama} telah masuk ke keranjang\nsilahkan lanjut ke menu pembayaran")
        enter()
        main()
    else  :
        print ("pesanan tidak tersedia, silahkan pesan ulang")
        enter()
        pesan()

    jumlah.append(jumlah)


def hapus():
    clear()
    cover()
    x = int(input ("hapus pesanan ke berapa ? >>"))-1
    pesanan.pop(x)
    jumlah.pop(x)
    berhasil = print(f"pesanan nomor {x} telah berhasil dihapus ")
    enter()
    main()


def keranjang():
    clear()
    cover()
    for x in range(len(pesanan)):
        print(f"pesanan atas nama : {atasnama} pesanan : {pesanan[x]} jumlah : {jumlah[x]}")
    enter()
    main()
    













def total(pesanan):
    global total
    
    return total 

def pembayaran(pesanan):
    clear ()
    cover()
    print (f"pesanan atas nama : {atasnama}")
    





    









def riwayat():
    print ("hello")




    
if __name__ == "__main__":
    main()