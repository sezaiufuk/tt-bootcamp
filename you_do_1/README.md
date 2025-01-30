# You Do 1: Binge Watching

## Brief

Operasyon Kodu: Binge Watching
Tarih: 30 Ocak 2025

Ekip merhabalar,

İş birimimizin yine size ihtiyacı var. Yeni oluşturulacak video platformumuz için son bir haftaları ve tavsiye motoru için ellerinde bir şey yok. Yurt dışı bir firmadan bir teklif istemişler velakin kalan bütçede yer de  yok. Konu bize intikal etti, biz de sizin adınıza söz vermiş bulunduk. İhtiyaçları olan temel tavsiye motoru için gerekli kodu 3 gün içinde geliştirmek durumundayız.

Dikkatli olun, eğitiminize güvenin ve görev başarıyla tamamlanana kadar temkinli hareket edin. Bilim mi film mi şakasını yapardım ancak sırası değil...

Başarılar,
Hüsnü Şensoy

## Detaylar

Amacımız bu ilk you do'da complex bir recommendation engine yazmak değil, sadece Python kaslarımızı tam anlamıyla oturtmak için biraz egzersiz yapmak.

Elimizde boyutu çok küçük olmayan 4 adet dosya var bunlar bazı filmlere kullanıcıların verdiği skoları içeriyor.

* `rating*.txt` dosya deseni `movie_id,user_id,tarih,rating` olacak şekilde 4 alandan oluşuyor.

* `movie_titles.csv` dosyası da `movie_id,yayım yılı,film adı`olacak şekilde 3 alandan oluşuyor.

Verinin tamamını `https://storage.googleapis.com/sadedegel/dataset/binge.tar.gz` linkinden indirilebilir durumda.


## İş Birimi Taleplerimiz

* Özellikle sistemimize yeni kayıt olan kullanıcılarımıza *cold start* bir tavsiye üretmek istiyoruz. Abone ile alaklı hiç bir fikrimizin olmadığı durum için ne yapabilir ? 

* Sistemde film izlemiş ve bir kaç filmi skorlamış kullanıcılarımıza hızlı çalışacak bir tavsiye motoru inşa etmek istiyoruz. Alternatifler ne olabilir ?

* Bazı filmleri sistemden kaldırmayı düşünüyoruz. Son olarak bunun için bir ricamız daha var. Verilen iki filmi bizim için kıyaslasanız ve bunların arasında bir fark var mı yok mu söyleseniz ? Böyle bir şeyi nasıl hallederiz ?


## Tavsiyeler

* Problemi bizim sağladığımız template üzerinden götürmek zorunda değilsiniz.

* Verinin boyutunun lütfen farkında olarak çalışın. Python hızlıca memory tüketebilen ve çok da verimli olmayan bir programlama ortamı

* Bir çıktı üretmeyi `cool` bir şeyler yapmaya tercih edin.
