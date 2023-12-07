from enum import Enum
from kps import KiviPaperiSakset
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class Vastustaja(Enum):
    Ihminen = 0
    YksinkertainenTekoaly = 1
    MonimutkainenTekoaly = 2

class Peligeneraattori:
    def luo_peli(vastustaja: Vastustaja) -> KiviPaperiSakset:
        if vastustaja == Vastustaja.Ihminen:
            return KPSPelaajaVsPelaaja()
        elif vastustaja == Vastustaja.YksinkertainenTekoaly:
            return KPSTekoaly(Tekoaly())
        
        return KPSTekoaly(TekoalyParannettu(10))