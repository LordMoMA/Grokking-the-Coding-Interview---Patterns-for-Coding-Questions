# 去过普吉岛的人员数据
users_visited_phuket = [
    {"first_name": "Sirena", "last_name": "Gross",
        "phone_number": "650-568-0388", "date_visited": "2018-03-14"},
    {"first_name": "James", "last_name": "Ashcraft",
        "phone_number": "412-334-4380", "date_visited": "2014-09-16"},
]

# 去过新西兰的人员数据
users_visited_nz = [
    {"first_name": "Justin", "last_name": "Malcom",
        "phone_number": "267-282-1964", "date_visited": "2011-03-13"},
    {"first_name": "Albert", "last_name": "Potter",
        "phone_number": "702-249-3714", "date_visited": "2013-09-11"},
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


def find_potential_customers_v3():
    return set(VisitRecord(**r) for r in users_visited_phuket) - \
        set(VisitRecord(**r) for r in users_visited_nz)
