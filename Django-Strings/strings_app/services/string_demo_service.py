"""
Orchestrator Service — coordinates repository and category services.
This is the main entry point for the Presentation Layer.
"""

from strings_app.domain.entities import StringDemoResult, StringMethodInfo
from strings_app.domain.enums import StringMethodCategory
from strings_app.repositories.string_repository import StringRepository
from strings_app.services.case_service import CaseService
from strings_app.services.creation_service import CreationService, SlicingService
from strings_app.services.format_service import FormatService
from strings_app.services.modify_service import ModifyService
from strings_app.services.search_service import SearchService
from strings_app.services.validation_service import ValidationService


class StringDemoService:
    """Facade that routes requests to the correct service layer module."""

    _SERVICE_MAP = {
        StringMethodCategory.CREATION: CreationService,
        StringMethodCategory.CASE: CaseService,
        StringMethodCategory.SEARCH: SearchService,
        StringMethodCategory.MODIFY: ModifyService,
        StringMethodCategory.FORMAT: FormatService,
        StringMethodCategory.VALIDATION: ValidationService,
        StringMethodCategory.SLICING: SlicingService,
    }

    def __init__(self, repository: StringRepository | None = None):
        self.repository = repository or StringRepository()

    def get_categories(self) -> list[StringMethodCategory]:
        return self.repository.get_categories()

    def get_sample_strings(self) -> list[str]:
        return self.repository.get_sample_strings()

    def get_method_catalog(self) -> list[StringMethodInfo]:
        return self.repository.get_all_methods()

    def get_methods_for_category(self, category: StringMethodCategory) -> list[StringMethodInfo]:
        return self.repository.get_methods_by_category(category)

    def run_category(self, category: StringMethodCategory, text: str) -> list[StringDemoResult]:
        service_cls = self._SERVICE_MAP[category]
        return service_cls().run_all(text)

    def run_all_categories(self, text: str) -> dict[StringMethodCategory, list[StringDemoResult]]:
        return {cat: self.run_category(cat, text) for cat in self.get_categories()}

    def get_architecture_layers(self) -> list[dict]:
        return [
            {
                "name": "Presentation Layer",
                "path": "strings_app/views/ + templates/",
                "role": "HTTP requests, HTML UI, user input",
                "color": "#3776ab",
            },
            {
                "name": "Service Layer",
                "path": "strings_app/services/",
                "role": "Business logic — runs string methods and builds results",
                "color": "#ffd43b",
            },
            {
                "name": "Repository Layer",
                "path": "strings_app/repositories/",
                "role": "Data access — sample strings and method catalog",
                "color": "#306998",
            },
            {
                "name": "Domain Layer",
                "path": "strings_app/domain/",
                "role": "Core entities, enums, and data structures",
                "color": "#ffffff",
            },
        ]
