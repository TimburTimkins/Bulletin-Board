from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import User, Ppost, Rresponce
from datetime import datetime
from .filter import PpostFilter
from .forms import PpostForm

class BoardList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Ppost
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_on'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'board.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'board'
    paginate_by = 2  # вот так мы можем указать количество записей на странице


class BoardDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Ppost
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'


class PersonalBoard(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Ppost
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_on'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'personal.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'board'
    # queryset = Ppost.objects.filter(author=User.name)

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PpostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# def create_post(request):  алтернативное создание поста
#     form = PpostForm()
#     if request.method == 'POST':
#         form = PpostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/all/')
#
#     return render(request, 'post_edit.html', {'form': form})


class PpostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PpostForm
    model = Ppost
    template_name = 'post_edit.html'
    success_url = reverse_lazy('boardlist')

    def post(self, request):
        if request.method == 'POST':
            form = PpostForm(request.POST or None)
            if form.is_valid():
                f = form.save(commit=False)
                f.author_id = self.request.user.id
                form.save()
                return redirect(f'/all/')

    # def author_post(request):
    #     Ppost.objects.create(author=request.user)
    #
    #     return render(request)
    #
    # """Посмотри рекуэст ниже"""

    # def form_valid(self, request):
    #     ppost = form.save(commit=False)
    #     response.user=request.name
    #     return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     project = Project.objects.get(slug=self.kwargs['project_slug'])
    #     form.instance.project = project
    #     return super(ResponseCreate, self).form_valid(form)


# Добавляем представление для изменения товара.
class PpostUpdate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PpostForm
    model = Ppost
    template_name = 'post_edit.html'
    success_url = reverse_lazy('boardlist')

    # def post(self, request):
    #     if request.method == 'POST':
    #         form = PpostForm(request.POST or None)
    #         if form.is_valid():
    #             f = form.save(commit=False)
    #             f.author_id = self.request.user.id
    #             form.save()
    #             return redirect(f'/all')


# Представление удаляющее товар.
class PpostDelete(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Ppost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('boardlist')
