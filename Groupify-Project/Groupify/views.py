from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from Groupify.models import Groups


# @csrf_exempt
# def remove_user_from_group(request, group_id):
#     return
#
# def get_group_by_id(request, group_id):
#     return
#
# def get_all_groups(request):
#     return
#
# @csrf_exempt
# def update_group(request, group_id):
#     if request.method == 'PUT':
#         # Retrieve group by ID from group model
#         try:
#             group = Group.objects.get(pk=group_id)
#         except Group.DoesNotExist:
#             return JsonResponse({'error': 'Group not found'}, status=404)
#
#         # Retrieve new name for the group from request body
#         new_name = request.POST.get('name')
#
#         # Update group name if new name is provided
#         if new_name:
#             group.name = new_name
#             group.save()
#
#         # Return a JSON response with the updated group data
#         response_data = {
#             'id': group.id,
#             'name': group.name,
#             'users': [{'id': user.id, 'name': user.name} for user in group.users.all()]
#         }
#         return JsonResponse(response_data)
#
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def add_user_to_group(request, group_id):
#     if request.method == 'POST':
#         # Retrieve group by ID from group model
#         try:
#             group = Group.objects.get(pk=group_id)
#         except Group.DoesNotExist:
#             return JsonResponse({'error': 'Group not found'}, status=404)
#
#         # Retrieve user by ID from user model
#         user_id = request.POST.get('user_id')
#         try:
#             user = User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=404)
#
#         # Add user to group
#         group.users.add(user)
#
#         # Return a JSON response with the updated group data
#         response_data = {
#             'id': group.id,
#             'name': group.name,
#             'users': [{'id': user.id, 'name': user.name} for user in group.users.all()]
#         }
#         return JsonResponse(response_data)
#
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required
def home_view(request):
    groups = Groups.objects.all()
    context = {'groups': groups}
    return render(request, 'home.html', context)

def login_view(request):
    if request.user.is_authenticated:
        if request.path == reverse('home'):
            return render(request, 'Home.html')
        else:
            return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Registration.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'Registration.html')

def register_view(request):
    if request.user.is_authenticated:
        if request.path == reverse('home'):
            return render(request, 'Home.html')
        else:
            return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            error_message = form.errors
    else:
        form = UserCreationForm()
        error_message = None
    return render(request, 'Registration.html', {'form': form, 'error_message': error_message})

def welcome_view(request):
    if request.user.is_authenticated:
        if request.path == reverse('home'):
            return render(request, 'Home.html')
        else:
            return redirect('home')
    else:
        return render(request, 'Welcome.html')

def groups_view(request):
    if request.user.is_authenticated:
        if request.path == reverse('home'):
            return render(request, 'Home.html')
        else:
            return redirect('home')
    else:
        return render(request, 'GroupDetails.html')

class CustomLoginView(LoginView):
    template_name = "Login.html"


@login_required
def create_group_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        visibility = request.POST.get('visibility')
        category = request.POST.get('category')

        group = Groups.objects.create(
            title=title,
            description=description,
            visibility=visibility,
            category=category,
            creator=request.user
        )

        # group.admins.add(request.user)
        group.members.add(request.user)

        return redirect('group_details', group_id=group.id)
    else:
        return render(request, 'CreateGroup.html')

def group_details(request, group_id):
    group = Groups.objects.get(id=group_id)
    context = {'group': group}
    return render(request, 'GroupDetails.html', context)
