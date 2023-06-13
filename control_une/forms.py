from django import forms
from .models import Logs, Circuitos, Afectaciones, Estado_SEN

class FormAfectaciones(forms.ModelForm):
    class Meta:
        model = Afectaciones
        fields = ('circuito', 'fecha', 'hora_afectacion', 'hora_restablecido')

class FormLogs(forms.ModelForm):
    class Meta:
        model = Logs
        fields = ('circuito', 'afectado', 'descripcion', 'mw_afectados_en_provincia', 'fecha')

class FormCircuitos(forms.ModelForm):
    class Meta:
        model = Circuitos
        fields = ('nombre', 'descripcion', 'balance_deficit', 'ultima_afectacion', 'numero_de_afectaciones')

class FormEstadoSEN(forms.ModelForm):
    class Meta:
        model = Estado_SEN
        fields = ('fecha', 'prevision_de_afectacion', 'afectacion_real', 'tiempo_de_afectacion')