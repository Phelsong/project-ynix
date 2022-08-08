from class_data import *
#----------------------------------------------------------------
witch = Class(id=8, name="Witch", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Staff_Attack = Skill(id=8.1, class_id=8, name="Staff Attack",  acc_rate=.45,
                   hit1=Hit(damage=12.59, hit_count=3, pvp_mod=0.12))
#----------------------------------------------------------------