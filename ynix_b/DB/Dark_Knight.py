from class_data import *
#----------------------------------------------------------------
dark_knight = Class(id=13, name="Dark Knight", dr=0, evasion=0)
# id = class ID xx = pre | 3xx = prime | 5xx = awk | 9xx = rabams
#----------------------------------------------------------------
Kriegsmesser_Training = Skill(id=13.1, class_id=13, name="Kriegsmesser Training",  acc_rate=.20,
                   hit1=Hit(damage=6.85, hit_count=9, pvp_mod=0.13))
#----------------------------------------------------------------