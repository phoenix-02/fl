from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Project, CustomUser


@csrf_exempt
def create_project(request):
    if request.method == 'POST' and CustomUser.objects.get(id=request.user.id).role in [1,2,4]:
        customer_id = int(request.POST['customer_id'])
        title = request.POST['title']
        description = request.POST['description']
        price = int(request.POST['price'])
        p = Project(title=title, description=description, price=price, customer_id=customer_id)
        p.save()
        return render(request, 'base.html', {'data': p})


@csrf_exempt
def edit_project(request):
    project_id = int(request.POST['project_id'])
    if request.method == 'POST' and CustomUser.objects.get(id=request.user.id).role in [2,4]:
        p = Project.objects.get(id=project_id)
        p.freelancers.add(1)
        p.save()
        return render(request, 'base.html', {'data': p.freelancers.first().id})
    if request.method == 'POST' and CustomUser.objects.get(id=request.user.id).role in [1,4]:
        p = Project.objects.get(id=project_id)
        p.is_published = request.POST['is_published']
        p.save()
        return render(request, 'base.html', {'data': p})

@csrf_exempt
def say_about_me(request):
    if request.method == 'POST' and CustomUser.objects.get(id=request.user.id).role in [2,4]:
        freelancer = CustomUser.objects.get(user=request.user)
        freelancer.about = request.POST['about']
        freelancer.save()
        return render(request, 'base.html', {'data': freelancer.id})


@csrf_exempt
def search(request):
    if request.method == 'POST' and CustomUser.objects.get(id=request.user.id).role in [1,3, 4]:
        search_result = []
        fields = ['title', 'description', 'price']
        for project in Project.objects.all():
            for field in fields:
                value = str(getattr(project, field))
                if project not in search_result and request.POST['search'] in value:
                    search_result.append(project)
        return render(request, 'base.html', {'data': search_result})
