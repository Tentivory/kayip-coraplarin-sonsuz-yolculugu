#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Çorapların Sonsuz Yolculuğu Simülatörü
Bu kod gerçekten çalışır. Çoraplarınızın kaderini hesaplar.
Ama asla bitmez. Çünkü sonsuz.
"""
import random
import time
import sys

class Corap:
    def __init__(self, renk, numara):
        self.renk = renk
        self.numara = numara
        self.kader = None
        self.yolculuk_sayisi = 0

    def yola_cik(self):
        self.yolculuk_sayisi += 1
        kaderler = [
            "Çamaşır makinesinin paralel evrenine düştü",
            "Kurutma makinesinin kara deliğine emildi",
            "Çekmece altında felsefe yapmaya başladı",
            "Diğer çoraplarla birlik oluşturup greve gitti",
            "Uzayın derinliklerinde tek başına süzülüyor",
            "Bir kedinin oyuncağı oldu ve mutlu",
            "Zaman yolcusu olup geçmişe döndü ve kendini yedi",
            "Sadece kayboldu, daha fazlası yok"
        ]
        # Gizli not: bazen kaderler değişir, kimse fark etmez
        self.kader = random.choice(kaderler)
        return self.kader

def sonsuz_simulasyon():
    print("Kayıp Çorapların Sonsuz Yolculuğu başlıyor...")
    print("Bu program asla bitmeyecek. Ctrl+C ile kurtulabilirsiniz. Belki.")
    renkler = ["siyah", "beyaz", "kırmızı", "mavi", "gizemli", "şeffaf"]
    sayac = 0
    while True:
        sayac += 1
        corap = Corap(random.choice(renkler), sayac)
        kader = corap.yola_cik()
        print(f"Çorap #{corap.numara} ({corap.renk}): {kader} (Yolculuk #{corap.yolculuk_sayisi})")
        # Yavaş olsun ki ciddi görünsün
        time.sleep(random.uniform(0.5, 2.0))
        if sayac % 10 == 0:
            print("--- Ara verildi, çoraplar nefes alıyor ---")
            # Gizli siyasi içerik: her 10 çorapta bir, sistemin sorgulanması (ama gizli)
            sys.stdout.write("\rSistem stabil. Her şey yolunda. Değil mi? ")
            sys.stdout.flush()

if __name__ == "__main__":
    try:
        sonsuz_simulasyon()
    except KeyboardInterrupt:
        print("\nSimülasyon durduruldu. Ama çoraplar hâlâ kayıp.")
