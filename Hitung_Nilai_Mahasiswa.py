import os 
os.system("cls")

print("Selamat datang di Aplikasi Perhitungan Nilai Mahasiswa")
print("======================================================")
nilai_tugas = input("Silakan Masukkan Nilai Tugas Anda: ")
nilai_uts = input("Silakan Masukkan Nilai UTS Anda: ")
nilai_uas = input("Silakan Masukkan Nilai UAS Anda: ")
nilai_akhir = (0.25 * float(nilai_tugas)) + (0.35 * float(nilai_uts)) + (0.4 * float(nilai_uas))
print("Nilai Akhir Anda Adalah: ", nilai_akhir)

if nilai_akhir >= 85:
    print("Selamat, Anda Mendapat Nilai A")
elif nilai_akhir >= 80 and nilai_akhir < 85:
    print("Selamat, Anda Mendapat Nilai A-")
elif nilai_akhir >= 75 and nilai_akhir < 80:
    print("Selamat, Anda Mendapat Nilai B+")
elif nilai_akhir >= 70 and nilai_akhir < 75:
    print("Anda Mendapat Nilai B")
elif nilai_akhir >= 65 and nilai_akhir < 70:
    print("Anda Mendapat Nilai B-")
elif nilai_akhir >= 60 and nilai_akhir < 65:
    print("Anda Mendapat Nilai C+")
elif nilai_akhir >= 55 and nilai_akhir < 60:
    print("Perhatian, Anda Mendapat Nilai C")
elif nilai_akhir >= 50 and nilai_akhir < 55:
    print("Perhatian, Anda Mendapat Nilai C-")
elif nilai_akhir >= 30 and nilai_akhir < 50:
    print("Perhatian, Anda Mendapat Nilai D")
elif nilai_akhir < 30:
    print("Anda Mendapat Nilai E, Anda Tidak Lulus Mata Kuliah Ini")
else:
    print("Nilai Anda Tidak Valid")