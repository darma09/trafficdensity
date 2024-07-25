import streamlit as st
import torch
from PIL import Image
import numpy as np
import shutil
import os

def detect_objects(image):
    # Pastikan direktori 'images' ada dan kosongkan jika ada file sebelumnya
    if not os.path.exists('images'):
        os.makedirs('images')
    else:
        for f in os.listdir('images'):
            os.remove(os.path.join('images', f))

    # Simpan gambar yang diunggah ke file
    image_path = "images/uploaded_image.jpg"
    image.save(image_path)
    
    # Muat model YOLOv5 dari GitHub
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    
    # Lakukan inferensi
    results = model(image_path)
    
    # Simpan hasil
    results.save()
    
    # Ekstrak dan hitung deteksi
    detections = results.pandas().xyxy[0]
    counts = {'motorcycle': 0, 'car': 0, 'person': 0}
    for _, row in detections.iterrows():
        if row['name'] in counts:
            counts[row['name']] += 1
    
    return counts, os.path.join('runs/detect/exp', os.path.basename(image_path))

# Antarmuka Streamlit
st.title("Traffic Density Detection using YOLOv5")
st.write("Upload an image and the model will detect and count motorcycles, cars, and pedestrians.")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    st.write("Detecting objects...")
    counts, result_image_path = detect_objects(image)
    
    st.write(f'Jumlah motor: {counts["motorcycle"]}')
    st.write(f'Jumlah mobil: {counts["car"]}')
    st.write(f'Jumlah pejalan kaki: {counts["person"]}')
    
    st.image(result_image_path, caption='Detected Image.', use_column_width=True)
