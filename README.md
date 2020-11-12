# Doremi Search Engine
Tugas Besar Aljabar Linier dan Geometri 2020/2021

## Table of contents
* [Description](#description)
* [Before you start](#before-you-start)
* [Inspiration](#inspiration)
* [Contact](#contact)

## Description
Program ini merupakan search engine dengan query berupa kalimat dalam bahasa Indonesia. Proses pencarian dokumen dilakukan berdasarkan dokumen-dokumen yang diunggah ke dalam program sebelum memulai pencarian. Proses pencarian dokumen yang paling sesuai dengan query dilakukan dengan menggunakan rumus cosine similarity (dot product) pada sistem temu balik aplikasi. Program akan menampilkan urutan dokumen berdasarkan tingkat kemiripannya dengan query, serta tabel yang merepresentasikan jumlah setiap kata pada dokumen yang sesuai dengan query.

Program ini ditulis dalam bahasa python. Untuk menjalankannya, silahkan install python terlebih dahulu di [sini](https://www.python.org/downloads/)

## Before you start
Sebelum memulai program pastikan anda sudah memiliki pip pada python. Instruksi untuk instalasi pip dapat dilihat di [sini](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/)

Kemudian pastikan anda sudah memiliki library berikut:
* flask
* flask-sqlalchemy
* pandas
* numpy
* sastrawi
* nltk

Untuk melakukan instalasi cukup menjalankan perintah pada terminal:

* `pip install <nama_library>` (untuk sistem operasi Windows dan Linux)
* `pip3 install <nama_library>` (untuk sistem operasi MacOS)

Khusus untuk library nltk, silahkan menjalankan python pada terminal, lalu tuliskan:

`import nltk `

`nltk.download()`

Sebelum menjalankan program, pastikan database untuk menyimpan dokumen sudah dibuat dengan menjalankan perintah pada terminal:
* `python generatedb.py` (untuk sistem operasi Windows dan Linux)
* `python3 generatedb.py` (untuk sistem operasi MacOS)

## Inspiration
Fungsi cosine similarity dan sistem temu balik aplikasi kami pelajari dari sebuah [website](https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-12-Aplikasi-dot-product-pada-IR.pdf) yang ditulis oleh Rinaldi Munir. Proses pembuatan Flask, database SQL, HTML dan CSS kami pelajari dari sumber online.

## Contact
Program ini dibuat oleh:
* [Andres Jerriel Sinabutar](https://github.com/andresjerriels)
* [Rafidika Samekto](https://github.com/rafidika)
* [Ryo Richardo](https://github.com/ryorichardo)
