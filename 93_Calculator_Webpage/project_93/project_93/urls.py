
from django.contrib import admin
from django.urls import path
from project_93_app.views import add, subtract, multiply, divide

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/<int:num_1>/<int:num_2>', add),
    path('subtract/<int:num_1>/<int:num_2>', subtract),
    path('multiply/<int:num_1>/<int:num_2>', multiply),
    path('divide/<int:num_1>/<int:num_2>', divide),
    
]
