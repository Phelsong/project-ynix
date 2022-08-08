from class_data import *
#----------------------------------------------------------------
mystic = Class(id=15, name="Mystic", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Heavy_Fist = Skill(id=15.1, class_id=15, name="Heavy Fist",  acc_rate=.20,
                   hit1=Hit(damage=8.09, hit_count=2, pvp_mod=0.23))
#----------------------------------------------------------------