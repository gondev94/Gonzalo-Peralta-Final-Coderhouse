from django.contrib import messages
from django.contrib.auth.decorators import login_not_required  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileForm
from django.db.models import Q  # Para búsquedas avanzadas
from .models import Freight  # Asegúrate de tener un modelo Freight para los fletes




@login_not_required
def index(request):
    return render(request, 'core/index.html')



@login_not_required
def about(request):
    return render(request, 'core/about.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        usuario = form.get_user()
        messages.success(
            self.request, f'Inicio de sesión exitoso ¡Bienvenido {usuario.username}!'
        )
        return super().form_valid(form)


@method_decorator(login_not_required, name='dispatch')
class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('core:index')

    def get_object(self):
        
        return self.request.user

@login_not_required
def search_freight(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Freight.objects.filter(
            Q(client_name__icontains=query) | Q(package_description__icontains=query)
        )

    return render(request, 'core/search.html', {'query': query, 'results': results})
