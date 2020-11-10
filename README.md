# Mini Search Engine
Tugas Besar Aljabar Linier dan Geometri 2020/2021

## Table of contents
* [Description](#description)
* [Before you start](#before-you-start)
* [Inspiration](#inspiration)
* [Contact](#contact)

## Description
Program ini merupakan search engine dengan query berupa kalimat dalam bahasa Indonesia. Proses pencarian dokumen dilakukan berdasarkan dokumen-dokumen yang diunggah ke dalam program sebelum memulai pencarian. Proses pencarian dokumen yang paling sesuai dengan query dilakukan dengan menggunakan rumus cosine similarity (dot product) pada sistem temu balik aplikasi. Program akan menampilkan urutan dokumen berdasarkan tingkat kemiripannya dengan query, serta tabel yang merepresentasikan jumlah setiap kata pada dokumen yang sesuai dengan query.

Program ini ditulis dalam bahasa python. Untuk menjalankannya, silahkan install terlebih dahulu python di [sini](https://www.python.org/downloads/)

## Before you start
Sebelum memulai program pastikan anda sudah memiliki library berikut:
* flask
* flask-sqlalchemy
* pandas
* numpy
* sastrawi
* nltk

Untuk melakukan instalasi cukup menjalankan perintah pada terminal:
`pip install <nama_library>`

Khusus untuk library nltk, silahkan menjalankan python pada terminal, lalu tuliskan:
`import nltk`
etc etc

## Inspiration
Fungsi cosine similarity dan sistem temu balik aplikasi kami pelajari dari website [ini](https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-12-Aplikasi-dot-product-pada-IR.pdf) yang ditulis oleh Rinaldi Munir. Proses pembuatan Flask, database SQL, HTML dan CSS kami pelajari dari sumber online, terutama dari stackoverflow.com dan github.com.

## Contact
Program ini dibuat oleh:
* [Andres Jerriel Sinabutar](https://github.com/andresjerriels)
* [Rafidika Samekto](https://github.com/rafidika)
* [Ryo Richardo](https://github.com/ryorichardo)