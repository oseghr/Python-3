#install all the libraries required
#create a function that collects a text and converts it to a QR code
#save the QR code as an image
#run the function
import qrcode

#User supplied information
site_url = input("Enter your site URL (eg. https://www.myapp.com):\n")
imageName = input("Enter your QR Code name:\n")

def generate_qrcode(site_url):
    #QR Code setup object parameters
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    #QR Code functionality
    qr.add_data(site_url)
    qr.make(fit = True)
    #QR Code Image settings
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{imageName}.png")
    print("QR Code generated successfully")

generate_qrcode(site_url)
