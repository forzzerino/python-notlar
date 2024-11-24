# Şartlı İfadeler
"""
tipi bool'dur. Doğru veya Yanlis ifade tutarlar
yargi bildirirler.

tek eşit -> = atama demektir
çift eşit -> == eşitlik kontrolü demektir
a = 8 ise
a = 6 == False;
a = 8 == True;

• x == y : x, y'ye eşit mi?
• x = y  : x, y'dir.
• x != y : x, y'ye eşit değil midir=
• x < y  : x, y'den kücük mü?
• x >= y : x, y'dem büyük eşit mi?
"""
# Mantıksal Operatörler
"""
diğer dillerde olan ||, &&, ! gibi operatörler
    pythonda       or, and, not şeklinde kullanilir.


•  and: her iki taraf da *TRUE* ise sonuç True
        ancak bir taraf bile *FALSE* ise sonuç False

•  or : taraflarin biri true ise sonuç True
        taraflarin ikisi de false ise sonuç False
     
"""

#if-else-elif yapilari ve recursion yapisi
"""
kod içinde belli durumlara göre farkli kodlari calistiririz.
bunlardan bazilari karar yapilari(if)dir

• eğer x 0'dan büyükse ekrana yaz.
    if x>0: print(x)
    x sifirdan kücük olursa kodu es geçer.

• if x>9 and x<55:  == diğer dillerde (x>9 && x<55)

if bloğuna girilmeyen durumlarda else bloğu tanimlandiysa
işlemler else blogunda yapilir.

elif durumu if ve else durumlari arasina tanimlanir
ara durumdur.
istenildigi kadar tanimlanabilir.

if()  -- 1. durum 
elif()-- 2. durum
else()-- 3. durum

kod
1. durum saglanmazsa 2. duruma
2. durum saglanmazsa 3. duruma atlar

•   girdi = input("bir sayi girin")
    n = int(girdi)
    if n<0: print("n negatif")
    elif n == 0: print("n 0dir")
    else: print("n pozitiftir.")

---------------------------
recursion: fonksiyonun kendi kendini cagirmasi durumudur.
• girilen sayidan, 0 a kadar sayan fonksiyon.
• fibonacci dizisi yazan fonksiyon
• faktoriyel hesabi yapan fonksiyon

• def geri_say(n):
    if n<=0:
        print(-- program sonu --)
    else:
        print(n)
        return geri_say(n-1)
n = 5 ----> 5 4 3 2 1 
"""
#QUIZ 1
"""
1) Kullanıcı tarafından girilen bir saynının tek mi çift mi olduğunu bulun.

    # Çözüm:
        sayi = input("bir sayi gir")
        n = int(sayi)

        if not n%2==0:
            print("tek")
        else:
            print("cift")

2) Kullanıcı tarafından girilen bir harfin sesli mi yoksa sessiz mi olduğunu bulalım.

    # Çözüm:
        harf = input("bir harf girin: ")

        if harf=="a" or harf=="e" or harf=="i" or harf=="o" or harf=="u":
            print("sesli harf")
        else:
            print("sessiz harf")

3) Kullanıcı tarafından girilen kenar sayısına göre hangi şekil oldunu dönen bir fonksiyon yazın.

    # Çözüm:
        kenar = input("lutfen seklin kenar sayisini girin: ")
        if kenar=="3":
            print("ucgen")
        elif kenar=="4":
            print("dortgen")
        elif kenar>=5:
            print("cokgen")
        else:
            print("sekil degil")

4) Bir aydaki gün sayısını ekrana yazdırın. Ay'ın adını kullanıcı belirleyecek.

    # Çözüm:
        def aydaki_gun_sayaci(ay=input("lutfen bir ay girin: ")):
        if ay=="ocak":
            print("ocak ayinda 31 gün vardir")

        elif ay=="subat":
            print("ocak ayinda 28 gün vardir")

        elif ay=="mart":
            print("ocak ayinda 30 gün vardir")

        elif ay=="nisan":
            print("ocak ayinda 30 gün vardir")

        elif ay=="mayis":
            print("ocak ayinda 31 gün vardir")

        else:
            print("tekrar deneyin")
            return aydaki_gun_sayaci()

5) Kenar uzunlukları verilen bir üçgenin adını ekrana yazan bir fonksiyon oluşturalım.
    # Çözüm:
        kenarBir = input("ücgenin birinci kenari girinizz: ")
        kenarIki= input("ücgenin ikinci kenari girinizz: ")
        kenarUc = input("ücgenin ucuncu kenari girinizz: ")


        n1 = int(kenarBir)
        n2 = int(kenarIki)
        n3 = int(kenarUc)

        if n1==n2==n3:
            print("eskenar ucgen")
        elif n1==n2 or n1==n3 or n2==n3:
            print("ikizkenar ucgen")
        else:
            print("cesitkenar ucgen")
            
6) Ay ve Güne göre hangi meyvenin yeneceğini bilen bir fonksiyon yazalım.
    İlkbahar: Erik
    Yaz: Karpuz
    Sonbahar: Ayva
    Kış: Portakal

    # Çözüm:
        def hangi_meyve_yenir():
    
    
        ay = input("lutfen ay adini giriniz: ")
        Gun = input("lutfen gun numarasini giriniz: ")
        gun = int(Gun)
        


        if ay=="ocak" or ay=="subat" or ay=="aralik":
            print("{} ayinin {}. gununde portakal yenir.".format(ay,gun))
        elif ay=="mart" or ay=="nisan" or ay=="mayis":
            print("{} ayinin {}. gununde erik yenir.".format(ay,gun))
        elif ay=="haziran" or ay=="temmuz" or ay=="agustos":
            print("{} ayinin {}. gununde karpuz yenir.".format(ay,gun))
        elif ay=="eylul" or ay=="ekim" or ay=="kasim":
            print("{} ayinin {}. gununde ayva yenir.".format(ay,gun))
        else:
            print("tekrar deneyin")
            return hangi_meyve_yenir

7) Kullanıcıdan C, Ç, P, S harflerinden birini isteyen bir fonksiyon yazalım.

Bu harfler haftanın günlerinin başlangıcı olsun. Gelen harfe göre hangi gün olduğunu tahmin etmeye çalışalım. 

Harflere göre ek sorular:
* C: "hafta içi mi" yoksa "hafta sonu mu"
* P: "hafta içi mi" yoksa "hafta sonu mu"
    * hafta içi: "hafta başı mı" yoksa "hafta ortası mı"

    # Çözüm:
        def gun_tahmini():
        harf = input("c, ç, p, s harflerinden birini tuslayiniz: ")

        if harf=="s":
            print("gün sali")
        elif harf=="ç":
            print("gün çarşamba")
        elif harf=="p":
            cevap= input("hafta içi mi, hafta sonu mu?: ")
            if cevap=="hafta içi":
                print("gün pazartesi")
            else:
                print("gün pazar")
        elif harf=="c":
            cevap= input("hafta içi mi, hafta sonu mu?: ")
            if cevap=="hafta içi":
                print("gün cuma")
            else:
                print("gün cumartesi")
        else:
            print("tekrar deneyin")
            return gun_tahmini

8) Kullanıcıdan pozitif bir sayı isteyelim. Girdinin gerçekten tamsayı olup olmadığını kontrol edelim. Ek olarak tam sayı ise bunun pozitif olup olmadığını da kontrol edelim.

Bu sayının tek-çift olmasına göre TUHAF mı TUHAF DEĞİL mi, buna karar verelim.

* Eğer sayı tek sayı ise TUHAF
* Eğer sayı çift ama 1 - 10 (ikisi de dahil) arasında ise TUHAF DEĞİL
* Eğer sayı çift ama 11 - 20 (ikisi de dahil) arasında ise TUHAF
* Eğer sayı çift ama 20 den büyükse TUHAF DEĞİL

    # Çözüm:
        def tahmin():
        sayi = input("bir pozitif sayi giriniz: ")
        
            
        try:
            sayi = int(sayi)
            if sayi>=0:
                if sayi%2!=0:  #tek sayi
                    print("tuhaf")
                elif sayi%2==0 and (1< sayi and sayi>10):
                    print("tuhaf degil")
                elif sayi%2==0 and (11< sayi and sayi>20):
                    print("tuhaf")
                else:
                    print("tuhaf degil")
            else:
                print("pozitif degil tekrar deneyin")
                return tahmin()
        except ValueError:
            print("bu bir tam sayi degil. tekrar deneyin")
            return tahmin() 

9) **TEK-ÇİFT Toplamlar Kuralı:** 
* İki sayının toplamı Tek ise sayılardan sadece biri Tek'tir.
* İki sayının toplamı Çift ise sayıların ikisi Tek ya da ikisi Çift'tir.

Kullanıcıdan iki sayı isteyip Tek-Çift Toplamlar Kuralına göre toplamın Tek mi yoksa Çift mi olduğunu bulan bir fonksiyon yazın.

**Önemli:** Bu soruyu x + y diyerek, direk toplam değeri üzerinden yapmayınız.

    # Çözüm:
        def tekmiciftmi():
        sayi1 = input("birinci sayiyi giriniz: ")
        sayibir = int(sayi1)
        
        sayi2 = input("ikinci sayiyi giriniz: ")
        sayiiki= int(sayi2)

        if (sayibir+sayiiki)%2!=0:
            print("biri tek \ntoplam={}".format(sayibir+sayiiki))
        else:
            if sayibir%2==0 and sayiiki%2==0:
                print("ikisi de cift\ntoplam={}".format(sayibir+sayiiki))
            else:
                print("biri cift\n toplam={}".format(sayibir+sayiiki))

10) Kullanıcıdan iki sayı alalım. Bu sayılardan hangisinin küçük, hangisinin büyük olduğunu bulalım.

Sonra büyük sayıdan geriye gidip, küçük sayıya kadar olan sayıları ekrana yazalım.

    # Çözüm:
        def gerigitmefonksiyonu():
        sayi1= input("birinci sayiyi girin: ")
        sayibir = int(sayi1)
        sayi2= input("ikinci sayiyi girin: ")
        sayiki = int(sayi2)

        if sayibir>sayiki:
            print("{0}, {1}'dan büyüktür.".format(sayibir,sayiki)) 
            while sayibir>=sayiki:
                print(sayibir)
                sayibir = sayibir - 1
        else:
            print("{0}, {1}'dan büyüktür.".format(sayiki,sayibir))
            while sayiki>=sayibir:
                print(sayiki)
                sayiki = sayiki - 1

          
"""

