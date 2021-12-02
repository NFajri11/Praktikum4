daftar = []

while True:
    Nama = input("Nama               : ")
    NIM = input("NIM                : ")
    Tugas = int(input("Nilai Tugas        : "))
    UTS = int(input("Nilai UTS          : "))
    UAS = int(input("Nilai UAS          : "))
    Nilai_Akhir = (Tugas * 30/100) + (UTS * 35/100) + (UAS * 35/100)
    daftar.append([Nama, NIM, Tugas, UTS, UAS, Nilai_Akhir])

    tanya = input("Tambah data? (y/t) : ")
    if( tanya == "t"):
        break

print ("|================================Daftar Nilai Mahasiswa=======================================|")
print ("|=============================================================================================|")
print ("| no |   Nama   |     NIM     |   Tugas    |     UTS    |     UAS     |      Nilai Akhir      |")
print ("|=============================================================================================|")
i=0

for x in daftar:
    i+=1
    print("|{no:4d}| {Nama:8s} | {NIM:10s} | {Tugas:10d}  |  {UTS:10d} | {UAS:10d}  | {NilaiAkhir:15.9f}      |"
        .format(no=i, Nama=x[0], NIM=x[1], Tugas=x[2], UTS=x[3], UAS=x[4], NilaiAkhir=x[5]))
print ("|=============================================================================================|")