
"""
Adı Ogrenci olan bir class tanımlayın.
Ogrenci'nin 2 özelliği var:
* isim (str)
* numara (str)

Bu Ogrenci class'ından iki öğrenci yaratın.
Bilgileri şu şekilde olacak:
1- isim: James Bond, numara: 007
2- isim: Klark Kent, numara: 333

Sonra bu iki öğrencinin adlarını print edin.

İpuçları:
* __init__

Beklenen Sonuç:
James Bond
Klark Kent
"""
class Ogrenci:
    def __init__(self,isim,numara) -> None:
        self.isim = str(isim)
        self.numara = str(numara)


og1 = Ogrenci("james bond","007")
og2 = Ogrenci("klark ken","333")

print(og1.isim,og2.isim)




"""
Soru 1'deki Ogrenci class'ımızın şimdi de kayıt olduğu dersleri tutan,
bir attribute'u (özelliği) daha olsun. 
Bu özelliğin adı 'dersler' olsun ve list tipinde olsun.
Bu özellik, Ogrenci yaratılırken boş liste olarak initialize olacak.

Ogrenci derslere birer birer katılacak.
Dolayısı ile 'derse_katil()' adında bir metodu da olacak.
Be metod parametre olarak katılacak dersi alacak.
Eğer ders henüz listede yoksa, o zaman kayıt olacak.

Ek olarak 'get_dersler' adında bir metod daha olacak.
Bu metod bize öğrencinin kayıt olduğu ders listesini verecek.

Buna göre Ogrenci class'ını modifiye edin.

Öğrencinin bilgileri şu şekilde olacak:
isim: Cin Ali, numara: 1111
katılacağı dersler: Temel Python ve Yapay Zeka

Beklenen Sonuç:
ogrenci.get_dersler()  ->  ['Temel Python', 'Yapay Zeka']
"""


import os
class Ogrenci:
    def __init__(self,isim,numara) -> None:
        clear = lambda: os.system("cls")
        clear()
        self.isim = str(isim)
        self.numara = str(numara)
        self.__ders = []
        print("ogrenci yaratildi. ismi: {}\n".format(self.isim))
        
    def derse_katil(self,*args):
        for arg in args:
            if arg in args:
                self.__ders.append(arg)
                print("'{}' dersi listeye eklendi.\n".format(arg))
            else:
                print("bu ders zaten kayitli.\n")
            
    def get_dersler(self):
        print("aldiginiz dersler:\n-----------------")
        for ders in self.__ders:
            print(ders,"\n")
            
            
ogrencim = Ogrenci("cin ali","1111")
ogrencim.derse_katil("temel python","yapay zeka")
        
        
print(ogrencim.get_dersler())



"""
İsmi Point olan bir class tanımlayın. 
X-Y koordinat düzleminde bir noktayı temsil etsin.
Docstring'i şu olsun: "(x,y) koordinat düzlemindeki bir noktayı gösterir."

Point'in iki attribute'u vardır: 
    * x (int) 
    * y (int)

Point'in __init__() metodunu tanımlayın.
Ek olarak uzaklık hesaplayan bir metodu vardır. Adı 'uzaklik'.
'uzaklik' metodu parametre olarak ikinci bir Point alır.
Ve kendisi (self) ile ikinci nokta arasındaki mesafeyi hesaplayarak döner.

İpuçları:
* uzaklık şöyle hesaplanır:
    * x'ler arasındaki farkın karesi ile 
    * y'ler arasındaki farkın karesinin toplamının karekökü
    * d = math.sqrt(x_ler_farki**2 + y_ler_farki**2)
    
Örnek çağırma:
nokta_1 -> (1, 7)
nokta_2 -> (4, 3)
uzaklik = nokta_1.uzaklik(nokta_2)
print(uzaklik)

Beklenen Cevap: 5.0


"""

import os
import math
class Point:
    def __init__(self,x=0,y=0) -> None:
        clear = lambda: os.system("cls")
        clear() 
        self.x = x
        self.y = y
        print("nokta olusturuldu")
        
    def uzaklik(self,point2):
        return math.sqrt((self.x-point2.x)**2 + (self.y-point2.y)**2)
        
        
