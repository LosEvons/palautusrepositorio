from matchers import All, And, HasAtLeast, HasFewerThan, Anti, Or, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher
        
    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))
    
    def all(self):
        return QueryBuilder(And(self._matcher, All()))
    
    def anti(self, condition):
        return QueryBuilder(And(self._matcher, Anti(condition)))

    def opt(self, matcher):
        return QueryBuilder(Or(self._matcher, matcher))
        
    def build(self):
        return self._matcher