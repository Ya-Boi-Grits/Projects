import qrcode


def create_qr_code(string):
    qr = qrcode.QRcode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3
    )

    qr.add_data(string)
    qr.make(fit=True)