nokta1 = Point(1,7)
ikiuzaklik = nokta1.uzaklik((Point(4,3)))
print(nokta1.__doc__)





"""
İsmi Rectangle olan bir class tanımlayın. 
X-Y koordinat düzleminde bir dikdörtgeni temsil etsin.
Docstring'i şu olsun: "(x,y) koordinat düzlemindeki bir dikdörtgeni gösterir."

Rectangle'in 4 attribute'u vardır: 
    * kose_1 (Point)
    * kose_2 (Point)
    * kose_3 (Point)
    * kose_4 (Point)
Bu dört köşenin tipi Soru 3'de tanımladığınız Point class'ıdır.

Köşelerden 1 ve 2 aynı doğru üzerinde, 3 ve 4 aynı doğru üzerindedir.

1..............2
.              .
.              .
.              .
3..............4

Rectangle'in __init__() metodunu tanımlayın.
Ek olarak enini ve boyunu hesaplayan metodları vardır:
    * en = 1 - 2 arası mesafe  -> en_hesapla()
    * boy = 1 - 3 arası mesafe -> boy_hesapla()
Rectangle bu mesafeleri hesaplamak için Point class'ını kullanır.

Son olarak alan hesaplayan bir metodu vardır. Adı 'alan'.
'alan' metodu dikdörtgenin alanını hesaplayarak döner.

Örnek çağırma:
p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

en = rect.en
boy = rect.boy
alan = rect.alan()

Beklenen Sonuç:
en: 4.0
boy: 6.0
alan: 24.0

"""

import os
import math
class Point:
    
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
        print("nokta olusturuldu")
        
    def uzaklik(self,point2):
        uzaklik1 = self.x - point2.x
        uzaklik2 = self.y - point2.y
        return math.sqrt(uzaklik1**2 + uzaklik2**2)
        
        
nokta1 = Point(1,7)
ikiuzaklik = nokta1.uzaklik((Point(4,3)))
print(nokta1.__doc__)


class Rectangle(Point):
   
    def __init__(self,kose1,kose2,kose3,kose4) -> None:
        clear = lambda: os.system("cls")
        clear()
        print("dikdörtgen oluşturuldu")
        self.kose_1 = kose1
        self.kose_2 = kose2 
        self.kose_3 = kose3 
        self.kose_4 = kose4  
    
    def en_hesapla(self):
        return self.kose_1.uzaklik(self.kose_2)
    
    def boy_hesapla(self):
        return self.kose_1.uzaklik(self.kose_3)
    
    def alan(self):
        return(self.en_hesapla() * self.boy_hesapla())
              
       
ddgen = Rectangle(Point(5,8),Point(9,8),Point(5,2),Point(9,2))
en = ddgen.en_hesapla()
boy = ddgen.boy_hesapla()
alan = ddgen.alan()
print(alan)
print(en, boy)






"""
Adı BankaHesabi olan bir class tanımlayın.
BankaHesabi'nin bir attibute'u vardır: bakiye (int)
Ek olarak iki adet metodu vardır:
* para_cek(tutar)   -> hesaptan para çeker
* para_yatir(tutar) -> hesaba para yatırır

İki metod da bakiye'yi günceller ve ikisi de geriye, kalan bakiye'yi döner.
Hesap açılırken (__init__) bakiye değeri 0'dır.
Ek olarak her seferinde print() yazmamak için, class içerisinde 'bakiye_goruntule' diye
bir metod olsun.
Bu metod çağrılınca şöyle yazsın: Hesap bakiyesi: xxxxxx

Örnek Çağırma:
hesap = BankaHesabi()
hesap.bakiye_goruntule()
hesap.para_yatir(500)
hesap.bakiye_goruntule()
hesap.para_cek(200)
hesap.bakiye_goruntule()

Beklenen Sonuç:
Hesap bakiyesi: 0
Hesap bakiyesi: 500
Hesap bakiyesi: 300
"""

