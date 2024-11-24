
# loop kavramı

"""
██       ██████   ██████  ██████      ██   ██  █████  ██    ██ ██████   █████  ███    ███ ██ 
██      ██    ██ ██    ██ ██   ██     ██  ██  ██   ██ ██    ██ ██   ██ ██   ██ ████  ████ ██ 
██      ██    ██ ██    ██ ██████      █████   ███████ ██    ██ ██████  ███████ ██ ████ ██ ██ 
██      ██    ██ ██    ██ ██          ██  ██  ██   ██  ██  ██  ██   ██ ██   ██ ██  ██  ██ ██ 
███████  ██████   ██████  ██          ██   ██ ██   ██   ████   ██   ██ ██   ██ ██      ██ ██ 
"""
"""
belli kurala göre belli operasyonu tekrar eden yapilar
pythonda döngüler
--> while ve for keywordleri ile kullanilir.

--------while döngüsü------
10'dan 1 e kadar geri sayip yazdirmak
n = 10
while n>0
    print n;
    n = n-1;

while, calismaya baslamadan önce kuralin dogrulugunu kontrol eder
(durma kurali)
dogru ise bir kere islem yapilir.
sonrasinda kural tekrar kontrol edilir.
bu sekilde sonsuz bir döngü olmamasi icin her seferinde kural kontrol edilir

her seferinde n'i bir azalttigimiz icin durma kuralina uyunca döngüden cikar

--------for döngüsü------
0'dan 10'a kadar olan sayilari ekrana yazdiralim
for i in range(10) = i: döngü degiskeni
    print(i)

for, bir aralikta (range) ya da liste icinde kolayca döngü kurulmasini saglar

* belli aralikta döner -> range(baslangic, bitis, artis)
for i in range(1, 10, 2)
    print(i) == 2,4,6,8,10

for i in range(5, 30, 3)
    print(i) = 5,8,11,14,17,20,23,26,29

----------string dönme-------

metin = "python"
for harf in metin
    print harf =  p,y,t,h,o,n


    
-----------length kavrami---------

python'da dizi olan tipler = str,list için uzunlugu len ile bulunur
len("python") = 6
len("canozturk") = 10

metin = input("metin gir")
uzunluk = len(metin)
print(uzunluk) = 6 


-----------enumarate kavrami---------

for döngüsü ile gezerken, döngünün o andaki indeksine ihtiyac duyariz
bunun icin hazir bulunan enumarate fonksiyonu kullanilir.

for index, harf in enumerate(metin)
    yeni_metin += harf
    if index< len(metin)
        yeni_metin += "-"

    print(yeni_metin)

    

-----------nested loops kavrami---------
döngü icinde döngü demektir

while i<3
    yildizlar = ""
    j = 0                                   * * *
    while j<3                               * * *
        yildizlar += "* "       cikti =     * * *
        j += 1
    print(yildizlar)
    i += 1




-----------break kavrami---------
bazen döngü tamamlanmadan döngüden cikmamiz gerekebilir
bunun icin break kullanilir

for harf in metin
    if harf == " "
        break

    print harf

for i in range(30,100,1)
    if fi % 11 == 0
        print(i)
        break
    else
        print(i)
            

-----------continue kavrami--------- 
döngünün bir sonraki adiminia atlamayi saglar
döngü icinde dönerken bir kosul saglanirsa o andaki adimi atlamak icin kullanilir
bir sonraki adima gecilir.

for i in range(1,11)
    if i % 2 == 1
        continue
    print(i)

for harf in metin
    if harf == " "
        continue
    print(harf)         

-----------for-else kavrami---------
bazen for dongusunun düzgün tamamlanip tamamlanmadigini kontol etmemiz gerekebilir
eger, for dongusu bir elemani icin calismamissa(break gormusse) o zaman duzgun calismamis demektir

bunun icin for-else kullanilir
2 ile 10 arasindaki sayilari yazdirdigimizi varsayalim
eger sayi 7'nin kati ise döngüden cik

for i in range(2,11)
    print(i)
    if i % 7 == 0
        break
else
    print("döngü düzgün calisti)
print( for düzgün calisti)
"""

"""
 ██████  ██    ██ ██ ███████        ██ 
██    ██ ██    ██ ██    ███        ███ 
██    ██ ██    ██ ██   ███   █████  ██ 
██ ▄▄ ██ ██    ██ ██  ███           ██ 
 ██████   ██████  ██ ███████        ██ 
    ▀▀                                 
"""
# QUIZ-1
"""
1) Ekrana yıldızlardan oluşmuş bir kare çizen bir fonksiyon yazın. <br>
Fonksiyon parametre olarak karenin bir kenarında bulunan yıldız sayısını alsın. <br>
Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman karenin 5 satırı ve her satırda 5 sütunu (yıldız) olur.<br>
Bunun için iç içe **while** döngüleri kullananın.

    CÖZÜM = def kare_yildiz_while(n)
                i = 0
                while i < n
                    yildizlar = ""
                    j=0
                    while j<n
                        yildizlar += "* "
                    print(yildizlar)
                    i += 1    

2= Ekrana yıldızlardan oluşmuş bir kare çizen bir fonksiyon yazın. <br>
Fonksiyon parametre olarak karenin bir kenarında bulunan yıldız sayısını alsın. <br>
Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman karenin 5 satırı ve her satırda 5 sütunu (yıldız) olur.<br>
Bunun için iç içe **for** döngüleri kullananın.

    cözüm = def kare_yildiz_for(n)
            for i in range(n)
                yildizlar = ""
                for j in range(n)
                    yildizlar += "* "
                print(yildizlar)

3) Ekrana yıldızlardan oluşmuş bir ikizkenar dik üçgen çizen bir fonksiyon yazın. <br>
Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın. <br>
    cözüm = ucgen_while(n)
        i = 0
        while i<n
            yildizlar = ""
            j=0
            while j<=i
                yildizlar += "* "
                j += 1
            i += 1

4) Ekrana yıldızlardan oluşmuş bir ikizkenar dik üçgen çizen bir fonksiyon yazın. <br>
Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın. <br>

    cözüm = ucgen_for(n)
        for i in range(n)
            yildizlar = ""
            for j in range(i+1)
                yildizlar += "* "
            print(yildizlar)

            
5) Ekrana yıldızlardan oluşmuş ters bir ikizkenar dik üçgen çizen bir fonksiyon yazın. <br>
Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın. <br>

    cözüm = def ters_ucgen_for(n)
                for i in range(n, 0 ,-1)
                    yildizlar = ""

                    for j in range(i)
                        yildizlar += "* "
                    print(yildizlar)

6) Ekrana yıldızlardan oluşmuş bir ikizkenar üçgen çizen bir fonksiyon yazın. <br>
Fonksiyon parametre olarak bir sütundaki yıldız sayısını alsın. <br>

    cözüm = ikizkenar_ucgen_for(n)
                ucgen_for(n)
                ters_ucgen_for(n)

7) Parametre olarak kendisine verilen bir sayının asal sayı olup olmadığını dönen `bool` bir fonksiyon yazın. <br>
Sayı asal ise True, asal değilse False dönecek.

    cözüm = def asal_mi(n)
                asal = True
                for i in range(2,n)
                    if n%i == 0
                        asal = False
                return asal

8) Parametre olarak kendisine verilen bir sayının bütün asal çarpanlarını bulan bir fonksiyon yazın.

    cözüm = def asal_carpanlar
                for i in range(2,n)
                    in n%2==0
                        if asal_mi(i)
                            print(i)

9) 1'den 50'ye (ikisi de dahil) kadar olan sayılar üzerinde dönen bir fonksiyon yazın. <br>
* 3'ün katları için sayının kendisi yerine "Üj" 
* 5'in katları için sayının kendisi yerine "Bej"
* 3 ve 5'in ortak katları için ise sayının kendisi yerine "ÜjBej" yazsın.

    cözüm = def ujbej()
                uj = "UJ"
                bej = "BEJ"
                for i in range(1,51)
                    if i % 3 == 0 and i % 5 == 0:
                        print(uj+bej)
                    elif i % 3 == 0
                        print(uj)
                    elif i % 5 == 0
                        print(bej)
                    else
                        print(i)

10) Girilen bir cümleyi önce kelimelerine ayıran, sonra da bu kelimelerdeki harflerin arasına '-' (tire) karakteri koyan bir fonksiyon yazın. Daha sonra kelimeleri de '__' (iki alt tire) karakteri ile birleştirsin.

Ve birleşmiş yeni cümleyi kullanıcıya dönsün.

* Cümleyi kelimelere parçalamak için split() fonksiyonunu kullanınız

    cözüm = def cumle_birlestir(cumle):
                kelimeler = cumle.split()er
                birlesmis_cumle = ""
                for kelime_index, kelime in enumerate(kelimeler):
                    birlesmis_kelime = ""
                    for harf_index, harf in enumerate(kelime):
                        birlesmis_kelime += harf
                        if harf_index < len(kelime) - 1:
                            birlesmis_kelime += "-"
                    birlesmis_cumle += birlesmis_kelime  
                    if kelime_index < len(kelimeler) - 1:
                        birlesmis_cumle += "__"
                    
                return birlesmis_cumle






"""









# string işlemleri

