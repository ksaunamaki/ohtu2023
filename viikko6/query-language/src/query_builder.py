from matchers import And, Or, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, test = All()):
        self._matcher = And(test)

    def oneOf(self, match1, match2):
        self._matcher = Or(match1, match2)

        return self

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def build(self):
        return self._matcher