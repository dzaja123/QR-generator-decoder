import qrcode


data = str(input("Унесите линк, текст или шифру за коју желите генерисати QR код: "))

img = qrcode.make(data) # генерисање QR-а 

filename = (f"QR.png")

img.save(filename) # чување QR-а у PNG формату

