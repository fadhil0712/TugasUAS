class BentukBantal():
    love = 40
    kotak = 30
    bulat = 70

    def turun(self, x):
        if x <= self.kotak:
            return 0
        elif x >= self.love:
            return 1
        else:
            return bawah(x, self.love, self.kotak)

    def pas(self, x):
        if self.kotak < x < self.love:
            return atas(x, self.kotak, self.love)
        elif self.love < x < self.bulat:
            return bawah(x, self.love, self.bulat)
        elif x == self.love:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.love:
            return 1
        elif x <= self.bulat:
            return 0
        else:
            return up(x, self.bulat, self.love)

class isiBantal():
    busa = 50
    silikon = 30
    kapuk = 40

    def sedikit(self, x):
        if x >= self.busa:
            return 0
        elif x <= self.silikon:
            return 1
        else:
            return down(x, self.silikon, self.busa)
    
    def cukup(self, x):
        if self.busa < x < self.silikon:
            return up(x, self.busa, self.silikon)
        elif self.silikon < x < self.kapuk:
            return down(x, self.silikon, self.kapuk)
        elif x == self.silikon:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.kapuk:
            return 1
        elif x <= self.silikon:
            return 0
        else:
            return up(x, self.silikon, self.kapuk)

class WarnaBantal():
    merah = 60
    kuning = 50
    hijau = 90

    def sedikit(self, x):
        if x >= self.kuning:
            return 0
        elif x <= self.merah:
            return 1
        else:
            return down(x, self.merah, self.kuning)
    
    def cukup(self, x):
        if self.merah < x < self.kuning:
            return up(x, self.kuning, self.merah)
        elif self.merah < x < self.hijau:
            return down(x, self.merah, self.hijau)
        elif x == self.merah:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.hijau:
            return 1
        elif x <= self.merah:
            return 0
        else:
            return up(x, self.merah, self.hijau)

class jenisBantal():
    bantalSofa = 40
    bantalLeher = 60
    bantalGuling = 80
   
    def sedikit(self, x):
        if x >= self.bantalLeher:
            return 0
        elif x <= self.bantalSofa:
            return 1
        else:
            return down(x, self.bantalSofa, self.bantalLeher)
    
    def cukup(self, x):
        if self.bantalSofa < x < self.bantalLeher:
            return up(x, self.bantalSofa, self.bantalLeher)
        elif self.bantalSofa < x < self.bantalGuling:
            return down(x, self.bantalLeher, self.bantalGuling)
        elif x == self.bantalLeher:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.bantalGuling:
            return 1
        elif x <= self.bantalLeher:
            return 0
        else:
            return up(x, self.bantalLeher, self.bantalGuling)
