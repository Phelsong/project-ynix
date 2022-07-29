#----------------------------------------------------------------------------
zone_list = {}
class Zone:
    def __init__(self, id, name, region, dr, evasion, mob_type):
        self.id = id
        self.name = name
        self.region = region
        self.dr = dr
        self.evasion = evasion
        self.mob_type = mob_type
        zone_list.setdefault(self.name, self)

#--------------------------------------------------------------------------
manshaum_forest = Zone(33, "manshaum_forest", "kamasylvia", 410, 0, "kamasylvian")
# castle_ruins_elvia = Zone(34, "castle_ruins_elvia", "serendia", 0, 0, "human")
thornwood_forest = Zone(35, "thornwood_forest", "o'dyllita", 460, 0, "kamasylvian")
elvia_saunels = Zone(43, "elvia_saunels", "calpheon", 700, 0, "demihuman")
tunkuta = Zone(44, "turos", "o'dyllita", 465, 0, "kamasylvian")
elvia_giants = Zone(54, "elvia_giants", "calpheon", 750, 0, "human")
gyfin_underground = Zone(59, "gyfin_underground", "kamasylvia", 450, 0, "kamasylvian")

