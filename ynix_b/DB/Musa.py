from class_data import *
#----------------------------------------------------------------
musa = Class(id=9, name="Musa", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Slice = Skill(id=9.1, class_id=9, name="Slice",  acc_rate=.05,
                   hit1=Hit(damage=10.60, hit_count=6, pvp_mod=0.64))
#----------------------------------------------------------------