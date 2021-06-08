class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state = self._state + 1

    def is_ripe(self):
        if self._state == 3:
            return True
        else:
            return False

class TomatoBush:
    def __init__(self, cnt):
        self.tomatoes = []
        for i in range(cnt):
            tomato = Tomato(i)
            self.tomatoes.append(tomato)

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if tomato.is_ripe() == False:
                return False
        return True

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe() == True:
            self._plant.give_away_all()
        else:
            print("ne sozreli")

    @staticmethod
    def knowledge_base():
        print("abc")

Gardener.knowledge_base()
great_tomato_bush = TomatoBush(4)
gardener = Gardener('Emilio', great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()