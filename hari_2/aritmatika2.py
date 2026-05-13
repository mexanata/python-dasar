def bmi(BB = None, TB = None):
    if BB is None or TB is None:
        print("parameter tidak lengkap")
        return None

    TB_m = TB / 100
    total = BB / (TB_m ** 2)
    return round(BB / (TB_m ** 2), 2)


def bmi_check(bmi):
    if bmi is None:
        return ("BMI tidak valid")

    if bmi < 18.5:
        return("Kurus")
    elif bmi < 25:
        return("Normal")
    elif bmi < 30:
        return("Gemuk")
    else:
        return("Obesitas")

