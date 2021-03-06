from django.shortcuts import render
from App import forms
from App.models import student_model


# Create your views here.
def index_views(request):
    # For view data
    student_list = student_model.objects.order_by('name')
    # End View
    diction = {'title': "This is index page",
               'student_list': student_list}
    return render(request, 'index.html', context=diction)


def student_views(request):
    student_form = forms.student_form()
    # main logic for insert
    if request.method == "POST":
        student_form = forms.student_form(request.POST)

        if student_form.is_valid():
            student_form.save(commit=True)
        # End insert

    diction = {'title': "This is Student page", 'student_form': student_form}
    return render(request, 'student.html', context=diction)


def studentinfo_views(request, studentid):
    studentinfo = student_model.objects.get(pk=studentid)
    diction = {'title': "This is StudentInformation page",
               'studentinfo': studentinfo}
    return render(request, 'student_info.html', context=diction)


def student_update(request, studentid):
    studentinfo = student_model.objects.get(pk=studentid)
    student_form = forms.student_form(instance=studentinfo)
    if request.method == "POST":
        form = forms.student_form(request.POST, instance=studentinfo)
        if form.is_valid():
            form.save(commit=True)
            return index_views(request)
    diction = {'student_form': student_form}
    return render(request, 'student_update.html', context=diction)

def student_delete(request, studentid):
    student = student_model.objects.get(pk=studentid).delete()
    diction = {'delete':"delete done"}
    return render(request, 'student_delete.html', context=diction)

