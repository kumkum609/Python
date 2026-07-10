import qrcode
#take the url from user
url = input("Enter the URL: ").strip()

#configure the Qr code with small version and border
qr =qrcode.QRCode(version=1,border=1)
qr.add_data(url)
qr.make(fit=True)
qr.print_ascii(invert=True)
print("Qr code generated!")