from django.shortcuts import render
from travelloapp.models import Destination

# Create your views here.
def index(request):
    dests= Destination.objects.all()
    return render(request,"index.html",{'dests': dests})
    # dest1= Destination()
    # dest1.id=1
    # dest1.name="Mumbai"
    # dest1.img= "destination_1.jpg"
    # dest1.desc= "City that never sleeps."
    # dest1.price= 650
    # dest1.offer= False

    # dest2= Destination()
    # dest2.id=2
    # dest2.name="Hyderbad"
    # dest2.img= "destination_2.jpg"
    # dest2.desc= "Biriyani City."
    # dest2.price= 400
    # dest2.offer= False

    # dest3= Destination()
    # dest3.id=3
    # dest3.name="Manali"
    # dest3.img= "destination_3.jpg"
    # dest3.desc= "City with adventure activities."
    # dest3.price= 750
    # dest3.offer= True

    