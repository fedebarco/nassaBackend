from django.http import HttpResponse,JsonResponse
import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg

def saludo(request):
    # Load database and choose the phases that will be considered
    db_alzn = Database('/Users/feder/sustancias/suspro\Fe-C.TDB')
    my_phases_alzn = ['LIQUID', 'GRAPHITE', 'BCC_A2']
    # Create a matplotlib Figure object and get the active Axes
    fig = plt.figure(figsize=(9,6))
    axes = fig.gca()
    # Compute the phase diagram and plot it on the existing axes using the `plot_kwargs={'ax': axes}` keyword argument
    binplot(db_alzn, ['C', 'Fe', 'VA'] , my_phases_alzn, {v.X('C'):(0,1,0.02), v.T: (300, 10000, 10), v.P:101325, v.N: 1}, plot_kwargs={'ax': axes})
    #plt.show()
    
    response = HttpResponse(content_type = 'image/png')
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(response)
    return response


def Calculaentalpia(request,temperatura,presion):
    return JsonResponse({'entalpia':'holabebe'})

def objetoJ(request):
    casa='5'
    return JsonResponse({'casa':casa})
