class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        tuotteet = []
        poistettu_yksi = False

        for t in self._tuotteet:
            if t.id == tuote.id:
                if not poistettu_yksi:
                    poistettu_yksi = True
                    continue

            tuotteet.append(tuote)

        self._tuotteet = tuotteet

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
