class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance (name, str) and not hasattr(self, "name") and 3 <= len(name):
            self._name = name
        else:
            raise Exception ("Invalid name value")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitor_counts = {}
        for trip in self.trips():
            if trip.visitor in visitor_counts:
                visitor_counts[trip.visitor] += 1
            else:
                visitor_counts[trip.visitor] = 1

        if not visitor_counts:
            return None

        best_visitor = max(visitor_counts, key=visitor_counts.get)
        return best_visitor
    
    @classmethod

    # def most_visited(cls):
    #     return max(cls.all, key = lambda park: park.total_visits())
    
    def most_visited(cls):
        def get_total_visits(park):
            return park.total_visits()
        
        return max(cls.all, key=get_total_visits)



class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance (start_date, str) and 7 <= len(start_date):
            self._start_date = start_date
        else:
            raise Exception ("Invalid start date value")

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and 7 <= len(end_date):
            self._end_date = end_date
        else:
            raise Exception("Invalid end date value")

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        

class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception ("Invalid name value")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        if not park.visitors():
            return 0
        return len([trip for trip in self.trips() if trip.national_park == park])