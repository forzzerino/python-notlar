""" 
Adı kume_yarat_ve_ekle olan bir fonksiyon yazın. Parametre olarak bir liste alsın.
Bu fonksiyon önce içinde aşağıdaki elemanlar olan bir Set yaratsın.
"Elma", "Armut", "Karpuz", "Çilek"
Ardından parametre olarak gelen listenin elemanlarını tek tek bu kümeye eklesin ve kümeyi geri 
dönsün.
İpuçları:
• {}
• add() """
eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']
def kume_yarat(liste):
    kume = {"elma","armut","karpuz","cilek"}
    kume.update(liste)
    print(kume)
    
kume_yarat(eklenecekler)


     
     

""" Parametre olarak iki Set alan bir fonksiyon yazın. Adı ayni_elemenlar olsun.
Fonksiyon bu iki küme içindeki ortak elemanları (kesişim kümesini) bir liste olarak dönsün.
Bu listenin elemanları küçükten büyüğe sıralı dönsün.
İpuçları:
• döngü kullanmayın
• intersection()
• sorted()
 """

def ayni_elemanlar(liste1,liste2):
    kesisimkumesi = list(liste1.intersection(liste2))
    kesisim = sorted(kesisimkumesi)
    print(kesisim)
    

set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}

ayni_elemanlar(set_1,set_2)



     
     
