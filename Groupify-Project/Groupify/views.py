from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Group, User


@csrf_exempt
def remove_user_from_group(request, group_id):
    if request.method == 'POST':
        # Retrieve user ID from request body
        user_id = request.POST.get('user_id')

        # Retrieve group by ID from group model
        try:
            group = Group.objects.get(pk=group_id)
        except Group.DoesNotExist:
            return JsonResponse({'error': 'Group not found'}, status=404)

        # Retrieve user by ID from the group's list of users
        try:
            user = group.users.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found in group'}, status=404)

        # Remove user from the group's list of users
        group.users.remove(user)

        return JsonResponse({'message': 'User removed from group'}, status=200)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_group_by_id(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group not found'}, status=404)

    return JsonResponse({
        'id': group.id,
        'name': group.name,
        'users': [{'id': user.id, 'name': user.name} for user in group.users.all()]
    })


def home(request):
    return render(request, 'Welcome.html')
