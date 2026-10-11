import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import io

st.set_page_config(page_title="Elias.smith - Ultra Premium", page_icon="✨")
st.title("✨ Photo Ultra Premium 8K")
st.markdown("### by **Elias.smith**")

uploaded = st.file_uploader("Choisis une photo", type=["jpg","png","jpeg","webp"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Avant")
    if st.button("🚀 Passer en Ultra Premium"):
        w,h = img.size
        img_big = img.resize((w*2, h*2), Image.LANCZOS)
        img_sharp = img_big.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=1))
        img_sharp = ImageEnhance.Contrast(img_sharp).enhance(1.2)
        st.image(img_sharp, caption="Apres - by Elias.smith")
        buf = io.BytesIO()
        img_sharp.save(buf, format="PNG")
        st.download_button("📥 Telecharger", buf.getvalue(), "elias_smith_8K.png", "image/png")

st.markdown("---")
st.write("© 2026 Elias.smith")