# Fonksiyonlar
"""
return:
foksiyonlar işini bitirince genelde geriye değer dönerler.
fonksiyonu çağiran yer de o değeri alir ve ona göre işlem yapar.

geriye değer dönmeyen fonksiyonlara "void fonksiyon" denir.
geriye değer dönme => return

returnden sonra gelen kodlar çaliştirilmaz.


#adim adim gelistirme
genelde bütün program tek seferde yapilmaz
bunun icin de adim adim gelistirme yapilir.
hata ayiklama (debug) icin olmazsa olmaz bir kavramdir.

pythonda fonksiyonlarbirinci seviye vatandastir
yain, fonksiyolnlar da ayni degiskenelr gibi atabnabilirler..
parametre olarak verilebilirler.


----- ALISING YENIDEN ADLANDIRMA -----
def kup(num)
    return num**3

kup(5) == 125

q = kup(5) der isek q==125 olur
type(q) = function olur

q = kup()
q(5) 
dersek, q(5) == 125 olarak gelir.



"""
# Parametre sayisi bilinmiyorsa (*args)
"""
bazen bir fonksiyonun ne kadar parametre alacagini bilemeyiz.
bu durumda *args yaziliri(arguments)

*parametre sayisi önceden bilinmeyen fonksiyon*
def toplam(*args):
    return sum(*args)

girilen bütün parametreleri toplayip verir.
    
"""
# lambda fonksiyonu
"""
bazen bir fonksiyonu isim vermeden direkt kullanmak isteyebiliriz
bunun icin lambda anahtar kelimesi kullanilir.
return degerleri yoktur.!!!!

*tek satir fonksiyonu olarak bilinir.

** metni parcalayan bir lambda fonks yazalim:
    metni_parcala = lambda x: x.split()

metni parcala(can ozturk) ==> "can", "ozturk"
"""
# iç içe fonksiyonlar (nested)
"""
bir fonksiyonun içinde başka bir fonksiyon tanimlanmasi gerekebilir.
buna "nested" fonksiyon denir

* bir sayinin 5 ve 8in ortak kati olup olmadigini bulalim
def ortakkatmi(n):
    def besin_kati(n):
        if n%5==0: true
        else: false
    def sekizin_kati(n):
        if n%8==0: true
        else: false
    if besin_kati(n) and sekizin_kati(n):
        return true
    else: false
"""
# değiştirilebilir x değiştirilemez (mutable - immutable)
"""
python'da her şey bir nesnedir.
ver her nesnenin bir tipi vardir.

değiştirilemez: bazi nesne tipleri atandiklari gibi kalir. icinden bir parca degisemez. (immutable)
degistirilebilir: bazi tiplerin ise bir parcasini degistirebilirsiniz. (mutable)

python'da:   *int = immutable
            *float = immutable
            *bool = immutable
            *str = immutable
            *tuple = immutable
            
            *list = mutable
            *dict = mutable

değiştirilemeyen tiplerde, data'yi degistirmek icin yeniden atama yapilir.
bu degistirmek sayilmaz(mute etmis sayilmayiz), sadece bellekteki veriyi degistirmis oluruz.
mute etmek = mutasyona uğratmak

 
"""
# deger olarak gecme(pass by value) - referans olarak gecme (pass by reference)
"""
mutable ve immutable tiplerinde bir fonksiyona parametre olarak gectiginde ne olur?
* immutable = pass by value (int, string, bool, char):
            kendisi degismeden kalir, fonksiyona kopyasi gecer.
* mutable = pass by reference:
            referansi gecer, bellekteki adresi gecer
            eger fonks icinde bu deger degisirse, orj degisken de degismis olur..

a = 45

print(a) => 45 degeri yazdirilir 

def degistir(a):
    a = 0
degistir(a)

print(degistir) => yine 45 degeri yazdirilir.

!! cünkü int degerler degistirilemez degerlerdir. 0 degeri sadece fonksiyon icinde degisir. (pass by value)

--------------------------------

list = ['1','2','3']
print(list) => 1, 2, 3 şeklinde cikar

def degistir(list):
    list[0] = '0'
    list[1] = 'b'
degistir(list)

print(degistir) => '0', 'b', '3' seklinde yazdirir.

!! çünkü list degistirilebilir bir tiptir ve degerleri adresten degirisir. (pass by reference)





"""

