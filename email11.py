import sys
import smtplib
import getpass

class Utama ():
    def __init__(self):

    pengirim = input ("Masukkan email pengirim (gmail): ")
    pwdpengirim = getpass.getpass("Masukkan password email pengirim :")
    penerima = input("Masukkan email tujuan :")
    pesan = input (" Masukkan pesan/isi email  :")

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.gmail.com","587")
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(pengirim, pwdpengirim)
        smtpObj.sendmail(pengirim,[penerima],pesan+"\n")
        print("Email telah terkirim")

    except smtplib.SMTPException:
        print("Email gagal terkirim!")


if __name__=="__main__":
    Utama()
    sys.exit()