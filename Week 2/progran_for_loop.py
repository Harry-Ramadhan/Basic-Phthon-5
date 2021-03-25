count = int(input("Berapa banyak data: "))

nama_pelanggan = []
nama_pelanggan = []

for i in range(count):
    print("Data ke {}" . format (i+1))
    nama = input("Nama: ")
    umur = int(input("Umur: "))

    nama_pelanggan.apppend(nama)
    umur_pelanggan.apppend(umur)

for i in range(len(nama_pelanggan)):
    print("Pelanggan: {} denagn usia: {}" .format(nama_pelanggan [i], umur_pelanggan [i]))