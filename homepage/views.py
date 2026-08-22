from django.shortcuts import render
from django.urls import reverse

def homepage(request):
    homepage_sections = [
        {
            "title": "Operations",
        },
        {
            "title": "Master Data",
            "cards": [
                {
                    "title": "Products",
                    "description": "Manage production items.",
                    "href": reverse("raw_material_list"),
                },
                {
                    "title": "Suppliers",
                    "description": "Manage stock suppliers.",
                    "href": reverse("supplier_list"),
                },
                {
                    "title": "Employees",
                    "description": "Manage employee information.",
                    "href": reverse("employee_list"),
                },
                {
                    "title": "Categories",
                    "description": "Manage employee information.",
                    "href": reverse("category_list"),
                },
                {
                    "title": "Admin",
                    "description": "Manage app data in the admin panel.",
                    "href": "/admin/",
                },
            ],
        },
    ]

    return render(request, "homepage.html", {
        "sections": homepage_sections
    })