import random
agirlik_listesi=[2,4,5,6,7,8,9,3]
deger_listesi=[10,19,23,27,31,35,40,14]
populasyon=["11001000", "01110000", "10100100", "00011010", "10001001","11100000", "00101100", "01010010", "10010100", "00001011"]

def hesapla(gen):
    top_kg=0
    top_puan=0

    for i in range(8):
        if gen[i] == "1":
            top_kg=top_kg + agirlik_listesi[i]
            top_puan=top_puan + deger_listesi[i]

    return top_kg, top_puan


for tur in range(3):
    print("")
    print("1.adım elimizde olan genler değerlendiriyoruz")
    print("")
    sonuc_listesi = []

    for gen in populasyon:
        kg,puan=hesapla(gen)
        if kg > 15:
            gercek_puan=0
            durum="ağırlığı geçti (0 Puan)"
        else:
            gercek_puan=puan
            durum="Geçerli"
        print("Gen=",gen,"& Kilo=",kg, "& Puan=", puan, "=", durum)
        sonuc_listesi=sonuc_listesi + [[gercek_puan, gen]]

    for i in range(10):
        for j in range(9):
            if sonuc_listesi[j][0] < sonuc_listesi[j + 1][0]:
                gecici=sonuc_listesi[j]
                sonuc_listesi[j]=sonuc_listesi[j + 1]
                sonuc_listesi[j + 1]=gecici
    print(" ")
    print("2.Adım İyiden kötüye sıraladık şimdi  İlk 5'i seçiyoruz.")
    print("")

    ebeveynler=[]
    for i in range(5):
        secilen=sonuc_listesi[i][1]
        puan=sonuc_listesi[i][0]
        ebeveynler=ebeveynler + [secilen]
        print("Secilen", i + 1, ":", secilen, "(Puan:", puan, ")")
    print(" ")
    print("Adım 3 Çaprazlama (Crossover) yapıyoruz.")
    print("Kesme noktası 4")
    print("")

    yeni_nesil=[]

    for i in range(5):
        anne=ebeveynler[i]

        if i == 4:
            baba=ebeveynler[0]
        else:
            baba=ebeveynler[i + 1]
        parca1=anne[0:4]
        parca2=baba[4:8]
        cocuk=parca1 + parca2
        yeni_nesil=yeni_nesil + [cocuk]
        print("Eşleşme=", anne, "+", baba, "=", cocuk)
    print(" ")
    print("4.Adım Mutasyon işlemi yapıyoruz")
    print(" ")
    sansli_kisi_no=random.randint(0, 4)
    sansli_bit_no=random.randint(0, 7)

    eski_hal=yeni_nesil[sansli_kisi_no]
    bas=eski_hal[0:sansli_bit_no]
    orta=eski_hal[sansli_bit_no]
    son=eski_hal[sansli_bit_no + 1:8]

    if orta=="1":
        yeni_orta="0"
    else:
        yeni_orta="1"

    mutasyonlu_hal=bas + yeni_orta + son
    yeni_nesil[sansli_kisi_no]=mutasyonlu_hal

    print("Mutasyon gerçekleşti")
    print("Değişen Çocuk Sırası:", sansli_kisi_no + 1)
    print("Değişen bit Sırası:", sansli_bit_no + 1)
    print("Eski=",eski_hal,"= Yeni=",mutasyonlu_hal)

    populasyon=ebeveynler + yeni_nesil
    print(" ")
    print("turu tamamladık")
    print("yeni popülasyon oluşturduk")