"""String creation basics and slicing operations."""

from strings_app.domain.entities import StringDemoResult
from strings_app.domain.enums import StringMethodCategory


class CreationService:
    CATEGORY = StringMethodCategory.CREATION

    def run_all(self, text: str) -> list[StringDemoResult]:
        part_a = text.strip()[:5] if text.strip() else "Hello"
        part_b = text.strip()[5:10] if len(text.strip()) > 5 else "World"
        return [
            StringDemoResult(
                method_name="concatenation (+)",
                category=self.CATEGORY,
                input_text=text,
                output=repr(part_a + " " + part_b),
                code_snippet=f'"{part_a}" + " " + "{part_b}"',
                explanation="Join strings with the + operator",
            ),
            StringDemoResult(
                method_name="repetition (*)",
                category=self.CATEGORY,
                input_text=text,
                output=repr((part_a or "ha") * 3),
                code_snippet=f'"{part_a or "ha"}" * 3',
                explanation="Repeat a string N times with *",
            ),
            StringDemoResult(
                method_name="len()",
                category=self.CATEGORY,
                input_text=text,
                output=str(len(text)),
                code_snippet="len(text)",
                explanation="Return the number of characters",
            ),
        ]


class SlicingService:
    CATEGORY = StringMethodCategory.SLICING

    def run_all(self, text: str) -> list[StringDemoResult]:
        sample = text.strip() or "Python"
        return [
            self._result("indexing [i]", text, repr(sample[0]), "First character", "text[0]"),
            self._result("negative index", text, repr(sample[-1]), "Last character", "text[-1]"),
            self._result("slicing [start:end]", text, repr(sample[1:4] if len(sample) >= 4 else sample), "Characters 1 through 3", "text[1:4]"),
            self._result("step slicing [::n]", text, repr(sample[::2]), "Every 2nd character", "text[::2]"),
            self._result("reverse [::-1]", text, repr(sample[::-1]), "Reverse the string", "text[::-1]"),
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
