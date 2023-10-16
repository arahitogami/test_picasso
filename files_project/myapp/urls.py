from rest_framework.routers import SimpleRouter

from myapp.views import FilesViewSet

files_router = SimpleRouter()

files_router.register(
    'storage',
    FilesViewSet,
    basename='api'
)

