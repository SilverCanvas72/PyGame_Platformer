class Tilemap:
    def __init__(self,tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgird_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + 'j10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}


        