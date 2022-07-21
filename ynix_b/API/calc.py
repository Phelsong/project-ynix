from math_data_temp import *
# ----------------------------------------------------------------
human_damage = attacker['human_damage']
# ----------------------------------------------------------------
# Mean
damage_mean = t_ap-t_dr
human_ap_mean = 0

if damage_mean > 0:
    damage_mean += human_damage * 2
elif damage_mean < 0:
    hd_temp = (human_damage - abs(damage_mean)/2)
    human_ap_mean = hd_temp*2 + \
        abs(damage_mean)/2 if hd_temp > 0 else human_damage/2

e_ap_mean = damage_mean + human_ap_mean

hit_damage_mean = (e_ap_mean * hit1 + t_ap +
                   human_ap_mean if e_ap_mean > 0 else 0 + t_ap + human_ap_mean)*.8
# ----------------------------------------------------------------
# damage range
damage_low = (t_ap-7)-t_dr
damage_high = (t_ap+7)-t_dr
human_ap_low = 0
human_ap_high = 0

if damage_low > 0:
    damage_low += human_damage * 2
elif damage_low < 0:
    hd_temp = (human_damage - abs(damage_low)/2)
    human_ap_low = hd_temp*2 + abs(damage_low) /2 if hd_temp > 0 else human_damage/2

if damage_high > 0:
    damage_high += human_damage * 2
elif damage_high < 0:
    hd_temp = (human_damage - abs(damage_high)/2)
    human_ap_high = hd_temp*2 + abs(damage_high)/2 if hd_temp > 0 else human_damage/2

e_ap_low = damage_low + human_ap_low
e_ap_high = damage_high + human_ap_high

hit_damage_low = (e_ap_low * hit1 + t_ap + human_ap_low if e_ap_low >
                  0 else t_ap + human_ap_low)*.8

hit_damage_high = (e_ap_high * hit1 + t_ap + human_ap_high if e_ap_high >
                  0 else t_ap + human_ap_high)*.8

# ----------------------------------------------------------------
# random


def random_hits(hit1, hit1_count):
    hit1_counter = 0
    skill_hit_damage = 0
    while hit1_counter <= hit1_count:
        damage_random = (t_ap-7 + random.randrange(0, 14)) - t_dr
        human_ap_random = 0
        if damage_random > 0:
            damage_random += human_damage * 2
        elif damage_random < 0:
            hd_temp = (human_damage - abs(damage_random)/2)
            human_ap_random = hd_temp*2 + \
                abs(damage_random)/2 if hd_temp > 0 else human_damage/2

        e_ap_random = damage_random + human_ap_random
        hit_damage_random = (e_ap_random * hit1 + t_ap +
                             human_ap_random if e_ap_random > 0 else 0 + t_ap + human_ap_random)*.8
        skill_hit_damage += hit_damage_random
        print("hit", hit1_counter, "damage: ", round(hit_damage_random))
        hit1_counter += 1
    return skill_hit_damage


# ----------------------------------------------------------------
# outputs
print("mean hit is:", hit_damage_mean)
print("hit range is:", hit_damage_low, "-", hit_damage_high)
print("total hit damage:", random_hits(hit1, hit1_count))