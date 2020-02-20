from django import forms
from .models import Report,ProblemReporting
from areas.models import ProductionLine
from django.shortcuts import get_object_or_404


class ReportResultForm(forms.Form):
    production_line = forms.ModelChoiceField(queryset=ProductionLine.objects.all())
    day = forms.CharField


class ReportSelectLineForm(forms.Form):
    production_line = forms.ModelChoiceField(
        queryset=ProductionLine.objects.none(), label='')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        print(user)
        super(ReportSelectLineForm, self).__init__(*args, **kwargs)
        self.fields['production_line'].queryset = ProductionLine.objects.filter(team_leader__user__username=user)
       

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        # fields = '__all__'
        exclude = ('user','productionline',)

    def __init__(self, *args, **kwargs):
        productionline =kwargs.pop('productionline',None)
        super().__init__(*args, **kwargs)
        if productionline is not None:
            line = get_object_or_404(ProductionLine,name=productionline)
            self.fields['product'].queryset = line.products.all()


    
class ProblemReportingForm(forms.ModelForm):

    class Meta:
        model = ProblemReporting
       # fields = '__all__'
        exclude = ('user','report','problem_id',)
