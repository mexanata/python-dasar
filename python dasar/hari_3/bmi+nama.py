from hari_2 import greeting
from hari_2 import aritmatika2 as f
from datetime import datetime
import sys

nama = greeting.ambil_nama()

if nama:
    greeting.sapa(nama)

    try:
        BB = float(input("masukan berat badan (kg):"))
        TB =float(input("masukan tinggi badan (cm):"))
    except ValueError:
        print("input harus angka!")
        sys.exit()

    hasil_bmi =f.bmi(BB, TB)
    kategori = f.bmi_check(hasil_bmi)

    print(f"\n{nama}, BMI kamu: {hasil_bmi} kegedean")
    print(f"Kategori: {kategori}")

# simpan ke file
    with open("data.txt", "a") as file:
        file.write(f"{datetime.now()} | {nama} | BB: {BB} | TB: {TB} | BMI: {hasil_bmi} | {kategori}\n")

    print("\nData berhasil disimpan ke data.txt")

