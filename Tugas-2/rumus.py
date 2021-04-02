def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=======================================")
        print(f"Nama: {kontak['nama']}")
        print(f"Telepon: {kontak['telepon']}")
def new_kontak():
    nama = input("Nama: ")
    telepon = input("Telepon: ")
    kontak = {
        "nama" : nama,
        "no telepon" : telepon
    }
    return kontak