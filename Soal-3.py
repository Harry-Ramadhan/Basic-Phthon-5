teori = 90
praktek = 90


if teori < 70 and praktek < 70:
    print("Anda harus mengulang ujian teori dan praktek.")
elif praktek < 70:
    print("Anda harus mengulang ujian praktek.")
elif teori < 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Selamat, anda lulus!")


