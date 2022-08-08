from class_data import *
#----------------------------------------------------------------
sage = Class(id=22, name="Sage", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Kyve_Mastery = Skill(id=22.1, class_id=22, name="Kyve Mastery",  acc_rate=.2,
                   hit1=Hit(damage=10.70, hit_count=2, pvp_mod=0.3))
#----------------------------------------------------------------