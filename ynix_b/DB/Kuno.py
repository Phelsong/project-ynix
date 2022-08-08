from class_data import *
#----------------------------------------------------------------
kunoichi = Class(id=11, name="Kunoichi", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Wind_Slash = Skill(id=11.1, class_id=11, name="Wind Slash",  acc_rate=.23,
                   hit1=Hit(damage=9.89, hit_count=2, pvp_mod=0.52))
#----------------------------------------------------------------