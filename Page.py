"""
****************************************
Location of the Class Page : 
/home/ryucoder/.local/lib/python3.6/site-packages/django/core/paginator.py
****************************************
"""

class Page(collections.Sequence):

    # ************************************************************
    # Method Resolution Order of Class Page
    # Class Page
    # Class Sequence
    # Class Reversible
    # Class Collection
    # Class Sized
    # Class Iterable
    # Class Container
    # Class object
    # ************************************************************


    """
    Attributes of Class Page
    """
    # No attributes are defined inside this class

    """
    Attributes of Class Sequence
    """
    # No attributes are defined inside this class

    """
    Attributes of Class Reversible
    """
    # No attributes are defined inside this class

    """
    Attributes of Class Collection
    """
    # No attributes are defined inside this class

    """
    Attributes of Class Sized
    """
    # No attributes are defined inside this class

    """
    Attributes of Class Iterable
    """
    # No attributes are defined inside this class

    """
    Attributes of Class Container
    """
    # No attributes are defined inside this class

    """
    Methods defined in Class Page
    """

    # Method of Class Page
    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        # The object_list is converted to a list so that if it was a QuerySet
        # it won't be a database hit per __getitem__.
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]

    # Method of Class Page
    def __init__(self, object_list, number, paginator):
        self.object_list = object_list
        self.number = number
        self.paginator = paginator

    # Method of Class Page
    def __len__(self):
        return len(self.object_list)

    # Method of Class Page
    def __repr__(self):
        return '<Page %s of %s>' % (self.number, self.paginator.num_pages)

    # Method of Class Page
    def end_index(self):
        """
        Returns the 1-based index of the last object on this page,
        relative to total objects found (hits).
        """
        # Special case for the last page because there can be orphans.
        if self.number == self.paginator.num_pages:
            return self.paginator.count
        return self.number * self.paginator.per_page

    # Method of Class Page
    def has_next(self):
        return self.number < self.paginator.num_pages

    # Method of Class Page
    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    # Method of Class Page
    def has_previous(self):
        return self.number > 1

    # Method of Class Page
    def next_page_number(self):
        return self.paginator.validate_number(self.number + 1)

    # Method of Class Page
    def previous_page_number(self):
        return self.paginator.validate_number(self.number - 1)

    # Method of Class Page
    def start_index(self):
        """
        Returns the 1-based index of the first object on this page,
        relative to total objects in the paginator.
        """
        # Special case, return zero if no items.
        if self.paginator.count == 0:
            return 0
        return (self.paginator.per_page * (self.number - 1)) + 1

    """
    Methods defined in Class Sequence
    """

    # Method of Class Sequence
    def __contains__(self, value):
        for v in self:
            if v is value or v == value:
                return True
        return False

    # Method of Class Sequence
    def __iter__(self):
        i = 0
        try:
            while True:
                v = self[i]
                yield v
                i += 1
        except IndexError:
            return

    # Method of Class Sequence
    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i]

    # Method of Class Sequence
    def count(self, value):
        'S.count(value) -> integer -- return number of occurrences of value'
        return sum(1 for v in self if v is value or v == value)

    # Method of Class Sequence
    def index(self, value, start=0, stop=None):
        '''S.index(value, [start, [stop]]) -> integer -- return first index of value.
           Raises ValueError if the value is not present.

           Supporting start and stop arguments is optional, but
           recommended.
        '''
        if start is not None and start < 0:
            start = max(len(self) + start, 0)
        if stop is not None and stop < 0:
            stop += len(self)

        i = start
        while stop is None or i < stop:
            try:
                v = self[i]
                if v is value or v == value:
                    return i
            except IndexError:
                break
            i += 1
        raise ValueError

    """
    Methods defined in Class Reversible
    """

    # No methods are defined in Class Reversible

    """
    Methods defined in Class Collection
    """

    # No methods are defined in Class Collection

    """
    Methods defined in Class Sized
    """

    # No methods are defined in Class Sized

    """
    Methods defined in Class Iterable
    """

    # No methods are defined in Class Iterable

    """
    Methods defined in Class Container
    """

    # No methods are defined in Class Container

