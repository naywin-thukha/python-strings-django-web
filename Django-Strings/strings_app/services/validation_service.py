"""Validation and inspection string methods."""

from strings_app.domain.entities import StringDemoResult
from strings_app.domain.enums import StringMethodCategory


class ValidationService:
    CATEGORY = StringMethodCategory.VALIDATION

    def run_all(self, text: str) -> list[StringDemoResult]:
        stripped = text.strip() or text
        return [
            self._result("isalpha()", stripped, str(stripped.isalpha()), "All characters are letters", "text.isalpha()"),
            self._result("isdigit()", stripped, str(stripped.isdigit()), "All characters are digits", "text.isdigit()"),
            self._result("isalnum()", stripped, str(stripped.isalnum()), "All characters are alphanumeric", "text.isalnum()"),
            self._result("isspace()", stripped, str(stripped.isspace()), "All characters are whitespace", "text.isspace()"),
            self._result("islower()", stripped, str(stripped.islower()), "All cased characters are lowercase", "text.islower()"),
            self._result("isupper()", stripped, str(stripped.isupper()), "All cased characters are uppercase", "text.isupper()"),
            self._result("isnumeric()", stripped, str(stripped.isnumeric()), "All characters are numeric", "text.isnumeric()"),
        ]

    def _result(self, method: str, text: str, output: str, explanation: str, code: str) -> StringDemoResult:
        return StringDemoResult(
            method_name=method,
            category=self.CATEGORY,
            input_text=text,
            output=output,
            code_snippet=code,
            explanation=explanation,
        )
