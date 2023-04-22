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
    # ... existing code for retrieving all groups ...


@csrf_exempt
def update_group(request, group_id):
    if request.method == 'PUT':
        # Retrieve group by ID from group model
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return JsonResponse({'error': 'Group not found'}, status=404)

        # Retrieve new name for the group from request body
        new_name = request.POST.get('name')

        # Update group name if new name is provided
        if new_name:
            group.name = new_name
            group.save()

        # Return a JSON response with the updated group data
        response_data = {
            'id': group.id,
            'name': group.name,
            'users': [{'id': user.id, 'name': user.name} for user in group.users.all()]
        }
        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def home(request):
    return render(request, 'Welcome.html')
