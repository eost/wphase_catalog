from django import forms
from django.utils import timezone
from .models import Event, Solution

class SearchForm(forms.Form):
    # Geography
    latitude_min  = forms.FloatField(min_value=-90,  max_value=90,   initial=-90)
    latitude_max  = forms.FloatField(min_value=-90,  max_value=90,   initial=90)
    longitude_min = forms.FloatField(min_value=-180, max_value=180,  initial=-180)
    longitude_max = forms.FloatField(min_value=-180, max_value=180,  initial=180)
    depth_min     = forms.FloatField(min_value=0,    max_value=1000, initial=0)
    depth_max     = forms.FloatField(min_value=0,    max_value=1000, initial=1000)
    # Date
    year_min  = forms.IntegerField(min_value=1976, max_value=2050, initial=1976)
    month_min = forms.IntegerField(min_value=1,    max_value=12,   initial=1)
    day_min   = forms.IntegerField(min_value=1,    max_value=31,   initial=1)
    year_max  = forms.IntegerField(min_value=1976, max_value=2050, initial=timezone.now().year)
    month_max = forms.IntegerField(min_value=1,    max_value=31,   initial=timezone.now().month)
    day_max   = forms.IntegerField(min_value=1,    max_value=31,   initial=timezone.now().day)
    # Magnitude
    mw_min = forms.FloatField(min_value=0,  max_value=10,   initial=0)
    mw_max = forms.FloatField(min_value=0,  max_value=10,   initial=10)
    # Nodal plane
    NPS_min = forms.FloatField(initial=0) 
    NPS_max = forms.FloatField(initial=360)
    NPD_min = forms.FloatField(initial=0)
    NPD_max = forms.FloatField(initial=90)
    NPR_min = forms.FloatField(initial=-180)
    NPR_max = forms.FloatField(initial=180)
    # Used data
    stations = forms.MultipleChoiceField(choices=((s, s) for s in Solution.get_all_stations()), required=False)
    # Quality control
    gap_min = forms.FloatField(initial=0) 
    gap_max = forms.FloatField(initial=360)

    # Display options
    """
    display_event    = forms.ChoiceField(choices=(('name_list','List of names'),('all_data','All data'), ('selected_data','Selected data')))
    options_event    = forms.MultipleChoiceField(choices=(('agency','EPI_agency'), ('date','EPI_date'), ('geography', 'EPI_geography'), ('magnitude','EPI_magnitude')), initial=('agency','EPI_agency'))

    display_solution = forms.ChoiceField(choices=(('none','None'),('name_list','List of names'), ('selected_data','Selected data')))
    options_solution = forms.MultipleChoiceField(choices=(('geninfo','General information'), ('cmtw','Centroid Moment Tensor WCMT'), ('bnpw', 'Best nodal planes WCMT'), ('eigw','Eigenvalues WCMT'), ('cmtr','Centroid Moment Tensor RCMT'), ('bnpr','Best nodal planes RCMT'), ('eigr','Eigenvalues RCMT'), ('filt','Filter parameters'), ('screen','Screening parameters'), ('data','Used data'), ('inv','Inversion parameters'), ('qc','Quality control') ), initial=('geninfo','General information'))
    """
    types_solution = forms.MultipleChoiceField(choices=(('preferred','Preferred solution'),('all', 'All solutions'), ('xy','Lat-Lon Gridsearch'), ('z','Depth Gridsearch'), ('ts','Time-shift Gridsearch'), ('th','RMS screening'), ('med','Median screening')), initial=('preferred','Preferred solution'), required=False)

    output_format  = forms.ChoiceField(choices=(('std','Standard'),('cmtsolution','CMTSOLUTION'),('full','Full format'),('data','Used data')), initial=('std', 'Standard'))

    order_solution = forms.ChoiceField(choices=(('time', 'Chronological order'), ('rev_time', 'Reverse chronological order'), ('mag', 'Magnitude order'), ('rev_mag', 'Reverse magnitude order')), initial=('time', 'Chronological order'))
