# program menghitung BMI
berat = float(input("masukan berat badan (kg):"))
tinggi_cm =float(input("masukan tinggi badan (cm):"))

tinggi_m = tinggi_cm / 100

# menghitung BMI
bmi = berat / (tinggi_m ** 2)
print(f"BMI Anda adalah: {bmi:.2f}")

# menentukan kategori bmi
if bmi < 18.5:
    print ("kategori : berat badan kurang ")
elif bmi < 18.5 and bmi < 25:
    print("kategori : berat badan normal ")
elif bmi < 25 and bmi < 30:
    print("kategori : berat badan berlebih ")

else:
    print("kategori : obesitas ")


