"""3. Buat flowchart dan program untuk mengevaluasi performa karyawan berdasarkan tiga indikator: 
jumlah proyek yang diselesaikan, waktu rata-rata penyelesaian proyek, dan umpan balik dari pelanggan. 
Sistem akan memberikan evaluasi seperti berikut:
Jika jumlah proyek lebih dari 20, waktu rata-rata kurang dari 7 hari, dan umpan balik dari pelanggan selalu positif, 
berikan evaluasi "Sangat Memuaskan".
Jika jumlah proyek antara 10-20, waktu rata-rata antara 7-14 hari, dan umpan balik sebagian besar 
positif, berikan evaluasi "Memuaskan". """

import os 

def clear():
    os.system('cls')

def garis():
    print ("="*70)

def cover  ():
    garis()
    print ("\t\t      Program evaluasi karyawan")
    garis ()

def main():
    clear()
    cover()
    global nama,selesaiproyek,waktu,umpan,kinerja
    nama = input ("masukkan nama karyawan :\t")
    selesaiproyek = int(input ("jumlah proyek yang diselesaikan : \t"))
    waktu = float (input("waktu rata rata penyelesaian proyek (masukkan angka saja)\t"))
    umpan = input ("bagaimana dengan rata rata umpan balik pelanggan : (positif)(negatif)\t").lower()

    if (selesaiproyek >20):
        if (waktu < 7):
            if umpan == "positif":
                kinerja = "sangat memuaskan"
                clear()
                hasil()
            elif umpan == "negatif":
                kinerja = "cukup memuaskan"
                clear()
                hasil()
        elif (waktu > 7) :
            kinerja = "memuaskan"
            clear()
            hasil()

    elif (10<= selesaiproyek<=20):
        if (7<=waktu<=14) :
            if umpan == "positif":
                kinerja = "memuasan"
                clear()
                hasil()
            else :
                kinerja = "cukup memuaskan"
                clear()
                hasil()
        elif waktu < 7 :
            kinerja = "memuaskan"
            clear()
            hasil()
        elif waktu < 7 :
            kinerja = "cukup memuaskan"
            clear()
            hasil()
    else :
        kinerja = "kurang memuaskan"
        clear()
        hasil()

def hasil ():
    cover()
    print (f"""
hasil evaluasi :
           Nama                           : {nama} 
           jumlah proyek                  : {selesaiproyek} proyek
           waktu rata rata proyek selesai : {waktu} hari
           umpan balik pelanggan          : {umpan} 
           kinerja                        : {kinerja}
""")
    garis ()

def ulang():
    ulang = input ("evaluasi lagi ? [y] atau [t]\t")
    if ulang == "y":
        main()
    else :
        print ("terimakasih semoga kinerjamu selalu baik")

if __name__ == "__main__":
    main()








