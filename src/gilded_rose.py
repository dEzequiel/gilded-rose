class Gilded_Rose(object):
    
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
