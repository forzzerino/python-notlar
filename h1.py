# PYTHON GIRIS DOSYASI
# bolum 1 - giris
"""
deger: programda anlam tasiyan yapilardir. hafizada yer tutarlar
tip: hafizanin formatini tanimlar.
    "hello world" => tipi-string    deger-"hello world"
"""

# bolum 2 - aritmetikler ve degiskenler
"""
a + b = toplama
a - b = cikarma
a * b = carpma
a / b = bolme (float deger verir)
a ** b = üstel
a // b = tam sayi bolmesi

degisken= bir degere atifta bulunan isimdir.
        sayi = 12 (deger)
                "sayi" = degerin adresine verilen isim

        print(sayi) => sayi degiskenine gider ve degiskenin
                        adresinde sakladigi degeri yazdirir.

degisken olusturulmasi:
♦ genelde snake_case kullanilir
♦ sayi ile baslayamaz
♦ bosluk kullanilmaz
♦ ozel karakter kullanilmaz
"""

# bolum 3 - veri tipleri ve numerik operasyonlar
"""
• text => string
• numerik => int, float
• liste => list, range
• iliski => dict
• kume => set
• boolean => bool


a = 4, b = 7 -> print(a+b)

---string iliskileri-----
string hem tek tirnak hem de cift tirnak gosterilebilir
stringde bolme ve cikarma yapilmaz
toplama ve carpma yapilabilir.

print("asfalt"*3) = asfaltasfaltasfalt
print("asfalt" + "kalem") = asfaltkalem

"""

# bolum 4 - fonksiyonlar
"""

bir islev icin yazilmis kod parcasi
cagirildigi zaman calisir
istege gore parametre alirlar
istege gore deger donerler

fonks_adi(), fonks_adi(parametreAdi1, parametreAdi2)

-----fonks tanimlamak------
def fonksiyon_adi():
    print(fonksiyon olusturduk)

fonksiyon_adi() ---> cagirilmis olur


♦ fonksiyon tanimlamalarda bileske olarak kullanilaniblir
    ogrenci_bilgisi():
        ogrenci_adi()
        ogrenci_no()        =>  Can Öztürk 2111505060 şeklinde cikti verir.
        ogrenci_okul()


----------parametreler------------
fonksiyonun calismasi icin iletilen girdiler
cagirilirken girilir

    fonksiyon_adi(p1, p2)
        islem_satiri = p1 + p2
    
    print(fonksiyon_adi(5, 4)
        ==== islem satirina p1-5 p2-4 seklinde bilgi girilir.

"""
# bolum 5 - scope, return, docstring
"""

----scope----

♦ degiskenin yasadigi yer
♦ indent ile tanimlanir
♦degiskene scope'unun disindan ulasmaya calisirsak NameError aliriz.

-> global'deki bir degiskeni fonksiyon icinde degistirmek icin 
    degiskenin basina "global" yazilir

aksi halde degeri degistirilen degisken sadece fonks icinde anlik degisir.

------return-----
fonks isini bitirdikten sonra geriye donecegi degerdir
donmeyen fonkslara "void" denir

    herhangi_bir_fonks():
        islem_satiri
        islem_satiri
        return 55

    herhangi_bir_fonks() == 55 degeri verir.

-----docstring----
♦fonks dokumantasyonu olarak adlandirilabilir
♦fonks bilgilerini verir
♦ genelde en basa yazilir

○ veri tiperi  
○ islemler                  yazilabilir docstring'e 
○ degisken bilgileri 
○ geri donus bilgisi
    
"""

# "quiz 1 - TEMELLER"

"""
♦ 24 dakika 36 saniye içinde toplam kaç adet saniye bulunur?
    
    toplam = 24*60 + 36
    print(toplam)

♦ Saatte ortalama 80 km hizla giden bir araç, 
    İstanbul'dan Ankara'ya kaç dakikada gider. 
    İstanbul, Ankara arasi mesafe 450 km dir.   

    saat = (450/80) * 60

♦ Ekrana "Seni seviyorum Python" yazabilir misiniz?
    print("seni seviyorum python")

♦ Ekrana 15 sayisinin tipini yazabilir misiniz?
    print(type(15))

♦ Ekrana "Selam Python" ifadesinin tipini yazabilir misiniz?
    print(type("selam python))

♦ Ekrana "15" ifadesinin tipini yazabilir misiniz?
    print(type("15"))

♦ 49 sayisinin 5 e bölümünden kalan kactir?
    print(49%5)
    --- % mod alma islemidir kalani verir. ---

♦ 49 sayisinin 5'e tam bölümü kactir (taban bölüm)?
    print(49//5)
    ---- // tam bolum islemidir----

♦ 1'den 5'e kadar olan sayilarin kareleri toplaminin ortalamasi kactir?
    print((1**2 + 2**2 + 3**2 + 4**2 + 5**2) / 5)      

♦ Karesi, 4'ün küpünden 17 fazla olan sayi kactir?
    print((4**3 +17)**0.5 )



"""

# "quiz 2 - DEGISKENLER"

