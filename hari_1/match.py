from re import match

nilai = input("masukan nilai (1-7): ")

match nilai:
    case "1" | "2" | "3" :
        print("hari kerja awal")
    case "4" | "5" :
        print("hari kerja akhir")
    case "6" | "7" :
        print("weekend")


