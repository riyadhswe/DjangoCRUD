from django.shortcuts import render
from App import forms


# Create your views here.
def index_views(request):
    diction = {'title': "This is index page"}
    return render(request, 'index.html', context=diction)


def student_views(request):
    form = forms.student_form()
    # main logic for insert
    if request.method == "POST":
        form = forms.student_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index_views(request)
        # End insert

    diction = {'title': "This is Student page", 'student_form': form}
    return render(request, 'student.html', context=diction)
