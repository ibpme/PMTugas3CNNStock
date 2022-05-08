# PMTugas3CNNStock

## Install Requirements

```bash
pip3 install -r requirements.txt
```

## Run Testing

```bash
python test_technical_indicators.py
```

## Tugas 3 - CNN untuk prediksi harga saham

Ketentuan umum
•Kali ini dengan model CNN kita bisa membangun model untuk prediksi menggunakan data masa lalunya dan data variabel-variabel actual lainnya.

•Data aktual yang sering dipergunakan orang untuk kebutuhan ini bisa berupa berbagai variabel Technical Indicators.

•Jadi tugas ini bisa dipandang sebagai jembatan untuk menuju proses pembuatan Trading Strategy Model, yang mungkin akan diperluas dan dipakai setelah lulus jadi sarjana.

•Deadline: 13 Mei 2022

Prosedur eksperimen
1.Setiap mahasiswa perlu mempelajari paper karya Omer Berat Sezer dan Ahmet Murat Ozbayoglu yang berjudul “Algorithmic financial trading with deep convolutional neural networks: Time series to image conversion approach”

2.Bila diperlukan, bisa juga ditambah dengan tulisan karya Asutosh Nayak berjudul “Stock Buy/Sell Prediction Using Convolutional Neural Network” di https://towardsdatascience.com/stock-market-action-prediction-with-convnet-8689238feae3

3.Mahasiswa perlu mengusahakan penggunaan data harga saham selama 20 tahun bila tersedia. Boleh harga saham Indonesia atau harga saham mana saja. Kadang data tidak tersedia lengkap seperti halnya dengan data harga saham Bank BNI yang hanya bisa didownload dari Yahoo Finance untuk periode 17 tahun saja.

4.Selain data harga saham, mahasiswa perlu mempersiapkan diri dengan berbagai variabel technical indicators yang sesuai dengan harga saham yang dipilih. Itu bisa diperoleh di https://www.alphavantage.co/

5.Untuk memahami tugas ini, mahasiswa perlu mencoba untuk melihat efek dari perubahan hyperparameter. Bila sudah paham, bangunlah model sendiri berdasarkan data harga saham dan beberapa data untuk variabel technical indicators yang sesuai.

6.Bila upaya pembuatan model untuk prediksi yang bagus sudah tercapai, maka lakukan langkah-langkah berikut

1.Buat laporan hasil eksperimen berbentuk paper (makalah) dan Notebook secara terpisah.

2.Buat rekaman video presentasi paper tersebut secara bergantian oleh anggota tim. Panjang maksimum video adalah 15 menit. Video harus diupload ke YouTube dan serahkan link-nya ke saya. (tentative/bonus)

7.Paper (makalah) harus memuat:
(a) Abstrak. Didalamnya dituliskan secara ringkas
i. Permasalahan yang dihadapi
ii. Alat untuk memecahkan masalah atau metodologi.
iii. Hasil yang diperoleh

(b) Pendahuluan. Pada pendahuluan perlu dituliskan gambaran masalah dan mengapa itu penting, serta latar belakang apa pun yang perlu diketahui pembacanya.

(c) Metodologi. Di bagian metode ini, akan dideskripsikan detail implementasi dan arsitektur model yang dibangun, dan dibahas cara untuk mendekati permasalahan dan desain solusinya.

(d) Hasil. Di bagian hasil, akan diperlihatkan kinerja model beserta semua metrik kinerja yang diperlukan untuk mendukungnya.

(e) Diskusi. Pada bagian diskusi ini akan disoroti makna hasil dan pendekatan yang diperoleh dalam pekerjaan ini

(f) Kontribusi. Ceritakan kontribusi masing-masing anggota tim di dalam kerjasama untuk menyelesaikan tugas ini.
