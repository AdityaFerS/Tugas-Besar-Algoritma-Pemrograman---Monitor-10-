# MONITOR 10 - TOLL GATE SYSTEM
# Mata Kuliah Pengenalan Komputasi Kelas 32
# Dosen : Dr. Muhammad Sonny Abfertiawan, S.T, M.T.

# Nama Anggota :
# Aditya Fernandes Sitepu (16623172)
# Dzaky Addimasyqi (16623292)
# Irgi Jasmine Nabila (16623092)
# Faras Ayu Novitri (16623037)
# Muhammad Bramantya A. M. (16623297)
# Nafisa Itqanti Yudistia (16623002) 


import tkinter as tk
from tkinter import messagebox, PhotoImage, ttk
import random

import time
from tkinter import *
from PIL import Image, ImageTk


# Inisialisasi Jendela/Window Utama
root = tk.Tk()
root.title("Toll Gate System")
root.configure(bg="#33FF8D")
root.resizable(False,False)
# Inisialisasi Variabel-Variabel yang akann digunakan pada elemen global
route_var = tk.StringVar(root)
final_route_var = tk.StringVar(root)
ticket_number = None
saldo = 0
rute_awal = None
final_route = None
vehicle_type = None
tarif_golongan = [1, 1.5, 2]  # Variabel ini harus dipastikan dengan metode global
vehicle_types = ["Golongan 1 (Mobil, Sedan, dsb.)", "Golongan 2(Truk 2,3 Gandar)", "Golongan 3 (Truk >3 Gandar)"]
def show_main_page():       # Page/Window Utama yang akan ditampilkan yang dimuat dalam prosedur show_main_page
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("300x390")
    # Fungsi untuk meng-handle submisi rute dan lanjut ke penggolongan kendaraan
    radio_var = tk.IntVar()     # Untuk menahan integer value yang akan digunakan di beberapa widget
    routes = ["Semarang", "Solo", "Ngawi", "Kertosono", "Mojokerto", "Surabaya"]

    def submit_route():
        global rute_awal    # Elemen global dari tkinter yang sangat penting untuk memodifikasi/menyimpan perubahan terhadap satu variabel yang diproses dalam satu fungsi ke fungsi lainnya untuk dapat diakses
        rute_awal = radio_var.get()
        if rute_awal:
            messagebox.showinfo("Gate Awal", f"Gate Awal Anda adalah : {routes[rute_awal-1]}")
            print('Gate Awal :', rute_awal)
            show_vehicle_selection()
        else:
            messagebox.showwarning("Invalid", "Mohon masukkan gate awal Anda dengan benar.")
            print('Gate Invalid/Kosong')

    # Saldo
    saldo_label = tk.Label(root, text="Masukkan saldo awal Anda : ")
    saldo_label.pack(pady=10)
    SALDO_var = tk.IntVar()
    saldo_entry = ttk.Entry(root, textvariable=SALDO_var)
    saldo_entry.pack(padx=10, pady=10, fill="x", expand=True)

    def tombol_saldo():
        global saldo
        saldo = SALDO_var.get()     # Ambil value dari entry saldo
        if saldo!= 0:
            tunjuk_saldo_label = tk.Label(root, text=f"Saldo Anda adalah : Rp{saldo}")
            tunjuk_saldo_label.pack(padx=10, fill="x", expand=True)
        else:
            messagebox.showwarning("Invalid", "Mohon masukkan saldo Anda dengan benar.")
            print('Saldo Invalid/Kosong')


    klik_saldo = tk.Button(root, text="Input", command=tombol_saldo)
    klik_saldo.pack(pady=10)

    def rute_semula():
        def create_radio_button(text, value):   # Fungsi dasar untuk pembuatan radio button yang memuat variabel penyimpan value, value itu sendiri, dan text (isi sub elemen radio button)      
            return tk.Radiobutton(root, text=text, variable=radio_var, value=value)

        for i, route in enumerate(routes):  # Penggunaan Loop untuk membuat radio-button agar efisien (tidak memakai banyak baris program)
            create_radio_button(route, i+1).pack()  # Dengan value i+1 karena looping dimulai dari 0
    
    # Buat sebuah text/header dengan elemen label dari tkinter
    label = tk.Label(root, text="Pilih Gate Awal Anda!")
    label.pack(pady=10)
    rute_semula()   # Panggil Fungsi yang telah di-define
    submit_button = tk.Button(root, text="Submit", command=submit_route)    # Elemen Tombol untuk men-submit pilihan rute awal pengguna 
    submit_button.pack(pady=10)

    def submit_vehicle_type():
        global vehicle_type
        vehicle_type = vehicle_var.get()
        if vehicle_type:
            messagebox.showinfo("Golongan Kendaraan", f"Golongan kendaraan Anda adalah : {vehicle_types[vehicle_type-1]}")
            print('Golongan Kendaraan:', vehicle_type)
            show_ticket()
        else:
            messagebox.showwarning("Invalid", "Mohon pilih golongan dengan benar!.")
            print('Golongan Kendaraan Invalid')

    vehicle_var = tk.IntVar()

    def calculate_tarif():      # Fungsi Pemroses Saldo dari Harga yang telah ditentukan
        global total, tarif, sampai, datang, rute_awal, final_route, saldo, golongan
        datang = rute_awal - 1
        sampai = final_route - 1

        arr_jarak = [72.64, 90.43, 87.02, 40.5, 36.27]      # Array Pemuat Jarak Antar satu pintu tol dengan pintu tol yang lain
        tarif_golongan = [1, 1.5, 2]        # Tarif dari golongan kendaraan
        golongan = vehicle_var.get()    # Ambil nilai dari value yang telah di-hold
        tarif = 0       # Inisialisasi variabel tarif yang akan diproses(ditambah) berdasarkan total biaya dari perjalanan

        if datang < sampai:     # Proses Penjumlahan tarif dari 1 pintu tol ke pintu tol yang lain
            for i in range(datang, sampai):
                tarif += arr_jarak[i] * 1000
        elif sampai < datang:
            for i in range(sampai, datang):
                tarif += arr_jarak[i] * 1000

        if golongan == 1:       # Pengali total biaya berdasarkan perjalanan dan golongan kendaraan
            total = tarif_golongan[0] * tarif
        elif golongan == 2:
            total = tarif_golongan[1] * tarif
        elif golongan == 3:
            total = tarif_golongan[2] * tarif

    def check_saldo_and_proceed():  # Fungsi pengecek, pemroses, dan penampil saldo
        global saldo, total
        if saldo >= total:
            saldo -= total
            messagebox.showinfo("Saldo Cukup", f"Transaksi berhasil. Sisa saldo Anda adalah: Rp{saldo}")
            next_step()
        else:
            messagebox.showwarning("Saldo Kurang", f"Saldo Anda tidak cukup. Tambahkan saldo minimal: Rp{total - saldo}")
            add_saldo()

    def add_saldo():        # Fungsi untuk Menambah Saldo apabila tidak mencukupi biaya perjalanan
        def update_saldo():
            global saldo    # Ingat untuk menggunakan elemen global karena nilai yang diubah akan digunakan di fungsi dan prosedur selanjutnya 
            additional_saldo = SALDO_var.get()
            saldo += additional_saldo
            messagebox.showinfo("Saldo Terupdate", f"Saldo Anda sekarang adalah: Rp{saldo}")
            if saldo >= total:
                check_saldo_and_proceed()
            else:
                messagebox.showwarning("Saldo Masih Kurang", f"Saldo Anda masih tidak cukup. Tambahkan lagi minimal: Rp{total - saldo}")
        
        for widget in root.winfo_children():        # Menghapus widget yang ada sebelumnya untuk memuat elemen-elemen lain, seperti label, button, entry, dll.
            widget.destroy()

        saldo_label = tk.Label(root, text="Tambahkan saldo Anda:")
        saldo_label.pack(pady=10)
        saldo_entry = ttk.Entry(root, textvariable=SALDO_var)
        saldo_entry.pack(pady=10, padx=10, fill="x", expand=True)
        submit_button = tk.Button(root, text="Submit", command=update_saldo)
        submit_button.pack(pady=10)

    def show_vehicle_selection():       # Fungsi Display Golongan Kendaraan
        for widget in root.winfo_children():
            widget.destroy()
        root.geometry("300x200")        # Pengubah Ukuran Window

        header_label = tk.Label(root, text=f"Gate awal Anda: {routes[rute_awal-1]}", font=("Arial", 14))
        header_label.pack(pady=10)

        label = tk.Label(root, text="Pilih Golongan Kendaraan Anda!")
        label.pack(pady=10)

        def create_radio_button(text, value):
            return tk.Radiobutton(root, text=text, variable=vehicle_var, value=value)

        vehicle_types = ["Golongan 1", "Golongan 2", "Golongan 3"]
        for i, vtype in enumerate(vehicle_types):
            create_radio_button(vtype, i+1).pack()

        submit_button = tk.Button(root, text="Submit", command=submit_vehicle_type)
        submit_button.pack(pady=10)

    def show_ticket():
        global ticket_number
        ticket_number = random.randint(1000, 9999)  # Digunakan modul dari library random untuk memuat bilangan integer 4 digit untuk tiket/karcis     
        messagebox.showinfo("Kode Tiket", f"Kode tiket Anda adalah : {ticket_number}")
        print('Kode tiket :', ticket_number)
        tahan() # Pemanggil Prosedur Penahan Window
    
    def tahan():
        for widget in root.winfo_children():
            widget.destroy()    # Jangan lupa untuk menghapus widget sebelumnya sebelum memuat elemen-elemen yang baru
        tahan_label = tk.Label(root, text="Selamat Jalan! Hati-hati dalam berkendara!\n(Tunggu hingga window selanjutnya muncul)\n(asumsi sedang di perjalanan)")
        tahan_label.pack(padx=10, fill="x", expand=True)
        root.geometry("300x200")
        root.update()
        time.sleep(4)   # Tahan Window selama beberapa detik (asumsi sedang berada di perjalanan)
        validate_ticket()

    def validate_ticket():      # Fungsi Pemvalidasi Tiket/Karcis
        for widget in root.winfo_children():
            widget.destroy()
        root.geometry("300x200")
        sapa_label = tk.Label(root, text="Selamat datang kembali !", font=("Helvetica", 10))
        sapa_label.pack(padx=10, fill="x", expand=True)
        label = tk.Label(root, text="Masukkan kode tiket Anda:", font=("Arial", 14))
        label.pack(pady=10)

        entry = tk.Entry(root, font=("Arial", 12))
        entry.pack(pady=10)

        def check_ticket():
            entered_ticket = entry.get()
            if entered_ticket.isdigit() and int(entered_ticket) == ticket_number:
                messagebox.showinfo("Ticket Valid", "Tiket sudah benar. Menuju Rute Final....")
                show_final_route_selection()
            else:
                messagebox.showerror("Tiket Invalid", "Tiket tidak benar. Silahkan coba lagi")

        submit_button = tk.Button(root, text="Submit", command=check_ticket)
        submit_button.pack(pady=10)

    def submit_final_route():       # Fungsi Untuk Mengirimkan Nilai dari Pilihan Gate Akhir
        global final_route, saldo
        final_route = radio_var2.get()
        if final_route == rute_awal:
            messagebox.showwarning("Salah!", f"Rute Tidak Boleh Sama dengan Rute Awal,\n You selected : {routes[final_route-1]}")
        elif final_route:
            calculate_tarif()
            messagebox.showinfo("Final Route Selected", f"You selected: {routes[final_route-1]}")
            print('Gate Final yang dipilih:', final_route)
            tunjuk_saldo_label = tk.Label(root, text=f"Saldo Anda adalah : Rp{saldo} dengan tarif Rp{total} dan tarif golongan {tarif_golongan[golongan-1]} dan tarif sementara {tarif} dengan koordinat {datang} menuju {sampai}")
            tunjuk_saldo_label.pack(padx=10, fill="x", expand=True)
            check_saldo_and_proceed()
        else:
            messagebox.showwarning("Invalid", "Mohon pilih rute final Anda dengan benar.")
            print('Gate Final Invalid/Kosong')

    def show_final_route_selection():
        global radio_var2
        for widget in root.winfo_children():
            widget.destroy()
        root.geometry("500x300")
        def create_radio_button(text, value):
            return tk.Radiobutton(root, text=text, variable=radio_var2, value=value)

        label = tk.Label(root, text="Select Your Final Route")
        label.pack(pady=10)

        radio_var2 = tk.IntVar()
        for i, route in enumerate(routes):
            create_radio_button(route, i+1).pack()

        submit_button = tk.Button(root, text="Submit", command=submit_final_route)
        submit_button.pack(pady=10, padx=10)

    def next_step():
        global lanjut_var
        for widget in root.winfo_children():
            widget.destroy()
        root.geometry("300x200")
        lanjut_label = tk.Label(root, text="Apakah Anda ingin melanjutkan perjalanan?")
        lanjut_label.pack(padx=10, fill="x", expand=True)

        def create_radio_button(text, value):
            return tk.Radiobutton(root, text=text, variable=lanjut_var, value=value)

        lanjut_var = tk.IntVar()
        create_radio_button("Lanjut", 1).pack()
        create_radio_button("Tidak", 0).pack()

        submit_button = tk.Button(root, text="Submit", command=pilihan_lanjut)
        submit_button.pack(pady=10)

    def pilihan_lanjut():
        lanjut_kah = lanjut_var.get()
        global rute_awal
        if lanjut_kah == 1:
            saldo_pilihan_lanjut()
            rute_awal = radio_var2.get()
            print('Rute Awal sekarang:', rute_awal)
        elif lanjut_kah == 0:
            tidak()

    def saldo_pilihan_lanjut():
        messagebox.showinfo("Saldo Aktual", f"Saldo Anda sekarang adalah {saldo}")
        show_ticket()

    def tidak():
        for widget in root.winfo_children():
            widget.destroy()

        tidak_label = tk.Label(root, text="Terima kasih telah menggunakan layanan kami!")
        tidak_label.pack(padx=10,pady=10, fill="x", expand=True)
        tidak_label = tk.Label(root, text="- Monitor 10", font="Gotham")
        tidak_label.pack(padx=10,pady=10, fill="x", expand=True)

        root.geometry("400x200")
        root.update()
        time.sleep(2)
        root.destroy()

# Landing Page/Window Pertama
def landing_page():
    for widget in root.winfo_children():
        widget.destroy()

    header_label = tk.Label(root, text="Monitor 10 \nToll Gate System", font=("Arial", 24), fg="white", bg="#3386FF", )
    header_label.pack(pady=10, padx=10)

    header_label = tk.Label(root, text="Pengenalan Komputasi - Kelas 32\nAditya Fernandes Sitepu (16623172)\nDzaky Addimasyqi (16623292)\nIrgi Jasmine Nabila (16623092)\nFaras Ayu Novitri (16623037)\nMuhammad Bramantya A. M. (16623297)\nNafisa Itqanti Yudistia (16623002)", font=("helvetica", 14), fg="white", bg="#3386FF")
    header_label.pack(pady=10, padx=10)

    root.update()

    start_button = tk.Button(root, text="Start", command=show_main_page, font=("Arial", 14),fg="Cyan", bg="#3386FF")
    start_button.pack(pady=10)

# Panggil/Tampilkan jendela pertama
landing_page()

# Looping untuk menjalankan window
root.mainloop()
