from collections import namedtuple

Event = namedtuple('Event', ['title'])

events = [
    Event('Game of Thrones begins'),
    Event('Avengers Endgame released'),
    Event('Python 3.8 released'),
    Event('COVID-19 declared a pandemic'),
]

# Check if there are any events and print the second and third objects
if events:
    print(events[1:3])
