import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ---- Load Model and Labels ----
MODEL_PATH = "keras_model.h5"
LABELS_PATH = "labels.txt"

# --- Fix: Patch DepthwiseConv2D to ignore 'groups' argument ---
from tensorflow.keras import layers

old_from_config = layers.DepthwiseConv2D.from_config

def patched_from_config(cls, config):
    # Remove 'groups' key if it exists in the layer config
    config.pop("groups", None)
    return old_from_config(cls, config)

layers.DepthwiseConv2D.from_config = classmethod(patched_from_config)
# ----------------------------------------------------------------

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    with open(LABELS_PATH, "r") as f:
        labels = [line.strip() for line in f.readlines() if line.strip()]
    return model, labels

model, labels = load_model()

# ---- Page Layout ----
st.title("🌊 CleanSeaVision: Ocean Waste Detector")
st.write("Upload an image to detect marine waste and promote sustainability!")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

# Eco tips
eco_tips = {
    "Plastic": "♻ Tip: Collect and recycle plastic bottles to prevent ocean pollution.",
    "Oil": "🛢 Tip: Report oil spills and avoid dumping waste oils into drains.",
    "Organic": "🍃 Tip: Compost organic waste or allow natural decomposition.",
    "Clean": "💧 Tip: Keep our waters clean by reducing plastic use.",
}

# ---- Prediction Section ----
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_resized = image.resize((224, 224))
    img_array = np.asarray(img_resized).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    idx = int(np.argmax(prediction))
    label = labels[idx]
    confidence = float(prediction[idx]) * 100

    st.subheader(f"Prediction: {label}")
    st.write(f"Confidence: {confidence:.2f}%")

    st.success(eco_tips.get(label, "🌱 Tip: Reduce, Reuse, Recycle. Every step counts!"))
