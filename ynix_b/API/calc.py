from math_data_temp import *
#----------------------------------------------------------------

human_ap = (attacker['human_damage'] * 2)


unmitigated_damage = t_ap-t_dr 


hit_damage = unmitigated_damage * hit1 + defender['dr']

print("mean hit is:", hit_damage)
print("total possible skill hit1 damage is:", hit_damage * hit1_count)