"""
███████ ████████ ██████  ██ ███    ██  ██████      ██ ███████ ██      ███████ ███    ███ ██      ███████ ██████  ██ 
██         ██    ██   ██ ██ ████   ██ ██           ██ ██      ██      ██      ████  ████ ██      ██      ██   ██ ██ 
███████    ██    ██████  ██ ██ ██  ██ ██   ███     ██ ███████ ██      █████   ██ ████ ██ ██      █████   ██████  ██ 
     ██    ██    ██   ██ ██ ██  ██ ██ ██    ██     ██      ██ ██      ██      ██  ██  ██ ██      ██      ██   ██ ██ 
███████    ██    ██   ██ ██ ██   ████  ██████      ██ ███████ ███████ ███████ ██      ██ ███████ ███████ ██   ██ ██
"""
"""
stringler integer,float, bool'a benzemezler
stringler birer dizidir.

yani iclerinde siralanmis olarak baska degerler tutarlar


----------- string bir dizidir -------------

meyve = "portakal"

index yapisi ile degiskenin elemanlarina erisilir.
meyve stringinin ilk harfine eriselim
index = 0 demektir.
print(meyve[0]) == p
print(meyve[4]) == a
                                p o r t a k a l
pythonda indexler 0'dan baslar. 0 1 2 3 4 5 6 7. index


------------- string uzunlugu (len) ---------------

bir dizinin uzunlugunu almak icin len fonksiyonu kullanilir.
meyve = "portakal"
uzunluk = len(meyve) == 8

------------- metin dilimleme ---------------------

metinden dilim secmek icin yine index yapisi kullanilir.
dizi(baslangic : bitis : artis)
baslangic bos kalirsa default = 0
bitis bos kalirsa default = son index
artis bos kalirsa default = 1
baslangic dahil, bitis dahil degildir.


s  = "derin ögrenme"
s[0:5] == derin
s[:5] == derin
s[5] == " "

----------------- ters index ---------------

soldan saga giden index ''normal index'' == 0'dan baslar
sagdan sola giden index ''ters index''  == -1'den baslar

rakamlarin sadece son elemanini almak istiyoruz
rakamlar = 123456789
print(rakamlar[8]) == 9
print(rakamlar[-1]) == 9

------------------- tersten dilimleme -------------------

geriye dilimleme de denir.
diiz[bitis: baslangi : -artis]
son eleman indexi = -1

rakamlar = "123456789"

rakamlari tersten basa dogru siralayalim
rakamlar[::-1] == "987654321"

---------------------- stringler degistirilemezler -------------------

pythonda stringler degistirilemezler (immutable)
degistirmek istenirse yenisinin atanmasi gerekir.

selamlama = "selam dünya"
selamlama = "hello world"


selamlama[:6] + "w" + selamlama[7:] == hello world

----------------------- string metodlari ----------------------

upper() == metni BÜYÜK yapar ==> BİLGİSAYAR
metin = "bilgisayar"
metin.upper()

lower() = metni kücük yapar
metin.lower()

strip() = metinin basindaki ve sonundaki bosluk karakterlerini siler
metin.strip()

.lstrip == soldaki bosluklari siler
.rstrip == sagdaki bosluklari siler

format() == metni degiskenlerle süsler
a = "python"
b = "yapay"
c = "zeka"
print(a+"ile"+b+c) == python ile yapay zeka

find() = metinde bir karakter veya metin parcasi bulur
    bulamazsa = -1
    bulursa = buldugu index

kelime = "pencere"
kelime.find("e) == 1, 4, 6

kelime.find("e",2,6)
kelime.find("e",2(2.indexte başla),6(6.indexe kadar git))

find(metin, baslangic,bitis)
kelime.find("l", 2,6 ) == -1

capitalize() = metinin bas harfini buyutur

title() = metinin bas harflerini büyük yapar

isdigit() = metin tam sayi mi degil mi diye kontrol eder
girdi = "42"
gidi.isdigit() == True

startswith() == metin verilen parca ile baslar mi?

gezegen = "mars"
gezegen.strartswith("m") == True

endswith() == metin verilen parca ile biter mi?

gezegen = "mars"
gezegen.strartswith("m") == False
gezegen.strartswith("s") == True

replace() = metindeki karakteri veya parcayi baska bir parcayla degistirir
bilmece = "carsidan aldim bi tane"
bilmece.replace("bir,"*") === "carsidan aldim * tane"

"""
# in operatörü

"""
karakter veya metin başka metinin icinde var mi kontrol eder
varsa true döner

agac = "ahlat agaci"
at = "at"

at in agac == True
a in agac == True
b in agac == false

"""

# metinleri karsilastirma
"""
bazenen iki metni karsilastirmamiz gerekebilir
bunlar esitler mi?
hangisi büyük?

meyve = "armut"
if meyve == "armut
    print("evet armut")
else
    print("degil armut)

if armut < elma:
    print(armut + elma +"dan kucuktur")
else
    print(armut + elma +"dan buyuktur")

neden?? a harfi e harfinden önce gelir. ASCII karakterlerine bakarlar



ord() == ascii karakterini gösteririr.
ord("a") = 97
ord("A") = 65
ord("e") = 101
ord("E") = 69

ASCII'ye göre bütün büyük harfler kücük harflerden önce gelir.




"""

# QUIZ-2
"""
 ██████  ██    ██ ██ ███████       ██████  
██    ██ ██    ██ ██    ███             ██ 
██    ██ ██    ██ ██   ███   █████  █████  
██ ▄▄ ██ ██    ██ ██  ███          ██      
 ██████   ██████  ██ ███████       ███████ 
    ▀▀                                     
"""
"""
1) Verilen bir metnin tüm kelimelerinin baş harflerini büyük, diğer harflerini ise küçük yapan bir fonksiyon yazın.
    cözüm = def sadece_bas_harfler_buyuk(metin):
            kucuk_metin = metin.lower()
            bas_hafr_buyuk_metin = kucuk_metin.title()   
            return bas_hafr_buyuk_metin


2) Parametre olarak bir metin, bir de harf alan bir fonksiyon yazın. <br>
Fonksiyonunuz verilen metnin içinde, verilen harften kaç tane olduğunu geri dönsün. <br>
**Not:** Hazır bir python string metodu kullanın ve kodunuz tek satır olsun. <br>

    cözüm = def harf_say(metin, harf):
            return metin.count(harf)

3) Kullanıcıdan bir cümle isteyin. <br>
Bu cümle içindeki her bir harfin kaç sefer geçtiğini alt alta print edin.<br>
Boşluk karakterini yazmayın. <br>
**İpucu:** Soru 2'de yazdığınız fonksiyonu kullanın

    cözüm = def harfleri_say():
            cumle = input("Lütfen bir cümle giriniz: ")
            yazilan_harfler = ""
            for harf in cumle:
            if harf == ' ':
            continue
            adet = harf_say(cumle, harf)
            if not harf in yazilan_harfler:
            print("{0} harfi {1} defa geçiyor".format(harf, adet))
            yazilan_harfler += harf

4) Metnimiz 'Pazartesi Salı Çarşamba Perşembe Cuma' olsun. <br>
Bu metin üzerinde dilimleme (slicing) kullanarak aşağıdaki sorulara cevap veriniz:
    cözüm = metin = 'Pazartesi Salı Çarşamba'
            İlk 3 karakter:
            metin[0:3]
            metin[:3]
            metin[7:11]
            metin[2:12]
            metin[3:6]



5) Metnimiz 'Pazartesi Salı Çarşamba Perşembe Cuma' olsun. <br>
Bu metin üzerinde dilimleme (slicing) kullanarak aşağıdaki sorulara cevap veriniz:


* 1. karakterden 7. karaktere kadar olan harfleri ikişer atlayarak bulunuz (2'li adım)
* 3. karakterden 20. karaktere kadar olan harfleri üçer atlayarak bulunuz (3'lü adım)
* Çift index'li karakterleri bulunuz (0, 2, 4, 6...)
* Tek index'li karakterleri bulunuz (1, 3, 5, 7...)

    cözüm = metin = 'Pazartesi Salı Çarşamba'
            metin[1:7:2]
            metin[3:20:3]
            metin[::2]
            metin[1::2]

6) Metnimiz 'Pazartesi Salı Çarşamba' olsun. <br>
Bu metin üzerinde dilimleme (slicing) kullanarak aşağıdaki sorulara cevap veriniz:
    cözüm = metin = 'Pazartesi Salı Çarşamba'
            metin[-1]
            metin[-3]
            metin[-3:]
            metin[::-1]

* Son karakteri bulunuz
* Sondan 5. karakteri bulunuz
* Son 3 karakteri bulunuz
* Metni tersten yazdırınız

7) Metnimiz 'Pazartesi Salı Çarşamba' olsun. <br>
Bu metin üzerinde dilimleme (slicing) kullanarak aşağıdaki sorulara cevap veriniz:


* Sondan 2. karakter ile sondan 6. karakter arasını bulunuz
* Sondan 2. karakter (dahil) ile sondan 6. karakter arasını bulunuz
* 10. index'li karakteri gösteren negatif index'i bulunuz (pozitif ve negatif index'ler toplamı dizinin uzunluğunu verir)
* Son karakter hariç tüm karakterleri bulunuz
* İlk ve Son karakter hariç, tüm karakterleri bulunuz

    cözüm = metin = 'Pazartesi Salı Çarşamba'
            metin[-6:-2]
            metin[-6:-1]
            uzunluk = len(metin)
        print("uzunluk:", uzunluk)
        print("10. indexteki karakter:", metin[10])
        negatif_index = uzunluk - 10
        negatif_index = -negatif_index
        print('{}. indexteki karakter: {}'.format(negatif_index, metin[negatif_index]))
        if metin[10] == metin[negatif_index]:
            print("{} ile {} indexteki karakterler eşit".format(10, negatif_index))
        else:
            print("{} ile {} indexteki karakterler eşit değil".format(10, negatif_index))

8) Aşağıdaki şekilde bir fonksiyon yazınız: <br>
Kullanıcıdan bir email adresi isteyiniz. <br>
Bu mail adresini, **index yapısı** kullanarak kullanıcı adı ve domain adı olarak ayırınız.

    cözüm = def email_ayir():
            email = input("Lütfen bir email giriniz: ")
            bolme_noktasi = email.find('@')
            if bolme_noktasi == -1:
                print("Uygunsuz email formatı")
            else:
                print("Kullanıcı Adı:", email[:bolme_noktasi])
                print("Domain Adı:", email[bolme_noktasi+1:])
9) Aşağıdaki şekilde bir fonksiyon yazınız: <br>
Kullanıcıdan bir cümle istesin ve cümlenin tersten yazılmış olarak dönsün.

    cözüm = def ters_cevir():
        cumle = input('Lütfen bir cümle giriniz: ') 
        return cumle[::-1]
10) Aşağıdaki şekilde bir fonksiyon yazınız: <br>
Kullanıcıdan bir cümle içindeki her bir karakteri alfabeden sıradaki karakter ile değiştirsin. 

Yapılacaklar:
* İç içe fonksiyonlar kullanın.
* İçeride harf_kucuk_mu() ve harf_buyuk_mu() şeklinde harfin küçük ya da büyük olduğunu veren fonksiyonlar olsun.
* İlgili alfabe ve bir harf alıp, o alfabede o harften sonra gelen harfi bulan, siradaki_harf() fonksiyonu olsun.
* Alfabeler:
    * alfabe_kucuk = 'abcçdefgğhıijklmnoöprsştuüvyz'
    * alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
* Metinden ilgili harfi almak için index kullanın.

**Beklenen Sonuç:** 

AraBaCı  ->  BsbCbÇi

    cözüm = def siradaki_harfle_degistir():
    
            cumle = input('Lütfen bir cümle giriniz: ')
            alfabe_kucuk = 'abcçdefgğhıijklmnoöprsştuüvyz'
            alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
            yeni_cumle = ""
            def harf_kucuk_mu(harf):
                return harf in alfabe_kucuk
            def harf_buyuk_mu(harf):
                return harf in alfabe_buyuk
            def siradaki_harf(alfabe, harf):
                index = alfabe.find(harf)
                return alfabe[index+1]
            
            
            for harf in cumle:
                if harf_kucuk_mu(harf):
                    yeni_harf = siradaki_harf(alfabe_kucuk, harf)
                elif harf_buyuk_mu(harf):
                    yeni_harf = siradaki_harf(alfabe_buyuk, harf)
                else:
                    yeni_harf = harf
                yeni_cumle += yeni_harf
                
            return yeni_cumle


"""

