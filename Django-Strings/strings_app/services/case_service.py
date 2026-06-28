"""Case conversion string methods."""

from strings_app.domain.entities import StringDemoResult
from strings_app.domain.enums import StringMethodCategory


class CaseService:
    CATEGORY = StringMethodCategory.CASE

    def run_all(self, text: str) -> list[StringDemoResult]:
        return [
            self._result("upper()", text, text.upper(), "Convert every character to uppercase"),
            self._result("lower()", text, text.lower(), "Convert every character to lowercase"),
            self._result("capitalize()", text, text.capitalize(), "First character upper, rest lower"),
            self._result("title()", text, text.title(), "Capitalize the first letter of each word"),
            self._result("swapcase()", text, text.swapcase(), "Swap uppercase and lowercase"),
            self._result("casefold()", text, text.casefold(), "Return a case-insensitive version for comparisons"),
        ]

    def _result(self, method: str, text: str, output: str, explanation: str) -> StringDemoResult:
        return StringDemoResult(
            method_name=method,
            category=self.CATEGORY,
            input_text=text,
            output=repr(output),
            code_snippet=f'"{text}".{method.rstrip("()")}()',
            explanation=explanation,
        )
