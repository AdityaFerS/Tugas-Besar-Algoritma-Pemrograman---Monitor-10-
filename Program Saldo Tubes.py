# Monitor 10 - Toll Gate System

import random
import time

# Data Array 
rute = ["Semarang", "Solo", "Ngawi", "Kertosono", "Mojokerto", "Surabaya"]
golongan = ["Golongan 1", "Golongan 2", "Golongan 3"]
tarif_golongan = [1, 1.5, 2]
arr_jarak = [72.64, 90.43, 87.02, 40.5, 36.27]
total = 0
tarif = 0
tujuan = 0
tiket = 0
konfirm = 0
# PROSEDUR 
def sapaan_awal(x):
    print(f"======Selamat datang di Gate {rute[x]}========")
    return ("")

# Ticketing dengan Output Random Integer 4 Digit (antara 1000 and 9999)
def generate_random_4_digit_integer():
    return random.randint(1000, 9999)
def generate_random_1_digit_integer():      # Random Integer Untuk Hold Terminal selama 1 - 10 detik
    return random.randint(1, 11)    
       
# Output Ticketing dengan Variabel
random_number = generate_random_4_digit_integer()
waktu = generate_random_1_digit_integer()


# RUTE AWAL

print("=====================")
print( "     Rute Awal       ")
print("=====================")

for i in range (6):
    print(f"{i+1}. {rute[i]}")
awal = int(input("Masukkan lokasi Gate awal : "))
print()
sapaan_awal(awal-1)


# GOLONGAN KENDARAAN
print("==============================")
print( "    Golongan Kendaraan       ")
print("==============================")
for i in range(3):
    print(f"{i+1}. {golongan[i]}")
kendaraan = int(input("Masukkan jenis golongan kendaraan : "))

# PILIHAN RUTE 
def pil_rute(a):
    print("=====================",a)
    print("     Pilihan Gate    ")
    print("=====================")



saldo = int(input("Masukkan saldo anda : Rp. "))
print("Tiket Anda adalah : ", random_number)
print("Selamat Jalan!")
import time

def main():
    input("Tekan Enter untuk mulai jalan...")
    
    # Record the start time
    start_time = time.time()
    time.sleep(3)
    input("Tekan Enter apabila sudah sampai...")
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the duration
    duration = end_time - start_time
    
    # Print the duration
    print(f"Lama perjalanan Anda adalah {duration:.2f} menit.")

if __name__ == "__main__":
    main()

# TICKETING
print("\nSelamat Datang Kembali!")
tiket = int(input("Masukkkan kode tiket Anda : "))
if tiket == random_number:
    print(f"Kode tiket {tiket} Anda sudah benar")
while tiket != random_number:
    tiket = int(input(f"Kode tiket {tiket} salah, Masukkkan kode tiket yang benar : "))

def akhir():
    print("\nSelamat Datang Kembali ! Pilih Posisi Gate Anda Sekarang !")
    pil_rute("")
    for i in range (6):
        print(f"{i+1}. {rute[i]}")
        if i==awal:
            print("",end="")
    return ()

akhir()
tujuan = int(input("Masukkan posisi Gate Anda sekarang : "))
while tujuan==awal:
    print("Pilihan posisi sekarang tidak boleh sama dengan gate awal!")
    tujuan = int(input("Masukkan posisi Gate yang benar : "))

# Tarif Pintu Tol untuk setiap rute awal dan tujuan
sampai = tujuan-1
datang = awal-1


if datang<sampai:
    count = datang
    while count<sampai:
        tarif += arr_jarak[count] * 1000
        count+=1
if sampai<datang:
    count = sampai
    while count>datang:
        tarif += arr_jarak[count] * 1000
        count-=1

# Total Biaya Tol Berdasarkan Golongan dan Jarak yang ditempuh
if kendaraan == 1:
    total += tarif_golongan[0] * tarif
elif kendaraan == 2:
    total += tarif_golongan[1] * tarif
elif kendaraan == 3:
    total += tarif_golongan[2] * tarif

