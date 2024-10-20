# Program sederhana yang meminta input angka dan menjumlahkannya hingga user memasukkan angka 0
total = 0
angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    total += angka
    angka = int(input("Masukkan angka lagi (0 untuk berhenti): "))

print(f"Total jumlah angka yang dimasukkan adalah: {total}")
