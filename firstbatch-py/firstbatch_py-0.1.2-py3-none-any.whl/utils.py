from typing import List

PersonaMap = {
   "Skin Care":96295,
   "City travels, Sightseeing":56046,
   "NBL":17013,
   "Extreme Sports":22967,
   "Language Learning":57813,
   "Physical therapy":98670,
   "Entrepreneurship":82189,
   "Horror & Thriller":21305,
   "DeFi":45252,
   "Agriculture Industry":58980,
   "Women's Fashion":99678,
   "Hip Hop":52608,
   "Gamer":21139,
   "Crime & Mystery":91229,
   "LGBTQ+":13908,
   "Men's Fashion":48831,
   "Stock Market":23170,
   "Pharmaceutical Industry":85328,
   "Solana":70321,
   "Game Development":29393,
   "Metaverses":41009,
   "Trans Community":84778,
   "Gourmet travels":19909,
   "Metal Industry":22701,
   "Biography":60436,
   "Infrastructure":56563,
   "Beauty Mavens":64310,
   "Astronomy, Space and Rocket Science":14108,
   "Poetry":57260,
   "Cats as pets":11760,
   "Researcher":95344,
   "Vegetarian Diet":72541,
   "Protocols":73710,
   "DJ":84603,
   "Electric Cars":56251,
   "Simulation Games":45839,
   "Advertisement Design":17930,
   "Robotics":27767,
   "Dancing":61531,
   "Artist":19919,
   "Console Games":45991,
   "Producing & Live shows":99961,
   "Open Source":36017,
   "Classic":71540,
   "F1":49731,
   "DIY":20475,
   "Healthcare":96154,
   "Biotech Industry":83320,
   "Aviation Industry":43826,
   "Binance Chain":55866,
   "BBQ & Grill":65271,
   "Bookworm":84820,
   "Healing & Medicals":75350,
   "Digital Art":15715,
   "Alcohols & cocktails":50646,
   "Sports Fan":37923,
   "Fashionable":85973,
   "Polar travels":42200,
   "WNBA":78114,
   "Activism Rights":82114,
   "Memes in general":50128,
   "Marketing & Ads":58295,
   "AR & VR":83246,
   "Ethereum":75450,
   "Family Person":68954,
   "Music Guru":36744,
   "Home Improvement":73533,
   "Mindfulness":49147,
   "NBA":71749,
   "Vegan & Vegetarian":62805,
   "Artificial Intelligence":47302,
   "Engineering":63400,
   "Distributed Systems":89624,
   "FPS games":67559,
   "Currencies/Exchanges":45149,
   "Automotive Enthusiasts":85752,
   "Self-Improvement":43231,
   "Zero-knowledge protocols":24126,
   "Online Education":61213,
   "Defense":60829,
   "Religious tourism, Pilgrimage":64656,
   "Construction Industry":55342,
   "Meditation":92071,
   "Mobile Games":77239,
   "Education Oriented":73501,
   "Traveler & Wanderer":10457,
   "Adventure traveling, Skiing, Climbing":84895,
   "Machine Learning":91706,
   "UX design":48423,
   "SUVs & off-roads":14485,
   "Keyboards, Keys":99074,
   "Nail Saloons":54528,
   "App Design":38752,
   "Devops":90352,
   "Sports games":57965,
   "Daycare & Preschool":58396,
   "ESports":86710,
   "Dental Care":24821,
   "NHL":52211,
   "Internet Safety":98758,
   "Blues":36935,
   "Organic Food":48207,
   "Vintage, Classics":75449,
   "Modelling":27513,
   "Rock":66067,
   "Automative Industry":11493,
   "Driverless, Smart Cars":47486,
   "Gastronome":19457,
   "Social Sciences":78049,
   "Smart Contracts":78849,
   "Vegan Diet":92627,
   "Birds":68547,
   "High-end, Luxury":52973,
   "Developer":60580,
   "Interior Design":99372,
   "Jazz":10714,
   "Avalanche":70000,
   "Elder Care":12306,
   "Premiere League":56451,
   "RnB - Soul":98030,
   "Power & Energy Industry":74595,
   "Parenting":57139,
   "Pop":97099,
   "Healthy Living":49770,
   "History Books":73421,
   "Fitness & Exercise":69976,
   "Beauty Saloons":68386,
   "Maths":53917,
   "Real Estate":67153,
   "Pet Adoption":36262,
   "Colleges & Universities":83678,
   "Career Improvement":70228,
   "Gardening":15949,
   "Business":84856,
   "Tech Guru":86620,
   "Fish & Aquariums":80090,
   "Garden & Decoration":14424,
   "Dogecoin":13328,
   "Piercing & Tatoos":86945,
   "Painting":71155,
   "Designer":90653,
   "Hair Saloons":68780,
   "Fiction":20911,
   "Artworks":15594,
   "Childrens book":89113,
   "Animal Care - Pet Person":94294,
   "Literature & Arts":22934,
   "Musician Gears":21321,
   "Meme Lord":94951,
   "Street Fashion":62420,
   "Biology, Bioscience":80349,
   "Exchanges":81597,
   "Herbs & Supplements":16306,
   "Musician":41393,
   "Web Development":74310,
   "Caravan/Minivan":18080,
   "Legal Services":10047,
   "Beach travel, Swimming":81637,
   "Invesment & VC's":78737,
   "World Cuisine":96085,
   "Crypto Trading":52055,
   "Product Design":70421,
   "Cult movies, Classics":64860,
   "Physics":85099,
   "RPGs, MMORPGS":12192,
   "Games":54668,
   "Web3 Builder":68088,
   "Rythm Section":16289,
   "Polygon":10351,
   "Vaccines":73026,
   "Web3.0 Citizen":60843,
   "Manifacturing Industry":51535,
   "Documentary":47662,
   "Retail Industry":72136,
   "Computer Graphics":15350,
   "NFL":59728,
   "Sustainable Fashion":32793,
   "Psychological therapy":66449,
   "Movie Enthusiast":43698,
   "Spa":29749,
   "Olympics":19203,
   "Internet of Things":84224,
   "Fantasy - Sci-Fi":85622,
   "Street Food":50288,
   "Dogs as pets":19519,
   "Rap":74163,
   "Arcade":61955
}
PersonhoodMap = {
   "rank_0":232921,
   "rank_1":466418,
   "rank_2":505497,
   "rank_3":205741,
   "rank_4":699826,
   "rank_5":858617
}


class EventTypes:
    AIRDROP = "Airdrop"
    INTEREST_GATED = "Interest-gated"
    PERSONHOOD = "Personhood"
    ZK_SEGMENTATION = "ZK-Segmentation"


class StateEnum:
    PAUSED = "PAUSED"
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INIT = "INIT"


class Gate:
    def __init__(self, group_id: int):
        self.group_id = int(group_id)


class Rule:
    def __init__(self, address: str, amount: int):
        self.address = address
        self.amount = amount

    def unroll(self):
        return {"address": self.address, "amount": self.amount}


def custom_persona_query(or_groups: List, not_group: List):
    query = ""
    for i, g in enumerate(or_groups):
        query += str(g)
        if i < len(or_groups)-1:
            query += " OR "
    query += " NOT "
    query += str(not_group)
    return query


class FirstBatchEvent:
    def __init__(self, name, event_id, event_type, state=StateEnum.INIT):
        self.name: str = name
        self.event_id: str = event_id
        self.event_type: EventTypes = event_type
        self.state = state
        self.gate_id: int = 0
        self.rules = []

    def attach_gate(self, gate: Gate):
        self.gate_id = gate.group_id

    def attach_rule(self, rule: Rule):
        self.rules.append(rule.unroll())
