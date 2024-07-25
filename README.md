# Deteksi Objek Menggunakan YOLOv5

Proyek ini menggunakan YOLOv5 untuk mendeteksi objek seperti motor, mobil, dan pejalan kaki dalam gambar lalu lintas.

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

1. Letakkan gambar dalam folder `images/`.
2. Jalankan skrip deteksi:
    ```bash
    python detect.py --source images/your_image.jpg
    ```

Hasil deteksi akan disimpan dalam folder `runs/detect/`.

## File yang Dibutuhkan
- Gambar untuk deteksi dalam folder `images/`.
- Model YOLOv5 dari repository [ultralytics/yolov5](https://github.com/ultralytics/yolov5).
