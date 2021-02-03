from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView, FormView, View, DeleteView
from layanan.models import catalog, journal, repository
from layanan.forms import catalogForm, journalForm, repositoryForm
from django.contrib.auth import authenticate, logout
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {
        'title':'Page Crud',
    }

    if request.method == "POST":
        if request.POST['logout'] == 'Submit':
            logout(request)

        return redirect('/')

    return render(request, 'crud/index.html', context)

class CatalogView(FormView, ListView):
    model = catalog
    form_class = catalogForm
    template_name = 'crud/catalog.html'
    context_object_name = 'catalogs'
    paginate_by = 5
    success_url = '/crud/catalog/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)            

    extra_context = {
        'title':'Catalog CRUD'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

def catalogDelete(request, delete_id):
    catalog.objects.filter(id=delete_id).delete()
    return redirect('pagecrud:catalogcrud')

def catalogUpdate(request, id_catalog):
    catalogs = catalog.objects.get(id=id_catalog)
    if request.POST:
        form = catalogForm(request.POST, instance=catalogs)
        if form.is_valid():
            form.save()
            return redirect('pagecrud:catalogcrud')
    else:
        form = catalogForm(instance=catalogs)
        context = {
            'form':form,
            'catalogs':catalogs,
        }
        return render(request, 'crud/catalog-update.html', context)

class JournalView(FormView, ListView):
    model = journal
    form_class = journalForm
    template_name = 'crud/journal.html'
    context_object_name = 'journals'
    paginate_by = 5
    success_url = '/crud/journal/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)            

    extra_context = {
        'title':'Journal CRUD'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

def journalDelete(request, delete_id):
    journal.objects.filter(id=delete_id).delete()
    return redirect('pagecrud:journalcrud')

def journalUpdate(request, id_journal):
    journals = journal.objects.get(id=id_journal)
    if request.POST:
        form = journalForm(request.POST, instance=journals)
        if form.is_valid():
            form.save()
            return redirect('pagecrud:journalcrud')
    else:
        form = journalForm(instance=journals)
        context = {
            'form':form,
            'journals':journals,
        }
        return render(request, 'crud/journal-update.html', context)



class RepositoryView(FormView, ListView):
    model = repository
    form_class = repositoryForm
    template_name = 'crud/repository.html'
    context_object_name = 'repositorys'
    paginate_by = 5
    success_url = '/crud/repository/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)            

    extra_context = {
        'title':'Repository CRUD'
    }

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(*args, **kwargs)

def repositoryDelete(request, delete_id):
    repository.objects.filter(id=delete_id).delete()
    return redirect('pagecrud:repositorycrud')

def repositoryUpdate(request, id_repository):
    repositorys = repository.objects.get(id=id_repository)
    if request.POST:
        form = repositoryForm(request.POST, instance=repositorys)
        if form.is_valid():
            form.save()
            return redirect('pagecrud:repositorycrud')
    else:
        form = repositoryForm(instance=repositorys)
        context = {
            'form':form,
            'repositorys':repositorys,
        }
        return render(request, 'crud/repository-update.html', context)



        


