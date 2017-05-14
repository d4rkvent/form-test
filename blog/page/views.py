from django.shortcuts import render

from .forms import PageForm


def page(request):
    form = PageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()




    context = {'form': form}
    return render(request, 'index.html', context)