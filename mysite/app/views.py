from django.shortcuts import render
from .models import Measure

def measures(request):
    if request.method == 'POST':
        selected_measure_ids = request.POST.getlist('selected_measures')
        selected_measures = Measure.objects.filter(id__in=selected_measure_ids)
        total_cost = sum([measure.cost for measure in selected_measures])
    else:
        total_cost = None
    measures = Measure.objects.all()
    context = {'measures': measures, 'total_cost': total_cost}
    return render(request=request, template_name='measures.html',context=context)