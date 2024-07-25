# Traffic Density Detection using YOLOv5

Proyek ini menggunakan YOLOv5 untuk mendeteksi objek seperti motor, mobil, dan pejalan kaki dalam gambar lalu lintas, dan menampilkan hasilnya menggunakan Streamlit.

## Instalasi

1. Clone repository ini:
    ```bash
    git clone https://github.com/username/traffic-detection.git
    cd traffic-detection
    ```

2. Instal dependensi:
    ```bash
    pip install -r requirements.txt
    ```

3. Unduh model YOLOv5:
    ```bash
    git clone https://github.com/ultralytics/yolov5
    cd yolov5
    pip install -r requirements.txt
    ```

## Penggunaan

1. Jalankan aplikasi Streamlit:
    ```bash
    streamlit run app.py
    ```

2. Unggah gambar untuk deteksi.
3. Hasil deteksi akan ditampilkan di browser.

## File yang Dibutuhkan
- Gambar untuk deteksi dalam folder `images/`.
- Model YOLOv5 dari repository [ultralytics/yolov5](https://github.com/ultralytics/yolov5).
