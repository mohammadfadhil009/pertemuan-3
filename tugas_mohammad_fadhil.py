sisi = float(input("Masukkan sisi_persegi : "))

output = {"luas" : round(sisi**2), "keliling" : round(sisi * 4)}

print(output[input("Pilih luas atau keliling : ")])

