# Praktikum 4 - Data List

NAMA : RIDHO FHADLY HAMZAH

NIM : 312410486

KELAS : TI.24.A5

# Kode Program
```python
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
```

# Penjelasan Kode
```python
nilai_data = []
```
Program dimulai dengan inisialisasi dictionary list data kosong dengan `nilai_data = []`.
```python
while True:
    print("\nMasukkan Data Mahasiswa")

    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
```
Selagi Program berjalan, pengguna akan diminta untuk menginput `Nama`, `NIM`, `Nilai Tugas`, `UTS`, dan `UAS`.
```python
nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
```
Setelah Pengguna menginput `Nilai Tugas`, `UTS`, dan `UAS`. Program akan mengalikan dan menjumlahkan semua total nilainya sesuai dengan bobot ketentuan yg berlaku.
```python
 nilai_data.append(data)  
```
Baris ini befungsi untuk menambahkan/memperbarui elemen yg diinput oleh pengguna ke dalam list kosong yg sudah dibuat pada awal program.
```python
tambah_data = input("Tambah Data Lagi? (y/t): ").lower()
    if tambah_data == 't':
        break
```
Setelah pengguna menginput `Nama`, `NIM`, `Nilai` `Tugas`, `UTS`, dan `UAS`, kemudian, program akan bertanya apakah ingin menambahkan data baru lagi atau tidak.

Jika pengguna memilih tidak`(t)`, maka program akan berakhir.
```python
print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
print("=" * 64)
for i, data in enumerate(nilai_data, start=1):
    print(f"{i}  | {data['nama']}\t| {data['nim']} | {data['tugas']}  | {data['uts']}| {data['uas']}| {data['nilai_akhir']:.2f}        |")
print("=" * 64)
```
Setelah Program berakhir, maka program akan menampilkan hasil data Mahasiswa dan Nilai Akhir yang sudah diinputkan.
# Flowchart Kode
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/prak4.drawio(2).png?raw=true)

# Hasil Kode 
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-11-14%20124523.png?raw=true)
