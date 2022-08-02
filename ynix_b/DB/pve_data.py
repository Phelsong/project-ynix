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
manshaum_forest = Zone(33, "Manshaum Forest", "Kamasylvia", 410, 0, "kamasylvian")
# castle_ruins_elvia = Zone(34, "Elvia - Castle Ruins", "Serendia", 0, 0, "human")
thornwood_forest = Zone(35, "Thornwood Forest", "O'dyllita", 460, 0, "kamasylvian")
elvia_saunels = Zone(43, "Elvia - Saunels", "Calpheon", 700, 0, "demihuman")
tunkuta = Zone(44, "Turos", "O'dyllita", 465, 0, "kamasylvian")
elvia_giants = Zone(54, "Elvia - Giants", "Calpheon", 750, 0, "human")
gyfin_underground = Zone(59, "Gyfin Underground", "Kamasylvia", 450, 0, "kamasylvian")

