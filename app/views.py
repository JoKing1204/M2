from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass


# Create your views here.
def list_view(
    request: HttpRequest,
) -> HttpResponse:
    teams = ["management", "procurement", "community", "documentation"]

    context = {"teams": teams}

    return render(
        request,
        "list.html",
        context,
    )


def parent(
    request: HttpRequest,
) -> HttpResponse:
    return render(
        request,
        "parent.html",
    )


@dataclass
class team:
    Tname: str
    Tdesc: str
    Tmembers: list[str]


Team_dict = {
    "management": team(
        "Management",
        "Management makes sure supplies are replinished and fully stocked, and the school is clean, and presentable to it's visitors..",
        ["Owen", "Jeremiah", "Nick", "Abigail", "Ab", "Mathew"],
    ),
    "procurement": team(
        "Procurement",
        "Procurement team's job is to keep the students fed, and the kitchen stocked with snacks and supplies. A regular refreshing budget is kept every week, and shopping trips are made by the team every Monday and Friday.",
        [
            "Adrian",
            "Bryce",
            "Big John",
            "Blaine",
            "Wyatt",
        ],
    ),
    "community": team(
        "Community",
        "Community team's job is to arrange community events for the students. These events occur every other friday, and can consist of days on the soccer field, Bowling days, Gaming Days, and many more.",
        ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
    "documentation": team(
        "Documentation",
        "Documentation team keeps the people updated on how Basecamp is doing, and what were are working on.",
        ["Conner", "Kaleigh", "Blair", "Mina", "Jay", "Joshua", "Kayleah"],
    ),
}


def teams(request: HttpRequest, team_num: str) -> HttpResponse:
    if team_num == "management":
        context1 = {"team": Team_dict["management"]}
        return render(request, "details.html", context1)
    elif team_num == "procurement":
        context2 = {"team": Team_dict["procurement"]}
        return render(request, "details.html", context2)
    elif team_num == "community":
        context3 = {"team": Team_dict["community"]}
        return render(request, "details.html", context3)
    elif team_num == "documentation":
        context4 = {"team": Team_dict["documentation"]}
        return render(request, "details.html", context4)

    else:
        return HttpResponse("no")