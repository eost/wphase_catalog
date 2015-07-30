from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from .models import Event, Solution
from .forms import SearchForm
from datetime import datetime
import sys, os, tarfile

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
    context_object_name = 's_results'

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
            types_solution   = form.cleaned_data['types_solution']
            if types_solution == []:
                types_solution = ["preferred"]
            output_format    = form.cleaned_data['output_format']
            order_solution   = form.cleaned_data['order_solution']

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
                        path = "media/"+name_file
                        if not os.path.isfile(path):
                            sol.plot(name_file)
                            print ("Picture was created")
                            

            # Sorting results
            if (order_solution == 'time'):
                s_results = sorted(s_results, key=lambda a: a.event.date())
            elif (order_solution == 'rev_time'):
                s_results = sorted(s_results, key=lambda a: a.event.date(), reverse=True)
            elif (order_solution == 'mag'):
                s_results = sorted(s_results, key=lambda a: a.w_mw)
            else: # if order_solution == 'rev_mag'
                s_results = sorted(s_results, key=lambda a: a.w_mw, reverse=True)

            request.session["types_solution"] = types_solution
            request.session["output_format"]  = output_format

            # For txt saved file
            request.session["sol_ids"]        = '_'.join(map(str,s_ids))

            # For results pagination
            paginator = Paginator(s_results, 10) # Show 10 results per page
            page = request.GET.get('page')
            try:
                res = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                res = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                res = paginator.page(paginator.num_pages)

            return render(request, 'wphase/results.html/', {'s_results':res})


        # form not valid
        else:
            return render(request, 'wphase/search_form.html',{'error_message': "Sorry, but the form is not valid.", 'form':SearchForm()})

    # if GET : create a blank form
    else:
        sol_ids = request.session["sol_ids"].split('_')
        sol_ids = map(int, sol_ids)
        s_results = []
        for i in sol_ids:
            s_results.append(Solution.objects.get(pk=i))
        paginator = Paginator(s_results, 10) # Show 10 results per page
        page = request.GET.get('page')
        try:
            res = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            res = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            res = paginator.page(paginator.num_pages)

        return render(request, 'wphase/results.html/', {'s_results':res})


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

def generate_targz(request, results):
    # Create and fill tar.gz file
    runs_results = tarfile.open("runs_results.tar.gz", "w:gz")
    runs_path = "/home/lucile/WPHASE/runs"
    if os.path.isdir(runs_path):
        for run in os.listdir(runs_path):
            run_path = os.path.join(runs_path, run)
            if os.path.isdir(run_path):
                cmt_path = os.path.join(run_path, "CMTSOLUTION")
                if os.path.isfile(cmt_path):
                    for r in results.split('_'):
                        sol = Solution.objects.get(pk=r)
                        with open(cmt_path) as cmt :
                            if (sol.event.eventid in cmt.readlines()[1].strip()):
                                if run not in runs_results :
                                    #runs_results.add(os.path.join(runs_path, run), arcname=run)
                                    runs_results.add(os.path.join(run_path, "i_master"), arcname=run+"/i_master")
                                    runs_results.add(os.path.join(run_path, "CMTSOLUTION"), arcname=run+"/CMTSOLUTION")
                                    if os.path.isfile(os.path.join(run_path, "wpinversion.ini")):
                                        runs_results.add(os.path.join(run_path, "wpinversion.ini"), arcname=run+"/wpinversion.ini")
                                    if os.path.isfile(os.path.join(run_path, "wpinversion_gs.ini")):
                                        runs_results.add(os.path.join(run_path, "wpinversion_gs.ini"), arcname=run+"/wpinversion_gs.ini")
                                    if os.path.isfile(os.path.join(run_path, "WCMTSOLUTION")):
                                        runs_results.add(os.path.join(run_path, "WCMTSOLUTION"), arcname=run+"/WCMTSOLUTION")
                                    if os.path.isfile(os.path.join(run_path, "ts_WCMTSOLUTION")):
                                        runs_results.add(os.path.join(run_path, "ts_WCMTSOLUTION"), arcname=run+"/ts_WCMTSOLUTION")
                                    if os.path.isfile(os.path.join(run_path, "xy_WCMTSOLUTION")):
                                        runs_results.add(os.path.join(run_path, "xy_WCMTSOLUTION"), arcname=run+"/xy_WCMTSOLUTION")
                                    if os.path.isfile(os.path.join(run_path, "p_wpinversion.ps")):
                                        runs_results.add(os.path.join(run_path, "p_wpinversion.ps"), arcname=run+"/p_wpinversion.ps")
                                    if os.path.isfile(os.path.join(run_path, "ts_p_wpinversion.ps")):
                                        runs_results.add(os.path.join(run_path, "ts_p_wpinversion.ps"), arcname=run+"/ts_p_wpinversion.ps")
                                    if os.path.isfile(os.path.join(run_path, "xy_p_wpinversion.ps")):
                                        runs_results.add(os.path.join(run_path, "xy_p_wpinversion.ps"), arcname=run+"/xy_p_wpinversion.ps")
                                    if os.path.isfile(os.path.join(run_path, "o_wpinversion.ps")):
                                        runs_results.add(os.path.join(run_path, "o_wpinversion"), arcname=run+"/o_wpinversion")

    runs_results.close()

    # Create response
    response = FileResponse(open('runs_results.tar.gz', 'rb'), content_type="application/x-gzip")
    response['Content-Disposition'] = 'attachment; filename="runs_results.tar.gz"'

    return response;

def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/wphase')
