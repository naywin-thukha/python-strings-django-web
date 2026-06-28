"""Modify and transform string methods."""

from strings_app.domain.entities import StringDemoResult
from strings_app.domain.enums import StringMethodCategory


class ModifyService:
    CATEGORY = StringMethodCategory.MODIFY

    def run_all(self, text: str) -> list[StringDemoResult]:
        old, new = self._pick_replace_pair(text)
        return [
            self._result("replace()", text, repr(text.replace(old, new)), f'Replace "{old}" → "{new}"', f'text.replace("{old}", "{new}")'),
            self._result("split()", text, repr(text.split()), "Split on whitespace", "text.split()"),
            self._result("split(',')", text, repr(text.split(",")), "Split on comma", 'text.split(",")'),
            self._result("join()", text, repr("-".join(text.split()[:3])), "Join first 3 words with '-'", '"-".join(text.split()[:3])'),
            self._result("strip()", text, repr(text.strip()), "Remove leading/trailing whitespace", "text.strip()"),
            self._result("lstrip()", text, repr(text.lstrip()), "Remove leading whitespace", "text.lstrip()"),
            self._result("rstrip()", text, repr(text.rstrip()), "Remove trailing whitespace", "text.rstrip()"),
            self._result("removeprefix()", text, repr(text.removeprefix(text[:3]) if len(text) >= 3 else text), "Remove prefix if present", f'text.removeprefix("{text[:3]}")'),
            self._result("removesuffix()", text, repr(text.removesuffix(text[-3:]) if len(text) >= 3 else text), "Remove suffix if present", f'text.removesuffix("{text[-3:]}")'),
        ]

    def _pick_replace_pair(self, text: str) -> tuple[str, str]:
        stripped = text.strip()
        if " " in stripped:
            word = stripped.split()[0]
            return word, word.upper()
        if len(stripped) >= 2:
            return stripped[0], stripped[0].upper()
        return "a", "A"

    def _result(self, method: str, text: str, output: str, explanation: str, code: str) -> StringDemoResult:
        return StringDemoResult(
            method_name=method,
            category=self.CATEGORY,
            input_text=text,
            output=output,
            code_snippet=code,
            explanation=explanation,
        )
