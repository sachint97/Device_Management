from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import Device
from app.form import DeviceForm
import logging

from opentelemetry import trace

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)

# Create your views here.
def device_list(request):
    device_list = Device.objects.all()
    items_per_page = 8
    paginator = Paginator(device_list, items_per_page)
    page = request.GET.get('page')

    try:
        devices = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        logger.error("Paginator not an integer.")
        devices = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results.
        logger.error("Paginator out of range.")
        devices = paginator.page(paginator.num_pages)
    logger.info("List all devices")
    context = {"device_list":devices}
    return render(request,"device_list.html",context)

def create_device(request):
    if request.method == 'POST':
        logger.info("Device creation initiated.")
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Device creation successful.")
            return redirect('device_list')
        else:logger.error("Invalid form")
    else:
        form = DeviceForm()

    return render(request, 'create_device.html', {'form': form})