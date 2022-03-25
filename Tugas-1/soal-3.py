nilaiTeori = float(input("Masukkan nilai ujian teori:"))
nilaiPraktek = float(input("Masukkan nilai ujian praktek:"))

if (nilaiTeori >= 70 and nilaiPraktek >= 70):
    print("Selamat, anda lulus!")
elif (nilaiTeori >= 70 and nilaiPraktek < 70):
    print("Anda harus mengulang ujian praktek.")
elif (nilaiTeori < 70 and nilaiPraktek >=70 ):
    print("Anda harus mengulang ujian teori.")
elif (nilaiTeori < 70 and nilaiPraktek < 70):
    print("Anda harus mengulang ujian teori dan praktek")