"""
██   ██ ███████ ██      ██ ███    ███ ███████     ██████  ██████   ██████       ██ ███████ ███████ ██ 
██  ██  ██      ██      ██ ████  ████ ██          ██   ██ ██   ██ ██    ██      ██ ██      ██      ██ 
█████   █████   ██      ██ ██ ████ ██ █████       ██████  ██████  ██    ██      ██ █████   ███████ ██ 
██  ██  ██      ██      ██ ██  ██  ██ ██          ██      ██   ██ ██    ██ ██   ██ ██           ██ ██ 
██   ██ ███████ ███████ ██ ██      ██ ███████     ██      ██   ██  ██████   █████  ███████ ███████ ██ 
"""
"""
kelime okumak icin open(file,mode)
                    r: okuma
                    a: append
                    w: write
                    x: create

file = open("kelimeler.txt")
file.readline()
file.readline()

satir = file.readline()
satir.split()
-------------------------

file = open('kelimeler.txt')

for index, line in enumerate(file):
    if index <= 20:
        print(line)
------------------------
file = open('kelimeler.txt')

for index, line in enumerate(file):
    if index <= 20:
        kelime_dizisi = line.split()
        print(kelime_dizisi)
    else:
        break
-------------------------------
file = open('kelimeler.txt')

for satir in file:
    kelime_dizisi = satir.split()
    kelime = kelime_dizisi[0]
    if len(kelime) > 10:
        print(kelime)
---------------------------------
file = open('kelimeler.txt')

for satir in file:
    kelime_dizisi = satir.split()
    kelime = kelime_dizisi[0]
    if not 'a' in kelime and 
       not 'e' in kelime and 
       not 'i' in kelime and 
       not 'o' in kelime and 
       not 'u' in kelime:
        print(kelime)
-------------------------------
file = open('kelimeler.txt')

for satir in file:
    kelime_dizisi = satir.split()
    kelime = kelime_dizisi[0]   
    if 'ae' in kelime:
        print(kelime)
-----------------------------------
def yasak_harf_var_mi(metin, yasak_harfler):
    
    for harf in metin:
        if harf in yasak_harfler:
            return True
    else:
        return False
cumle = 'Bu bir normal metindir.'
yasak = 'ae'

yasak_harf_var_mi(cumle, yasak)

cumle = 'Bu bir normal metindir.'
yasak = 'üö'

yasak_harf_var_mi(cumle, yasak)
--------------------------------------
def sadece_sunlari_kullanir(metin, harfler):
    
    for harf in metin:
        
        # harf gerçekten harf mi, yoksa noktalama işareti mi? -> isalpha()
        if harf.isalpha() and not harf in harfler:
            return False
    else:
        return True

cumle = 'ey edip adanada pide ye'
harfler = 'adeinpy'
sadece_sunlari_kullanir(cumle, harfler)
cumle = 'ey edip adanada pide ye k'
harfler = 'adeinpy'
sadece_sunlari_kullanir(cumle, harfler)
--------------------------------------------
def lorem_sadece_sunlari_kullanir(harfler):
    file = open('kelimeler.txt')
    for satir in file:
        
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]
        
        if sadece_sunlari_kullanir(kelime, harfler):
            print(kelime)

harfler = 'ens'
lorem_sadece_sunlari_kullanir(harfler)
    



















                                                      
                                                            
           
"""














"""

██      ██ ███████ ████████ ███████ ██      ███████ ██████  
██      ██ ██         ██    ██      ██      ██      ██   ██ 
██      ██ ███████    ██    █████   ██      █████   ██████  
██      ██      ██    ██    ██      ██      ██      ██   ██ 
███████ ██ ███████    ██    ███████ ███████ ███████ ██   ██ 


"""

"""

list bir dizidir.
listlerde de index yapisi ile içindekilere erişilebilir.

listler [] ile gösterilir.

listem = [10,20,30,40] ===> 4 elemanli bir liste
listem2 = [ucgen,dortgen,besgen] 
            0.    1.      2.    index
karmaliste = [3,"mail", True,2.3]  ==> farkli tur degiskenleri tutabilir
bosliste = []

listem[0] == 10
listem[2] == 30


------------------listeler degistirilebilir (mutable)--------------------
peynirler = ["ezine","hellim", "tulum"]
ilk peyniri degistirelim

peynirler[0] = "can peyniri"

print(peynirler) == "can peyniri", "hellim","tulum"
------------------- listelerde döngüler----------------
for peynir in peynirler
    print(peynir)

ezine
hellim
tulum

for index,sayi in enumerate(sayilar)
    sayi = sayi*10
    sayilar[index] = sayi

for index,kelime in enumerate(peynirler)
    peynirler[i] = peynir + "peyniri"
    print(peynirler[i])

    
---------------------- liste operasyonlari -----------------------

listlerde + ve * islemleri yapiliabiliyordur
kendi mantiklari vardir

+ operatörü = listeleri uc uca ekler.

a = [10,20,30]
b = [40,50,60]

c = a + b
c == 10,20,30,40,50,60
 
hafta_ici = [pazartesi,sali,carsamba]
hafta_sonu= [cumartesi,pazar]

hafta = hafta_ici + hafta_sonu  ==> pazartesi,sali,carsamba,cumartesi,pazar


metin = "araba"
metin*5
ArabaArabaArabaArabaAraba

-------------------------- liste dilimleme ---------------------------
liste = [a,b,c,d,e,f]

liste[1:5] == b,c,d,e
liste[:4] == a,b,c,d

------------------------- liste kopyalama ----------------
yeniliste = liste[:]
baskayeniliste = liste[:]

bu olusturulan listeler farkli listelerdir

------------ id yöntemi--------------
pythonda tüm nesneler bir id ile tutulur.(bellekteki adresi)
id() ile bulnuur.

id(liste) == 359322843
id(yeniliste) == 43859445             === ücünün icerigi ayni olsa da
id(baskayeniliste) == 543843239             hepsi farkli listelerdir

------------------------------- list metodlari ----------------------
pythonda listler icin hazir metodlar
append() = listenin sonuna yeni bir eleman ekler.
insert() == belli indexe eleman ekler
extend() = listeye liste ekler
sort() = listeyi belli bir siraya göre siralar
sorted() = listeyi siralar ama yeni bir liste verir.

harfler = [a,b,c,d,e]

harfler.append(f) == a,b,c,d,e,f
harfler.insert(2,"k") == a,b,k,c,d,e

sayilar = [1,2,3]

harfler.extend(sayilar) == a,b,c,d,e,1,2,3

karisikharfler = [a,c,d,b]
karisikharfler.sort() == a,b,c,d

karisikharfler.sorted() == a,b,c,d ==> ama kopyasini verir.


------------------------------ listeden eleman silmek ------------------------
listeden eleman silmek birkac yöntem ile yapilabilir.
eger silinecek elemanin indexsi biliniyorrsa 
pop(index)
dizi = [x,y,z,t]

silinen =  dizi.pop(0) ===> x
print(dizi) == y,z,t

pop'a index girilmezse sondakini siler.

eger silinecek elemana ihtiyac yoksa
del
del dizi[0] == y,z,t

del dizi[0:3] == bütün elemanlar silinir. [] kalir

eğer silinecek eleman biliniyorsa
remove()

dizi.remove("t") == x,y,z

------------------------------- listler ve stringler ----------------------
string bir karakter dizisi, list ise deger dizisidir

ikisi de dizidir.

eğer stringi list'e çevirmek istersek list() yapicisi kullanilir.

gun = "pazxartesi" (str)

list(gun) == p,a,z,a,r,t,e,s,i


metin = "bugün hava biraz soğuk"
kelimeler = metin.split()

kelimeler = "bugün", "hava", "biraz", "soğuk"

---------------------- range fonksiyonu --------------------
range(1,10,2)

liste = [2,5,8,11,14,17,20,23,26,29]

aralik = range(2,30,3)

range_liste ==> [2,5,8,11,14,17,20,23,26,29]

---------------------- nesneler ve degerler --------------------
a = "kivi"  id(a) = 1512443
b = "kivi"  id(b) = 1512443

python iki degiskenin degeri ayni ve degiskenelr immutable oldugu icin
iki farkli degisken yaratmak yerine
ikisini ayni adrese yolladi

x = [1,2,3]
y = [1,2,3]

x == y ?? ttrue
id(x) == id(y) ?? false

-------------- is ifadesi (nesne kontorlü) ------------------
x == y -> deger kontrolü
id(x) == id(y) -> nesne kontrolü yapilir

a = [1,2,3,4,5]   
b = [1,2,3,4,5]

a is b ==> ayni nesne degirlerdir. False

s1 = "bilgisayar"
s2 = "bilgisayar"

s1 is s2 => true



pythonda tip türleri = 
primitive(basit) = int,float,str,bool
nonprimitive(karmasik) = list,dict,tupe

-------------- list'in argüman olarak fonksiyona gecilmesi ------------------
harfler = [a,b,c]
def buyuk_harf_ekle(harf_listesi)
    harf_listesi.insert(1,A)
    harf_listesi.insert(2,B)
    harf_listesi.insert(3,C)

buyuk_harf_ekle(harfler)

harfler = a,A,b,B,c,C,


-------------- matris operasyonlari  ------------------
                                ----------
A = [[1,2,3][4,5,6][7,8,9]]  === | 1 2 3 |
                                 | 4 5 6 |
                                 | 7 8 9 |
                                ----------

A[0] = 1,2,3
A[1] = 4,5,6


B = [[10,20,30][40,50,60][70,80,90]]

C = A + B ==> [[1,2,3][4,5,6][7,8,9][10,20,30][40,50,60][70,80,90]]

for i in range(len(A))
    for j in range(len(B))
        c[i][j] = A[i][j] + B[i][j]
print c

[11,22,33][44,55,66][77,88,99]


"""

