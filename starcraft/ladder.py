class Ladder:
    def __init__(self, region: str, ladder_id: str, league_id: id, division: str, min_mmr: int, max_mmr: int):
        self.region = region
        self.id = ladder_id
        self.league_id = league_id
        self.division = division
        self.min_mmr = min_mmr
        self.max_mmr = max_mmr
