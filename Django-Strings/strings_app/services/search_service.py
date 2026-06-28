"""Search and find string methods."""

from strings_app.domain.entities import StringDemoResult
from strings_app.domain.enums import StringMethodCategory


class SearchService:
    CATEGORY = StringMethodCategory.SEARCH

    def run_all(self, text: str) -> list[StringDemoResult]:
        needle = self._pick_needle(text)
        char = needle[0] if needle else " "
        prefix = needle[:3] if len(needle) >= 3 else needle
        suffix = needle[-3:] if len(needle) >= 3 else needle

        return [
            self._result("find()", text, str(text.find(needle)), f'Index of "{needle}" (-1 if not found)', f'text.find("{needle}")'),
            self._result("index()", text, self._safe_index(text, needle), f'Index of "{needle}" (raises ValueError if missing)', f'text.index("{needle}")'),
            self._result("count()", text, str(text.count(char)), f'Count of "{char}"', f'text.count("{char}")'),
            self._result("startswith()", text, str(text.startswith(prefix)), f'Starts with "{prefix}"', f'text.startswith("{prefix}")'),
            self._result("endswith()", text, str(text.endswith(suffix)), f'Ends with "{suffix}"', f'text.endswith("{suffix}")'),
            self._result("in operator", text, str(needle in text), f'Is "{needle}" contained in text?', f'"{needle}" in text'),
        ]

    def _pick_needle(self, text: str) -> str:
        stripped = text.strip()
        if len(stripped) >= 4:
            return stripped[1:4]
        return stripped or "a"

    def _safe_index(self, text: str, needle: str) -> str:
        try:
            return str(text.index(needle))
        except ValueError:
            return "ValueError: substring not found"

    def _result(self, method: str, text: str, output: str, explanation: str, code: str) -> StringDemoResult:
        return StringDemoResult(
            method_name=method,
            category=self.CATEGORY,
            input_text=text,
            output=output,
            code_snippet=code,
            explanation=explanation,
        )
