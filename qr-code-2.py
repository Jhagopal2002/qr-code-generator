import qrcode
from PIL import Image


qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=12,border=5,
                 )
qr.add_data("https://www.linkedin.com/in/gopal-kumar-jha-146316281/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("Linkedin Page-2.png")

  
