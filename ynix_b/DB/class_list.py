#-------------------------------------------------------------------------------
class_list = {}

class Class:
    def __init__(self, id, name, dr, evasion):
        self.id = id
        self.name = name
        self.dr = dr
        self.evasion = evasion
        class_list.setdefault(self.name, self)

#------------------------------------------------------------------------------
warrior = Class(id=1, name="Warrior", dr=0, evasion=0)
ranger = Class(id=2, name="Ranger", dr=0, evasion=0)
sorceress = Class(id=3, name="Sorceress", dr=0, evasion=0)
berserker = Class(id=4, name="Berserker", dr=0, evasion=0)
tamer = Class(id=5, name="Tamer", dr=0, evasion=0)
valkyrie = Class(id=6, name="Valkyrie", dr=0, evasion=0)
wizard = Class(id=7, name="Wizard", dr=0, evasion=0)
witch = Class(id=8, name="Witch", dr=0, evasion=0)
musa = Class(id=9, name="Musa", dr=0, evasion=0)
maewha = Class(id=10, name="Maewha", dr=0, evasion=0)
kunoichi = Class(id=11, name="Kunoichi", dr=0, evasion=0)
ninja = Class(id=12, name="Ninja", dr=0, evasion=0)
dark_knight = Class(id=13, name="Dark Knight", dr=0, evasion=0)
striker = Class(id=14, name="Striker", dr=0, evasion=0)
mystic = Class(id=15, name="Mystic", dr=0, evasion=0)
lahn = Class(id=16, name="Lahn", dr=0, evasion=0)
archer = Class(id=17, name="Archer", dr=0, evasion=0)
shai = Class(id=18, name="Shai", dr=0, evasion=0)
guardian = Class(id=19, name="Guardian", dr=0, evasion=0)
hashashin = Class(id=20, name="Hashashin", dr=0, evasion=0)
nova = Class(id=21, name="Nova", dr=0, evasion=0)
sage= Class(id=22, name="Sage", dr=0, evasion=0)
corsair = Class(id=23, name="Corsair", dr=0, evasion=0)
drakania = Class(id=24, name="Drakania", dr=0, evasion=0)
