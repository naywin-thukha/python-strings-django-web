"""Formatting and alignment string methods."""

from strings_app.domain.entities import StringDemoResult
from strings_app.domain.enums import StringMethodCategory


class FormatService:
    CATEGORY = StringMethodCategory.FORMAT

    def run_all(self, text: str) -> list[StringDemoResult]:
        name = text.strip().split()[0] if text.strip() else "Python"
        age = 30
        return [
            self._result(
                "format()",
                text,
                repr("{} is {} years old".format(name, age)),
                "Classic .format() template",
                '"{} is {} years old".format(name, age)',
            ),
            self._result(
                "f-string",
                text,
                repr(f"Hello, {name}!"),
                "Formatted string literal (Python 3.6+)",
                'f"Hello, {name}!"',
            ),
            self._result("center()", text, repr(text.strip().center(40, "-")), "Center in 40-char field", 'text.center(40, "-")'),
            self._result("ljust()", text, repr(text.strip().ljust(30)), "Left-align in 30-char field", "text.ljust(30)"),
            self._result("rjust()", text, repr(text.strip().rjust(30)), "Right-align in 30-char field", "text.rjust(30)"),
            self._result("zfill()", text, repr(text.strip()[:5].zfill(8) if text.strip() else "42".zfill(5)), "Zero-pad on the left", 'text.zfill(8)'),
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
