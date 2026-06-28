from django.urls import path

from strings_app.views import demo_views

urlpatterns = [
    path("", demo_views.home, name="home"),
    path("category/<str:category>/", demo_views.category_demo, name="category"),
    path("playground/", demo_views.playground, name="playground"),
    path("catalog/", demo_views.method_catalog, name="catalog"),
    path("api/demo/", demo_views.api_demo, name="api_demo"),
]
