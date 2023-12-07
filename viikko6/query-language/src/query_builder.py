from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, test = All()):
        self._matcher = And(test)

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def build(self):
        return self._matcher