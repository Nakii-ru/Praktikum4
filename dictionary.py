nilai_data = []

while True:
    print("\nMasukkan Data Mahasiswa")

    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    data = {
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    nilai_data.append(data)

    tambah_data = input("Tambah Data Lagi? (y/t): ").lower()
    if tambah_data == 't':
        break

print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
print("=" * 64)
for i, data in enumerate(nilai_data, start=1):
    print(f"{i}  | {data['nama']}\t| {data['nim']} | {data['tugas']}  | {data['uts']}| {data['uas']}| {data['nilai_akhir']:.2f}        |")
print("=" * 64)