# QUIZ-3
"""
 ██████  ██    ██ ██ ███████       ██████  
██    ██ ██    ██ ██    ███             ██ 
██    ██ ██    ██ ██   ███   █████  █████  
██ ▄▄ ██ ██    ██ ██  ███               ██ 
 ██████   ██████  ██ ███████       ██████ 
 
 """
"""
1)Parametre olarak bir liste alan bir fonksiyon yazın. Adı **toplam** olsun.
Bu fonksiyon kendisine verilen listenin tüm elemanlarını toplasın ve geriye genel toplam dönsün.
    cözüm = def toplam(liste):
            toplam = 0
            for i in liste:
                toplam += i
         return toplam
2)Parametre olarak, iç içe bir liste (nested list) alan bir fonksiyon yazın. İsmi **iki_seviye_toplam** olsun. Bu iç içe liste parametresi 2 seviyeli olsun.
Fonksiyon bu iç içe listenin tüm iç elemanları da dahil olmak üzere, genel toplam hesaplasın ve dönsün.

    cözüm = def iki_seviye_toplam(dizi):
            
            toplam = 0
            
            for eleman in dizi:
                   
                if type(eleman) == list:
                    for ic_eleman in eleman:            
                        toplam += ic_eleman
                elif str(eleman).isdigit():
                    toplam += eleman
                    
            return toplam
3) Soru 2'de yazdığımız fonksiyon sadece 2 seviyeli iç içe liste alabiliyordu. Şimdi bunu jenerik bir hale getirelim ve her seviye iç içe listeyi toplayabilsin. İsmi **ic_ice_toplam** olsun. 
Fonksiyon bu iç içe listenin tüm iç elemanları da dahil olmak üzere, genel toplam hesaplasın ve dönsün.

cözüm = 
def ic_ice_toplam(dizi):
    
    toplam = 0
    
    for eleman in dizi:
        if type(eleman) == int:
            toplam += eleman 
        elif type(eleman) == list:
             toplam += ic_ice_toplam(eleman)
            
    return toplam
4)Parametre olarak bir liste alan bir fonksiyon yazınız. Adı **kareler** olsun.
Fonksiyonumuz listedeki her bir elemanın karesini hesaplayacak ve yeni bir listeye ekleyecek. Sonuçta bu yeni listeyi dönecek. Yani parametre olarak gelen listedeki, elemanların karesini tutan yeni bir liste verecek.

cözüm =
def kareler(liste):
    yeni_liste = list()    
    for i, eleman in enumerate(liste):
        yeni_liste.append(eleman**2)
        
    return yeni_liste
5)Parametre olarak bir liste alan bir fonksiyon yazınız. Adı **kareler_toplami** olsun.
Fonksiyonumuz listenin başından başlarak elemanların karelerini alacak. Bu kareleri toplayarak yeni bir liste oluşturacak. Oluşan yeni listenin her bir elemanı, parametre olan gelen listedeki o index'e kadar olan kareler toplamı olacak.
Yani, yeni listedeki 4. eleman, gelen listedeki 1-2-3-4. elemanların kareleri toplamı olacak.
Böylece sona kadar gidecek. Ve bu şekilde oluşan yeni listeyi dönecek.

cözüm =
def kareler_toplami(liste):
    
    yeni_liste = []
    
    for eleman in liste:
        yeni_liste_toplami = toplam(yeni_liste)
        yeni_toplam = yeni_liste_toplami + eleman**2
        yeni_liste.append(yeni_toplam)
        
    return yeni_liste
6)istenin tek index'leri (1,3,5...) toplamı ile çift index'leri (0,2,4...) toplamı arasındaki farkı veren bir fonksiyon yazınız.
Adı **tek_cift_index_farki** olsun.

cözüm =
def tek_cift_index_farki(dizi):
    tekler = dizi[1::2]
    tekler_toplami = toplam(tekler)
    ciftler = dizi[::2]
    ciftler_toplami = toplam(ciftler)
    fark = tekler_toplami - ciftler_toplami
    
    return fark

7)Parametre olarak kendisine verilen listeyi kırpan bir fonksiyon yazın. Kırpma işlemi dizinin ilk ve son elemanını silmek demektir.
Fonksiyonumuzun adı **kirpan** olsun ve kendisine verilen parametreyi **yerinde** değiştirsin. Yani dışarıdaki orijinal listeyi modifiye etsin. Geriye hiçbir değer dönmesin. (None)
Fonksiyonu şu şekilde test ediniz ve dizinin yerinde değiştiğini ispatlayınız:

cözüm = 
def kirpan(liste):

    liste.pop(0)

    liste.pop()

8) Parametre olarak bir liste bir de sıralama tipi isteyen bir fonksiyon yazın. Adı **sirala** olsun.
Sırala Fonksiyonu, liste ile beraber tipi boolean olan **azalan_mi** adında bir parametre alacak. Bu parametresnin default değeri False olacak.
* Eğer azalan_mi parametresi True ise, fonksiyon listeyi büyükten küçüğe sıralayacak, 
* Eğer azalan_mi parametresi False ise, fonksiyon listeyi küçükten büyüğe sıralayacak
Sonunda sıralanmış listeyi geri dönecek.

cözüm = 
def sirala(liste, azalan_mi = False):
    sirali_liste = []
    if azalan_mi:
        sirali_liste = sorted(liste, reverse=True)
    else:
        sirali_liste = sorted(liste)
        
    return sirali_liste

9)Matematik'teki ardışık sayılar aslında bir listedir
**Gauss Yöntemi** ardışık sayıların toplamını veren bir yöntemdir. Ve şu şekilde çalışır:
* Önce listeyi küçükten büyüğe yazar
* Sonra büyükten küçüğe yazar
* Bu iki listeyi index bazlı alt alta toplar
* Bulduğu değeri 2'ye böler (çünkü listeyi 2 kere yazmıştır)
* Gauss Yöntemi böylece ardışık sayılar toplamını bulmuş olur
Bu soruda, 20'den başlayıp 300'e kadar 5'er 5'er artarak giden sayıların toplamını Gauss Yöntemi ile bulan bir fonksiyon yazın. Fonksiyonun adı **gauss** olsun.

Fonksiyon parametre olarak, başlangıç değeri, bitiş değeri ve artış miktarını alsın.

Parametrelerin adlari ve default değerleri şu şekilde olsun:
* baslangic -> 1
* bitis -> 100
* artis -> 2

cözüm = 
def gauss(baslangic=1, bitis=100, artis=2):
    liste = list(range(baslangic, bitis, artis))
    ters_liste = liste[::-1]
    toplam = 0
    
    for i in range(len(liste)):
        ikili_toplam = liste[i] + ters_liste[i]
        toplam += ikili_toplam
    sonuc = toplam / 2
    
    return sonuc      

10) Verilen bir listenin büyükten küçüğe sıralı olup olmadığını kontrol eden bir fonksiyon yazın. 
Adı **azalan_sirali_mi** olsun, ve eğer liste büyükten küçüğe sıralı ise True, değilse False dönsün.

cözüm = 
def azalan_sirali_mi(liste): 
    for i, eleman_1 in enumerate(liste):
        for j, eleman_2 in enumerate(liste):
            if j > i:
                if eleman_2 > eleman_1:
                    return False
                
    return True











"""







