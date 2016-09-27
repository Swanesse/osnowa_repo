from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #adres URL panelu administracyjnego
    url(r'^admin/', include(admin.site.urls)),
    #przekazanie adresów URL z osnowy_app tutaj (do osnowy)
    url(r'', include('osnowa_app.urls'))
]
