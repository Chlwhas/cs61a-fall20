class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def __str__(self):
        if self.pouch_contents:
            return f"The kangaroo's pouch contains: {self.pouch_contents}."
        else:
            return "The kangaroo's pouch is empty."

    def put_in_pouch(self, s):
        if s in self.pouch_contents:
            return "Object already in pouch."
        else:
            return self.pouch_contents.append(s)



