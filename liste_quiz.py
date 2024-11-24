# Soru 1:
# Parametre olarak bir liste alan bir fonksiyon yazın. Adı toplam olsun.
# Bu fonksiyon kendisine verilen listenin tüm elemanlarını toplasın ve geriye genel toplam dönsün.

listem = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def toplam(list):
    toplam = 0
    for i in list:
        toplam += i
    print(toplam)

toplam(listem)


# Soru 2:
# Parametre olarak, iç içe bir liste (nested list) alan bir fonksiyon yazın. İsmi iki_seviye_toplam
# olsun. Bu iç içe liste parametresi 2 seviyeli olsun.
# Fonksiyon bu iç içe listenin tüm iç elemanları da dahil olmak üzere, genel toplam hesaplasın ve
# dönsün.

liste = [[5, 8], [1, 4, 7], [10], 3]

def ic_ice_toplama(dizi):
    toplam = 0
    for eleman in dizi:
        if type(eleman) == list:
            for ic_eleman in eleman:
                toplam += ic_eleman
        elif str(eleman).isdigit():
            toplam += eleman
    print(toplam)

ic_ice_toplama(liste)


# Soru 3:
# Soru 2'de yazdığımız fonksiyon sadece 2 seviyeli iç içe liste alabiliyordu. Şimdi bunu jenerik bir
# hale getirelim ve her seviye iç içe listeyi toplayabilsin. İsmi ic_ice_toplam olsun.
# Fonksiyon bu iç içe listenin tüm iç elemanları da dahil olmak üzere, genel toplam hesaplasın ve
# dönsün.

def ic_ice_toplam(liste):
    toplam = 0
    for eleman in liste:
        if isinstance(eleman, list):
            toplam += ic_ice_toplam(eleman)
        else:
            toplam += eleman
    return toplam

liste = [[5, 8], [1, 4, 7, [8, 2]], [10, [-1, 2]], 3]
print(ic_ice_toplam(liste))


# Soru 4:
# Parametre olarak bir liste alan bir fonksiyon yazınız. Adı kareler olsun.
# Fonksiyonumuz listedeki her bir elemanın karesini hesaplayacak ve yeni bir listeye ekleyecek.
# Sonuçta bu yeni listeyi dönecek.

dizi = [1, 2, 3, 4, 5]

def kareler(list):
    karelerListesi = []
    for i in list:
        karelerListesi.append(i * i)
    print(karelerListesi)

kareler(dizi)


# Soru 5:
# Parametre olarak bir liste alan bir fonksiyon yazınız. Adı kareler_toplami olsun.
# Fonksiyonumuz listenin başından başlarak elemanların karelerini alacak. Bu kareleri toplayarak
# yeni bir liste oluşturacak.

dizi = [1, 2, 3, 4, 5]

def karelerListeToplami(list):
    karelerToplami = []
    for i in list:
        karelerToplami.append(i * i)  # 1, 4, 9, 16, 25
    toplamlarListesi = []
    toplam = 0
    for i in karelerToplami:
        toplam += i
        toplamlarListesi.append(toplam)  # 1, 5, 14, 30, 55
    print(toplamlarListesi)

karelerListeToplami(dizi)


# Soru 6:
# Listenin tek index'leri (1,3,5...) toplamı ile çift index'leri (0,2,4...) toplamı arasındaki farkı veren bir
# fonksiyon yazınız.

dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def tek_cift_index_farki(list):
    tekler = list[1::2]
    ciftler = list[::2]
    print(sum(ciftler) - sum(tekler))

tek_cift_index_farki(dizi)


# Soru 7:
# Parametre olarak kendisine verilen listeyi kırpan bir fonksiyon yazın.

dizi = [1, 2, 3, 4, 5, 6, 7]
print("kirpan öncesi dizi:" + str(dizi))

def kirpan(liste):
    del liste[0]
    del liste[-1]

kirpan(dizi)
print("kirpan sonrası dizi:" + str(dizi))


# Soru 8:
# Parametre olarak bir liste bir de sıralama tipi isteyen bir fonksiyon yazın. Adı sirala olsun.

dizi = [3, 2, 6, 9, 7, 1, 4, 8, 5]

def sirala(list, azalan_mi=False):
    return sorted(list, reverse=azalan_mi)

print(sirala(dizi, azalan_mi=True))
print(sirala(dizi))


# Soru 9:
# Gauss Yöntemi ile ardışık sayılar toplamını hesaplayan bir fonksiyon yazınız.

def gauss(baslangic=1, bitis=100, artis=2):
    sayilar = list(range(baslangic, bitis, artis))
    kucukten = sorted(sayilar)
    buyukten = sorted(sayilar, reverse=True)
    toplam = sum([k + b for k, b in zip(kucukten, buyukten)])
    return toplam // 2

print(gauss(20, 301, 5))


# Soru 10:
# Verilen bir listenin büyükten küçüğe sıralı olup olmadığını kontrol eden bir fonksiyon yazınız.

def azalan_sirali_mi(list):
    return list == sorted(list, reverse=True)

print(azalan_sirali_mi([9, 7, 5, 3, 1]))
print(azalan_sirali_mi([1, 2, 3, 4, 5]))
