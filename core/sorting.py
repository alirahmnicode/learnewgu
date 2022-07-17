class SortObject:
    def __init__(self, request, queryset) -> None:
        self.request = request
        self.queryset = queryset

    def sort(self):
        sort = self.sort_by()
        if sort:
            return self.queryset.order_by(sort)
        else:
            return self.queryset


    def sort_by(self):
        return self.request.get('sort_by')

    @property
    def qs(self):
        return self.sort()
        