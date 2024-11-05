from typing import Any


class AttributeMixin:
    def with_attribute(self, attr: Any, value: Any) -> "AttributeMixin":
        if attr in self.__dict__:
            self.__setattr__(attr, value)
        return self

    def attrs(self) -> list:
        return list(self.__dict__.keys())
