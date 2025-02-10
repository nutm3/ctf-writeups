# Ben 10
> ...


## About the Challenge
Kami diberikan sebuah desc dan dist untuk kita pelajari.
`[dist.zip]`

## How to Solve?
Pertama kita bisa extract dengan `unzip dist.zip`. Lalu diperoleh beberapa distribustion file

![img1](images/img1.png)

pada app.js kita lihat hanya mekanisme register, login, dan tidak ada satu pun vuln yang terlihat yang mungkin kita berfikir adalah sql injection, tetapi tidak bisa dia menggunakan syntax `?` dimana ini adalah mekanisme aman input control dari sql syntax.
```
...snippet...
cursor.execute("INSERT INTO users (username, password, admin_username) VALUES (?, ?, ?)",
                (username, password, admin_username))
cursor.execute("INSERT INTO users (username, password, admin_username) VALUES (?, ?, ?)",
                (admin_username, admin_password, None))
conn.commit()
...snippet...
```

lalu pada route /reset_password juga kita tidak memungkinkan untuk reset password admin

```
...snippet...
if username.startswith('admin'):
    flash("Admin users cannot request a reset token.", "error")
...snippet...
```


tetapi saya coba untuk regist dengan username admin tetapi tidak bisa, username already exists. oke tetapi kita pahami disini bahwa kita diharuskan untuk masuk sebagai ke admin. 

setelah saya perhatikan beberapa kali bahwa ada 2 functionality ane pada route `/image/<image_id>`. 
```
...snippet...
if image_id == 'ben10' and not username.startswith('admin'):
    return redirect(url_for('missing_permissions'))

flag = None
if username.startswith('admin') and image_id == 'ben10':
    flag = FLAG
...snippet...
```

functionality pertama dengan urutan jika image_id == 'ben10' dan username dari cookie tidak diawali `admin` maka gagal 
functionality kedua dengan urutan jika username dari cookie tidak diawali `admin` dan image_id == 'ben10' maka gagal 

dari sini saya paham bahwa kita harus akses ke `/image/ben10` terlebih dahulu baru setelahnya ubah cookie dengan set role ke admin. Dan yap flag pun didapatkan
![img2](images/img2.png)

```
srdlen{b3n_l0v3s_br0k3n_4cc355_c0ntr0l_vulns}
```
