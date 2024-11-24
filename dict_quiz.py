"""
kelimeler.txt dosyasını okuyan ve buradaki kelimelerden bir dictionary yaratan bir fonksiyon 
yazın. Fonskiyon sadece 19 karakter ve üstü olan kelimeleri alsın.
Dictionary'nin key'i karakter sayısı (uzunluk) olacak, ve değeri de bu karakter sayısına sahip 
kelimeleri içeren bir liste (List) olacak.
Fonksiyon'un adı uzunluk_kelimeler olsun ve yarattığı Dictionary'yi dönsün.
İpucu:
kelimeler.txt dosyasını okumak için Kelimeler Uygulaması nı tekrar gözden 
geçirebilirsiniz."""


def uzunluk_kelimeler():
    kelimeler = open("kelimeler.txt","r")
    sozluk = dict()
    for i,satir in enumerate(kelimeler):
        satir_dizisi = satir.split()
        kelime = satir_dizisi[0]
        if len(kelime)>=19:
            if not len(kelime) in sozluk:
                sozluk[len(kelime)]  = [kelime]
            else:
                sozluk[len(kelime)].append(kelime)
    print(sozluk)     
uzunluk_kelimeler()
            
     
""":
İsimleri arac_yarat_1, arac_yarat_2 ,arac_yarat_3, arac_yarat_4 olan 4 fonksiyon yazın.
Bu fonksiyonlar aşağıdaki gibi bir dictionary yaratsın ve dict'in adı arac olsun:  {'marka': 'Ford', 
'model': 'Mustang', 'yil': 1964, 'renk': 'Kırmızı', 'fiyat': 30000, 'km': 89000, 'motor': 1.6} 

Fonksiyonlar dictionary'yi birbirinden farklı yöntemler ile yaratsın. Fonksiyonlar arac sozlüğünü 
geri dönsün.
İpuçları:
• {}
• dict()
• update( """

def arac_yarat(model,yil,renk,fiyat,km,motor):
    arac = {}
    arac["model"] = model
    arac["yil"] = yil
    arac["renk"] = renk
    arac["fiyat"] = fiyat
    arac["km"] = km
    arac["motor"] = motor
    print(arac)

arac_yarat("ford",2005,"kirmizi","159-999","299-000","2.0")


def arac_yarat(model,yil,renk,fiyat,km,motor):
    arac = {}
    arac.update({
        "model": model,
        "yil": yil,
        "renk": renk,
        "fiyat": fiyat,
        "km": km,
        "motor": motor,
         
    })
    

arac_yarat("ford",2005,"kirmizi","159-999","299-000","2.0")



"""
sAdı yeni_arac_yarat bir fonksiyon yazın. 
Bu fonksiyon Soru 3'teki fonksiyonlardan birini çağırsın 
ve arac sözlüğünü alsın.
Sonra arac sozlüğünün elemanlarını bir döngü ve update() kullanarak başka bir sözlüğe kopyalayasın.
Kopyalarken, hem orijinal elemanı alsın hem de her bir key'in sonuna "_2" eki ekleyerek yeni bir eleman olarak eklesin.
Yeni sözlüğümüzün adı yeni_arac olsun. 
Ve fonksiyon bu sözlüğü dönsün.
İpuçları:
• copy()
• update()
• items()
Örnek Çıktı:  {'marka': 'Ford', 'model': 'Mustang', 'yil': 1964, 'renk': 'Kırmızı', 'fiyat': 30000, 'km': 
89000, 'motor': 1.6, 'marka_2': 'Ford', 'model_2': 'Mustang', 'yil_2': 1964, 'renk_2': 'Kırmızı', 
'fiyat_2': 30000, 'km_2': 89000, 'motor_2': 1.6} """

def arac_yarat(model,yil,renk,fiyat,km,motor):
    global arac
    arac = {}
    arac.update({
        "model": model,
        "yil": yil,
        "renk": renk,
        "fiyat": fiyat,
        "km": km,
        "motor": motor,
         
    })


def yeni_arac_yarat():
    arac_yarat("ford",2005,"kirmizi","159-999","299-000","2.0")
    arac_2 = arac.copy()
    for item in arac.items():
        key = item[0]
        value = item[1]
        key += "_2"
        
        arac_2[key] = value
    print(arac_2)
         
    
yeni_arac_yarat()