class BankaHesabi:
    def __init__(self,bakiye=0) -> None:
        self.__bakiye = bakiye
        print("banka hesabi olusturuldu")

    def para_cek(self,tutar):
        if self.__bakiye<tutar:
            print("yeterli paran yok")
        else:
            self.__bakiye = self.__bakiye - tutar
            print("{}TL cekildi.\nKalan Bakiyen = {}".format(tutar,self.__bakiye))
            
    def bakiye_goruntule(self):
        print("mevcut bakiyeniz: {}TL".format(self.__bakiye))      
            
            
            
    def para_yatir(self,tutar):
        if tutar<0:
            print("negatif yatiramazsin kardesim")
        else:
            self.__bakiye = self.__bakiye + tutar
            print("bakiyen güncellendi. yeni bakiyen = {}".format(self.__bakiye))

import os
clear = lambda: os.system("cls")
clear()


hesap = BankaHesabi()
hesap.bakiye_goruntule()
hesap.para_yatir(500)
hesap.bakiye_goruntule()
hesap.para_cek(200)
hesap.bakiye_goruntule()

import os
clear = lambda: os.system("cls")
clear()






"""

adı MinimumBakiyeHesabi olan bir class tanımlayın.
Bu class, Soru 5'te tanımladığınız BankaHesabi class'ından kalıtım alacak.
Bu class içinde bakiye'nin bir minimum değeri tutulacak. (minimum_bakiye)
Bu değer hesap yaratılırken girilecek.

Eğer kullanıcı para çekmek isterse, 'para_cek(tutar)' metodu ile, 
o zaman minimum_bakiye'yi kontrol edeceğiz.
Eğer bu tutar çekilince, hesap bakiyesi minimum_bakiye'nin altına düşecek olursa,
para çekme işlemini iptal edip ekrana şöyle yazacak:
"Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında."

Ek olarak bu class'ı print eden biri anlamlı bir metin görsün diye,
"Bu MinimumBakiye sınıfıdır." şeklinde dönsün.

İpuçları:
* super()
* __str__
* para çekme işlemini bu class içinde yapmayın, ana class'ı yapıyor zaten

Örnek Çağırma:
minimum_hesap = MinimumBakiyeHesabi(100)
print(minimum_hesap)
minimum_hesap.para_yatir(500)
minimum_hesap.bakiye_goruntule()
minimum_hesap.para_cek(200)
minimum_hesap.bakiye_goruntule()
minimum_hesap.para_cek(300)
minimum_hesap.bakiye_goruntule()

Beklenen Sonuç:
Bu MinimumBakiye sınıfıdır.
Hesap bakiyesi: 500
Hesap bakiyesi: 300
Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında.
Hesap bakiyesi: 300

"""

class BankaHesabi:
    def __init__(self,bakiye) -> None:
        self.bakiye = bakiye
        self.bakiye_goruntule()
    
    def bakiyedondur(self):
        return self.bakiye

    def para_cek(self,tutar):
        if self.bakiye<tutar:
            print("yeterli paran yok")
        else:
            self.bakiye = self.bakiye - tutar
            print("{}TL cekildi.\nKalan Bakiyen = {}".format(tutar,self.bakiye))
            
    def bakiye_goruntule(self):
        print("mevcut bakiyeniz: {}TL".format(self.bakiye))      
            
            
            
    def para_yatir(self,tutar):
        if tutar<0:
            print("negatif yatiramazsin kardesim")
        else:
            self.bakiye = self.bakiye + tutar
            print("{}TL yatirildi".format(tutar))
            print("bakiyen güncellendi. yeni bakiyen = {}".format(self.bakiye))




class MinimumBakiyeHesabi(BankaHesabi):
    def __init__(self, minbakiye,bakiye) -> None:
        super().__init__(bakiye)
        
        self.minbakiye = minbakiye
        
    def min_bakiye_goruntule(self):
        print("min bakiye: {}".format(self.minbakiye))
        
        
    def para_cek(self,cekilecektutar):
        if super().bakiyedondur() - cekilecektutar < self.minbakiye:
            print("Üzgünüz, çekilmek istenen tutar minimum_bakiye'nin altında.")
        else:
            super().para_cek(cekilecektutar)
        

    def __str__(self) -> str:
        return "Bu MinimumBakiye sınıfıdır."




min_hesap = MinimumBakiyeHesabi(100,0)
min_hesap.min_bakiye_goruntule()
min_hesap.para_yatir(500)
min_hesap.para_cek(200)
min_hesap.para_cek(300)







