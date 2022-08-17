# --------------------------------------------------------------------------------
class Class:
    def __init__(self, id, name, dr, evasion):
        self.id = id
        self.name = name
        self.dr = dr
        self.evasion = evasion
        self.species = "human"
        class_list.setdefault(self.name, self)
        # self.skills = {}


# --------------------------------------------------------------------------------
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
class Skill:
    def __init__(
        self,
        id,
        class_id,
        name,
        acc_rate,
        hit1,
        hit2=None,
        hit3=None,
        hit4=None,
        hit5=None,
        hit6=None,
        reduced_on_cd=False,
    ):
        self.id = id
        self.class_id = class_id
        self.name = name
        self.acc_rate = acc_rate
        self.hit1 = hit1.__dict__ if hit1 is not None else None
        self.hit2 = hit2.__dict__ if hit2 is not None else None
        self.hit3 = hit3.__dict__ if hit3 is not None else None
        self.hit4 = hit4.__dict__ if hit4 is not None else None
        self.hit5 = hit5.__dict__ if hit5 is not None else None
        self.hit6 = hit6.__dict__ if hit6 is not None else None
        self.reduced_on_cd = reduced_on_cd
        skill_list.setdefault(self.name, self)


class Hit:
    def __init__(self, damage, hit_count, pvp_mod, pve_crit_rate=0, pvp_crit_rate=0):
        self.damage = damage
        self.hit_count = hit_count
        self.pvp_mod = pvp_mod
        self.pve_crit_rate = pve_crit_rate
        self.pvp_crit_rate = pvp_crit_rate


# ------------------------------------------------------------------------------

class_list = {}
skill_list = {}
import Archer
import Berserker
import Corsair
import Dark_Knight
import Drakania
import Guardian
import Hashashin
import Kuno
import Lahn
import Maewha
import Musa
import Mystic
import Ninja
import Nova
import Ranger
import Sage
import Shai
import Sorceress
import Striker
import Tamer
import Valkyrie
import Warrior
import Witch
import Wizard

# list variables are for seed functions
# -------------------------------------------------------------------------------
