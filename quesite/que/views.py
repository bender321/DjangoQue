from django.shortcuts import render
from django.contrib import messages
from .forms import InputForm
from .models import FirstQue, SecondQue, ThirdQue
from .logger import logger


def index(request):
    context = {}

    if request.POST:
        if request.POST.get('insert'):
            form = InputForm(request.POST)
            if form.data.get('user_name') != '':
                if form.is_valid():

                    form.save()
                    form = InputForm()
                    context['form'] = form

        elif request.POST.get('first_to_second'):
            item = FirstQue.objects.first()

            if item is not None:
                SecondQue.objects.create(user_name=item.user_name)
                logger(str(item.user_name) + 'was deleted from first que...')
                item.delete()

        elif request.POST.get('second_to_third'):
            item = SecondQue.objects.first()

            if item is not None:
                ThirdQue.objects.create(user_name=item.user_name)
                logger(str(item.user_name) + 'was deleted from second que...')
                item.delete()

        elif request.POST.get('third_to_remove'):
            item = ThirdQue.objects.first()

            if item is not None:
                logger(str(item.user_name) + 'was deleted from third que...')
                item.delete()
                messages.error(request, 'Čekatel úspešně odbaven!')

    firstQ = FirstQue.objects.all().order_by('id')[:3]
    secondQ = SecondQue.objects.all().order_by('id')[:3]
    thirdQ = ThirdQue.objects.all().order_by('id')[:3]

    context['firstQ'] = firstQ
    context['secondQ'] = secondQ
    context['thirdQ'] = thirdQ

    form = InputForm()
    context['form'] = form

    return render(request, 'index.html', context)