#   
 
"""
 ██████  ██  ██████ ████████ ██  ██████  ███    ██  █████  ██████  ██    ██ 
 ██   ██ ██ ██         ██    ██ ██    ██ ████   ██ ██   ██ ██   ██  ██  ██  
 ██   ██ ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████ ██████    ████   
 ██   ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ ██   ██ ██   ██    ██    
 ██████  ██  ██████    ██    ██  ██████  ██   ████ ██   ██ ██   ██    ██ 
 """
"""
dictionary sozluk yapilaridir.
calisan = {
    'ad': 'can ozturk',
    'yas': 20,
    'bolum': 'ogrenci'
}
Dictionary'yi, List'in daha genel yapisi olarak düsünebiliriz. 
Listede index'ler tam sayı (int) olmak zorundadır
Python bu index'leri kendi belirler.
Dictionary'de ise index'leri biz belirleriz
sadece tam sayı değil istediğimiz hemen hemen her tür olabilir.

key: value

İngilizce-Türkçe Sözlüğe (ingTRSozluk) bakıp, İngilizce 'hello' kelimesinin Türkçe karşılığını alırsanız aşağıdaki şekilde sonuç döner:

ingTRSozluk['hello'] = 'selam'

--------------------- dictionary yaratma ---------------------
ditionary {} ile yaratilir -> dict()
ingTR = {
araba = {
    'Audi': 'Almanya',
    'Mazda': 'Japonya',
    'Fiat': 'İtalya'
}

Dictionary için [] ile index alma yok.

[] içine index numarası değil -> key yazılır.

araba[0] == listelerde olur
araba['Audi'] == dict'lerde olur

--------------------- dict eleman ekleme ---------------
Listelerde eleman eklemek için -> append(), insert()

Dictionary için bu metodlar yoktur.

dict[key] = value
ingTR = dict{}
ingTR['one'] = 'bir'
ingTR['two'] = 'iki'
ingTR['three'] = 'üç'
print(ingTR) == {'one': 'bir', 'two': 'iki', 'three': 'üç'}

---------------------- update --------------------
arac = {
    'marka': 'Ford',
    'model': 'Mustang',
    'yil': 1964
}

eklenecek = {'renk': 'kırmızı'}

arac.update(eklenecek)

sonuc = {'marka': 'Ford', 'model': 'Mustang', 'yil': 1964, 'renk': 'kırmızı'}

eklenecekler = {
        'fiyat': 300000, 
        'km': 89000, 
        'motor': 1.6
}

arac.update(eklenecekler)

{'marka': 'Ford',
 'model': 'Mustang',
 'yil': 1964,
 'renk': 'kırmızı',
 'fiyat': 300000,
 'km': 89000,
 'motor': 1.6}

 ---------------------------- eleman silme -------------------

 pop() ve del kullaniriz.
ingTR = {}

ingTR['one'] = 'bir'
ingTR['two'] = 'iki'
ingTR['three'] = 'üç'
ingTR['four'] = 'dört'

ingTR.pop('four')

---------------------- eleman okuma --------------------------
dict[key] = value
ingTR['seven'] == yedi
ingTR['ten'] == on

--------------------------- eleman üzerinden dönme ------------------
arabalar = {
    'Audi': 'Almanya',
    'Mazda': 'Japonya',
    'Fiat': 'İtalya',
    'Ford': 'Amerika'
}
for araba in arabalar.items():          ('Audi', 'Almanya')
    print(araba)                               =====    ('Mazda', 'Japonya')
                                        ('Fiat', 'İtalya')
                                        ('Ford', 'Amerika')


"""
# QUIZ-4
"""
 ██████  ██    ██ ██ ███████       ██   ██ 
██    ██ ██    ██ ██    ███        ██   ██ 
██    ██ ██    ██ ██   ███   █████ ███████ 
██ ▄▄ ██ ██    ██ ██  ███               ██ 
 ██████   ██████  ██ ███████            ██ 
    ▀▀                                     
"""
"""
1)`kelimeler.txt` dosyasını okuyan ve buradaki kelimelerden bir dictionary yaratan bir fonksiyon yazın. Fonskiyon sadece 19 karakter ve üstü olan kelimeleri alsın.
Dictionary'nin key'i kelime olacak, ve değeri de kelimenin harf sayısı yani uzunluğu olacak.
Fonksiyon'un adı **kelimeler_sozlugu** olsun ve yarattığı Dictionary'yi dönsün.

cözüm = 
def kelimeler_sozlugu():

    sozluk = dict()
    dosya = open('kelimeler.txt')
    for i ,satir in enumerate(dosya):
        satir_dizisi = satir.split()
        kelime = satir_dizisi[0]
        if len(kelime) >= MIN_KARAKTER_UZUNLUGU:
            if not kelime in sozluk:
                sozluk[kelime] = len(kelime)
    
    return sozluk
2) `kelimeler.txt` dosyasını okuyan ve buradaki kelimelerden bir dictionary yaratan bir fonksiyon yazın. Fonskiyon sadece 19 karakter ve üstü olan kelimeleri alsın.
Dictionary'nin key'i karakter sayısı (uzunluk) olacak, ve değeri de bu karakter sayısına sahip kelimeleri içeren bir liste (List) olacak.
Fonksiyon'un adı **uzunluk_kelimeler** olsun ve yarattığı Dictionary'yi dönsün.

cözüm = 
def uzunluk_kelimeler():
    sozluk = dict()
    dosya = open('kelimeler.txt')
    for i ,satir in enumerate(dosya):
        
        satir_dizisi = satir.split()
        kelime = satir_dizisi[0]
        uzunluk = len(kelime)
        if uzunluk >= MIN_KARAKTER_UZUNLUGU:
                if not uzunluk in sozluk:
                sozluk[uzunluk] = [kelime]
            else:
                sozluk[uzunluk].append(kelime)
                
    return sozluk
3)isimleri **arac_yarat_1, arac_yarat_2 ,arac_yarat_3, arac_yarat_4** olan 4 fonksiyon yazın.
Bu fonksiyonlar aşağıdaki gibi bir dictionary yaratsın ve dict'in adı **arac** olsun:

{'marka': 'Ford',
 'model': 'Mustang',
 'yil': 1964,
 'renk': 'Kırmızı',
 'fiyat': 30000,
 'km': 89000,
 'motor': 1.6}
Fonksiyonlar dictionary'yi birbirinden farklı yöntemler ile yaratsın. Fonksiyonlar arac sozlüğünü geri 

cözüm = 
def arac_yarat_1():
    arac = {}
    arac['marka'] = 'Ford'
    arac['model'] = 'Mustang'
    arac['yil'] = 1964
    arac['renk'] = 'Kırmızı'
    arac['fiyat'] = 30000
    arac['km'] = 89000
    arac['motor'] = 1.6
    
    return arac
4)Adı **yeni_arac_yarat** bir fonksiyon yazın. Bu fonksiyon Soru 3'teki fonksiyonlardan birini çağırsın ve **arac** sözlüğünü alsın.
Sonra **arac** sozlüğünün elemanlarını bir döngü ve `update()` kullanarak başka bir sözlüğe kopyalayasın.
Kopyalarken, hem orijinal elemanı alsın hem de her bir key'in sonuna "_2" eki ekleyerek yeni bir eleman olarak eklesin.
Yeni sözlüğümüzün adı **yeni_arac** olsun. Ve fonksiyon bu sözlüğü dönsün.

cözüm = 
def yeni_arac_yarat():
    arac = arac_yarat_4()
    yeni_arac = arac.copy()
    for item in arac.items():
        
        
        key = item[0]
        value = item[1]
        key += "_2"
        
yeni_arac[key] = value
        
    return yeni_arac
5)Aşağıdaki Dictionary'leri birleştirip ortaya yeni bir dictionary çıkaran ve bunu geri dönen bir fonksiyon yazın.
Fonksiyon bu 3 dictionary'yi parametre olacak alacak ve adı **sozluk_birlestir** olacak.

cözüm = 
def sozluk_birlestir(d1, d2, d3):
    
    sozluk = {}
    for e in (d1, d2, d3):
        sozluk.update(e)
        
    return sozluk
6) Verilen iki sözlüğü içinde key'leri aynı olan elemanların değerlerini toplayan bir fonksiyon yazın. 
Eğer key ikisinde ortak değilse almasın, sadece ortak key'leri alsın.
Fonksiyonun adı **ayni_key_toplamlari** olsun.

cözüm = 
ef ayni_key_toplamlari(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise Exception('Parametrelerin ikisi de sözlük olmalı')
    if len(d1) != len(d2):
        raise Exception('Sözlüklerin uzunluğu aynı olmalı')
    sozluk = {}
    
    for key in d1:
        if key in d2:    
            sozluk[key] = d1[key] + d2[key]
    
    return sozluk




"""













