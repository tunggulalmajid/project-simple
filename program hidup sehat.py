'''
1. Buat flowchart dan sintax program untuk memberikan rekomendasi gaya hidup sehat berdasarkan
 beberapa input dari pengguna, seperti usia, berat badan, tinggi badan, dan tingkat
aktivitas fisik (rendah, sedang, tinggi).Program akan memberikan saran seperti berikut:

Jika usia di bawah 18 tahun dan tingkat aktivitas fisik rendah, rekomendasikan. 
"Tingkatkan aktivitas fisik dengan berolahraga minimal 30 menit setiap hari."

Jika BMI (Body Mass Index) antara 25 dan 29.9 dan tingkat aktivitas fisik rendah atau sedang, 
rekomendasikan "Kurangi asupan kalori dan lakukan olahraga rutin untuk mencapai berat badan ideal."

Jika usia di atas 40 tahun dan BMI lebih dari 30, serta tingkat aktivitas fisik rendah, rekomendasikan 
"Konsultasikan dengan dokter untuk program penurunan berat badan yang sesuai."

Jika semua kondisi tidak terpenuhi, rekomendasikan "Lanjutkan gaya hidup sehat Anda.
'''
import os
import termcolor

def clear():
    os.system ('cls')

def garis():
    termcolor.cprint('='*50, 'cyan')

def cover ():
    garis()
    print ('\t    program gaya hidup sehat ')
    garis()


def main():
    global nama,usia,berat,tinggi,aktivitas,bmi,saran
    clear()
    cover()
    nama = input('masukkan nama :\t')
    usia = int (input('masukkan usia anda sekarang :\t'))
    berat = int (input('masukkan berat badan anda sekarang :\t'))
    tinggi = int (input('masukkan tinggi badan anda sekarang :\t'))
    aktivitas = input ('bagaimana aktivitas anda : [rendah][sedang][tinggi]\t').lower()
    
    bmi = float (berat/((tinggi*0.01)**2))

    if usia < 18 :
        if aktivitas == 'rendah':
            saran = "tingkatkan aktivitas fisik dengan berolahraga minimal 30 menit setiap hari"
            hasil()
        else :
            saran = "jaga asupan gizi seimbang untuk mencapai perkembangan maksimal"
            hasil()
    elif (25<bmi<29.9):
        if aktivitas in ["rendah","sedang"]:
            saran = "kurangi asupan kalori dan lakukan olahraga rutin untuk mencapai berat badan ideal"
            hasil()
        else :
            saran = "jaga pola makan untuk mendapatkan berat badan ideal"
            hasil()
    elif bmi >30:
        if usia >40 :
            if aktivitas == 'rendah':
                saran = "konsultasikan dengan dokter untuk program penurunan berat badan"
                hasil()
            else :
                saran = "jaga pola makan seimbang serta konsisten dalam menjalaninya"
                hasil()
    else :
        saran = "lanjutkan gaya hidup sehat anda"
        hasil()

def hasil(): 
    clear()
    cover()
    print (f'''
hasil pemerikasaan :
        Nama               : {nama}
        usia               : {usia} tahun
        berat badan        : {berat} kg
        tinggi badan       : {tinggi} cm
        aktivitas fisik    : {aktivitas} 
        BMI                : {bmi:.2f} 
        saran              : {saran}
''')
    ulang = input ('lakukan pemeriksaan lagi [y] atau [t]')
    if ulang == "y":
        main ()
    elif ulang == "t":
        print ('terimakasih telah memakai program ini')
    else :
        print ('terimakasih telah memakai program ini')
    
if __name__=="__main__":
    main()










