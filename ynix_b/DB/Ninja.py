from class_data import *
#----------------------------------------------------------------
ninja = Class(id=12, name="Ninja", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Wind_Slash = Skill(id=12.1, class_id=12, name="Wind Slash",  acc_rate=.23,
                   hit1=Hit(damage=9.89, hit_count=1, pvp_mod=0.46))
#----------------------------------------------------------------