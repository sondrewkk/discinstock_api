from fastapi import Depends
from typing import Optional

from ..util.pagination import PaginationParameters


class CommonQueryParameters:
    def __init__(
        self,
        in_stock: Optional[bool] = True,
        pagination: PaginationParameters = Depends(),
    ) -> None:
        self.in_stock = in_stock
        self.pagination = pagination

class SearchQueryParameters:
    def __init__(
        self,
        spider_name: Optional[str] = None,
    ) -> None:
        self.spider_name = spider_name
    
    def dict(self):
        return self.__dict__