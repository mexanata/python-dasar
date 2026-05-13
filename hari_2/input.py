import aritmatika2 as f

BB = float(input("masukan berat badan (kg):"))
TB =float(input("masukan tinggi badan (cm):"))

bmi =f.bmi(BB, TB)
print("BMI Anda adalah: ", bmi)

f.bmi_check(bmi)

with open("data.txt", "a") as file:
    file.write(f"{bmi}\n")
