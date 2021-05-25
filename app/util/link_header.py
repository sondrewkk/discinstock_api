from math import floor
from .pagination import Pagination

class LinkHeader:
    def __init__(self, host: str, endpoint: str, pagination: Pagination) -> None:
        self.host = host
        self.endpoint = endpoint
        self.pagination = pagination
        self.link_header = self.__create_link_header()
    
    def get(self) -> str:
        return self.link_header

    def __create_link_header(self) -> str: 
        links = []
        links.append(self.__create_first_link())
        links.append(self.__create_last_link())

        if self.pagination.has_next():
            links.append(self.__create_next_link())
        
        if self.pagination.has_prev():
            links.append(self.__create_prev_link())

        return ",".join(links)
        
    def __create_first_link(self) -> str:
        query = f"in_stock=true&skip={ self.pagination.skip }&limit={ self.pagination.limit }"
        link = f"<https://{ self.host }/{ self.endpoint }?{ query }>; rel=\"first\""
        return link

    def __create_last_link(self) -> str:
        pages = floor(self.pagination.total / self.pagination.limit)
        skip = self.pagination.limit * pages

        query = f"in_stock=true&skip={ skip }&limit={ self.pagination.limit }"
        link = f"<https://{ self.host }/{ self.endpoint }?{ query }>; rel=\"last\""
        return link

    def __create_next_link(self) -> str:
        skip = self.pagination.skip + self.pagination.limit
        query = f"in_stock=true&skip={ skip }&limit={ self.pagination.limit }"
        link = f"<https://{ self.host }/{ self.endpoint }?{ query }>; rel=\"next\""
        return link
    
    def __create_prev_link(self) -> str:
        skip = self.pagination.skip - self.pagination.limit
        query = f"in_stock=true&skip={ skip }&limit={ self.pagination.limit }"
        link = f"<https://{ self.host }/{ self.endpoint }?{ query }>; rel=\"prev\""
        return link
    