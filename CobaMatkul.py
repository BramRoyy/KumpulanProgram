import sys
import time
import getpass
# Login
hello= """
         ___________   
        |___     ___| _______   __                 __    __
            |   |    |   ____| |  |               |  |  |  |
            |   |    |  |____  |  |      ______   |  |  |  |  
            |   |    |   ____| |  |     |______|  |  |  |  |  
            |   |    |  |____  |  |___            |  |__|  |
            |___|    |_______| |______|            \_______/
                                                            By Bram
                                 """
print(hello)
x = 'abrahamrudianto'
y = 'bramroyy'

def login():
    user = input('Username : ')
    passw= input('Password : ')
    if user == x and passw == y:
        print("\nHai Abraham Roy Rudianto, Selamat Datang!\n")
        print("Loading..\n")
        time.sleep(2)
        sys.exit
    else:
        print ('Password Salah')
        login()

if __name__== '__main__':
    login()


import sys
import time


a =  '\n08.30 - 10.30   PENDIDIKAN PANCASILA\n13.30 - 15.30   BAHASA INGGRIS\n16.30 - 18.30   LOGIKA MATEMATIKA\n'
b =  '\n13.30 - 15.30   KALKULUS\n'
c =  '\n12.30 - 15.30   PENGENALAN PEMROGRAMAN\n15.30 - 18.30   PENDIDIKAN KARAKTER\n'
d =  '\n12.30 - 14.30   KALKULUS\n14.30 - 16.30   LOGIKA MATEMATIKA\n'
e =  '\n12.30 - 14.30   PENDIDIKAN AGAMA KATOLIK DAN ETIKA\n'

# Menu
print("|| ========= || MENU || ========= ||")
print("")
print("\t1. Senin")
print("\t2. Selasa")
print("\t3. Rabu")
print("\t4. Kamis")
print("\t5. Jumat")
print("\t6. Exit")
print("")
print("|| ============================== ||")

# Fungsi Pilihan/Input 
def Kontrol():
    pert=input('\nPilih Harinya : ')
    if pert=='Senin':
        print("\nPlease Wait...")
        time.sleep(2)
        print(a)
        return Kontrol()
    elif pert=='Selasa':
        print("\nPlease Wait...")
        time.sleep(2)
        print(b)
        return Kontrol()
    elif pert=='Rabu':
        print("\nPlease Wait...")
        time.sleep(2)
        print(c)
        return Kontrol()
    elif pert=='Kamis':
        print("\nPlease Wait...")
        time.sleep(2)
        print(d)
        return Kontrol()
    elif pert=='Jumat':
        print("\nPlease Wait...")
        time.sleep(2)
        print(e)
        return Kontrol()
    elif pert=='Exit':
        print("BYE-BYE :)")
        sys.exit()
print= Kontrol()
