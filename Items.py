


class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value



class Gold(Item):
    def __init__(self, amt):
        self.amt = 20
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
