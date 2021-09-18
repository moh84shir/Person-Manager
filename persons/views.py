from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http import HttpResponseForbidden

from .models import Person


def home_page(request):
    persons = Person.objects.all()[::-1]
    persons_length = len(persons)

    context = {
        "persons": persons,
        "persons_length": persons_length,
    }
    if persons_length == 0:
        context.update(erorr="ما الان هیچ شخصی نداریم!")
    return render(request, 'index.html', context)


def create_person(request):
    this_person = request.POST['new_person']
    Person.objects.create(person_name=this_person)
    messages.success(request, f"{this_person} با موفقیت اضافه شد.")
    return redirect("/")


def delete_person(request, **kwargs):
    this_pk = kwargs['pk']
    this_person = get_object_or_404(Person, pk=this_pk)
    this_person.delete()
    messages.error(request, f"{this_person} با موفقیت حذف شد.")
    return redirect("/")


def update_person(request, **kwargs):
    this_pk = kwargs['pk']
    this_title = request.POST['new_person_name']
    this_person = get_object_or_404(Person, pk=this_pk)

    if str(this_title) != str(this_person):
        messages.success(
            request, f"{this_person} با موفقیت به {this_title} ویرایش شد.")
        this_person.person_name = this_title
        this_person.save()
        return redirect("/")
    else:
        return HttpResponseForbidden(
            """
                <h1 style='text-align:center;color:red;'>
                    لطفا برای ویرایش مقدار نام شخص را تغییر دهید
                </h1>
            """
        )
