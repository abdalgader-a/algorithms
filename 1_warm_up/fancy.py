"""
Description: Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Complexity:
    add_item is O(1)
    get_classiness is O(n)

"""


class Classy(object):
    def __init__(self):
        self.items = []
        self.scoreDict = {'tophat': 2, 'bowtie': 4, 'monocle': 5}

    def add_item(self, s):
        self.items.append(s)

    def get_classiness(self):
        score = 0
        if len(self.items) == 0:
            return 0
        else:
            for i in self.items:
                if i in self.scoreDict.keys():
                    score += self.scoreDict[i]
            return score


# Test cases
me = Classy()

print(me.get_classiness())
me.add_item("tophat")
print(me.get_classiness())
me.add_item("bowtie")
me.add_item("jacket")
me.add_item("monocle")
print(me.get_classiness())
