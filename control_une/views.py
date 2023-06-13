from django.shortcuts import render, HttpResponse, redirect
from .forms import FormAfectaciones, FormEstadoSEN
from .models import Estado_SEN
from django.utils import timezone
from . import utils
import datetime
import pandas as pd
import numpy

# Create your views here.
def index(request):
    context = {}
    month = []
    days = []
    today = datetime.date.today()
    for day_ in range(15, 0, -1):
        day_to_function = today.day - day_
        month_ = today.month
        if day_to_function <=0:
            day_to_function += utils.get_day_for_graphic(month_)
            month_ = today.month - 1
        month.append(month_)
        days.append(day_to_function)
        
    deficit_pronosticado = []
    deficit_real = []    
    tiempo_de_afectacion = []
    for i in range(0, 15, 1):
        try:
            estado = Estado_SEN.objects.filter(fecha__month = month[i], fecha__day = days[i]).get()
            deficit_pronosticado.append(estado.prevision_de_afectacion)
            deficit_real.append(estado.afectacion_real)
            tiempo_de_afectacion.append(utils.convertir_segundos_a_horas(estado.tiempo_de_afectacion))
        except:
            deficit_pronosticado.append(0)
            deficit_real.append(0)

    days_to_text = utils.title_for_graphic_days(month, days)
    print(month)
    print(days)
    print(days_to_text)
    print(tiempo_de_afectacion)
    context |= {'deficit_real': deficit_real, 'deficit_pronosticado': deficit_pronosticado}
    context |= {'dias_deficit': days_to_text}
    context |= {'tiempo_de_afectacion': tiempo_de_afectacion}


    #Data Analytics with pandas
    data_une = {'deficit real': deficit_real, 'deficit pronosticado': deficit_pronosticado}
    df = pd.DataFrame(data = data_une)
    print(df.mean())
    return render(request, 'pages/index.html', context)

def status(request):
    if request.method == "POST":
        if request.POST['form-type'] == 'estado-sen':
            form = FormEstadoSEN(request.POST)
            if not form.is_valid():
                return redirect('status/')
            
            estado_sen = form.save(commit = False)

            try:
                estados = Estado_SEN.objects.filter(fecha__month = estado_sen.fecha.month)
            except:
                estados = False
            

            if estados:
                existe = False
                for estado in estados:
                    if estado.fecha == estado_sen.fecha:
                        existe = True
                
                if existe:
                    return redirect('status/')
            
            estado_sen.save()

    context = {'form_estado_sen': FormEstadoSEN(), 'form_afectaciones': FormAfectaciones()}
    return render(request, 'pages/add_status.html', context)