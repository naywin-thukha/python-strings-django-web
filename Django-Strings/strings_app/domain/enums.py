from enum import Enum


class StringMethodCategory(str, Enum):
    """Groups Python string methods by purpose for the presentation."""

    CREATION = "creation"
    CASE = "case"
    SEARCH = "search"
    MODIFY = "modify"
    FORMAT = "format"
    VALIDATION = "validation"
    SLICING = "slicing"

    @property
    def label(self) -> str:
        return {
            "creation": "String Creation & Basics",
            "case": "Case Conversion",
            "search": "Search & Find",
            "modify": "Modify & Transform",
            "format": "Formatting & Alignment",
            "validation": "Validation & Inspection",
            "slicing": "Slicing & Indexing",
        }[self.value]

    @property
    def description(self) -> str:
        return {
            "creation": "How strings are created and combined in Python",
            "case": "Methods that change letter casing",
            "search": "Methods to locate substrings and patterns",
            "modify": "Methods that change string content",
            "format": "Methods for layout, padding, and templates",
            "validation": "Methods that inspect string content",
            "slicing": "Accessing parts of a string with indexes and slices",
        }[self.value]