saldo = saldo - total  # Pengurangan Saldo
print("Total biaya perjalanan Anda adalah : Rp",total)
print(f"Sisa Saldo Anda adalah Rp{saldo}")
# SALDO
while saldo<total:
    print("Saldo Anda tidak mencukupi")
    print(f"Sisa Saldo Anda adalah Rp{saldo}, Isi Saldo?")
    print("Konfirmasi?\n1. ya\n2. Tidak")
    if konfirm==1:
        saldo += tambah
    else:
        saldo += 0
    tambah = int(input("Masukkan tambahan saldo yang diinginkan : "))
    print(f"Tagihan Anda akan bernilai sebesar {tambah}")
    print("Konfirmasi?\n1. ya\n2. Tidak")
    konfirm = int(input("Masukkan piliihan Anda : "))
    if konfirm==1:
        saldo += tambah
    else:
        saldo += 0

print("\nLanjut Perjalanan?")
print("1. Ya")
print("2. Tidak")
jawaban = int(input("Masukkan pilihan Anda : "))

while jawaban==1:
    awal = tujuan
    # PILIHAN RUTE 
    def pil_rute(a):
        print("=====================",a)
        print("     Pilihan Gate    ")
        print("=====================")

    def generate_random_4_digit_integer():
        return random.randint(1000, 9999)

    random_number = generate_random_4_digit_integer()

    print("Tiket Anda adalah : ", random_number)
    print("Selamat Jalan!")
    import time

    def main():
        input("Tekan Enter untuk mulai jalan...")
        
        # Record the start time
        start_time = time.time()
        time.sleep(3)
        input("Tekan Enter apabila sudah sampai...")
        
        # Record the end time
        end_time = time.time()
        
        # Calculate the duration
        duration = end_time - start_time
        
        # Print the duration
        print(f"Lama perjalanan Anda adalah {duration:.2f} menit.")

    if __name__ == "__main__":
        main()

    # TICKETING
    print("\nSelamat Datang Kembali!")
    tiket = int(input("Masukkkan kode tiket Anda : "))
    if tiket == random_number:
        print(f"Kode tiket {tiket} Anda sudah benar")
    while tiket != random_number:
        tiket = int(input(f"Kode tiket {tiket} salah, Masukkkan kode tiket yang benar : "))

    def akhir():
        print("\nSelamat Datang Kembali ! Pilih Posisi Gate Anda Sekarang !")
        pil_rute("")
        for i in range (6):
            print(f"{i+1}. {rute[i]}")
            if i==awal:
                print("",end="")
        return ()

    akhir()
    tujuan = int(input("Masukkan posisi Gate Anda sekarang : "))
    while tujuan==awal:
        print("Pilihan posisi sekarang tidak boleh sama dengan gate awal!")
        tujuan = int(input("Masukkan posisi Gate yang benar : "))

    # Tarif Pintu Tol untuk setiap rute awal dan tujuan
    sampai = tujuan-1
    datang = awal-1

    if datang<sampai:
        count = datang
        while count<sampai:
            tarif += arr_jarak[count] * 1000
            count+=1
    if sampai<datang:
        count = sampai
        while count>datang:
            tarif += arr_jarak[count] * 1000
            count-=1

    # Total Biaya Tol Berdasarkan Golongan dan Jarak yang ditempuh
    if kendaraan == 1:
        total += tarif_golongan[0] * tarif
    elif kendaraan == 2:
        total += tarif_golongan[1] * tarif
    elif kendaraan == 3:
        total += tarif_golongan[2] * tarif

    saldo = saldo - total  # Pengurangan Saldo
    print("Total biaya perjalanan Anda adalah : Rp",total)
    print(f"Sisa Saldo Anda adalah Rp{saldo}")
    # SALDO
    while saldo<total:
        print("Saldo Anda tidak mencukupi")
        print("Isi Saldo?")
        print("Konfirmasi?\n1. ya\n2. Tidak")
        if konfirm==1:
            saldo += tambah
        else:
            saldo += 0
        tambah = int(input("Masukkan tambahan saldo yang diinginkan : "))
        print(f"Tagihan Anda akan bernilai sebesar {tambah}")
        print("Konfirmasi?\n1. ya\n2. Tidak")
        konfirm = int(input("Masukkan piliihan Anda : "))
        if konfirm==1:
            saldo += tambah
        else:
            saldo += 0

    print("\nLanjut Perjalanan?")
    print("1. Ya")
    print("2. Tidak")
    jawaban = int(input("Masukkan pilihan Anda : "))

print("Terima kasih sudah memercayakan layanan tol kami! :)")
