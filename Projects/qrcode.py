#install all the libraries required
#create a function that collects a text and converts it to a QR code
#save the QR code as an image
#run the function
import qrcode

def generate_qrcode(text):
    #QR Code setup object parameters
    qr = qrcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    #QR Code functionality
    qr.add_data(text)
    qr.make(fit = True)
    #QR Code Image settings
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrImg.png")

generate_qrcode("https://www.cymworx.com")
