from class_data import *
#----------------------------------------------------------------
tamer = Class(id=5, name="Tamer", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Leaf_Slash = Skill(id=5.1, class_id=5, name="Leaf Slash",  acc_rate=.1,
                   hit1=Hit(damage=10.10, hit_count=3, pvp_mod=0.6))
#----------------------------------------------------------------