## Analisis Sentimen Twitter

Analisis Sentimen Twitter terhadap Kuliah Online menggunakan algoritma Naive Bayes.

## Instalasi

1. Install **Python 3.8.***.
2. Install **XAMPP**.
3. Import database aplikasi:
   - Jalankan **XAMPP**.
   - Buka phpMyAdmin dengan cara menekan tombol admin pada modul **MySQL**.
   - Pilih **import** pada navbar phpMyAdmin.
   - Tekan **Choose file**.
   - Pilih file **database.sql**.
4. Buka CMD dalam direktori lalu ketik perintah `python -m venv Env` untuk membuat python virtual environment.
5. Jalankan **start-env.bat** untuk masuk ke dalam virtual environment.
6. Ketik perintah `pip install -r requirements.txt` untuk menginstal kebutuhan dari python.
7. Ketik perintah `pip install mysqlclient-1.4.6-cp38-cp38-win_amd64.whl` untuk menginstal mysqlclient.
8. Ketik perintah `python`.
9. Ketik perintah `import nltk`.
10. Ketik perintah `nltk.download('stopwords')`.
11. Ketik perintah `exit()`.
12. Jalankan start-project.bat untuk menjalankan aplikasi.
13. Buka URL http://127.0.0.1:8000/ pada browser yang digunakan untuk membuka aplikasi.
