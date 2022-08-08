from class_data import *
#----------------------------------------------------------------
guardian = Class(id=19, name="Guardian", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Frost_Strike = Skill(id=19.1, class_id=19, name="Frost Strike",  acc_rate=.20,
                   hit1=Hit(damage=8.22, hit_count=2, pvp_mod=0.30))
#----------------------------------------------------------------