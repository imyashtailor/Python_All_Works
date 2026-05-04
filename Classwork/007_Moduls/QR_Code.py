import qrcode

#create and make the qrcode
img = qrcode.make('https://www.google.com/')

#save image file
img.save('google_qr.png')