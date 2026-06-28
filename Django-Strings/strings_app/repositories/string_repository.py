"""
Repository Layer — provides sample strings and method catalog.
No business logic here; just data access.
"""

from strings_app.domain.entities import StringMethodInfo
from strings_app.domain.enums import StringMethodCategory


class StringRepository:
    """In-memory catalog of demo strings and documented methods."""

    SAMPLE_STRINGS = [
        "  Hello, Python Strings!  ",
        "python programming",
        "user@example.com",
        "The quick brown fox jumps over the lazy dog",
        "12345",
        "Hello123World",
        "a,b,c,d,e",
        "Mississippi",
    ]

    METHOD_CATALOG: list[StringMethodInfo] = [
        # Creation
        StringMethodInfo(
            "concatenation (+)", StringMethodCategory.CREATION,
            "Join strings with the + operator",
            '"Hello" + " " + "World"',
            "Hello + World",
        ),
        StringMethodInfo(
            "repetition (*)", StringMethodCategory.CREATION,
            "Repeat a string N times with *",
            '"ha" * 3',
            "ha",
        ),
        StringMethodInfo(
            "len()", StringMethodCategory.CREATION,
            "Return the number of characters",
            "len(text)",
        ),
        # Case
        StringMethodInfo("upper()", StringMethodCategory.CASE, "Convert all characters to uppercase", "text.upper()"),
        StringMethodInfo("lower()", StringMethodCategory.CASE, "Convert all characters to lowercase", "text.lower()"),
        StringMethodInfo("capitalize()", StringMethodCategory.CASE, "First char upper, rest lower", "text.capitalize()"),
        StringMethodInfo("title()", StringMethodCategory.CASE, "Title-case each word", "text.title()"),
        StringMethodInfo("swapcase()", StringMethodCategory.CASE, "Swap upper ↔ lower", "text.swapcase()"),
        StringMethodInfo("casefold()", StringMethodCategory.CASE, "Aggressive lowercase for comparison", "text.casefold()"),
        # Search
        StringMethodInfo("find()", StringMethodCategory.SEARCH, "Return index of substring (-1 if missing)", 'text.find("fox")'),
        StringMethodInfo("index()", StringMethodCategory.SEARCH, "Like find() but raises ValueError", 'text.index("fox")'),
        StringMethodInfo("count()", StringMethodCategory.SEARCH, "Count non-overlapping occurrences", 'text.count("s")'),
        StringMethodInfo("startswith()", StringMethodCategory.SEARCH, "Check if string starts with prefix", 'text.startswith("The")'),
        StringMethodInfo("endswith()", StringMethodCategory.SEARCH, "Check if string ends with suffix", 'text.endswith("dog")'),
        StringMethodInfo("in operator", StringMethodCategory.SEARCH, "Membership test", '"fox" in text'),
        # Modify
        StringMethodInfo("replace()", StringMethodCategory.MODIFY, "Replace occurrences of a substring", 'text.replace("fox", "cat")'),
        StringMethodInfo("split()", StringMethodCategory.MODIFY, "Split into a list by delimiter", 'text.split(",")'),
        StringMethodInfo("join()", StringMethodCategory.MODIFY, "Join iterable with separator", '"-".join(["a","b","c"])'),
        StringMethodInfo("strip()", StringMethodCategory.MODIFY, "Remove leading/trailing whitespace", "text.strip()"),
        StringMethodInfo("lstrip()", StringMethodCategory.MODIFY, "Remove leading whitespace", "text.lstrip()"),
        StringMethodInfo("rstrip()", StringMethodCategory.MODIFY, "Remove trailing whitespace", "text.rstrip()"),
        StringMethodInfo("removeprefix()", StringMethodCategory.MODIFY, "Remove prefix if present", 'text.removeprefix("The ")'),
        StringMethodInfo("removesuffix()", StringMethodCategory.MODIFY, "Remove suffix if present", 'text.removesuffix(" dog")'),
        # Format
        StringMethodInfo("format()", StringMethodCategory.FORMAT, "Template formatting with placeholders", '"{} is {} years old".format(name, age)'),
        StringMethodInfo("f-string", StringMethodCategory.FORMAT, "Formatted string literals (Python 3.6+)", 'f"Hello, {name}!"'),
        StringMethodInfo("center()", StringMethodCategory.FORMAT, "Center string in given width", 'text.center(40, "-")'),
        StringMethodInfo("ljust()", StringMethodCategory.FORMAT, "Left-align in given width", 'text.ljust(30)'),
        StringMethodInfo("rjust()", StringMethodCategory.FORMAT, "Right-align in given width", 'text.rjust(30)'),
        StringMethodInfo("zfill()", StringMethodCategory.FORMAT, "Pad with zeros on the left", '"42".zfill(5)'),
        # Validation
        StringMethodInfo("isalpha()", StringMethodCategory.VALIDATION, "True if all chars are letters", "text.isalpha()"),
        StringMethodInfo("isdigit()", StringMethodCategory.VALIDATION, "True if all chars are digits", "text.isdigit()"),
        StringMethodInfo("isalnum()", StringMethodCategory.VALIDATION, "True if all chars are alphanumeric", "text.isalnum()"),
        StringMethodInfo("isspace()", StringMethodCategory.VALIDATION, "True if all chars are whitespace", "text.isspace()"),
        StringMethodInfo("islower()", StringMethodCategory.VALIDATION, "True if all cased chars are lowercase", "text.islower()"),
        StringMethodInfo("isupper()", StringMethodCategory.VALIDATION, "True if all cased chars are uppercase", "text.isupper()"),
        StringMethodInfo("isnumeric()", StringMethodCategory.VALIDATION, "True if all chars are numeric", "text.isnumeric()"),
        # Slicing
        StringMethodInfo("indexing [i]", StringMethodCategory.SLICING, "Access character at position i", "text[0]"),
        StringMethodInfo("negative index", StringMethodCategory.SLICING, "Access from the end", "text[-1]"),
        StringMethodInfo("slicing [start:end]", StringMethodCategory.SLICING, "Extract a substring", "text[4:9]"),
        StringMethodInfo("step slicing [::n]", StringMethodCategory.SLICING, "Every nth character", "text[::2]"),
        StringMethodInfo("reverse [::−1]", StringMethodCategory.SLICING, "Reverse a string", "text[::-1]"),
    ]

    def get_sample_strings(self) -> list[str]:
        return list(self.SAMPLE_STRINGS)

    def get_all_methods(self) -> list[StringMethodInfo]:
        return list(self.METHOD_CATALOG)

    def get_methods_by_category(self, category: StringMethodCategory) -> list[StringMethodInfo]:
        return [m for m in self.METHOD_CATALOG if m.category == category]

    def get_categories(self) -> list[StringMethodCategory]:
        return list(StringMethodCategory)
