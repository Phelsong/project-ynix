from class_data import *
#----------------------------------------------------------------
berserker = Class(id=4, name="Berserker", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Elastic_Force = Skill(id=4.1, class_id=4, name="Elastic Force",  acc_rate=.035,
                   hit1=Hit(damage=9.15, hit_count=1, pvp_mod=0.49),
                   hit2=Hit(damage=9.15, hit_count=1, pvp_mod=0.49),
                   hit3=Hit(damage=9.15, hit_count=2, pvp_mod=0.49),
                   hit4=Hit(damage=9.15, hit_count=2, pvp_mod=0.49))
#----------------------------------------------------------------