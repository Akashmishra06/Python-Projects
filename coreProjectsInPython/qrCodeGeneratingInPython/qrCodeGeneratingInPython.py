import qrcode

# Create a QR code instance
qr_code = qrcode.QRCode(
    version=1,  # QR code version
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size around the QR code
)

# Add data to the QR code
data = "https://chat.openai.com/c/ad97550b-c55c-489a-8619-c558555b2561"
qr_code.add_data(data)
qr_code.make(fit=True)

# Generate the QR code image
qr_img = qr_code.make_image(fill_color="black", back_color="white")

# Save the QR code image
qr_img.save("chat-gpt-address.png")
