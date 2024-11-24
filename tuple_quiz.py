"""
Soru 1:
Aşağıdaki şekilde bir fonksiyon yazın. Adı tuple_yarat olsun.  Fonksiyonumuz önce içinde 1'den 
10'a kadar değerlerin olduğu bir Tuple yaratsın.  Ardından bu Tuple'a 11'den 20'ye kadar olan 
sayıları eklesin ve Tuple'ın son halini dönsün.
İpuçları:
• Tuple'lar Immutable'dır. O Tuple'a nasıl yeni eleman eklenir?
• for döngüsü ve range() kullanın

"""

def tuple_yarat():
    sayi_aralik = tuple(range(1,11))
    yeni_aralik = tuple(range(11,21))
    sayi_aralik = sayi_aralik + yeni_aralik
    print(sayi_aralik)
tuple_yarat() 









"""
Parametre olarak verilen bir Tuple'ı String'e dönüştüren ve bu String'i geri dönen bir fonksiyon 
yazın.  Adı tuple_to_string olsun.
İpuçları:
• join()"""

def tuple_to_string(param):
    yeni_string = " ".join(param)
    
    print(yeni_string)
    
    print(type(yeni_string))
aaaa = tuple("python")

tuple_to_string(aaaa)



    










"""
Soru 3:
Parametre olarak verilen bir String'i önce List'e sonra da bu List'i Tuple'a dönnüştüren bir 
fonksiyon yazın.  Adı string_to_list_to_tuple olsun ve Tuple'ı geri dönsün.
İpuçları:
• sadece constructor metodlarını kullanın
– list()
– tuple()
"""










t = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)

"""
Soru 4:
Parametre olarak bir Tuple ve bir index alan bir fonksiyon yazın.  Fonksiyon, verilen index'te yer 
alan elemanın tüm Tuple içinde kaç sefer yer aldığını bize dönsün. Adı kac_kere_geciyor olsun.
İpuçları:
• count(
"""


""" def kac_kere_geciyor(parametre, index):
    sayac = 0
    liste = list()
    for i in parametre:
        if i == index:
            sayac += 1
    print(sayac)

kac_kere_geciyor(t,2) """





"""
Soru 5:
Tuple üzerinde dilimleme işlemleri daha önce String ve List'lerde gördüğümüz gibidir.
Elimizde şu şekilde bir Tuple olsun: tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
Aşağıdaki sorulara slicing yani dilimleme ile (index bazlı) cevap veriniz:
1. 4'cü eleman (dahil) ile 7'ci eleman (dahil) arasını bulun
2. İlk 5 elemanı bulun
3. 6'cı elemandan (dahil) sonrasını bulun
4. Tüm elemanları bulun
5. Sondan 2. elemanı bulun
6. Son 4 elemanı bulun
7. 2'ci elemandan başlayıp, 8'ci elemana kadar 2'şer atlayarak yazın
8. Tüm elemanları 3'er atlayarak yazın
9. 9'uncu elemandan, 3'cü elemana (hariç) kadar tersten yazın
10. tup'u tersten yazın
11. tup'u tersten 2'şer atlayarak yazın
12. Son elemana (hariç) kadar olan tüm elemanlarını ters index ile alınız
"""
""" tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
def bulma_fonks(tup):
    print("dort ve yedi arasi: {}".format(tup[3:7]))
    print("ilk bes elemanm: {}".format(tup[0:4]))
    print("altıncıdan sonra: {}".format(tup[5:]))
    print("tum elemanlar: {}".format(tup[::]))
    print("sondan ikinci: {}".format(tup[-2:-1:]))
bulma_fonks(tup) """







