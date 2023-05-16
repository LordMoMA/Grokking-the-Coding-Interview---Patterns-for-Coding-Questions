class Events:
    def __init__(self, events):
        self.events = events

    def is_empty(self):
        return not bool(self.events)

    def list_events_by_range(self, start, end):
        return self.events[start:end]


events = Events([
    'Game of Thrones begins',
    'Avengers Endgame released',
    'Python 3.8 released',
    'COVID-19 declared a pandemic',
])

# 判断是否有内容，打印第二个和第三个对象
if not events.is_empty():
    print(events.list_events_by_range(1, 3))
