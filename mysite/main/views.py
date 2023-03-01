from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import HomeSlider, HomeSliderActive, Contact_Us, Category
from .forms import Contact_Us_form
# Create your views here.


class HomeListView(ListView):
    template_name='main/index.html'

    def get(self, request):
        home_slider_active = HomeSliderActive.objects.all()[0]
        home_slider = HomeSlider.objects.all()
        category_list = Category.objects.all()
        return render(request, self.template_name, {
            'home_slider_active':home_slider_active,
            'home_slider':home_slider,
            'category_list':category_list
        })
    

def contact(request):
    if request.method == "POST":
        form = Contact_Us_form(request.POST)
        if form.is_valid():
            Contact_Us.objects.create(**form.cleaned_data)
            return redirect('contact-us')
    else:
        form = Contact_Us_form()
    return render(request, 'main/contact-us.html', {'form':form})