import requests
from django.core import serializers
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views import generic
from archiEmbarque.models import Device


# Create your views here.
class DeviceList(generic.ListView):
    model = Device

    def get_queryset(self):
        allDevicesKnown = Device.objects.all()
        unreachable = []
        for device in allDevicesKnown:
            try:
                api_response = requests.get('http://' + device.ip, timeout=10)
                if api_response.status_code is not 200:
                    unreachable.append(device.id)
            except:
                unreachable.append(device.id)

        reachableDevices = allDevicesKnown.exclude(id__in=unreachable)
        return reachableDevices


class DeviceDetails(generic.DetailView):
    model = Device


def deviceListJson(request):
    reachableOnly = request.GET.get('reachable', False)
    if reachableOnly == 'true':

        allDevicesKnown = Device.objects.all()
        unreachable = []
        for device in allDevicesKnown:
            try:
                api_response = requests.get('http://' + device.ip, timeout=10)
                if api_response.status_code is not 200:
                    unreachable.append(device.id)
            except:
                unreachable.append(device.id)

        reachableDevices = allDevicesKnown.exclude(id__in=unreachable)

        data = serializers.serialize("json", reachableDevices)

    else:
        data = serializers.serialize("json", Device.objects.all())

    return HttpResponse(data)

def deviceItemJson(request, pk):
    data = serializers.serialize("json", Device.objects.filter(id=pk))
    return HttpResponse(data)

def Digital(request, pk):
    if request.method == 'GET':
        print('GETd')
        gpio = request.GET.get('gpio', None)
        if gpio is None:
            return HttpResponseNotFound('<h1>Missing parameters gpio</h1>')

        device = Device.objects.get(id=pk)
        try:
            api_response1 = requests.get('http://' + device.ip + '/digital?gpio=' + str(gpio), timeout=10)
            if api_response1.status_code is not 200:
                return HttpResponseNotFound(api_response1.content)
            else:
                context = {
                    'result': api_response1.content
                }
                return render(request, 'archiEmbarque/digitalGet.html', context=context)
        except:
            return HttpResponseNotFound('<h1>Device unreachable</h1>')

    elif request.method == 'POST':
        gpio = request.POST.get('gpio', None)
        value = request.POST.get('value', None)
        if gpio is None or value is None:
            return HttpResponseNotFound('<h1>Missing parameters gpio and/or value</h1>')

        device = Device.objects.get(id=pk)
        try:
            api_response1 = requests.get('http://' + device.ip + '/digitalpost?gpio=' + str(gpio) + '&value=' + str(value),
                                         timeout=10)
            if api_response1.status_code is not 200:
                return HttpResponseNotFound(api_response1.content)
            else:
                context = {
                    'result': api_response1.content
                }
                return render(request, 'archiEmbarque/digitalGet.html', context=context)
        except:
            return HttpResponseNotFound('<h1>Device unreachable</h1>')