""" 
Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_sonunu_degistir 
olsun.  Bu listenin elemanları birer Tuple olsun.  Her bir tuple farklı uzunlukta olabilir. Dolayısı ile 
Listenin elemanlarının uzunlukları sabit değil.  Yazacağınız fonksiyon, Liste içindeki her bir Tuple 
elamanının son üyesini silsin, yerine karesini yazsın.
İpuçları:
• Liste yerinde değişsin, yani parametre olarak gelen orjinal liste değişsin
• Tuple'ın son elemanını index ile nasıl alacağınızı düşünün
• Listenin içinde for ile dönerken, döngüdeki elemanı değiştirseniz de liste değişmez.
• Listeyi değiştirmenin bir yolunu bulmalısınız (enumerate())
• Tuple birleştirmeye dikkat ediniz (tek elemanlı bir Tuple nasıl olur? """

""" tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]
import math
def kareler_tuple(liste):
    for index, tup in enumerate(liste):
        son_elemana_kadar = tup[:-1]
        son_eleman_karesi = tup[-1]**2
        tup = son_elemana_kadar + (son_eleman_karesi,)
        liste[index] = tup
    print(liste)
        

    
kareler_tuple(tuple_listesi) """

""" 

Soru 7:
Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_karesi_ile_degistir 
olsun.  Bu listenin elemanları birer Tuple olsun.  Her bir tuple farklı uzunlukta olabilir. Dolayısı ile 
Listenin elemanlarının uzunlukları sabit değil.  Yazacağınız fonksiyon, Liste içindeki her bir Tuple 
elamanının tüm elemanlarının yerine karelerini yazsın.
Ve yeni kareli listeyi geri dönsün.
İpuçları:
• Parametre olarak gelen orjinal liste değişmesin
• Listenin içinde for ile dönerken, döngüdeki elemanı değiştirseniz de liste değişmez """


""" 
tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]
def tuple_liste_degistir(liste):
    yeni_liste = liste.copy()
    for index, tup in enumerate(liste):
        yeni_tup = tuple()
        for t in tup:
            yeni_tup += (t**2,)
        yeni_liste[index] = yeni_tup    
    print(yeni_liste)

tuple_liste_degistir(tuple_listesi)

 """
 
 
"""  Fonksiyon bu 4 listedeki, karşılıklı elemanları alacak ve 2'şer elemanlı 2 Tuple haline getirecek. 
Ve geriye bir Dictionary dönecek.
• İlk Tuple -> (Oyuncu Adı, Karakter Adı)
• İkinci Tuple -> (Film Adı, Çekim Yılı)
Bu Dictionary'nin key'leri İlk Tuple, value'ları ise İkinci Tuple olacak.
İpuçları:
• zip(
    
# listeler:
oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma 
Stone']
karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']
filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La 
Land']
yillar = [1972, 2008, 2010, 2016]    
  """
""" oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma Stone']

karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']

filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']

yillar = [1972, 2008, 2010, 2016] 



def birlestir(oyuncu_adi, karakter_adi, film_adi, yillar):
    liste_oyuncuAdi = oyuncu_adi
    liste_karakterAdi = karakter_adi
    birlesmis_liste = zip(oyuncu_adi,karakter_adi)
    
    
    liste_film = film_adi
    liste_yil = yillar
    birlesmis_liste_2 = zip(film_adi,yillar)
    
    
    hepsi_toplam = zip(birlesmis_liste,birlesmis_liste_2)
    
    dict_toplam = dict(hepsi_toplam)
    print(dict_toplam)

    
birlestir(oyuncular,karakterler,filmler,yillar)
  """
 
 
 
""" Soru 9:
Parametre olarak bir Tuple alan bir fonksiyon yazın. Adı tuple_sirala olsun.
Parametre olarak gelen Tuple, içinde Tuple'lar tutan bir yapı olsun. Yani elemanlar da Tuple 
olsun. Ve bu elemanlardan herbiri 2 elemanlı bir Tuple olacak.
Fonksiyon, parametre olarak gelen Tuple'i sıralayacak ve sıralı bir Tuple dönecek.
Sıralama kuralı, 2. eleman olacak. Yani içerideki Tuple'ların 2. elemanına bakıp ona göre 
sıralayacak.
İpuçları:
• lambda fonksiyon kullanınız"""

tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))

def tuple_sirala(liste):
    print(sorted(liste, key=lambda x: x[1]))
    
tuple_sirala(tuple_of_tuples)
     
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 