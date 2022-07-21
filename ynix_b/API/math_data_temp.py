import random
#----------------------------------------------------------------
attacker = {
    'ap': 0,
    'ap_range': self.ap - 6 + random.randrange(1,12),
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
defender = {
    'dr': 0,
    'dr_rate': 0,
    'evasion': 0,
    'evasion_rate': 0,
    'dr_debuffs': 0,
    'dr_combat_buffs': 0,
    'evasion_combat_buffs': 0,
    'evasion_debuffs': 0
}
hit1 = 8.89
hit1_count = 29

t_ap = attacker['ap'] + attacker['monster_ap'] + \
    attacker['ap_combat_buffs'] - attacker['ap_debuffs']

t_acc_rate = attacker['acc_rate'] + attacker['acc_combat_buffs'] + \
    (attacker['acc'] * .21) - attacker['acc_debuffs']

t_dr = defender['dr'] + defender['dr_combat_buffs'] - defender['dr_debuffs']

t_evasion_rate = defender['evasion_rate'] + (defender['evasion'] * .21) + \
    defender['evasion_combat_buffs'] - defender['evasion_debuffs']


