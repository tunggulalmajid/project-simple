import os

def clear ():
    os.system('cls')

def garis():
    print ('='*50)

def cover():
    garis ()
    print ("\tProgram Pajak Penghasilan Tahunan")
    garis()
                                                                                
def main ():
    global nama,penghasilan,status,penghasilan,pajak,totalpajak,penghasilanTahunan
    clear()
    cover()
    nama = input ("ketik nama anda : ")
    penghasilan = int(input ("masukkan penghasilan anda perbulan : "))
    status = input ("ketik [sudah menikah] atau [belum menikah]  ").lower()

    penghasilanTahunan = penghasilan * 12

    if penghasilanTahunan > 500000000 :
        if status.lower() == "sudah menikah":
            pajak = "30% penghasilan tahunan"
            totalpajak = (30/100)*penghasilanTahunan
            hasil()
        else :
            pajak = "25% penghasilan tahunan"
            totalpajak = (25/100)*penghasilanTahunan
            hasil()
    elif 250000000 < penghasilanTahunan < 500000000:
        if status.lower() == "sudah menikah":
            pajak = "20% penghasilan tahunan"
            totalpajak = (20/100)*penghasilanTahunan
            hasil()
        else :
            pajak = "15% penghasilan tahunan"
            totalpajak = (15/100)*penghasilanTahunan
            hasil()
    else :
        pajak = "10% penghasilan tahunan"
        totalpajak = (10/100)*penghasilanTahunan
        hasil()

def hasil ():
    clear ()
    cover()
    print ("\t       Hasil Penghitungan")
    garis ()
    print (f"""
Nama                        : {nama}
Status                      : {status}
Penghasilan Per Bulanan     : {penghasilan:,}
Penghasilan Per Tahun       : {penghasilanTahunan:,}
Pajak Tahunan               : {pajak}
Total Biaya Pajak Per Tahun : {int(totalpajak):,}
""")
    garis ()
    ulang = input ("apakah ingin menghitung lagi [y] atau [t]  ")
    if ulang == "y":
        main ()
    else :
        print ("terimakasih telah memakai program ini ")



if __name__ == "__main__":
    main()






