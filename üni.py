YESIL="\033[32m"
KIRMIZI="\033[31m"
SIYAH_BEYAZ="\033[30;47m"
RESET="\033[0m"

print(f"{SIYAH_BEYAZ} TÜRK HAVA KURUMU ÜNİVERSİYESİ{RESET}")
print(f"{SIYAH_BEYAZ} DÖNEM NOTU HESAPLAMA {RESET}")
print("."*30)
vize=int(input("Vize notu: "))
final=int(input("Final notu: "))

ortalama=(vize * 0.4)+(final * 0.6)

if ortalama>=90:
    harf_notu="AA"

elif ortalama>=85:
    harf_notu="BA"

elif ortalama>=80:
    harf_notu="BB"

elif ortalama>=75:
    harf_notu="CB"

elif ortalama>=70:
    harf_notu="CC"

elif ortalama>=65:
    harf_notu="DC"

elif ortalama>=60:
    harf_notu="DD"

elif ortalama>=50:
    harf_notu="FD"

else:
    harf_notu="FF"
if ortalama>=45:
    print(f"{YESIL}Ortalama: {ortalama} - GEÇTİN{RESET}")
else:
    print(f"{KIRMIZI}Ortalama: {ortalama} - KALDIN{RESET}")

print(f"Ortalamanız: {ortalama}")
print(f"Harf Notunuz: {harf_notu}")
