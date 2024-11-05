import random
import string


def get_random_string(length: int = 20, letters=string.ascii_lowercase) -> str:
    """Generates random string with specified length.

    @param length: returned string length.
    """
    return "".join(random.choice(letters) for _ in range(length))


def get_random_int(length: int = 10) -> int:
    """Generates random integer with specified length.

    @param length: returned int length.
    """
    minimum = pow(10, length - 1)
    maximum = pow(10, length) - 1
    return random.randint(minimum, maximum)


def get_data_product_name(prefix: str = "auto_product", length: int = 20) -> str:
    """Generates random data product name that has a specified prefix.

    @param prefix: prefix which should be a part of the string
    @param length: length of the generated part of the string
    """
    return get_random_string_with_prefix(prefix=prefix, length=length)


def get_table_name(prefix: str = "auto_table", length: int = 20) -> str:
    """Generates random table name that has a specified prefix.

    @param prefix: prefix which should be a part of the string
    @param length: length of the generated part of the string
    """
    return get_random_string_with_prefix(prefix=prefix, length=length)


def get_random_string_with_prefix(prefix: str, length: int = 20, delimiter: str = "_") -> str:
    """Generates random string that has a specified prefix.

    @param prefix: prefix which should be a part of the string
    @param length: length of the generated part of the string
    @param delimiter: delimiter that'll be used to separate words
    """
    return f"{prefix}{delimiter}{get_random_string(length=length)}"


def get_xfail_bug_reason(jira_id: str, summary: str, host: str = "xxx.atlassian.net") -> str:
    assert jira_id.startswith("NEOS")
    return f"Bug https://{host}/browse/{jira_id} {summary}"


def sanitize_name(name: str) -> str:
    return name.replace(" ", "_").lower()


def sanitize_id(identifier: str, new_char="") -> str:
    return identifier.replace("-", new_char).lower()
