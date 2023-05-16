
class Events:
    def __init__(self, events):
        self.events = events

    def __len__(self):
        return len(self.events)

    def __getitem__(self, index):
        return self.events[index]


events = Events([
    'Game of Thrones begins',
    'Avengers Endgame released',
    'Python 3.8 released',
    'COVID-19 declared a pandemic',
])

if events:
    print(events[1:3])
