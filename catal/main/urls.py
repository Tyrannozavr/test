from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:post_slug>/', show_post, name='post'),
    path('stock/', stock, name='stock'),
    path('price/', price, name='price'),
    path('calculator/', calculator, name='calculator'),
    #path('catalog/', catalog, name='catalog'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('catalog/brands/', brand_list, name='brands'),
    path('catalog/marks_unsorted/', marks_list_unsorted, name='brands'),
    path('catalog/marks_sorted/', marks_list_sorted, name='brands'),
    path('catalog/<slug:catalyst_slug>/', show_catalyst, name='catalyst'),
]