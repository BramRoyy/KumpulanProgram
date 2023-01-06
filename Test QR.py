import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 3,
)
qr.add_data('youtube.com')

img = qr.make_image(
    fill_color = "purple",
    back_color = "white"
)
img.save("QR to Youtube.jpg")