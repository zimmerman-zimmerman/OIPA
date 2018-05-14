from django.conf.urls import url

import api.export.views

app_name = 'api'
urlpatterns = [
    url(r'^activities/',
        api.export.views.IATIActivityList.as_view(),
        name='activity-export'),
]