"""

♦ "Ekrana "Hello Python" yazmak için noktali yeri doldurun:"
 ".....("Hello World!")"
    print("hello world")

♦ "Aşağidaki kodda yeralan yazim hatasini düzeltin.",
 "print("5 2'den büyüktür.')"
        print("5, 2'den buyuktur")

♦ Asakigdaki satiri yorum satiri yapiniz"
    "Bu bir yorum satiridir."
        # bu bir yorum satiridir.

♦ Çok satir yorum özelliğini kullanip asagidaki satirlari yorum satiri yapin",
"Bu yorum satiri",
"Çok satirdir",
"Sadece bir satir yorum değil..."

        
        "Bu yorum satiri"
        "Çok satirdir",
        "Sadece bir satir yorum değil..."
        
♦ İsmi araba_markasi olan bir değişken yaratin ve bu değişkene Volvo değerini atayin.  
    def araba_markasi = volvo

♦ x ve y adinda iki değişken yaratin ve değerlerini 20 ve 80 olarak atayin.
z adinda bir değişken yaratin, değerini x + y olarak atayin ve ekrana gösterin.
    x = 20
    y = 80
    z = x + y
    print(z)

♦ Değişken adindan, kullanilmasi yasak olan karakterleri cikarin.
"**2benim-ilk_değişkenim = "Yapay Zeka"**"
    benim_ilk_degiskenim = "yapay zeka"    

♦ Üç değişkene ayni değeri tek seferde atamak için aşağidaki boşluklari doldurun.
"x ... y ... z = "Portakal""
    x, y, z = "portakal"


"""

# "quiz 3 - FONKSIYONLAR"
"""
♦ Ekrana "Selam Dünya!" yazan bir fonksiyon yazin.
    def fonksiyon():
    print("selam dünya")

♦String şeklinde iki parametre alan bir fonksiyon yazin. 
Bu parametreleri kişi ismi kabul edelim."
"Fonksiyon bu iki ismi "ve" ile bağlayarak selamlasin."
"Ör: Selam Clark Kent ve Superman. "
"(String'in format fonksiyonu kullanin.)"

    def birlestirme():
        birlesim = "selam {} ve {}. Nasilsin?"
        print(birlesim.format(isim_bir, isim_iki))    

    print(birlestirme())

♦ Kullanicidan girdi olarak ismini isteyen bir fonksiyon yazin.
"Bu fonksiyon aldiği ismi "Selam sana ...." şeklinde selamlasin.
"(Girdi almak için input() fonksiyonunu kullanin.)"

    isim = input("isim girin")
    print("selam sana " + isim)

♦ "Parametre olarak 3 sayi alan bir fonksiyon yazin.
"Fonksiyon bu sayilardan en büyüğünü size geri dönsün.
"Bu fonksiyonun docstring'ini de yazin.

    ilk_sayi = input("ilk sayiyi girin: ")
    ikinci_sayi = input("ikinci sayiyi girin: ")
    ucuncu_sayi = input("ucuncu sayiyi girin: ")
    
    ***
    Ust tarafta kullanicidan 3 tane sayi girmesini istedik.
    Bunu 'input' fonksiyonunun kullanarak yaptik.
    Bu girilen sayilari degiskenlere atadi.
    ***

    def maksimum_getir(sayi_bir, sayi_iki, sayi_uc):
        return max(sayi_bir, sayi_iki, sayi_uc)
    ***
    Bir fonksiyon olusturup girilen üc sayiyi karsilastirmaya basladik
     boylelikle karar verilecek ve en buyuk deger bulunana kadar devam edecek
    sonucunda ise en buyuk deger return edilecek.
    *** 


print("girilen sayilardan en buyugu: " + maksimum_getir(ilk_sayi, ikinci_sayi, ucuncu_sayi))

♦ Parametre olarak gelen metni parçalayan küçük harfe çeviren bir fonksiyon yazin.
    metin = "aNNe"
    def duzgun_metin(bozuk_metin):
        duzg_islemi = bozuk_metin.lower()
        
        kesme_islemi = duzg_islemi.strip("n")
        print(kesme_islemi)

    print(duzgun_metin(metin))

♦ Parametre olarak gelen iki sayinin toplamini dönen bir fonksiyon yazin.
    sayi = 3
    sayi_iki = 4

    def toplam(sayi_ilk, sayi_iki):
        sonuc = sayi_ilk + sayi_iki
        return sonuc

    print(toplam(sayi, sayi_iki))

♦ Parametre olarak gelen 3 sayi alan bir fonksiyon yazin.
"Fonksiyon bu sayilarin ikili farklarini alsin ve bu farklardan en küçüğünü dönsün.
    import math

    sayiBir = 55
    sayiIki = 5
    sayiUc= 8

    def farklari(ilk, ikinci, ucuncu):
        birVeIki = abs(ilk - ikinci) 
        birVeUc = abs(ilk - ucuncu) 
        ikiVeUc = abs(ikinci - ucuncu)

        return(max(birVeIki, birVeUc, ikiVeUc))

    print(farklari(sayiBir,sayiIki,sayiUc))

♦ Parametre olarak bir sayi alan bir fonksiyon yazin.
"Fonksiyon bu sayinin karekökünü dönsün"

    import math
    sayi = 16
    def karekok(ilk):
        return (math.sqrt(ilk))

    print(karekok(16))

♦ Parametre olarak bir sayi alan bir fonksiyon yazin. 
Fonksiyon bu sayinin logaritmasini dönsün
import math

    sayi = 10
    def karekok(ilk):
        return(math.log(ilk))

    print(karekok(sayi)),

♦ Parametre olarak 2 sayi alan bir fonksiyon yazin.
Bu sayilari bir dik üçgenin dik kenarlari  olarak düşünelim.
Fonksiyon bu üçgenin hipotenüsünü dönsün.

    import math
    kenarBir = 8
    kenarIki = 15

    def hipotenus(kenarDikey, kenarYatay):
        return (math.hypot(kenarDikey, kenarYatay))

    print(hipotenus(kenarBir, kenarIki))

"""