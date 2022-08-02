from class_data import *
shai = Class(id=18, name="Shai", dr=23, evasion=0)
# ----------------------------------------------------------------
Swing_Swing = Skill(id=18_1, class_id=18, name="Swing Swing", acc_rate=.11,
                    hit1=Hit(damage=16.69, hit_count=2, pvp_mod=0.2),
                    hit2=Hit(damage=16.69, hit_count=2, pvp_mod=0.2),
                    hit3=Hit(damage=16.69, hit_count=2, pvp_mod=0.2),
                    hit4=Hit(damage=16.69, hit_count=2, pvp_mod=0.2))
# ------------------------------------------------------------------
Twirl = Skill(id=18_2, class_id= 18, name="Twirl", acc_rate=.09,
              hit1=Hit(damage=6.12, hit_count=26, pvp_mod=0.333),
              hit2=Hit(damage=6.12, hit_count=35, pvp_mod=0.333))
# -------------------------------------------------------------------
Go_Away = Skill(id=18_3, class_id=18, name="Go Away", acc_rate=.12,
                hit1=Hit(damage=7.91, hit_count=3, pvp_mod=0.1))
# ---------------------------------------------------------------------
One_Two_Three = Skill(id=18_4, class_id=18, name="One-Two-Three", acc_rate=.11,
                      hit1=Hit(damage=8.89, hit_count=29, pvp_mod=0.273),
                      hit2=Hit(damage=8.89, hit_count=27, pvp_mod=0.273),
                      hit3=Hit(damage=7.92, hit_count=37, pve_crit_rate=.5, pvp_mod=0.237))
# ---------------------------------------------------------------------
Eat_This = Skill(id=18_8, class_id=18, name="Eat This!", acc_rate=.05,
                 hit1=Hit(damage=14.52, hit_count=4, pve_crit_rate=1, pvp_mod=0.2))
# ---------------------------------------------------------------------
