# Mini Search Engine
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
Sebelum memulai program pastikan anda sudah memiliki pip pada python. Pip dapat diinstall dengan menjalankan perintah `sudo apt install python3-pip` pada terminal.

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

## Inspiration
Fungsi cosine similarity dan sistem temu balik aplikasi kami pelajari dari zebuah [website](https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-12-Aplikasi-dot-product-pada-IR.pdf) yang ditulis oleh Rinaldi Munir. Proses pembuatan Flask, database SQL, HTML dan CSS kami pelajari dari sumber online.

## Contact
Program ini dibuat oleh:
* [Andres Jerriel Sinabutar](https://github.com/andresjerriels)
* [Rafidika Samekto](https://github.com/rafidika)
* [Ryo Richardo](https://github.com/ryorichardo)