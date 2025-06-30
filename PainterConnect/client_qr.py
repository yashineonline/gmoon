import qrcode
import streamlit as st
import tempfile
import os

st.title("📱 QR Code Generator for PainterConnect")

st.write("Paste your deployed Streamlit client app link below:")

url = st.text_input("Streamlit Client App URL")

if url:
    qr = qrcode.make(url)

     # Create a temporary directory to save the QR code
    with tempfile.TemporaryDirectory() as temp_dir:
        qr_path = os.path.join(temp_dir, "client_qr.png")
        qr.save(qr_path)
        st.image(qr_path, caption="Scan this QR to open the form!")
        st.success("✅ QR Code generated and saved temporarily.")



