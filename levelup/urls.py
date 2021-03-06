from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views import Games, GameTypes, Events, Profile


# if did not have slash is false i would have to manually place it in the url
# router is an instance of the default router class. default router class is built in to the django framework
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypes, 'gametype')
# r symbolizes is telling python it is a regex string
# games on the left is what the url is suppose to be therefore /games
#game on the right is the singular version of the route which tells django what the query/model will be to use for that route
router.register(r'games', Games, 'game')
router.register(r'events', Events, 'event')
router.register(r'profile', Profile, 'profile')
#url patterns even though registered we have to add to the url patterns to hit the routes. so on the backend using localhost8000
urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('levelupreports.urls')),
]
