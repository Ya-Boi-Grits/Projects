import qrcode  # Imports a Python library


def create_qr_code(string):  # TLDR: uses tje qrcode class in a function that takes a string
    # Sets constraints for the object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(string)
    qr.make(fit=True)

    # Sets the colors and saves the image into current directory
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("someQRcode.png")


create_qr_code("https://www.protondb.com/")
