from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    LocationListCreateView,
    LocationRetrieveUpdateDestroyView
)

urlpatterns = [
    # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),

    # Location URLs
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDestroyView.as_view(), name='location-detail'),
]




# from django.contrib import admin
# from django.urls import path, include
# from .views import (
#     CompanyListCreateView,
#     CompanyRetrieveUpdateDestroyView,
#     LocationListCreateView,
#     LocationRetrieveUpdateDestroyView
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('locations_api.urls')),

#     # Company URLs
#     path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
#     path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),

#     # Location URLs
#     path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
#     path('locations/<int:pk>/', LocationRetrieveUpdateDestroyView.as_view(), name='location-detail'),
# ]




