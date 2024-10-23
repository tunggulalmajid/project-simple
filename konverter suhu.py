import os 
import termcolor

def clear():
    os.system('cls')

def garis ():
    termcolor.cprint('='*50,"cyan")

def cover ():
    clear()
    garis()
    print ('\n\t program konverter suhu sederhana\n')
    garis()

def program():
    print ('''
silahkan pilih opsi yang ingin digunakan :
           1.convert celcius
           2.convert reamur 
           3.convert farenheit
           4.convert kelvin
''')

def main ():
    clear()
    cover()
    program()
    inputuser = int(input('silahkan masukkan piliihan sesuai dengan angka : ' ''))
    if inputuser == 1:
        enter = input ('tekan [ENTER] untuk melanjutkan' '')
        celcius()
    elif inputuser == 2:
        enter = input ('tekan [ENTER] untuk melanjutkan' '')
        reamur()
    elif inputuser == 3:
        enter = input ('tekan [ENTER] untuk melanjutkan ' '')
        farenheit()
    elif inputuser == 4:
        enter = input ('tekan [ENTER] untuk melanjutkan ' '')
        kelvin()

def celcius():
    clear()
    cover()
    celci = float(input('masukkan suhu dalam bentuk celcius :' ''))
    celcirea = int((4/5) * celci)
    celcifare = int((9/5) * celci + 32)
    celcikel = int(273 + celci)

    garis()
    print (f'''
suhu dalam celcius   : {celci}
suhu dalam reamur    : {celcirea}
suhu dalam farenheit : {celcifare}
suhu dalam kelvin    : {celcikel}
''')
    ulang = input ('ketik [y] jika ingin mengulang\nketik [s]untuk selesai\n')
    if ulang == 'y':
        main ()
    elif ulang =='s':
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')
    else :
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')

def reamur ():
    clear()
    cover()
    rea = float(input('masukkan suhu dalam bentuk reamur :' ''))
    reacelci = int((5/4) * rea)
    reafare = int((9/4) * rea + 32)
    reakel = int((5/4 *rea) + 273)

    garis()
    print (f'''
suhu dalam reamur    : {rea}
suhu dalam celcius   : {reacelci}
suhu dalam farenheit : {reafare}
suhu dalam kelvin    : {reakel}
''')
    ulang = input ('ketik [y] jika ingin mengulang\nketik [s]untuk selesai\n')
    if ulang == 'y':
        main ()
    elif ulang =='s':
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')
    else :
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')
    
def farenheit ():
    clear()
    cover()
    fare = float(input('masukkan suhu dalam bentuk farenheit :' ''))
    farecelci = int((fare - 32)*(5/9))
    farerea = int((fare - 32)*(4/9))
    farekel = int(273 + (fare - 32)*(5/9))

    garis()
    print (f'''
suhu dalam farenheit : {fare}
suhu dalam celcius   : {farecelci}
suhu dalam reamur    : {farerea}
suhu dalam kelvin    : {farekel}
''')
    ulang = input ('ketik [y] jika ingin mengulang\nketik [s]untuk selesai\n')
    if ulang == 'y':
        main ()
    elif ulang =='s':
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')
    else :
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')
    

def kelvin ():
    clear()
    cover()
    kel = float(input('masukkan suhu dalam bentuk kelvin :' ''))
    kelcel = int(kel - 273)
    kelrea = int((kel - 273)*(4/5))
    kelfar = int(((kel - 273)*(9/5)) + 32 )

    garis()
    print (f'''
suhu dalam kelvin    : {kel}
suhu dalam celcius   : {kelcel}
suhu dalam reamur    : {kelrea}
suhu dalam farenheit : {kelfar}
''')
    ulang = input ('ketik [y] jika ingin mengulang\nketik [s]untuk selesai\n')
    if ulang == 'y':
        main ()
    elif ulang =='s':
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')
    else :
        clear()
        cover()
        print ('terimakasih telah menggunakan program ini')

if __name__ == '__main__':
    main()