class PaginationParameters:
    def __init__(self, limit: int = 50, skip: int = 0) -> None:
        self.limit = limit
        self.skip = skip


class Pagination:
    def __init__(self, skip: int, limit: int, total: int):
        if skip > total:
            raise SkipToLargeException

        self.skip = skip
        self.limit = limit
        self.total = total

    def has_next(self):
        has_next = self.skip + self.limit < self.total
        return has_next

    def has_prev(self):
        has_prev = self.skip - self.limit >= 0
        return has_prev


class SkipToLargeException(Exception):
    def __init__(
        self,
        message="Skip is larger than the total amout results. Cant create a valid pagination object",
    ) -> None:
        super().__init__(message)
