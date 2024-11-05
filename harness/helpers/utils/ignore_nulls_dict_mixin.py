from dataclasses import asdict

from dataclasses_json import DataClassJsonMixin


class NotNullAsDictMixin:
    def as_dict(self) -> dict:
        data = self.to_dict() if isinstance(self, DataClassJsonMixin) else asdict(self)
        return {key: value for key, value in data.items() if value is not None}
