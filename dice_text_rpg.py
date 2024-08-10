
def oyun_bitme():
    if rakip_can <= 0:
        altin = random.randint(1,100)
        print("Tebrikler! Rakibi katlettin!")
        print(f"Ödül olarak {altin} altın kazandın!")
    if karakter_can <= 0:
        altin = random.randint(1,100)
        print("Rakip seni katletti!")
        print(f"Üstündeki {altin} altını rakip aldı...")
import time
import math
import random
karakter_can = 100
rakip_can = 100
savas = int(input("Karşında bir rakip çıktı! Savaşacak mısın, Kaçacak mısın? (Savaşmak için: 1, Kaçmak için: 0)"))
if savas == 1:
    print("Nasıl bir strateji düşünüyorsun?")
    time.sleep(1)
    print("Eğer saklanmayı tercih edersen, rakip'ten saklanırsın ve hp regen şansın olur.")
    time.sleep(1)
    print("Eğer agresif tercih edersen, dmg range'in artar ve daha çok vurma ihtimalin olur.")
    time.sleep(1)
    print("Eğer defansif tercih edersen, rakibin dmg range'i azalır ve daha az hasar alma ihtimalin olur.")
    time.sleep(1)
    while karakter_can and rakip_can >=0:
        strateji = int(input("Saldırı stratejin hangisi? (Saklanma 1, Agresif 2, Defansif 3): "))
        liste = [1,2,3]
        if strateji == 1:
            kacak = random.randint(1,12)
            print("Demek saklanmayı tercih ettin! Zarın atılıyor!")
            time.sleep(1)
            print(f"Zarın {kacak} geldi!")
            if kacak <6:
                kacak_hasari = random.randint(1,10)
                karakter_can -=kacak_hasari
                print(f"Zarın 6 dan küçük olduğu için {kacak_hasari} hasar yiyorsun.")
                print(f"Yeni canın {karakter_can}!")
                oyun_bitme()
            else:
                hp_regen = random.randint(1,10)
                karakter_can +=hp_regen
                print(f"Zarın 6 dan büyük olduğu için saklandığın yerde seni bulamadılar!")
                print(f"{hp_regen} can yeniledin! Yeni canın {karakter_can}!")
        if strateji == 2:
            print("Demek agresifliği tercih ettin! Zarın atılıyor!")
            agresif = random.randint(1,12)
            time.sleep(1)
            print(f"Zarın {agresif} geldi!")
            if agresif <6:
                agresif_hasari = random.randint(1,10)
                rakip_hasari = random.randint(1,10)
                karakter_can -= rakip_hasari
                rakip_can -= agresif_hasari
                print(f"Zarın 6'dan küçük geldiği için 1 ve 10 arasından {agresif_hasari} hasar vurdun!")
                print(f"Rakip sana {rakip_hasari} hasar vurdu!")
                time.sleep(1)
                print(f"Senin canın {karakter_can}, Rakibin canı {rakip_can}.")
                oyun_bitme()
            else:
                agresif_hasari = random.randint(5,15)
                rakip_hasari = random.randint(1,10)
                karakter_can -= rakip_hasari
                rakip_can -= agresif_hasari
                print(f"Zarın 6'dan büyük geldiği için 5 ve 15 arasından {agresif_hasari} hasar vurdun!")
                print(f"Rakip sana {rakip_hasari} hasar vurdu!")
                time.sleep(1)
                print(f"Senin canın {karakter_can}, Rakibin canı {rakip_can}.")
                oyun_bitme()
        if strateji == 3:
            print("Demek defansifliği tercih ettin! Zarın atılıyor!")
            defansif = random.randint(1,12)
            time.sleep(1)
            print(f"Zarın {defansif} geldi!")
            if defansif <6:
                defansif_hasari = random.randint(1,10)
                rakip_hasari = random.randint(1,10)
                karakter_can -= rakip_hasari
                rakip_can -= defansif_hasari
                print(f"Rakibe {defansif_hasari} hasar vurdun!")
                print(f"Zarın 6'dan küçük geldiği için 1-10 arasından rakip sana {rakip_hasari} hasar vurdu!")
                time.sleep(1)
                print(f"Senin canın {karakter_can}, Rakibin canı {rakip_can}.")
                oyun_bitme()
            else:
                defansif_hasari = random.randint(1,10)
                rakip_hasari = random.randint(1,5)
                karakter_can -= rakip_hasari
                rakip_can -= defansif_hasari
                print(f"Sen rakibe {defansif_hasari} hasar vurdun!")
                print(f"Zarın 6'dan büyük geldiği için rakip sana 1 ve 5 arasından {rakip_hasari} hasar vurdu!")
                time.sleep(1)
                print(f"Senin canın {karakter_can}, Rakibin canı {rakip_can}.")
                oyun_bitme()
        if strateji not in liste:
            print("Geçersiz strateji seçimi! Lütfen 1, 2 veya 3 girin.")
            continue  
if savas == 0:
    print("Seni korkak! Demek kaçıyorsun ha! Neyse zaten senden de bu beklenirdi..")
    time.sleep(1)
    altin = random.randint(1,100)
    print(f"{altin} altınını almadan göndermem ama!")