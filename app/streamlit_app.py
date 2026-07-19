from __future__ import annotations

import io

import streamlit as st
from PIL import Image

from cpathlab.inference.predictor import DemoPredictor

st.set_page_config(page_title="Computational Pathology AI Lab", layout="centered")
st.title("Computational Pathology AI Lab")
st.error("Research demonstration only. Not a medical device and not for clinical diagnosis.")
st.caption("The default interface uses a deterministic placeholder unless you connect a trained checkpoint.")
file = st.file_uploader("Upload a PNG, JPEG, or TIFF patch", type=["png", "jpg", "jpeg", "tif", "tiff"])
if file:
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    st.image(image, caption="Uploaded research image")
    result = DemoPredictor().predict(image)
    st.metric("Demo score", f"{result.probability:.3f}")
    st.write(result.model_status)
