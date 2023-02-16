#install all the libraries required
#create a function that collects a text and converts it to a QR code
#save the QR code as an image
#run the function
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )