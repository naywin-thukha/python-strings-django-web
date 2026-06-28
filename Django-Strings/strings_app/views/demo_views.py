"""Presentation Layer — Django views."""

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from strings_app.domain.enums import StringMethodCategory
from strings_app.services.string_demo_service import StringDemoService

_service = StringDemoService()


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "strings_app/home.html",
        {
            "layers": _service.get_architecture_layers(),
            "categories": _service.get_categories(),
            "sample_strings": _service.get_sample_strings(),
        },
    )


def category_demo(request: HttpRequest, category: str) -> HttpResponse:
    cat = StringMethodCategory(category)
    text = request.GET.get("text", _service.get_sample_strings()[0])
    results = _service.run_category(cat, text)
    return render(
        request,
        "strings_app/category.html",
        {
            "category": cat,
            "results": results,
            "text": text,
            "sample_strings": _service.get_sample_strings(),
            "methods": _service.get_methods_for_category(cat),
        },
    )


def playground(request: HttpRequest) -> HttpResponse:
    text = request.GET.get("text", _service.get_sample_strings()[0])
    all_results = _service.run_all_categories(text)
    category_results = [
        (cat, all_results[cat]) for cat in _service.get_categories()
    ]
    return render(
        request,
        "strings_app/playground.html",
        {
            "text": text,
            "category_results": category_results,
            "sample_strings": _service.get_sample_strings(),
        },
    )


def method_catalog(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "strings_app/catalog.html",
        {
            "methods": _service.get_method_catalog(),
            "categories": _service.get_categories(),
        },
    )


@require_POST
def api_demo(request: HttpRequest) -> JsonResponse:
    """JSON API endpoint for live demos during presentation."""
    text = request.POST.get("text", "")
    category = request.POST.get("category", "case")
    cat = StringMethodCategory(category)
    results = _service.run_category(cat, text)
    return JsonResponse(
        {
            "input": text,
            "category": cat.value,
            "results": [
                {
                    "method": r.method_name,
                    "output": r.output,
                    "code": r.code_snippet,
                    "explanation": r.explanation,
                }
                for r in results
            ],
        }
    )
