from django.conf.urls import url
from quiz import views
urlpatterns = [
	url(r"^$", views.start),
	url(r"^quiz/[0-9]+/$", views.quiz),
	url(r"^quiz/[0-9]+/question/[0-9]+/$", views.question),
	url(r"^quiz/[0-9]+/completed/$", views.results),
]