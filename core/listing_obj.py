import datetime
from django.utils import dateformat, formats, timezone

class Listing:
    def __init__(self, queryset=None) -> None:
        self.queryset = list(queryset.values('pk', 'text', 'translation',
                                            'type', 'review_count', 'created'))

    def range_of_objects(self, number_of_objects, end_objects):
        self.next_objects = int(end_objects)
        self.previous_objects = self.next_objects - int(number_of_objects)

    def get_objects(self):
        if self.queryset:
            queryset = self.queryset[self.previous_objects:self.next_objects]
            self.add_counter()
            return queryset

    def formating_date(self, date):
        items = date.split(' ')[0]
        date = ''
        for d in reversed(items.split('-')):
            date+= f"{d} "
        return date

    def add_counter(self):
        counter = 15
        for obj in self.queryset:
            print(obj['created'])
            print(dateformat.format(obj['created'],'%d-%m-%Y %H:%M:%S'))
            counter+=1
            obj['counter'] = counter