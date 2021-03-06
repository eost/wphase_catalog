from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from .models import Event, Solution
from .forms import SearchForm
from datetime import datetime
import sys, os

class IndexView(generic.ListView):
    template_name = 'wphase/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        return sorted(Event.objects.all(), key=lambda a: a.date(), reverse=True)[:5]

class EventView(generic.DetailView):
    model = Event
    template_name = 'wphase/event.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context["solutions"] = Solution.objects.filter(event=context["event"].eventid)
        return context

class SolutionView(generic.DetailView):
    model = Solution
    template_name = 'wphase/solution.html'

class SearchView(generic.ListView):
    template_name = 'wphase/search_form.html'
    context_object_name = 'form'

    def get_queryset(self):
        return SearchForm()

class ResultsView(generic.ListView):
    template_name = 'wphase/results.html'
    context_object_name = 'es_results'

    def get_queryset(self):
        return None


def search(request):
    # if POST : process the form data
    if request.method == 'POST':
        form = SearchForm(request.POST) # "binding" data to form
        if form.is_valid():
            latitude_min     = form.cleaned_data['latitude_min']
            latitude_max     = form.cleaned_data['latitude_max']
            longitude_min    = form.cleaned_data['longitude_min']
            longitude_max    = form.cleaned_data['longitude_max']
            depth_min        = form.cleaned_data['depth_min']
            depth_max        = form.cleaned_data['depth_max']
            year_min         = form.cleaned_data['year_min']
            month_min        = form.cleaned_data['month_min']
            day_min          = form.cleaned_data['day_min']
            year_max         = form.cleaned_data['year_max']
            month_max        = form.cleaned_data['month_max']
            day_max          = form.cleaned_data['day_max']
            mw_min           = form.cleaned_data['mw_min']
            mw_max           = form.cleaned_data['mw_max']
            NPS_min          = form.cleaned_data['NPS_min']
            NPS_max          = form.cleaned_data['NPS_max']
            NPD_min          = form.cleaned_data['NPD_min']
            NPD_max          = form.cleaned_data['NPD_max']
            NPR_min          = form.cleaned_data['NPR_min']
            NPR_max          = form.cleaned_data['NPR_max']
            stations         = form.cleaned_data['stations']
            gap_min          = form.cleaned_data['gap_min']
            gap_max          = form.cleaned_data['gap_max']
            """
            display_event    = form.cleaned_data['display_event']
            display_solution = form.cleaned_data['display_solution']
            options_event    = form.cleaned_data['options_event']
            options_solution = form.cleaned_data['options_solution']
            """
            types_solution   = form.cleaned_data['types_solution']
            output_format    = form.cleaned_data['output_format']

            # Filter on solution data
            kwargs_s = {}
            if latitude_min and latitude_max:
                kwargs_s['w_latitude__range'] = (latitude_min,latitude_max)
            if longitude_min and longitude_max:
                kwargs_s['w_longitude__range'] = (longitude_min,longitude_max)
            if depth_min and depth_max:
                kwargs_s['w_depth__range'] = (depth_min,depth_max)
            if mw_min and mw_max:
                kwargs_s['w_mw__range'] = (mw_min,mw_max)
            if stations:
                for s in stations:
                    kwargs_s['stations__icontains'] = s
            if gap_min and gap_max:
                kwargs_s['gap__range'] = (gap_min,gap_max)

            solutions = Solution.objects.filter(**kwargs_s)
            solutions = solutions.filter( (Q(w_np1_strike__range=(NPS_min,NPS_max))&Q(w_np1_dip__range=(NPD_min,NPD_max))&Q(w_np1_rake__range=(NPR_min,NPR_max))) | (Q(w_np2_strike__range=(NPS_min,NPS_max))&Q(w_np2_dip__range=(NPD_min,NPD_max))&Q(w_np2_rake__range=(NPR_min,NPR_max))) )

            # Filter on event data
            events = Event.objects.all()
            #       Algorithm probably can be improved...
            if year_min and year_max and month_min and month_max and day_min and day_max:
                events = events.filter( (Q(epi_year__gt=year_min)&Q(epi_year__lt=year_max)) | (Q(epi_year=year_min)&Q(epi_month__gt=month_min)&Q(epi_month__lte=12)) | (Q(epi_year=year_min)&Q(epi_month=month_min)&Q(epi_day__gte=day_min)&Q(epi_day__lte=31)) | (Q(epi_year=year_max)&Q(epi_month__gte=1)&Q(epi_month__lt=month_max)) | (Q(epi_year=year_max)&Q(epi_month=month_max)&Q(epi_day__gte=1)&Q(epi_day__lte=day_max)) )

            # Crossing filter results
            es_results = {}
            e_results = []
            s_results = []
            s_ids     = []
            for sol in solutions:
                if (sol.event in events):
                    ens = Solution.objects.filter(event=sol.event).values_list('status', flat=True)
                    if "preferred" in types_solution:
                        if "xy" in sol.status:
                            s_results.append(sol)
                            s_ids.append(sol.id)
                            if (sol.event not in e_results):
                                e_results.append(sol.event)
                        elif "z" in sol.status and "wp_xy" not in ens:
                            s_results.append(sol)
                            s_ids.append(sol.id)
                            if (sol.event not in e_results):
                                e_results.append(sol.event)
                        elif "ts" in sol.status and "wp_xy" not in ens and "wp_z" not in ens:
                            s_results.append(sol)
                            s_ids.append(sol.id)
                            if (sol.event not in e_results):
                                e_results.append(sol.event)
                        elif "th" in sol.status and "wp_xy" not in ens and "wp_z" not in ens and "wp_ts" not in ens :
                            if sol.status[5:] == min([th[5:] for th in ens.filter(status__contains="th")]):
                                s_results.append(sol)
                                s_ids.append(sol.id)
                                if (sol.event not in e_results):
                                    e_results.append(sol.event)
                        elif "med" in sol.status and "wp_xy" not in ens and "wp_z" not in ens and "wp_ts" not in ens and not ens.filter(status__contains="th") :
                            s_results.append(sol)
                            s_ids.append(sol.id)
                            if (sol.event not in e_results):
                                e_results.append(sol.event)
                    else :
                        s_results.append(sol)
                        s_ids.append(sol.id)
                        if (sol.event not in e_results):
                            e_results.append(sol.event)

                    if output_format == "std":
                        name_file = sol.event_id + "_" + sol.status + ".png"
                        sol.plot(name_file)

            es_results["events"]           = e_results
            es_results["solutions"]        = s_results
            """
            es_results["display_event"]    = display_event
            es_results["display_solution"] = display_solution
            es_results["options_event"]    = options_event
            es_results["options_solution"] = options_solution
            """
            es_results["types_solution"]   = types_solution
            es_results["output_format"]    = output_format

            # For txt saved file
            es_results["sol_ids"]          = '_'.join(map(str,s_ids))

            # For results pagination
            paginator = Paginator(es_results["solutions"], 10) # Show 10 results per page
            page = request.GET.get('page')
            try:
                res = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                res = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                res = paginator.page(paginator.num_pages)
            es_results["pag"] = res

            return render(request, 'wphase/results.html/', {'es_results':es_results})


        # form not valid
        else:
            return render(request, 'wphase/search_form.html',{'error_message': "Sorry, but the form is not valid.", 'form':SearchForm()})

    # if GET : create a blank form
    else:
        form = SearchForm()
        return render(request, 'wphase/search_form.html', {'form':form})


def generate_txt(request, results):
    # Create the HttpResponse object with the appropriate header.
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="results.txt"'
    for r in results.split('_'):
        sol  = Solution.objects.get(pk=r)
        txt  = sol.event.capsule() + "\n"
        txt += "event name    : " + sol.event.eventid        + "\n"
        txt += "time shift    : " + str(sol.w_time_shift)    + "\n"
        txt += "half duration : " + str(sol.w_half_duration) + "\n"
        txt += "latitude      : " + str(sol.w_latitude)      + "\n"
        txt += "longitude     : " + str(sol.w_longitude)     + "\n"
        txt += "depth         : " + str(sol.w_depth)         + "\n"
        txt += "Mrr           : " + str(sol.w_mrr)           + "\n"
        txt += "Mtt           : " + str(sol.w_mtt)           + "\n"
        txt += "Mpp           : " + str(sol.w_mpp)           + "\n"
        txt += "Mrt           : " + str(sol.w_mrt)           + "\n"
        txt += "Mrp           : " + str(sol.w_mrp)           + "\n"
        txt += "Mtp           : " + str(sol.w_mtp)           + "\n\n"
        response.write(txt)
    return response
