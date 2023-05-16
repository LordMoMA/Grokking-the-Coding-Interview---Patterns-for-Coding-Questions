from dataclasses import dataclass, field

tourists_visited_hk = [
    {"first_name": "Sirena", "last_name": "Gross",
        "phone_number": "650-568-0388", "date_visited": "2018-03-14"},
    {"first_name": "James", "last_name": "Ashcraft",
        "phone_number": "412-334-4380", "date_visited": "2014-09-16"},
    {"first_name": "Emma", "last_name": "Johnson",
        "phone_number": "503-221-8792", "date_visited": "2020-06-02"},
    {"first_name": "Oliver", "last_name": "Smith",
        "phone_number": "281-555-9012", "date_visited": "2019-11-30"},
    {"first_name": "Sophia", "last_name": "Lee",
        "phone_number": "786-555-2468", "date_visited": "2017-08-25"},
    {"first_name": "Benjamin", "last_name": "Brown",
        "phone_number": "408-555-7890", "date_visited": "2016-05-12"},
    {"first_name": "Isabella", "last_name": "Davis",
        "phone_number": "917-555-1234", "date_visited": "2021-02-19"},
    {"first_name": "Ethan", "last_name": "Wilson",
        "phone_number": "972-555-5678", "date_visited": "2015-07-08"},
    {"first_name": "Ava", "last_name": "Thompson",
        "phone_number": "213-555-9876", "date_visited": "2013-12-23"},
    {"first_name": "Noah", "last_name": "Martinez",
        "phone_number": "619-555-6543", "date_visited": "2018-09-10"}
]

tourists_visited_nyc = [
    {"first_name": "Justin", "last_name": "Malcom",
        "phone_number": "267-282-1964", "date_visited": "2011-03-13"},
    {"first_name": "Albert", "last_name": "Potter",
        "phone_number": "702-249-3714", "date_visited": "2013-09-11"},
    {"first_name": "Sirena", "last_name": "Gross",
        "phone_number": "650-568-0388", "date_visited": "2018-03-14"},
    {"first_name": "Oliver", "last_name": "Smith",
        "phone_number": "281-555-9012", "date_visited": "2019-11-30"},
    {"first_name": "Sophia", "last_name": "Lee",
        "phone_number": "786-555-2468", "date_visited": "2017-08-25"},
    {"first_name": "Ethan", "last_name": "Wilson",
        "phone_number": "972-555-5678", "date_visited": "2015-07-08"},
    {"first_name": "Mia", "last_name": "Anderson",
        "phone_number": "512-555-7890", "date_visited": "2017-04-05"},
    {"first_name": "Liam", "last_name": "Taylor",
        "phone_number": "714-555-1234", "date_visited": "2019-11-18"},
    {"first_name": "Charlotte", "last_name": "Wilson",
        "phone_number": "203-555-5678", "date_visited": "2016-03-22"}
]


class VisitRecord:

    def __init__(self, first_name, last_name, phone_number, date_visited):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_visited = date_visited

    def __hash__(self):
        return hash(
            (self.first_name, self.last_name, self.phone_number)
        )

    def __eq__(self, other):
        if isinstance(other, VisitRecord) and hash(other) == hash(self):
            return True
        return False

    def __repr__(self):
        return f"VisitRecord(first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, date_visited={self.date_visited})\n"


def find_potential_customers_v3():
    return set(VisitRecord(**r) for r in tourists_visited_hk) - \
        set(VisitRecord(**r) for r in tourists_visited_nyc)


@dataclass(unsafe_hash=True)
class VisitRecordDC:
    first_name: str
    last_name: str
    phone_number: str
    date_visited: str = field(hash=False, compare=False)


def find_potential_customers_v4():
    return set(VisitRecordDC(**r) for r in tourists_visited_hk) - \
        set(VisitRecordDC(**r) for r in tourists_visited_nyc)


print(find_potential_customers_v4())
