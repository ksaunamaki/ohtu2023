from peligeneraattori import Peligeneraattori, Vastustaja
from kps import KiviPaperiSakset

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        
        peli: KiviPaperiSakset = None

        vastaus = input()

        if vastaus == "a":
            peli = Peligeneraattori.luo_peli(Vastustaja.Ihminen)
        elif vastaus == "b":
            peli = Peligeneraattori.luo_peli(Vastustaja.YksinkertainenTekoaly)
        elif vastaus == "c":
            peli = Peligeneraattori.luo_peli(Vastustaja.MonimutkainenTekoaly)
        else:
            break

        peli.tulosta_ohje()
        peli.pelaa()



if __name__ == "__main__":
    main()
