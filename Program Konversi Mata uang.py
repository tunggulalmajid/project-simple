import os 
import termcolor

def clear ():
    os.system('cls')

def garis ():
    termcolor.cprint ('='*50,"blue")

def cover ():
    garis ()
    print ("\n\t Program Konversi Nilai Mata Uang\n")
    garis ()


def enter():
    enter = input ("tekan [ENTER] untuk melanjutkan\t")


def menu ():
    clear ()
    cover ()
    print ("""
pilihan menu :
        1. Konversi Mata Uang Rupiah 
        2. Konversi Mata Uang Dollar
        3. Konversi Mata Uang Ringgit 
        4. Konversi Mata Uang Won
        5. Konversi Mata Uang Yen
""")
    menu = int (input ("pilih opsi yang ingin anda gunakan"))
    if menu == 1:
        enter()
        clear()
        rupiah()
    elif menu == 2:
        enter()
        clear()
        dollar()
    elif menu == 3:
        enter()
        clear()
        ringgit()
    elif menu == 4:
        enter()
        clear()
        won ()
    elif menu == 5:
        enter()
        clear()
        yen ()

def rupiah():
    clear()
    cover()
    nilai = int (input ("\nmasukkan nominal uang yang ingin di konversi :\t"))
    dollar = float(nilai/15500)
    ringgit = float(nilai/3567)
    won = float (nilai/11.52)
    yen = float (nilai/108.65)
    print (f"""
    mata uang yang ingin di konversi : 
           rupiah : Rp {nilai:,}
    
    hasil konversi :
            dollar  : {dollar:.2f}  
            ringgit : {ringgit:.2f} 
            won     : {won:.2f}     
            yen     : {yen:.2f}     
           """)
    ulang()

def dollar():
    cover()
    nilai = int (input ("masukkan nominal uang yang ingin di konversi :\t"))
    rupiah = float(nilai*15500)
    ringgit = float(nilai * 4.34)
    won = float (nilai*1340.14)
    yen = float (nilai*141.77)
    print (f"""
    mata uang yang ingin di konversi : 
           dollar : Rp {nilai}
    
    hasil konversi :
            rupiah  : {rupiah:,}  
            ringgit : {ringgit:.2f} 
            won     : {won:.2f}     
            yen     : {yen:.2f}     
           """)
    ulang()

def ringgit():
    cover()
    nilai = int (input ("masukkan nominal uang yang ingin di konversi :\t"))
    rupiah = float(nilai*3567)
    dollar = float(nilai/4.34)
    won = float (nilai*309.17)
    yen = float (nilai*32.6)
    print (f"""
    mata uang yang ingin di konversi : 
           ringgit : Rp {nilai}
    
    hasil konversi :
            rupiah  : {rupiah:,} 
            dollar  : {dollar:.2f}  
            won     : {won:.2f}     
            yen     : {yen:.2f}     
           """)
    ulang()

def won():
    cover()
    nilai = int (input ("masukkan nominal uang yang ingin di konversi :\t"))
    rupiah = float (nilai*11.52)
    dollar = float(nilai/15500)
    ringgit = float(nilai/309.17)
    yen = float (nilai/9.46)
    print (f"""
    mata uang yang ingin di konversi : 
           won : Rp {nilai}
    
    hasil konversi :
            rupiah  : {rupiah:,}     
            dollar  : {dollar:.2f}  
            ringgit : {ringgit:.2f} 
            yen     : {yen:.2f}     
           """)
    ulang()

def yen():
    cover()
    nilai = int (input ("masukkan nominal uang yang ingin di konversi :\t"))
    rupiah = float (nilai*108.65)
    dollar = float(nilai/141.77)
    ringgit = float(nilai/309.17)
    won = float (nilai*9.46)
    print (f"""
    mata uang yang ingin di konversi : 
           yen : Rp {nilai}
    
    hasil konversi :
            rupiah  : {rupiah:,}     
            dollar  : {dollar:.2f}  
            ringgit : {ringgit:.2f} 
            won     : {won:.2f}     
           """)
    ulang()

def ulang ():
    ulang = input ("Konversi Nillai lagi [y] atau [t]")
    if ulang =="y":
        menu()
    else :
        print ("terima kasih telah menggunakan program ini")







if __name__ == "__main__":
   menu()