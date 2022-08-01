from class_data import *
#----------------------------------------------------------------
Swing_Swing = Skill(id=18_1, name="Swing Swing", acc_rate=.11,
                    hit1=Hit(damage=16.69, hit_count=2, crit_rate=0),
                    hit2=Hit(damage=16.69, hit_count=2, crit_rate=0),   
                    hit3=Hit(damage=16.69, hit_count=2, crit_rate=0),
                    hit4=Hit(damage=16.69, hit_count=2, crit_rate=0))
#------------------------------------------------------------------
Skills = {
    'One_Two_Three': {
        'skill_id': 18_2,
        'skill_accuracy': .11,
        'skill_details': {
            'hit1': 889,
            'hit1_count':29,
            'hit1_crit_pve': 0,
            'hit1_crit_pvp': 0,
            'hit1_pvp_mod': .273,
            'hit2': 889,
            'hit2_count':27,
            'hit2_crit_pve': 0,
            'hit2_crit_pvp': 0,
            'hit2_pvp_mod': .273,
            'hit3': 792,
            'hit3_count': 37,
            'hit3_crit_pve': .5,
            'hit3_crit_pvp': 0,
            'hit3_pvp_mod': .237
        }
    },
    'Eat_This_VI': {
        'skill_id': 18_4,
        'skill_acc': .05,
        'skill_details': {
            'hit1': 1452,
            'hit1_count': 4,
            'hit1_crit_pve': 1,
            'hit1_crit_pvp': 0,
            'hit1_pvp_mod': .2},
    }
}
