# Program Daftar Kontak
# Fungsi
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print(f"Nama: {kontak['nama']}")
        print(f"No Telepon: {kontak['no telepon']}")
def new_kontak():
    nama = input("Nama: ")
    no_telepon = input("No Telepon: ")
    kontak = {
        "nama" : nama,
        "no telepon" : no_telepon
    }
    return kontak

# List of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Farhan",
    "no telepon" : "08123456789"
})
daftar_kontak.append({ "nama" : "Joko",
    "no telepon" : "08987654321"
})

# Menu program
while True:
    print("Selamat Datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    option = (input("Pilih Menu: "))

    if option == "3":
        break
    elif option == "1":
        display_kontak(daftar_kontak)
    elif option == "2":
        kontak = new_kontak()
        daftar_kontak.append(kontak)
    else:
        print("Menu tidak tersedia")
print("Program selesai, sampai jumpa!")