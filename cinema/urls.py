from django.urls import path, include
from rest_framework import routers
from rest_framework.urls import app_name

from cinema.views import GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieViewSet, MovieSessionViewSet

router = routers.DefaultRouter()
router.register("genre", GenreViewSet)
router.register("actor", ActorViewSet)
router.register("cinema_hall", CinemaHallViewSet)
router.register("movie", MovieViewSet)
router.register("movie_session", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
