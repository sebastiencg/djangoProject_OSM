from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Route, Waypoint
import json
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html', {})
@csrf_exempt
def save_route(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        waypoints = data.get('waypoints', [])
        route_name = data.get('name', '')  # Récupérer le nom du trajet

        if not route_name:
            return JsonResponse({'status': 'failed', 'error': 'Le nom du trajet est requis.'}, status=400)

        # Créer un nouvel objet Route avec le nom spécifié
        route = Route.objects.create(name=route_name)

        # Sauvegarder les waypoints associés
        for index, point in enumerate(waypoints):
            Waypoint.objects.create(
                route=route,
                latitude=point['lat'],
                longitude=point['lng'],
                order=index
            )

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'failed', 'error': 'Requête invalide.'}, status=400)

def list_routes(request):
    routes = Route.objects.all()
    return render(request, 'list_routes.html', {'routes': routes})

def get_route(request, route_id):
    try:
        route = Route.objects.get(id=route_id)
        waypoints = route.waypoints.all()
        waypoint_list = []
        for waypoint in waypoints:
            waypoint_list.append({
                'lat': waypoint.latitude,
                'lng': waypoint.longitude,
                'order': waypoint.order
            })
        return JsonResponse({'status': 'success', 'waypoints': waypoint_list})
    except Route.DoesNotExist:
        return JsonResponse({'status': 'failed', 'error': 'Trajet introuvable'}, status=404)