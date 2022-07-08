class Listing:
    def __init__(self, queryset=None) -> None:
        self.queryset = queryset

    def range_of_objects(self, number_of_objects, end_objects):
        self.next_objects = int(end_objects)
        self.previous_objects = self.next_objects - int(number_of_objects)

    def get_objects(self):
        if self.queryset:
            queryset = self.queryset[self.previous_objects:self.next_objects]
            return self.list_objects(queryset)

    def list_objects(self, queryset):
        data = []
        if queryset:
            counter = 15
            for obj in queryset:
                counter+=1
                item = {
                    "pk": obj.pk,
                    "counter": counter,
                    "text": obj.text,
                    "translation": obj.translation,
                    "type": obj.type,
                    "review_count": obj.review_count,
                    "created": obj.created,
                }
                data.append(item)
        return data
