from django.contrib import admin
from django.urls import path, include
from rest_framework import schemas
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

# generator = schemas.SchemaGenerator(title='Poll API Schema')
# schema = generator.get_schema()
schema_view = get_schema_view(title='Poll API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('pollapp.urls')),
    # path('api-auth/', include('rest_framework.urls'))
    path('docs/', include_docs_urls(title='Poll API')),
    path('schema/', schema_view),
]
