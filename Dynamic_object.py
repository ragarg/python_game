import Object

class DinamicObject(Object.Object):
    def __init__(self, level, x, y, image, ObjectAtrtibutes):
        Object.Object.__init__(x, y, image)
        self.BasicAttributes(self, self.LVL, self.OA)
        self.ActiveIndicator = 0

    def BasicAttributes(self, level, ObjectAtrtibutes):
        self.UPAttributes = ObjectAtrtibutes[UPAttributes]
        self.Agi = ObjectAtrtibutes[Agi]
        self.Int = ObjectAtrtibutes[Int]
        self.Str = ObjectAtrtibutes[Str]
        self.Speed = ObjectAtrtibutes[Speed] + UPSpeed(UPAgi = self.Agi)
        self.Hp = ObjectAtrtibutes[Hp] + UPHP(UPStr = self.Str)
        self.Mp = ObjectAtrtibutes[Hp] + UPMP(UPInt =self.Int)
        self.Def = ObjectAtrtibutes[Def] + UPDef(UPAgi = self.Agi)
        self.Atk = ObjectAtrtibutes[Atk] + UPAtk(UPAgi = self.Agi, UPStr = self.Str)
        self.MAtk = ObjectAtrtibutes[Matk] + UPMatk(UPInt = self.Int)
        self.LevelUP(lvlup = level)

    def LevelUP(self, lvlup = 1):
        self.UPSpeed(self.UPAttributes[Agi] * lvlup)
        self.UPAtk(self.UPAttributes[Agi] * lvlup, self.UPAttributes[Str]  * lvlup)
        self.UPDef(self.UPAttributes[Agi] * lvlup)
        self.UPHP(self.UPAttributes[Str] * lvlup)
        self.UPMP(self.UPAttributes[Int] * lvlup)
        self.UPMatk(self.UPAttributes[Int] * lvlup)
        self.Agi += self.UPAttributes[Agi] * lvlup
        self.Str += self.UPAttributes[Str] * lvlup
        self.Int += self.UPAttributes[Int] * lvlup


    def UPSpeed(self, UPAgi):
        pass

    def UPMP(self, UPInt):
        pass

    def UPHP(self, UPStr):
        pass

    def UPDef(self, UPAgi):
        pass

    def UPAtk(self, UPAgi, UPStr):
        pass

    def UPMatk(self, UPInt):
        pass

