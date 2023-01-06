import os
import sys
import time
hello= """
             __      __    ____   ___   _  _
            |  |   / _ \  /  __| |_ _| | \| |
            |  |_ | (_) ||  (_ |  | |  | .' |
            |____| \___/  \____| |___| |_|\_|

                                            By Bram
                                 """
print(hello)
x = 'Username'
y = 'bramganteng'

def login():
    os.system('clear')
    user = input('Username : ')
    passw= input('Password : ')
    if user == x and passw == y:
        time.sleep(2)
        sys.exit
    else:
        print ('Password Salah')
        login()

if __name__== '__main__':
    login()

opening = """
|==============================================================================|
|============================|| JADWAL MATKUL ||===============================|
|==============================================================================|
                                                                      """
print(opening)


#NAMA
import os
import sys
import time
z = 'p'
def name():
    os.system('clear')
    nama = input('Nama Mahasiswa : ')
    if nama == z:
        time.sleep(0.5)
        sys.exit
    else:
        print('Nama Mahasiswa Salah')
        name()

if __name__== '__main__':
    name()

# NIM    
import os
import sys
import time
N = '1301213202'
def nomorinduk():
    os.system('clear')
    nim = input('NIM : ')
    if nim == N:
        time.sleep(1)
        sys.exit
    else:
        print('NIM Salah')
        nomorinduk()

if __name__ == '__main__':
    nomorinduk()

#Jadwal
import sys
import time
pil1 = 'Senin'
pil2 = 'Selasa'
pil3 = 'Rabu'
pil4 = 'Kamis'
pil5 = 'Jumat'
def JADWAL ():
    