"""
Aşağdaki şekilde iki class tanımlayın:

Sarki:
Şarkılarımızı tutmak için kullanacağız.
Her şarkının; 'adi', 'sanatci', 'album' ve 'sarki_no' diye özellikleri var.
'album' adlı özellik Album class'ı tipinde olacak.

Album:
Albümlerimizi tutacak.
Her albümün; 'adi', 'sanatci', 'yil' ve 'sarkilar' diye özellikleri var.
'sarkilar' bir liste olacak ve içinde Sarki nesnelerini tutacak.
Album'un içinde 'sarki_ekle()' adlı bir metod var ve bu metod albüme şarkı ekler.
Bunu yaparken bir şarkı numarası üretir ve öyle ekler.

Album içindeki şarkıları tek tek ekrana yazdırın.

İpuçları:
* önce albüm sonra şarkı üretin

Örnek Çağırma:
album = Album('Yesterday and Today', 'The Beatles', 1966)
album.sarki_ekle('Yesterday')
album.sarki_ekle('Act Naturally')
album.sarki_ekle('What Goes On')

Beklenen Sonuç:
Yesterday
Act Naturally
What Goes On
"""

class sarki:
    def __init__(self,sarkiadi,sarkisanatci,sarkialbum,sarkino) -> None:
        self.sarkiadi = sarkiadi
        self.sarkisanatci = sarkisanatci
        self.sarkialbum = sarkialbum
        self.sarkino = sarkino
        
   

class album:
    def __init__(self,albumadi,albumsanatci,albumyil) -> None:
        self.albumadi = albumadi
        self.albumsanatci = albumsanatci
        self.albumyil = albumyil
        self.sarkilar = ["{} Albumunun Sarklari:\n".format(self.albumadi)]
        print("album olusturuldu. Adi:{}, Author: {}".format(self.albumadi,self.albumsanatci))
    
    def sarkiekle(self,sarki_adi):
        sarki_no = len(self.sarkilar)
        
        Sarki = sarki(sarki_adi,self.albumsanatci,self,sarki_no)
        
        self.sarkilar.append(Sarki) 
        print("sarki basariyla eklendi") 
    
    def __str__(self) -> str:
        return self.albumadi  
    
    
alb = album("yesterday and today","the beatles",1996)
alb.sarkiekle("yesterday")
alb.sarkiyazdir()


class sanatci:
    def __init__(self,sanatciismi) -> None:
        self.sanatciismi = sanatciismi
        self.sanatcialbumler = ["Sanatcinin albumleri:\n"]
        print("sanatci olustu")

    # def album_ekle(self,*album):
    #     for album in album.albumadi:
    #         if not album.albumadi in self.sanatcialbumler:
    #             self.sanatcialbumler.append(album.albumadi)
    #             print("{} albumu listeye eklendi".format(album.albumadi))
    #         else:
    #             print("bu albüm zaten listede.")
    
    def album_ekle(self,eklenecekalbum):
        if not eklenecekalbum in self.sanatcialbumler:
            
            self.sanatcialbumler.append(eklenecekalbum)
            print("{} albumu sanatcinin album listesine eklendi.".format(eklenecekalbum.albumadi))
        else:
            print("bu albüm zaten listede")
    
         
    def album_yazdir(self):
        for album in self.sanatcialbumler:
            print(album)
            
            
    def album_sarkilari_yazdir(self):
        for album in self.sanatcialbumler:
            print(album," albumunun sarkilari:\n")
            for sarki in album.sarkilar:
                print(sarki)
        
    
beatles = sanatci("the beatles")
album1 = album("yesterday and today", "the beatles",1966) 
album1.sarkiekle("yesterday")
album1.sarkiekle("act naturally")
beatles.album_ekle(album1)


print("-----------------------------------------------")
album2 = album("let it be","the beatles",1970)
album2.sarkiekle("let it be")
album2.sarkiekle("for you blue")
beatles.album_ekle(album2)

# beatles.album_yazdir( )
for album in beatles.sanatcialbumler:
    for sarki in album.sarkilar:
        print(sarki)


sarkilar = [sarki for album in beatles.albumler for sarki in album1.album]