# Tuple
"""
████████ ██    ██ ██████  ██      ███████ 
   ██    ██    ██ ██   ██ ██      ██      
   ██    ██    ██ ██████  ██      █████   
   ██    ██    ██ ██      ██      ██      
   ██     ██████  ██      ███████ ███████
   
"""
"""
   
Tuple da Dizi ipinde bir değişkendir.
Tuple'lar herhangi bir türde değer alabilirler ve tam sayılar ile indexlenirler. 
Dolayısı ile List'lere çok benzerler.
Tuple ile List arasındaki en önemli fark; List Mutable iken Tuple Immutable (Değiştirilemez) dir.
Tuple virgül ile ayrılmış bir listedir.


t = 'x', 'y', 'z', 'q', 'p'
tek_tuple = ('x',)
dil = tuple('Python')
prin t(dil) = ('P', 'y', 't', 'h', 'o', 'n')

tup = ('t', 'u', 'p', 'l', 'e')
tpu[0] = 't'
tup[4] = 'l'


------------------- tuple atamasi ---------------------------------------
print("a:", a)
print("b:", b)

gecici = a

a = b

b = gecici

print("a:", a)
print("b:", b)

Tuple Ataması için iki taraftaki değişken sayısının aynı olması lazım:


Bir liste içindeki herbir değeri, ayrı bir değişkene atayalım:
a, b, c, d = ['Python', 'Java', 'JavaScript', 'C#']
print(a)        Python
print(b)        Java
print(c)        JavaScript
print(d)        C#

----------------------- zip fonksiyonu ------------------------
`zip()` Python içinde hazır bir fonksiyondur. 
İki veya daha fazla Dizi (index ile erişilebilen tipler: List, Tuple, String, Range) tipinde değişken alır.
Zip yani fermuar fonksiyonu adından da anlaşılacağı gibi, her bir dizideki karşlıklı elemanları alarak bir tuple oluşturur. 
Böylece tuple'lardan oluşan bir zip nesnesi döner.

metin = 'xyzt'
liste = [1, 2, 3, 4]
fermuar = zip(metin, liste)
print(fermuar)

---------------- dict'ler ve tuple'lar --------------------------
sozluk = {
    'A': ord('A'),
    'B': ord('B'),
    'C': ord('C'),
    'a': ord('a'),
    'b': ord('b'),
    'c': ord('c')
}

print(sozluk)   ===> {'A': 65, 'B': 66, 'C': 67, 'a': 97, 'b': 98, 'c': 99}

------------------ bir tuple'i dict yapmak -------------------------------

aylar_gunler = [
    ('Ocak', 31),
    ('Şubat', 28),
    ('Mart', 31),
    ('Nisan', 30)
]

aylar = dict(aylar_gunler)

print(aylar)
print(type(aylar))  ===> {'Ocak': 31, 'Şubat': 28, 'Mart': 31, 'Nisan': 30}

"""









# set 

"""
███████ ███████ ████████ 
██      ██         ██    
███████ █████      ██    
     ██ ██         ██    
███████ ███████    ██   



"""
"""
Set bir python Data Structer (Veri Yapısı) tipidir .

* Set'ler birden çok değeri tek bir değişkende tutmak için kullanılır.
* Set'ler sırasız (unordered) ve indexlenmemiş (unindexed) koleksiyonlardır.
* Set'ler iki şekilde yaratılır:
    * süslü parantez ile (ama içine eleman vererek)
    * `set()` constructor'ı ile
* Set'in elemanları tekildir. (Matematikteki Kümeler gibi)

------------------------ set yaratmak ----------------------
 Set Yaratma

# süslü parantez ile 
# ama süslü parantez boş olursa -> dicitonary yaratır
# süslü parantez içerisine eleman vermek lazım

kume = {}
type(kume) ===> dict
kume = {'at', 'kedi', 'köpek', 'at', 'tavşan', 'kedi'}
type(kume) =====> set

**set()** constructor'ı ile küme yaratmak:

harfler = set({'A', 'B', 'C', 'D', 'E'})
print(harfler) ====> {'A', 'B', 'C', 'D', 'E'}

Set'ler sırasız yapılardır. Sıra aranmaz. Index de yoktur.

---------------------------- set metodları -----------------------------

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print(notlar) ==> {'A', 'B', 'C'}

dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print(dereceler) ==> {'A', 'F', 'T', 'B', 'L'}

birleşim = union()
fark = difference()
alt kümesi mi? = issubset()
üst kümesi mi? = isupperset()
ayrık küme mi? = symmetric_difference()  

eleman ekleme = add()
eleman cıkarma = remove()
birsürü eleman ekleme = update()














"""










# comprehension
"""
 ██████  ██████  ███    ███ ██████  ██████  ███████ ██   ██ ███████ ███    ██ ███████ ██  ██████  ███    ██ 
██      ██    ██ ████  ████ ██   ██ ██   ██ ██      ██   ██ ██      ████   ██ ██      ██ ██    ██ ████   ██ 
██      ██    ██ ██ ████ ██ ██████  ██████  █████   ███████ █████   ██ ██  ██ ███████ ██ ██    ██ ██ ██  ██ 
██      ██    ██ ██  ██  ██ ██      ██   ██ ██      ██   ██ ██      ██  ██ ██      ██ ██ ██    ██ ██  ██ ██ 
 ██████  ██████  ██      ██ ██      ██   ██ ███████ ██   ██ ███████ ██   ████ ███████ ██  ██████  ██   ████
 
 """
 
 
"""
Comprehension Python'da, dizi tipinde değişkenler üzerinde kolayca döngü kurmamızı sağlayan yapılardır.

1'den 10'a kadar olan sayıların karelerini içeren bir liste yapalım:
    kareler = []

    kareler_comp = [i**2 for i in range(1, 11)]

    print(kareler_comp)

1'den 7'ye kadar olan sayıların küplerini ekrana yazalım: 

    kupler_comp = [k**3
               for k in range(1, 7)]

    kupler_comp

'lorem impsum' ifadesinin harflerini büyük harfler yapıp bir listeye ekleyelim.
text = 'lorem ipsum'
    buyuk_comp = [t.upper()
                for t in text]
    print(buyuk_comp) ========== ['L', 'O', 'R', 'E', 'M', ' ', 'I', 'P', 'S', 'U', 'M']

----------------------  nested comps ----------------------------------------
harfler = ['A', 'B']
sayilar = [1, 2, 3]

sonuc = [(harf, sayi) 
         for harf in harfler 
         for sayi in sayilar]

print(sonuc) ===> [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3)]

1'den 10'a kadar olan tüm sayıları, kendileri key ve kendinden küçük pozitif tam sayılar da value listesi olacak şekilde bir dict kuralım:
    kucukler_comp = {i: [j for j in range(1, i+1)] 
                    for i in range(1, 11)}

    print(kucukler_comp)


---------------------------- if-else yapısı -----------------------------------------
1'den 20'ye kadar olan tek sayıları önce döngü sonra comprehension ile bulalım:
tekler = []

for i in range(1, 21):
    if i % 2 == 1:
        tekler.append(i)
    
print(tekler) ===> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


tekler_comp = [i
               for i in range(1, 21)
               if i % 2 == 1]

print(tekler_comp) ===> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""



















"""
██   ██  █████  ████████  █████      ██    ██  ██████  ███    ██ ███████ ████████ ██ ███    ███ ██ 
██   ██ ██   ██    ██    ██   ██      ██  ██  ██    ██ ████   ██ ██         ██    ██ ████  ████ ██ 
███████ ███████    ██    ███████       ████   ██    ██ ██ ██  ██ █████      ██    ██ ██ ████ ██ ██ 
██   ██ ██   ██    ██    ██   ██        ██    ██    ██ ██  ██ ██ ██         ██    ██ ██  ██  ██ ██ 
██   ██ ██   ██    ██    ██   ██        ██     ██████  ██   ████ ███████    ██    ██ ██      ██ ██ 

"""


# hata yonetimi 

"""
-------------------------- Exception ile Syntax Error Farkı -------------------------

Bir Python programı, bir hata ile karşılaştığında durur.
İşte, bu durma işleminin nasıl olacağına Exception Handling (Hata Yönetimi).

Python'da hata (error) iki türlü olur:
 * Syntax Error (Yazım Hatası)
 * Exception (uygulama hatası)

 Syntax Error (Sözdizimi Hatası):

Python Parser'ı (kod oluşturucu) yazım şekli Python kurallarına uymuyorsa, "Syntax Error" üretir.

Hata tipi: SyntaxError

exception: Syntax'ı doğru olan, ama Python Interpreter'ın çalışırken (run-time) aldığı hatalardır.

------------------------ exception firlatmak ------------------------------------
def hata_firlat():
    girdi = input("Lütfen bir sayı giriniz: ")

    # eğer biz bu olası hatayı düşünmezsek -> crach
    if not girdi.isdigit():
        raise Exception('Sayı girmedeniz...')

    sayi = int(girdi)
    print(sayi)

Yukarıda yaptığımız if kontrolü aslında bir assertion (doğrulama) işlemi idi.
Yani eğer o kod bloğu doğrulanmadı ise (assert olmadı ise) devam etme dedik Python'a.
Python'da eğer sadece doğrulama amaçlı bir kod yazacaksanız if yerine bunun için özel yazılmış bir komut var:
'assert' komutu.
assert <kontrol ifadesi>
şeklide kullanırız ve eğer <kontrol ifadesi> doğrulanmazsa, kod burada durur istediğiniz hatayı fırlatır.
Genellikle debug işlemleri için çok kullanılır.


def girdi_dogrula():
    girdi = input("Lütfen bir sayı giriniz: ")

    assert int(girdi), ValueError('Sayı girmediniz...')

    sayi = int(girdi)
    print(sayi)

    
Şimdi eğer, kullanıcı sayı değil de alfanumerik bir değer girerse ortaya ValueError çıkacağını bildiğimize
göre artık jenerik Exception fırlatmak yerine direk ValueError tipinde bir hata fırlatabiliriz   

def girdi_dogrula():
    girdi = input("Lütfen bir sayı giriniz: ")

    assert int(girdi), ValueError('Sayı girmediniz...')

    sayi = int(girdi)
    print(sayi)