# QUIZ 2
""" 
1) Ekrandan girdi okuyan fonksiyonlar yazdık. Şimdi bu girdi okuma işini jenerik bir hale getirelim.<br>
Bu fonksiyon, parametre olarak, text türünde bir istek metni alsın ve bu metne göre kullanıcıdan girdi istesin.
Sonra aldığı girdiyi bize geri göndersin (dönsün).
    # Çözüm:
        def okuma(text):
            print(type(text))    
            return text


        text = input("bir metin giriniz: ")
        print(okuma(text))

2) Soru 1'de yazdığımız jenerik girdi fonksiyonun bize sürekli metin `(str)` döndüğünü biliyoruz.
Ama tamsayı istediğimiz durumlar da oldu.
Şimdi yeni bir fonksiyon yazalım.
Bu yeni fonksiyon, girdi_al fonksiyonun bize döndüğü değer üzerinden tam sayı olup olmadığını kontrol etsin ve 
bize tamsayı ise True değilse False dönsün.

    # Çözüm: 
        def okuma(text):
        print(type(text))    
        return text

        def tamsayi_mi(text):
                if text.isdigit():
                    return "true"
            
                else:
                    return "false"


        print(tamsayi_mi(okuma(input("bir metin girin: "))))

3) Şoru 1 ve Soru 2'deki fonksiyonları kullanarak kullanıcıdan tamsayı alalım. Ve bu sayıyı dönelim.
Soru 2 bize tamsayı almayı garantiler.
Kullanıcı tamsayı girmemişse tekrar tekrar (recursive) soralım.
    # Çözüm:

    def okuma(text): 
        try:
            sayi = int(text)
            print(text)
        except ValueError:
            print("tekrar dene: ")
            return okuma

    metin = input("bir tam sayi girin: ")
    okuma(metin)

4)Kullanıcıdan 1-7 arasında bir gün numarası alıp, 
bu numaranın hangi gün değerine ait olduğunu dönen bir fonksiyon yazalım.

    # Çözüm:
    def haftanin_gunu():
        i = input("lutfen 1-7 arasinda bir sayi girin")
        if i=="1":
            print("pazartesi")
        elif i=="2":
            print("sali")
        elif i=="3":
            print("carsamba")
        elif i=="4":
            print("persembe")
        elif i=="5":
            print("cuma")
        elif i=="6":
            print("cumartesi")
        elif i=="7":
            print("pazar")
        else:
            print("tekrar deneyin")
            return haftanin_gunu

    haftanin_gunu()

6) Adı `aritmetik_ortalama` olan bir fonksiyon tanımlayın. <br>
Bu fonksiyon değişken uzunlukta parametre alıyor alsın. <br>
Yani parametre sayısı önceden belli değil. <br>
Fonksiyonunuz aldığı bu parametrelerin aritmetik ortalamasını ekrana yazsın. <br>
* Aritmetik Ortalama = Toplam / Eleman Sayısı

    # Çözüm:
    def aritemetik_ortalama(*args):
        return sum(args)/len(args)

    ort = aritemetik_ortalama(1,2)

    print(ort)


7) Dairenin alanını hesaplayan bir fonksiyon yazınız. 
Parametre olarak yarıçap alsın ve tüm fonksiyon tek satır olsun.
    
    # Çözüm:
        def daireAlani(r):
            return 3.14*r**2

        print(daireAlani(14))   



8) Çemberin çevresini hesaplayan bir fonksiyon yazınız. 
Parametre olarak yarıçap alsın ve tüm fonksiyon tek satır olsun.
Çember Çevresi = 2 * \pi * r
    
    # Çözüm:
        def cemberAlani(r):
            return 3.14*r*2

        print(cemberAlani(14)) 

9) Dikdörtgenin alanını hesaplayan bir fonksiyon yazınız. 
Parametre olarak kısa (a) ve uzun kenarı (b) alsın ve tüm fonksiyon tek satır olsun.
Dikdörtgen Alanı = a * b

    # Çözüm:
        def dikdortgenAlani(a,b):
            return a*b

        print(dikdortgenAlani(5,21))

10) Silindirin hacmini hesaplayan bir fonksiyon yazın. <br>
Bu fonksiyon parametre olarak silindirin taban yarıçapını (r) ve yüksekliğini alsın. <br>
* Silindir, üstünde ve altında daire olan, yan yüzeyi ise açılınca diktörtgen olan bir şekildir.

    # Çözüm: 
        def silindirHacmi(r,h):
                return 3.14*r**2*h

        print(silindirHacmi(5,21))


"""











