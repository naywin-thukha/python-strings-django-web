from dataclasses import dataclass, field

from .enums import StringMethodCategory


@dataclass(frozen=True)
class StringMethodInfo:
    """Metadata about a single string method or operation."""

    name: str
    category: StringMethodCategory
    description: str
    example_code: str
    sample_input: str = ""


@dataclass
class StringDemoResult:
    """Output of running a string operation — passed up through all layers."""

    method_name: str
    category: StringMethodCategory
    input_text: str
    output: str
    code_snippet: str
    explanation: str = ""
    extra: dict = field(default_factory=dict)