------------------------ try-except ------------------------------
try:
    - kodu çalıştırmaya çalışır
    - hata yoksa, try'in sonuna kadar gelir
    - hata varsa, kod try'dan çıkar
except:
    - eğer try içinde hata alınmışsa, except'e gelir
    - derleyici hata olan yereden except içine atlar
    - yani hatanın yakalandığı yer except bloğudur.

    
    
def karesini_hesapla_try():
    try:
        girdi = input("Lütfen bir tam sayı giriniz: ")
        sayi = int(girdi)
        print(sayi**2)
    except:
        print('Sayı girmediniz...')

        
        
        
def karesini_hesapla_try_again():
    try:
        girdi = input("Lütfen bir tam sayı giriniz: ")
        sayi = int(girdi)
        print(sayi**2)
    except:
        print('Sayı girmediniz...')
        karesini_hesapla_try_again()


def dosya_ac(dosya_yolu):
    try:
        # dosya aç -> open()
        dosya = open(dosya_yolu)

        # satır satır
        for satir in dosya:
            print(satir.split())
    except:
        print("Maalesef dosya bulunamadı...")

Kod try içinde çalışırken, hata alırsa ilgili except bloğuna gelir.
Hata almazsa, (varsa) else bloğuna gelir.

def dosya_ac(yol):
    try:
        dosya = open(yol, encoding='utf-8')
    except FileNotFoundError:
        print('Dosya bulunamadı...')
    else:
        print(dosya.read())

Bazı durumlarda kodun hiçbirşey yapmadan devam etmesini isteriz -> pass
def dosya_ac_pass(yol):
    try:
        dosya = open(yol, encoding='utf-8')
    except FileNotFoundError as ex:
        pass
    else:
        print(dosya.read())



    try:
        <---- kod ---->
    except:
        <---- hata ---->
    else:
        <---- hatasız işleme ---->
    finally:
        <----- ne olursa olsun ----->

