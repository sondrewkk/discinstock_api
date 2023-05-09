from humps import camelize

class Camelize:

    @staticmethod
    def to_camel(snake_str: str) -> str:
        return camelize(snake_str)
