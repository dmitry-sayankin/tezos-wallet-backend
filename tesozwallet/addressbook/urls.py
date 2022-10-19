from django.urls import include, path

from rest_framework import routers

from addressbook.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)

urlpatterns = [
   path('', include(router.urls)),
]