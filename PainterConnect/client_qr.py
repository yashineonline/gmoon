import qrcode
import streamlit as st

st.title("📱 QR Code Generator for PainterConnect")

st.write("Paste your deployed Streamlit client app link below:")

url = st.text_input("Streamlit Client App URL")

if url:
    qr = qrcode.make(url)
    qr.save("client_qr.png")
    st.image("client_qr.png", caption="Scan this QR to open the form!")
    st.success("✅ QR Code generated and saved as 'client_qr.png'")
