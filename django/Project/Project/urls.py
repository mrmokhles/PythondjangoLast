
from django.contrib import admin
from django.urls import path,include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.SignupPage,name='signup'),

    path('login/',views.LoginPage,name='login'),

    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    
    path('saveEnquiry/',views.saveEnquiry,name='saveEnquiry'),

    path('contacts/',views.contactPage,name='contacts'),

    path('update/',views.UpdateBlog,name='update'),

    path('update/edit/<int:id>',views.EditBlog,name='edit'),

    path('up/<int:id>',views.up,name='up'),

    path('update/delete/<int:id>',views.deleteData,name='delete'),

    path('searchEmployee/',views.searchEmp,name='searchEmployee'),

    path('search/',views.searchBar,name='search'),

    path('countries_gdp_list', views.countries_gdp_list, name='countries_gdp_list'),
    path('countries_gdp_excel', views.countries_gdp_excel, name='countries_gdp_excel'),

    path('savecountries/',views.savecountries,name='savecountries'),

    path('import/',views.importExcel,name='import'),

    path('gallery', views.gallery, name="gallery"),
    
    path('cascade', views.Cascade, name="cascade"),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    
    
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

    path('json', views.json, name='json'),


    path('api',include('api.urls')),
    


 
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
