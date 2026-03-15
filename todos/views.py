from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Category
from django.db import IntegrityError

# Django rest framework imports
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, TodoSerializer

# Authentication imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    # Only get todos belonging to logged in user
    todos = Todo.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos, 'categories': categories})

@login_required
def todo_add(request):
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        # ✅ Handles empty category safely
        category = Category.objects.filter(id=category_id, user=request.user).first() if category_id else None
        Todo.objects.create(
            title=title,
            description=description,
            category=category,
            user=request.user
        )
        return redirect('todo_list')
    return render(request, 'todos/todo_add.html', {'categories': categories})

@login_required
def todo_complete(request, pk):
    # Only get todo if it belongs to logged in user
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

@login_required
def todo_edit(request, pk):
    # Only get todo if it belongs to logged in user
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        category_id = request.POST.get('category')
        # ✅ Handles empty category safely
        todo.category = Category.objects.filter(id=category_id, user=request.user).first() if category_id else None
        todo.save()
        return redirect('todo_list')
    return render(request, 'todos/todo_edit.html', {'todo': todo, 'categories': categories})

@login_required
def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try :
            Category.objects.create(name=name, user=request.user)
            return redirect('todo_list')
        except IntegrityError:
            return render(request, 'todos/category_add.html', {
                'error': 'Category "' + name + '" already exists!'
            })
    return render(request, 'todos/category_add.html')

@login_required
def todo_delete(request, pk):
    # Only get todo if it belongs to logged in user
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('todo_list')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_todo_list(request):
    if request.method == 'GET':
        # Only return logged in user's todos
        todos = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) # ← link to logged in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_todo_detail(request, pk):
    # Only get todo if it belongs to logged in user
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_category_list(request):
    if request.method == 'GET':
        categories = Category.objects.filter(user=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Authentication views
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})