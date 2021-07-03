from django.shortcuts import render
from django.views.generic import View
from .models import Trolleibus,Taxi,Sprinter

class MainView(View):
    def get(self, request):
        return render(request, template_name="main/main.html")


class TrolleibusesView(View):
    trolleibus=Trolleibus.objects.all()
    def get(self, request):
        return render(request, template_name="main/trolleibuses.html",context={'trolleibuss':self.trolleibus})

class Trolleibus1View(View):
    trolleibus=Trolleibus.objects.get(id=1)
    def get(self, request):
        return render(request, template_name="main/trolleibus1.html",context={'trolleibuss':self.trolleibus})
class Trolleibus2View(View):
    trolleibus=Trolleibus.objects.get(id=2)
    def get(self, request):
        return render(request, template_name="main/trolleibus2.html",context={'trolleibuss':self.trolleibus})
class Trolleibus3View(View):
    trolleibus=Trolleibus.objects.get(id=3)
    def get(self, request):
        return render(request, template_name="main/trolleibus3.html",context={'trolleibuss':self.trolleibus})
class Trolleibus4View(View):
    trolleibus=Trolleibus.objects.get(id=4)
    def get(self, request):
        return render(request, template_name="main/trolleibus4.html",context={'trolleibuss':self.trolleibus})



class TaxiesView(View):
    taxi=Taxi.objects.all()
    def get(self, request):
        return render(request, template_name="main/taxies.html",context={'taxis':self.taxi})

class Taxi1View(View):
    taxi=Taxi.objects.get(id=1)
    def get(self, request):
        return render(request, template_name="main/taxi1.html",context={'taxi':self.taxi})
class Taxi2View(View):
    taxi=Taxi.objects.get(id=2)
    def get(self, request):
        return render(request, template_name="main/taxi2.html",context={'taxi':self.taxi})
class Taxi3View(View):
    taxi=Taxi.objects.get(id=3)
    def get(self, request):
        return render(request, template_name="main/taxi3.html",context={'taxi':self.taxi})
class Taxi4View(View):
    taxi=Taxi.objects.get(id=4)
    def get(self, request):
        return render(request, template_name="main/taxi4.html",context={'taxi':self.taxi})



class SprinteresView(View):
    sprinter=Sprinter.objects.all()
    def get(self, request):
        return render(request, template_name="main/sprinteres.html",context={'sprinters':self.sprinter})

class Sprinter1View(View):
    sprinter=Sprinter.objects.get(id=1)
    def get(self, request):
        return render(request, template_name="main/sprinter1.html",context={'sprinter':self.sprinter})
class Sprinter2View(View):
    sprinter=Sprinter.objects.get(id=2)
    def get(self, request):
        return render(request, template_name="main/sprinter2.html",context={'sprinter':self.sprinter})
class Sprinter3View(View):
    sprinter=Sprinter.objects.get(id=3)
    def get(self, request):
        return render(request, template_name="main/sprinter3.html",context={'sprinter':self.sprinter})
class Sprinter4View(View):
    sprinter=Sprinter.objects.get(id=4)
    def get(self, request):
        return render(request, template_name="main/sprinter4.html",context={'sprinter':self.sprinter})




