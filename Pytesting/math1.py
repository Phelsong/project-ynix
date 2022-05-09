# psuedo references
crit_rate = .2
crit_damage = 2
back_damage = 1.5

def effective_AP():
    total_ap = 500
    all_dr = 400
    eff_ap = (total_ap * .9) - all_dr + (total_ap * .1)
    
def hit_rate():
    min_dodge = .05
    evasion_num = 1000
    evasion_rate = .05
    effective_evasion  = (evasion_num*.195) + evasion_rate
    accuracy_num = 800
    accuracy_rate = .04
    effective_acc = (accuracy_num*.195) + accuracy_rate
    
    dodge_rate = effective_evasion - effective_acc + min_dodge
    #if over 0
    
