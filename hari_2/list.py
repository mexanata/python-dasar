index = [0,1,2,3,4,5,6,7]
nama = ["alice","bob","charlie","edi","farah","dona","pixel"]
nilai = [80,90,100,80,60,90,100]

nama_slice_3_tengah = nama[2:5]
nilai_slice_3_tengah = nilai[2:5]

nama_slice_3_tengah[2] = "poki"
print("\n")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#insert
nama_slice_3_tengah.insert(1,"niko")
nilai_slice_3_tengah[0] = 99
print("\n")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#append
nama_slice_3_tengah.append("mark")
print("\n")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#sort
nama_slice_3_tengah.sort()
print("\n SORT")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#

#print(nama)
#print(nilai)

#print("\n")
#print("print dengan index")
#print(f"nama {nama[1]} mendapatkan nilai {nilai[1]}")

#for i in range(len(nama)):
    #print(f"nama {nama[i]} mendapatkan nilai {nilai[i]}")
