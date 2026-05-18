from _pydatetime import datetime

def sapa():
    print("Halo")

def ambil_nama():
    nama = input("masukkan nama: ")
    if not nama:
        print("silahkan masukkan nama")
        return None
    return nama

def sapa(nama):
    print(f"Halo {nama}")

def waktu_sekarang():
    return datetime.now()
