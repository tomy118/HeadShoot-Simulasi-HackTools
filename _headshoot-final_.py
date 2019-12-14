import time

def inputUser():
    nama = input('Masukan Nama Lengkap Anda!\n$=> ')
    print('Hallo!,',nama,'\nSelamat datang di Aplikasi Headshoot\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(5)
    headers()
def headers():
    print("Headshoot [Versi UPJ-2019071064-001]\n(c) University Pembangunan Jaya. Hak Cipta Dilindungi Undang-undang\nNote: Silahkan input menu untuk menuju halaman menu")
    router = input("$=> ")
    if router in ['Menu', 'menu']:
        menu()
def menu():
    print("""
    ######################################################
    #            => TENTUKAN PILIHAN ANDA <=             #
    # ================================================== #
    # --> Tersedia           | --> Maaf! Belum Tersedia  #
    # -------------------------------------------------- #
    # [1] Scan IP            | [1] Attacker #            #
    # [2] Keluar             | [2] Deface #              #
    #                        | [3] System Protect        #
    # -------------------------------------------------- #
    # ====================================> Simulasi v.1 #
    ######################################################""")
    print('Silahkan masukan value yang muncul di layar anda!\nPilihan Anda [ 1 | 2 ]?')
    pil = input("$=> ")
    if pil in ['1', 'Scan IP', 'SCAN IP', 'scan ip']:
        menu1()
    elif pil in ['2','Keluar','KELUAR','keluar']:
        print('Good Bye!\nSee You Next Time :-)')
        exit()
    else:
        menu()

def menu1():
    print("""
    ++++++++++++++++++++++++++++++
    +     SCAN IP <-By Link      +
    + -------------------------- +
    + [1] Google                 +
    + [2] Facebook               +
    + [3] Instagram              +
    + [4] Whatsapp               +
    +++++++++++++++++++++++++++++
    Note:
    Inputkan 1 > 2 > 3 > 4 """)
    pil1 = input("$=> ")
    if pil1 == "1":
        google()
    elif pil1 == "2":
        facebook()
    elif pil1 == "3":
        instagram()
    elif pil1 == "4":
        whatsapp()
    else:
        print('Maaf inputan yang Anda masukan tidak sesuai dengan arahan Kami !!!\nCoba Lagi yaaa.')
        menu1()

#-------------------------- Pemisah ---------------------------------------------------

def lanjutWa():
    print("Anda mau lihat info lebih detail? [ Y | N ]")
    router01 = input("$=> ")
    if router01 in ['Y','y']:
        print('Ok! Mohon tunggu sebentar, kami sedang siapkan untuk anda')
        time.sleep(3)
        infoWa()

def lanjutIg():
    print("Anda mau lihat info lebih detail? [ Y | N ]")
    router01 = input("$=> ")
    if router01 in ['Y','y']:
        print('Ok! Mohon tunggu sebentar, kami sedang siapkan untuk anda')
        time.sleep(3)
        infoIg()

def lanjutG():
    print("Anda mau lihat info lebih detail? [ Y | N ]")
    router01 = input("$=> ")
    if router01 in ['Y','y']:
        print('Ok! Mohon tunggu sebentar, kami sedang siapkan untuk anda')
        time.sleep(3)
        infoG()

def lanjutFb():
    print("Anda mau lihat info lebih detail? [ Y | N ]")
    router01 = input("$=> ")
    if router01 in ['Y','y']:
        print('Ok! Mohon tunggu sebentar, kami sedang siapkan untuk anda')
        time.sleep(3)
        infoFb()

# ------------------------- Pemisah -----------------------------------------------------------------

def infoG():
    time.sleep(2)
    print("""
     _______________________________________________________________
    |                      IP CHECKER PROFILE                       |
    -----------------------------------------------------------------
    | Hostname        | any-in-2678.1e100.net                       |
    | Address type    | IPv4                                        |
    | ASN             | AS15169 Google LLC                          |
    | Organization    | Google LLC (google.com)                     |
    | Route           | 216.239.38.0/24                             |
    | City            | Los Angeles                                 |
    | Region          | California                                  |
    | Postal Code     | 90041                                       |
    | Coordinates     | 34.1339,-118.2082                           |
    | Timezone        | America/New_York                            |
    | Country         | United States                               |
    -----------------------------------------------------------------
    """)
    print('Tugas Kami sudah selesai.\nSee you Next Time, Good Bye')

def infoIg():
    time.sleep(2)
    print("""
     _______________________________________________________________
    |                      IP CHECKER PROFILE                       |
    -----------------------------------------------------------------
    | Hostname        | ec2-3-232-116-152.compute-1.amazonaws.com   |
    | Address type    | IPv4                                        |
    | ASN             | AS14618 Amazon.com, Inc.                    |
    | Organization    | Amazon Data Services NoVa (amazon.com)      |
    | Route           | 3.224.0.0/12                                |
    | City            | Virginia Beach                              |
    | Region          | Virginia                                    |
    | Postal Code     | 23465                                       |
    | Coordinates     | 36.8512,-76.1692                            |
    | Timezone        | America/New_York                            |
    | Country         | United States                               |
    -----------------------------------------------------------------
    """)
    print('Tugas Kami sudah selesai.\nSee you Next Time, Good Bye')

def infoFb():
    time.sleep(2)
    print("""
     _______________________________________________________________
    |                      IP CHECKER PROFILE                       |
    -----------------------------------------------------------------
    | Hostname        | edge-star-mini-shv-02-sin2.facebook.com     |
    | Address type    | IPv4                                        |
    | ASN             | AS32934 Facebook, Inc.                      |
    | Organization    | Facebook, Inc. (facebook.com)               |
    | Route           | 157.240.25.0/24                             |
    | City            | New York City                               |
    | Region          | New York                                    |
    | Postal Code     | 10004                                       |
    | Coordinates     | 40.7143,-74.0060                            |
    | Timezone        | America/New_York                            |
    | Country         | United States                               |
    -----------------------------------------------------------------
    """)
    print('Tugas Kami sudah selesai.\nSee you Next Time, Good Bye')

def infoWa():
    time.sleep(2)
    print("""
     _______________________________________________________________
    |                      IP CHECKER PROFILE                       |
    -----------------------------------------------------------------
    | Hostname        | aa.3c.37a9.ip4.static.sl-reverse.com        |
    | Address type    | IPv4                                        |
    | ASN             | AS36351 SoftLayer Technologies Inc.         |
    | Organization    | WhatsApp Inc. (whatsapp.net)                |
    | Route           | 169.55.60.0/22                              |
    | City            | New York City                               |
    | Region          | New York                                    |
    | Postal Code     | 10004                                       |
    | Coordinates     | 40.7143,-74.0060                            |
    | Timezone        | America/New_York                            |
    | Country         | United States                               |
    -----------------------------------------------------------------
    """)
    print('Tugas Kami sudah selesai.\nSee you Next Time, Good Bye')

def keluar():
    router01 = input("$=> ")
    if router01 in ['Y','y']:
        print('Silahkan pilih menu lagi')
        Headshoot.menu()
    else:
        exit()

# ------------------------- Pemisah -----------------------------------------------------------------

# Google
def google():
    print('='*82)
    print('{:^82}'.format("---------- SCAN IP - Google ----------"))
    print('='*82)
    print("Contoh: $=> ping www.google.com atau ping google.com")
    router = input("$=\Google> ")

    if router == "ping www.google.com":
        print("Pinging www.google.com with 32 bytes of data:")
        progress()
    elif router == "ping google.com":
        print("Pinging www.google.com with 32 bytes of data:")
        progress()
    else:
        print("Maaf inputan yang",router," tidak sesuai dengan Keyword Kami !!!")
        exit()

def progress():
    size = 100

    for i in range(0,101):
        print("Please Wait! Our Ip Address Is Being Generated | times=",i)

        if i is size:
            print("IP ADDRESS SUDAH DITEMUKAN :-)")
            print("IP Address = 74.125.68.106")
            statistics()
            break
    else:
        print("Maaf! Kami tidak menemukan Alamat IP yang dituju")

def statistics():
    print("\nPing statistics for 74.125.68.106:")
    print("     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
    print("Approximate round trip times in milli seconds:")
    print("     Minimum = 6ms, Maximum = 14ms, Average = 10ms")
    lanjutG()
# ------------------------- Pemisah -----------------------------------------------------------------
# Facebook
def facebook():
    print('='*82)
    print('{:^82}'.format("---------- SCAN IP - Facebook ----------"))
    print('='*82)
    print("Contoh: $=> ping www.facebook.com atau ping facebook.com")
    router1 = input("$=\Facebook> ")

    if router1 == "ping www.facebook.com":
        print("Pinging www.facebook.com with 32 bytes of data:")
        progress1()
    elif router1 == "ping facebook.com":
        print("Pinging www.facebook.com with 32 bytes of data:")
        progress1()
    else:
        print("Maaf inputan yang",router1," tidak sesuai dengan Keyword Kami !!!")
        exit()

def progress1():
    size1 = 100

    for i in range(0,101):
        print("Please Wait! Our Ip Address Is Being Generated | times=",i)

        if i is size1:
            print("IP ADDRESS SUDAH DITEMUKAN :-)")
            print("IP Address = 157.240.13.35")
            statistics1()
            break
    else:
        print("Maaf! Kami tidak menemukan Alamat IP yang dituju")

def statistics1():
    print("\nPing statistics for 157.240.13.35:")
    print("     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
    print("Approximate round trip times in milli seconds:")
    print("     Minimum = 18ms, Maximum = 20ms, Average = 19ms")
    lanjutFb()
# ------------------------- Pemisah -----------------------------------------------------------------
# Instagram
def instagram():
    print('='*82)
    print('{:^82}'.format("---------- SCAN IP - Instagram ----------"))
    print('='*82)
    print("Contoh: $=> ping www.instagram.com atau ping instagram.com")
    router2 = input("$=\Instagram> ")

    if router2 == "ping www.instagram.com":
        print("Pinging www.instagram.com with 32 bytes of data:")
        progress2()
    elif router2 == "ping instagram.com":
        print("Pinging www.instagram.com with 32 bytes of data:")
        progress2()
    else:
        print("Maaf inputan yang",router2," tidak sesuai dengan Keyword Kami !!!")
        exit()

def progress2():
    size2 = 100

    for i in range(0,101):
        print("Please Wait! Our Ip Address Is Being Generated | times=",i)

        if i is size2:
            print("IP ADDRESS SUDAH DITEMUKAN :-)")
            print("IP Address = 3.214.49.6")
            statistics2()
            break
    else:
        print("Maaf! Kami tidak menemukan Alamat IP yang dituju")

def statistics2():
    print("\nPing statistics for 3.214.49.6:")
    print("     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
    print("Approximate round trip times in milli seconds:")
    print("     Minimum = 258ms, Maximum = 284ms, Average = 271ms")
    lanjutIg()
# ------------------------- Pemisah -----------------------------------------------------------------
# Pebo
def whatsapp():
    print('='*82)
    print('{:^82}'.format("---------- SCAN IP - Whatsapp ----------"))
    print('='*82)
    print("Contoh: $=> ping www.whatsapp.com atau ping whatsapp.com")
    router3 = input("$=\Whatsapp> ")

    if router3 == "ping www.whatsapp.com":
        print("Pinging www.whatsapp.com with 32 bytes of data:")
        progress3()
    elif router3 == "ping whatsapp.com":
        print("Pinging www.whatsapp.com with 32 bytes of data:")
        progress3()
    else:
        print("Maaf inputan yang",router3," tidak sesuai dengan Keyword Kami !!!")
        exit()

def progress3():
    size3 = 10

    for i in range(0,12):
        time.sleep(2)
        print("Please Wait! Our Ip Address Is Being Generated |")

        if i is size3:
            time.sleep(2)
            print("IP ADDRESS SUDAH DITEMUKAN :-)")
            print("IP Address = 103.129.222.134")
            statistics3()
            break
    else:
        print("Maaf! Kami tidak menemukan Alamat IP yang dituju")

def statistics3():
    print("\nPing statistics for 103.125.222.134:")
    print("     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
    print("Approximate round trip times in milli seconds:")
    print("     Minimum = 6ms, Maximum = 7ms, Average = 6ms\n")
    lanjutWa()

inputUser()
