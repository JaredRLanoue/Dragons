from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from yourapp.models import Group

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
