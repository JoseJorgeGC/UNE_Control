def get_day_for_graphic(actual_month):
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_of_month[actual_month + 1]

def title_for_graphic_days(month, days):
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'
              , 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    titles = []
    i = 0
    for day in days:
        title = f"{day} de {months[month[i]-1]}"
        titles.append(title)
        i += 1

    return titles

def convertir_segundos_a_horas(_segundos):
    minutos = _segundos // 60
    segundos = _segundos % 60

    horas = minutos // 60
    minutos = minutos % 60
    tiempo = f"{horas}:{minutos}"
    return tiempo