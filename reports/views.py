from django.shortcuts import render,get_object_or_404,redirect
from .forms import ProblemReportingForm,ReportForm,ReportSelectLineForm,ReportResultForm
from .models import Report
from areas.models import ProductionLine
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,FormView
from django.urls import reverse_lazy

class SelectView(FormView):
    template_name = 'reports/select.html'
    form_class = ReportResultForm
    success_url = reverse_lazy('reports:home')

    def form_valid(self, form):
        self.request.session['day'] = self.request.POST.get('day',None)
        print(self.request.session['day'])
        return super(SelectView,self).form_valid(form)


    
class HomeView(FormView):
    template_name = 'reports/home.html'
    form_class = ReportSelectLineForm

    def get_form_kwargs(self):
        kwargs = super(HomeView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def post(self,*args, **kwargs):
        prod_line = self.request.POST.get("prod_line")
        return redirect('reports:report_view',productionline=prod_line)


class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/update.html'

    def get_success_url(self):
        return self.request.path


@login_required
def delete_view(request,*args,**kwargs):
    r_id =kwargs.get('pk')
    obj =Report.objects.get(id=r_id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def report_view(request,productionline):
    templates = 'reports/index.html'
    rform = ReportForm(request.POST or None,productionline=productionline)
    pform = ProblemReportingForm(request.POST or None)
   
    queryset = Report.objects.filter(productionline__name =productionline)
    r_id = request.POST.get('report_id')
    line = get_object_or_404(ProductionLine,name=productionline)
    # print(line)

    if 'btn_sub_report_form' in request.POST:
        print(request.user)
        if rform.is_valid():
            obj =rform.save(commit=False)
            obj.user = request.user
            obj.productionline = line
            obj.save()
            return redirect(request.META.get('HTTP_REFERER'))

    elif 'btn_sub_problem_report' in request.POST:
        if pform.is_valid():
            report = Report.objects.get(id=r_id)
            obj = pform.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()
            return redirect(request.META.get('HTTP_REFERER'))

       
   
    context ={
        'rform':rform,
        'pform':pform,
        'object_list':queryset
    }
    return render(request,templates,context)
