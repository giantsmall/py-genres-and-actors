import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genres = ["Western", "Action", "Dramma"]
    for genre in genres:
        Genre.objects.create(name=genre)
    for actor_name in ["George Klooney",
                       "Kianu Reaves",
                       "Scarlett Keegan",
                       "Will Smith",
                       "Jaden Smith",
                       "Scarlett Johansson"]:
        name_parts = actor_name.split(" ")
        Actor.objects.create(first_name=name_parts[0], last_name=name_parts[1])

    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu")
    Actor.objects.filter(last_name="Reaves").update(last_name="Reeves")
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")
