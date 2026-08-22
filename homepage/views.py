from django.shortcuts import render

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
                    "href": "/raw_material",
                },
                {
                    "title": "Suppliers",
                    "description": "Manage stock suppliers.",
                    "href": "/supplier",
                },
                {
                    "title": "Employees",
                    "description": "Manage employee information.",
                    "href": "/employees/",
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