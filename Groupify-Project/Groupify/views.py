# views.py

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Group, User


@csrf_exempt
def remove_user_from_group(request, group_id):
    # ... existing code for removing a user from a group ...


def get_group_by_id(request, group_id):
    # ... existing code for retrieving a group by ID ...


def get_all_groups(request):
    groups = Group.objects.all()
    response_data = {
        'groups': []
    }
    for group in groups:
        group_data = {
            'id': group.id,
            'name': group.name,
            'users': [{'id': user.id, 'name': user.name} for user in group.users.all()]
        }
        response_data['groups'].append(group_data)
    return JsonResponse(response_data)


def home(request):
    return render(request, 'Welcome.html')
