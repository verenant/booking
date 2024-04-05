from django.shortcuts import render , get_object_or_404
from .models import Vehicle, PostImage

def vehicle_view(request):
    vehicles = Vehicle.objects.all()
    return render(request,'vehicle.html',{
        'vehicles':vehicles
    }) # возможно "vehicles"  на post  поменять надо будет

def detail_view(request,id):
    vehicle = get_object_or_404(Vehicle,id = id )
    photos = PostImage.objects.filter(post=vehicle) # возможно post на vehicle поменять надо будет
    return render(request, "detail.html",{
        'vehicle':vehicle,
        'photos':photos,
        'id':id
    })

