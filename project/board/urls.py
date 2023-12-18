from django.urls import path, include
# Импортируем созданное нами представление
from .views import BoardList, BoardDetail, PersonalBoard, PpostCreate, PpostUpdate


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('all/', BoardList.as_view(), name='boardlist'),
   path('post/<int:pk>', BoardDetail.as_view(), name='boarddetail'),
   path('personal', PersonalBoard.as_view(), name='personalboard'),
   path('create/', PpostCreate.as_view(), name='postedit'),
   path('update/<int:pk>', PpostUpdate.as_view(), name='postupdate'),
   # path('delete/<int:pk>', PpostDelete.as_view(), name='postdelete'),
]