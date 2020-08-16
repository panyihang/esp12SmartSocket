from django.shortcuts import render
import mqttClien
def test(request):
    context          = {}
    context['temperature'] = 31
    context['humidity'] = 47
    context['light0'] = 'on'
    if request.method == "POST":
        if (request.POST.get("on")) != None:
            context['light0'] = 'on'
            mqttClien.main('set light0 on')
        elif (request.POST.get("off")) != None:
            context['light0'] = 'off'
            mqttClien.main('set light0 off')
    return render(request, 'test.html', context)