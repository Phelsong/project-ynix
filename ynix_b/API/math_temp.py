Attacker = {
    'ap': 0,
    'aap': 0,
    'acc': 0,
    'acc_rate': 0,
    'monster_ap': 0,
    'kama_damage': 0,
    'demi_damage': 0,
    'human_damage': 0,
    'crit_damage': 0,
    'back_damage': 0,
    'ap_combat_buffs': 0,
    'ap_debuffs': 0,
    'acc_combat_buffs': 0,
    'acc_debuffs': 0,
}
Defender = {
    'dr': 0,
    'dr_rate': 0,
    'evasion': 0,
    'evasion_rate': 0,
    'dr_debuffs': 0,
    'dr_combat_buffs': 0,
    'evasion_combat_buffs': 0,
    'evasion_debuffs': 0
}

t_ap = attacker_ap + monster_ap + (human_damage * 1.6) + ap_combat_buffs - ap_debuffs

t_acc_rate = acc_rate + acc_combat_buffs + (acc * .21) - acc_debuffs

t_dr = dr + dr_combat_buffs - dr_debuffs

t_evasion_rate = evasion_rate + (evasion * .21) + evasion_combat_buffs - evasion_debuffs

unmitigated_damage = t_ap-t_dr
hit_damage = unmitigated_damage * hit1 + dr

print("mean hit is:", hit_damage)
print("total possible skill hit1 damage is:", hit_damage * hit1_count)