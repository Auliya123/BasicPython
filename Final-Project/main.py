import smtplib, ssl,os

from getpass import getpass

import send

port = 465  # port for SMTP_SSL()
email_directory = os.getcwd() + "/Final-Project/receiver_list.txt"

# LOGIN
def login(server):
    print("LOGIN")
    global email
    email = input("Email: ")
    password = getpass(prompt="Enter your password: ")
    try:
        server.login(email, password)
        print("You are logged in")
        return True
    except:
        print("Invalid Login")
        return False

# Create a secure SSL Context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    auth = login(server)
    if auth:
       count = 0
       while count != 3:   
            print("--- Menu --- \n 1. Kirim Pesan \n 2. Kirim File \n 3. Keluar ")
            menu = int(input("Pilih Menu: "))
            count = menu

            if menu == 1:
                subject = input("Subject: ")
                text = input("Message: ")
                send.message(server, email, subject, text)
            elif menu == 2:
                subject = input("Subject: ")
                text = input("Message: ")
                send.attachment(server, email, subject, text)
            elif menu == 3:
                print("Program selesai, sampai jumpa! ")
                break
            else:
                print("Menu tidak tersedia ")