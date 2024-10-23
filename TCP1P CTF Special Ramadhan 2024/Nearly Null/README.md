#TCP1P CTF Special Ramadhan 2024

#Desc
> I have a document to be reviewed, but i cannot even extract it from the archive.

`[document.zip]`

## About the Challenge
Given the file document.zip

## How to solve?
Mungkin seperti soal sebelumnya, kita coba extract dulu.
![img1](img/1.png)

Dan yap mungkin ini yang dikatakan yang sekarang belum tentu sama seperti yang dulu. 

Kita coba cek dulu filenya.
![img2](img/2.png)

Saya mendapatkan referensi disini, 'http'. Ternyata ada 3 hal yang di ubah saya disini yaitu :
```
filename local header = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
filename length = 1F 00
filename directory header = AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```
![img3](img/3.png)

Alhamdulillah, file berhasil kita perbaiki. 
Kita coba extract, dan yap ini hasilnya file dengan nama `AAAAAAA...`
![img4](img/4.png)

Aku membuka flag ini di libreoffice writer
![img5](img/5.png)

```
TCP1P{UuUuU_n0w_y0u_c4n_r3v3aL_mY_s3cr3t}
```
