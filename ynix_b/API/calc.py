from math_data_temp import *
# ----------------------------------------------------------------
ap_range_low = t_ap - 6
ap_range_high = t_ap + 6
human_ap = (attacker['human_damage'] * 2)
#----------------------------------------------------------------
unmitigated_damage_mean = t_ap-t_dr

#----------------------------------------------------------------
hit_damage = ((unmitigated_damage_mean if unmitigated_damage_mean > 0 else 0) * hit1 + t_ap)*.8


print("mean hit is:", hit_damage)
# print("hit range is:", hit_damage_range_low, "-", hit_damage_range_high)
#----------------------------------------------------------------
print("mean hit is:", hit_damage)
print("total possible skill hit1 damage is:", hit_damage * hit1_count)
