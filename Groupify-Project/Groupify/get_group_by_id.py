from django.http import JsonResponse
from yourapp.models import Group

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

