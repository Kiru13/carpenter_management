
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from crapp.views import kitchendetails_view,cart_view,doors_view,edit_door_system,edit_system, home_view,login_view,logout_view,register_view,handle_view,cart_view,halldetails_view,bedroomdetails_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('handles/',handle_view),
    path('doors/',doors_view),
    path('cart/<int:id>',cart_view),
    path('k_details/<int:id>',kitchendetails_view),
    path('b_details/<int:id>',bedroomdetails_view),
    path('h_details/<int:id>',halldetails_view),

    path('', RedirectView.as_view(url='/home')),

    path('handles/<int:id>/edit', edit_system, name='edit_system'),
    path('doors/<int:id>/edit', edit_door_system, name='edit_door_system'),
    

]
