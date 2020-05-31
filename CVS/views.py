from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Set, Images
from .forms import SetCreate
# from django import forms


# Create your views here.
@login_required(login_url="login")
def index(request):
    return render(request,'Blocks/CVS/index.html')

@login_required(login_url="login")
def micro(request):
    shelf = Set.objects.all()
    return render(request,'Blocks/CVS/micro/index.html', {'shelf': shelf})

@login_required(login_url="login")
def upload(request):
    upload = SetCreate()
    if request.method == 'POST':
        upload = SetCreate(request.POST, request.FILES)
        if upload.is_valid():
            set_obj = upload.save(commit = False)
            set_obj.author = request.user
            set_obj.save()
            return redirect('micro')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'micro'}}">reload</a>""")
    else:
        return render(request, 'Blocks/CVS/micro/new.html', {'upload_form':upload})

@login_required
def micro_update(request, set_id):
    set_id = int(set_id)
    try:
        set_self = Set.objects.get(id = set_id)
    except Set.DoesNotExist:
        return redirect('micro')
    set_form = SetCreate(request.POST or None, instance = set_self)
    if set_form.is_valid():
       set_form.save()
       return redirect('micro')
    return render(request, 'Blocks/CVS/micro/new.html', {'upload_form':set_form})

@login_required
def micro_delete(request, set_id):
    set_id = int(set_id)
    try:
        set_self = Set.objects.get(id = set_id)
    except Set.DoesNotExist:
        return redirect('micro')
    set_self.delete()
    return redirect('micro')

def micro_show(request, set_id):
    try:
        set = Set.objects.get(pk=set_id)
    except Set.DoesNotExist:
        raise Http404("Set does not exist")
    return render(request, 'Blocks/CVS/micro/show.html', {'set': set})