def bolme(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('sonuc:', result)
    finally:
        print('İşlem tamamlandı.'

def dosya_ac(path):
    try:
        file = open(path, encoding='utf-8')
    except Exception as ext:
        print(ext)
    else:
        print(file.read())
    finally:
        # burada file.close() demeden -> file var mı -> try
        try:
            file.close()
        except:
            pass
"""

















# moduller
"""
███    ███  ██████  ██████  ██    ██ ██      ██      ███████ ██████  
████  ████ ██    ██ ██   ██ ██    ██ ██      ██      ██      ██   ██ 
██ ████ ██ ██    ██ ██   ██ ██    ██ ██      ██      █████   ██████  
██  ██  ██ ██    ██ ██   ██ ██    ██ ██      ██      ██      ██   ██ 
██      ██  ██████  ██████   ██████  ███████ ███████ ███████ ██   ██
"""
"""


Standart Moduller
Moduler Programlama:
1- Kod tekraranı önler
2- Organizasyon (web, db, api...)
3- Bakımını ve Yönetimini


Modul: .py ile biten Ptyhon dosyalarına
Paket: Birçok modülü içeren Python klasörleridir

import math
pi_sayisi = math.pi


import random
olasilik = random.random()

rasgele_sayi = random.randint(10, 50)
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
eleman = random.choice(liste)
orneklem = random.sample(liste, 3)


import platform

print('platform:', platform)
platform türü
print('platform türü:', platform.platform())

platform mimarisi
print('platform mimarisi:', platform.architecture())

makine tipi
print('makine tipi:', platform.machine())
OS
print('İşletim Sistemi:', platform.system())

def girdi_iste(tip='metin'):
    return input("Lütfen bir {0} giriniz: ".format(tip))


def string_al():
    

    girdi = girdi_iste()
    return girdi


def tamsayi_al():
    
    # tam sayı alana kadar istemeye devam eder
    while True:
        try:
            girdi = girdi_iste(tip='tamsayı')
            sayi = int(girdi)
        except ValueError:
            continue
        else:
            return sayi


def ondalik_sayi_al():
    
    # ondalık sayı alana kadar istemeye devam eder
    while True:
        try:
            girdi = girdi_iste(tip='ondalık sayı')
            ondalik_sayi = float(girdi)
        except ValueError:
            continue
        else:
            return ondalik_sayi

"""
















# format islemleri

"""
███████  ██████  ██████  ███    ███  █████  ████████     ██ ███████ ██      ███████ ███    ███ ██      ███████ ██████  ██ 
██      ██    ██ ██   ██ ████  ████ ██   ██    ██        ██ ██      ██      ██      ████  ████ ██      ██      ██   ██ ██ 
█████   ██    ██ ██████  ██ ████ ██ ███████    ██        ██ ███████ ██      █████   ██ ████ ██ ██      █████   ██████  ██ 
██      ██    ██ ██   ██ ██  ██  ██ ██   ██    ██        ██      ██ ██      ██      ██  ██  ██ ██      ██      ██   ██ ██ 
██       ██████  ██   ██ ██      ██ ██   ██    ██        ██ ███████ ███████ ███████ ██      ██ ███████ ███████ ██   ██ ██ 
"""



"""
Format İşlemleri

Python'da String Formatlama 4 yol ile yapılır:
1- % operatörü (eski stil formatlama)
2- str.format (yeni stil formatlama)
3- f-strings (String Interpolation)
4- Template Strings

% Operatoru
- %s -> string
- %d -> integer
- %f -> float
    - %.<n>f -> sıfırdan sonra n hane

    
    
gun = 'Pazartesi'
print('Bugün günlerden %s' % gun)

sayi = 28
print("Euclid'e göre %d bir mükemmel sayıdır." % sayi)

pi = math.pi
metin = "pi sayısı: %.4f" % pi
print(metin)

# birden fazla % operatoru
bilgi = "Python, ilk olarak %d'de yayınlandı ve %.2f yıldan fazladır kullanılıyor" % (1991, 30)
print(bilgi)


süslü {} ile string formatlama
# index vermeden
selam = 'Selam sana {} {}'
print(selam.format('Peter', 'Parker'))

# index vererek
ifade = "{0} kelimesinin {1} adet harfi var."
print(ifade.format("Python", len('Python')))

# isim vererek
adi_nereden_gelir = "{ad} ismi {kaynak}"

print(adi_nereden_gelir.format(ad="Python", kaynak="Monthy Python dizisinden gelir."))

print(adi_nereden_gelir.format(ad='Java', kaynak="Endonezya'daki Java kahve türünden gelir."))

3. f-strings (String Interpolation)

* f-strings Python 3 ile geldi (yeni)
* f' ...string...' şeklinde string'in başına f harfi konur
* str.format() gibi çalışır ama daha dinamiktir
* {} süslü parantez ile kullanılır


x = 2
y = 3

carpim = x * y
print(f"{x} * {y} = {carpim}")

# direk {} içinden de işlem yapılabilir (ifade çalıştırılabilir)
print(f"{x} * {y} = {x * y}")

veri = ['Klark Kent', 'Metropolis', 'Daily Planet']
print(f'{veri[0]}, yani Superman, kurgusal {veri[1]} şehrinde, {veri[2]} gazetesinde çalışır.')

# Önemli Not:
# f-strings Python 3.6 ile geldi.













"""

# dosya okuma islemleri









"""
██████   ██████  ███████ ██    ██  █████      ██ ███████ ██      ███████ ███    ███ ██      ███████ ██████  ██ 
██   ██ ██    ██ ██       ██  ██  ██   ██     ██ ██      ██      ██      ████  ████ ██      ██      ██   ██ ██ 
██   ██ ██    ██ ███████   ████   ███████     ██ ███████ ██      █████   ██ ████ ██ ██      █████   ██████  ██ 
██   ██ ██    ██      ██    ██    ██   ██     ██      ██ ██      ██      ██  ██  ██ ██      ██      ██   ██ ██ 
██████   ██████  ███████    ██    ██   ██     ██ ███████ ███████ ███████ ██      ██ ███████ ███████ ██   ██ ██ 
                                                                                                               
"""


"""
Dosya Tipleri:
1- Binary Tipi
    * pdf, doc, jpg, png
    
2- Text Tipi
    * txt, xml, html, .py, .java



Encoding: Verinin byte yapısıdır -> nasıl tutulduğu

İki yaygın encoding şekli:
1- ASCII (128 karakter)
2- UNICODE (1.114.112 karakter)



Python'da dosya açmak için -> open()

encoding vermeden
file = open('kelimeler.txt')
print(file.read())

encoding vermedik -> ü : Ã¼
encoding ile
print(file.read())
file.close()

Dosya Açma Şekilleri (Modlar):
* r: okuma (read)
* w: yazma (write)
* a: ekleme (append)
* x: yaratma (create)
* t: text dosyası formatında
* b: binary dosyası formatında
* +: update modu (read + write)


-------------- dosya silme ve adlandirma -----------------
Python'da dosyaları:
* yeniden adlandırma (rename)
* silme
* yaratma

os modülü ile yapılır


YENİDEN ADLANDIRMA -> rename()
Örnek
os.rename('silinecek.txt', 'silinmeden_once_rename.txt')

dosya yoksa -> FileNotFoundError
try:
    os.rename('silinecek.txt', 'silinmeden_once_rename.txt')
except:
     print('dosya bulunamadı...')

------------------- klasör yaratma -----------------

1- os.mkdir()
    * mkdir() -> tek klasör yaratır
    * makedirs() -> birden fazla klasör yaratır

2. path.Path.mkdir() -> hem tekli hem de çoklu klasör yaratır.

import os
from pathlib import Path

# ana klasör yolu
ana_klasor_yolu = os.getcwd()
# dosya zaten var -> FileExistsError
# os.mkdir('ornek_klasor_1')

# os.mkdir('ornek_klasor_2')

# p = Path('path_klasoru_1')
# p.mkdir()

# try:
#     p2 = Path('path_klasoru_2')
#     p2.mkdir()
# except FileExistsError as dosya_var_hatasi:
#     print(dosya_var_hatasi)


--------------------- klasör silme, kopyalama, taşıma -----------------------


 ---------Klasör Silme---------
os.rmdir() -> tek klasör siler (klasör BOŞ ise)
pathlib.Path.rmdir() -> tek klasör siler (klasör BOŞ ise)
shutil.rmtree() -> tüm klasör ağacını siler


---------Klasör kopyalama---------
Dosya Kopayalama
 shutil.copy()
shutil.copy2()
Source -> Destination
src = 'kaynak_klasor/k1.txt'
dst = 'hedef_klasor/h1.txt'
shutil.copy(src, dst)

Klasör Kopyalama
shutil.copytree()
shutil.copytree('kaynak_klasor', 'kaynak_klasor_kopyasi')




---------Dosya ve Klasör Taşıma---------
shutil.move(kaynak, hedef)
shutil.move('kaynak_klasor/k1.txt', 'hedef_klasor')
shutil.move('kaynak_klasor_kopyasi', 'hedef_klasor')
-

--------Klasörü Yeniden Adlandırma---------
os.rename('kaynak_klasor', 'final_klasoru')





"""











"""
 ██████   ██████  ██████  
██    ██ ██    ██ ██   ██ 
██    ██ ██    ██ ██████  
██    ██ ██    ██ ██      
 ██████   ██████  ██      
                       
"""

# OOP

"""
Object Oriented Programming (OOP)
Nesne Tabanlı Programlama

Nesne -> etrafımızdaki herşey

Python'da nesnelerin özellikleri:
* öznitelikler (attribute)
* davranışları (behavior)

Örnek:
Penguen
attribute * öznitelikleri: adi, yaşı, boyu, kilosu, rengi, turu...
* davranışları: yüzme, yürüme, şarkı söyleme, dans etme...

OOP: Kod tekrarını önlemek için var.
DRY: Do not repeat yourself

--------------------Class (Sınıf)------------------------
Class bir nesnenin eskiz çizimidir.
Mimari çizimidir.
Nesnenin neye benzeyeceğini anlatır.
Ör: Bina bir nesnedir. O binanın kağıt üstündeki çizimi (mimari çizim) Class'dır.

- --------------------Object (Nesne)---------------------------
Nesne, Class'ın hayat bulmuş şeklidir. (instance)
Class'ın ete kemiğe bürünmüş halidir.
Instance: Tekil olarak YARATILMIŞ bir nesnedir.

--------------------class attribute(özellik)---------------------
Bütün Penguen'lerin ortak özellikleri vardır.
Bilimsel olarak türü (species) -> kuş
İşte sınıftan (class) üretilmiş bütün varlıklarda (nesne) ortak olan özelliklere;
Class Attribute

--------------------Instance attribute(özellikler)------------------------------
Tekil bir nesneye özel nitelikler; 
Instance Attribute
Penguen, yaşı, rengi, kilosu, boyu


self: o anda yaratılan nesneyi anlatır
Attribute'lara -> '.' ile erişilir.
* Class Attribute ise -> .__class__.
* Instance Attribute -> .

Metodlar (Davranışlar):
Method bir class içinde tanımlanmış fonksiyondur.
Nesnelerin davranışlarını anlatır.

class Penguen:

    # class attribute
    tur = 'Kuş'

    # instance attribute'lar
    def __init__(self, ad, yas, renk):
        self.ad = ad
        self.yas = yas
        self.renk = renk

    # instance method (varlığın metodu)
    def yuzme(self):
        return f"{self.ad} yüzebilir."

    def sarki_soyle(self, soyleyebilir_mi=False):
        if soyleyebilir_mi:
            return f"{self.ad} şarkı söylebilir."
        else:
            return f"{self.ad} şarkı söylemeyez."

    def dans_et(self, dans_edebilir_mi=False):
        if dans_edebilir_mi:
            return f"{self.ad} dans edebilir."
        else:
            return f"{self.ad} dans edemez."

            
            
            
            
------------------------------ KALITIM ---------------------------
Aynen gerçek hayattaki gibi, OOP'de Class'lar birbirinden Kalıtım alabilirler.
Kalıtım Alan Class -> Child Class, Derived Class (Çocuk Classı)
Kalıtım Veren Class -> Parent Class, Base Class (Ana Class) - Super

class Kus:
    def __init__(self):
        print('Kuş yaratıldı.')

    def kimimBen(self):
        print('Ben bir Kuşum.')

    def ucma(self):
        print('Kuşlar uçabilir.')

    def yuzme(self):
        print('Kuşlar yüzebilir.')


class Baykus(Kus):
    # Bir sınıf hangi sınıftan kalıtım alıyorsa, parantez içinde ana sınıf yazılır.

    def __init__(self):
        # önce ana sınıfının, super(), __init__() metodunu çağır
        super().__init__()
        print('Baykuş yaratıldı.')

    def kimimBen(self):
        print('Ben bir Baykuşum.')

    # Baykuş da tüm kuşlar gibi uçtuğu için ucma() metodunu overrirde (ezmek) etmeye gerek yok
    # aynen kullanacağız

    def yuzme(self):
        print('Baykuşlar yüzemez.')

    # Baykuşların gece görüşü vardır.
    def gece_gorusu(self):
        print("Baykuşun gece görüşü vardır.")

----------------------------- ENCAPSULATION ---------------------------       
OOP'de dışarıdan direk olarak bizim class'ımız içindeki
attribute'lara erişilmesini istemeyebiliriz.

Attribute gizleme : '__' ile yapılır
İki alt tireli (__<name>) Private olmuş olur.  
        
    class Telefon:
    def __init__(self):
        # telefonun standart fiyatını belirleyelim
        self.__fiyat = 1000

    def sat(self):
        print('Satış Fiyatı: {} TL'.format(self.__fiyat))

    def set_fiyat(self, yeni_fiyat):
        # KONTROL -> fiyat negatif mi?
        if yeni_fiyat <= 0:
            print('Negatif Fiyat olamaz.')
        else:
            self.__fiyat = yeni_fiyat

    def get_fiyat(self):
        return self.__fiyat
tel.renk = 'Siyah'
Python'da herhangi bir nesneye dışarıdan (class'tan bağımsız) özellik verebilirsiniz.
Ama bu özellik class'a yansımaz.    
        
Get-Set Metoları -> Getter-Setter
Class'ın private attribute'ları için alma ve set etme işlemlerini yapar.
        
------------------------------ POLYMORPHISM ---------------------------    
Çok şekillilik -> Bir arayüz (interface) farklı yerlerde farklı amaçlar için kullanılır.    
     
     
     
     class Kus:
    def __init__(self):
        print('Kuş yaratıldı.')

    def kimimBen(self):
        print('Ben bir Kuşum.')

    def ucma(self):
        print('Kuşlar uçabilir.')

    def yuzme(self):
        print('Kuşlar yüzebilir.')   
        
 
 
 
 
 
 class Baykus(Kus):
    # Bir sınıf hangi sınıftan kalıtım alıyorsa, parantez içinde ana sınıf yazılır.

    def __init__(self):
        # önce ana sınıfının, super(), __init__() metodunu çağır
        # super().__init__()
        print('Baykuş yaratıldı.')

    def kimimBen(self):
        print('Ben bir Baykuşum.')

    # Baykuş da tüm kuşlar gibi uçtuğu için ucma() metodunu overrirde (ezmek) etmeye gerek yok
    # aynen kullanacağız

    def yuzme(self):
        print('Baykuşlar yüzemez.')

    # Baykuşların gece görüşü vardır.
    def gece_gorusu(self):
        print("Baykuşun gece görüşü vardır.")       
        
   
   
   
   
   class Penguen(Kus):
    def __init__(self):
        # super().__init__()
        print('Penguen yaratıldı.')

    def kimimBen(self):
        print('Ben bir Penguenim.')

    def ucma(self):  # override
        print('Penguenler uçamaz.')     
        
        
   class Anasinif_1:
    pass

class Anasinif_2:
    pass

class Altsinif(Anasinif_1,Anasinif_2):
    pass

import datetime
import _strptime












class Saat:
    def __init__(self,saat,dakika,saniye) -> None:
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye        

    def saatikur(self,saat,dakika,saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye
        
    def saatKac(self):
        return "Saat: {}:{}:{}".format(self.__saat,self.__dakika,self.__saniye)
    

class Takvim(object):
    def __init__(self,gun,ay,yil) -> None:
        self.takvimKur(gun,ay,yil)
    def takvimKur(self,gun,ay,yil):
        self.gun = gun
        self.ay = ay
        self.yil = yil
        
        
    def bugunNe(self):
        return "Gunun Tarihi: {}, {}, {}".format(self.gun,self.ay,self.yil)


class SaatliTakvim(Saat, Takvim):
    def __init__(self, saat, dakika, saniye,gun,ay,yil) -> None:
    
    
        #####SUPER CAGIRILMAZ CUNKU BIRDEN FAZLA SUPERI OLUR


        Saat.__init__(self, saat, dakika, saniye)
        Takvim.__init__(self,gun,ay,yil)
        
saatTakvim = SaatliTakvim(1,2,3,4,5,6)

print(saatTakvim.saatKac())
print(saatTakvim.bugunNe())

saatTakvim.saatikur(7,8,9)
print(saatTakvim.saatKac())     
        
        
        
        
"""













