# -------------------------------------------------------------------------------
from ast import If
from typing import Optional


class_list = {}
#class_list var for seed function

class Class:
    def __init__(self, id, name, dr, evasion):
        self.id = id
        self.name = name
        self.dr = dr
        self.evasion = evasion
        self.species = "human"
        class_list.setdefault(self.name, self)


class Skill:
    def __init__(self, id, name, acc_rate, hit1, hit2, hit3, hit4, hit5, hit6, reduced_on_cd: Optional(bool) = False):
        self.id = id
        self.name = name
        self.acc_rate = acc_rate
        self.hit1 = hit1
        self.hit2 = hit2 if hit2 is not None else None
        self.hit3 = hit3 if hit3 is not None else None
        self.hit4 = hit4 if hit4 is not None else None
        self.hit5 = hit5 if hit5 is not None else None
        self.hit6 = hit6 if hit6 is not None else None
        self.reduced_on_cd = reduced_on_cd


class Hit:
    def __init__(self, damage, hit_count, crit_rate, pvp_mod):
        self.damage = damage
        self.hit_count = hit_count
        self.crit_rate = crit_rate
        self.pvp_mod = pvp_mod


# ------------------------------------------------------------------------------
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
sage = Class(id=22, name="Sage", dr=0, evasion=0)
corsair = Class(id=23, name="Corsair", dr=0, evasion=0)
drakania = Class(id=24, name="Drakania", dr=0, evasion=0)



