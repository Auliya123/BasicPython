contactList = []

def inputData():
    name = input("Nama: ")
    phone = input("No Telepon: ")
    contactData = {"name" : name,"phone" :phone}
    contactList.append(contactData)
    print("Kontak berhasil ditambahkan")

count = 0
while count != 3:
    print("--- Menu --- \n 1. Daftar Kontak \n 2. Tambah Kontak \n 3. Keluar ")
    menu = int(input("Pilih Menu: "))
    count = menu

    if menu == 1:
        print("Daftar Kontak:")
        
        if len(contactList) == 0:
            print("Kontak kosong")

        for i in range(len(contactList)):
            print("Nama: {}".format(contactList[i]["name"]))
            print("No Telepon: {}".format(contactList[i]["phone"]))
    elif menu == 2:
        inputData()
    elif menu == 3:
        print("Program selesai, sampai jumpa! ")
        break
    else:
        print("Menu tidak tersedia ")
