from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, date, time, timedelta
import numpy as np
import matplotlib.pyplot as plt

class Event(models.Model):
    eventid = models.CharField(primary_key=True, max_length=15)

    # epicenter
    epi_agency    = models.CharField(max_length=5)
    epi_year      = models.IntegerField()
    epi_month     = models.IntegerField()
    epi_day       = models.IntegerField()
    epi_hour      = models.IntegerField()
    epi_minute    = models.IntegerField()
    epi_second    = models.IntegerField()
    epi_latitude  = models.FloatField()
    epi_longitude = models.FloatField()
    epi_depth     = models.FloatField()
    epi_m1        = models.FloatField()
    epi_m2        = models.FloatField()
    epi_region    = models.CharField(max_length=32)

    # comments
    comments = ArrayField(models.CharField(max_length=50, default=""), default=[""])

    def __str__(self):
        return self.eventid + " " + self.epi_region

    def date(self):
        return datetime(self.epi_year, self.epi_month, self.epi_day, self.epi_hour, self.epi_minute, self.epi_second)

    def capsule(self):
        res        = [" "] * 85
        res[1:4]   = self.epi_agency
        res[5:8]   = str(self.epi_year)
        res[9]    = " "
        res[10:11] = str(self.epi_month)
        res[12]    = " "
        res[13:14] = str(self.epi_day)
        res[15]    = " "
        res[16:17] = str(self.epi_hour)
        res[18]    = " "
        res[19:20] = str(self.epi_minute)
        res[21]    = " "
        res[22:26] = str(self.epi_second)
        res[27]    = " "
        res[28:35] = str(self.epi_latitude)
        res[36]    = " "
        res[37:45] = str(self.epi_longitude)
        res[46]    = " "
        res[47:51] = str(self.epi_depth)
        res[52]    = " "
        res[53:55] = str(self.epi_m1)
        res[56]    = " "
        res[57:59] = str(self.epi_m2)
        res[60]    = " "
        res[61:]   = self.epi_region
        return ''.join(res)

class Solution(models.Model):
    event        = models.ForeignKey('Event') # renamed event_id by Django
    status       = models.CharField(max_length=10)
    code_version = models.IntegerField()
    gf_path      = models.CharField(max_length=50, default="")

    # flags
    o_covf       = models.CharField(max_length=30)
    o_cmtf       = models.CharField(max_length=30)
    cmtfile      = models.CharField(max_length=30)
    th_val       = models.FloatField()
    rms_r_th     = models.FloatField()
    cth_val      = models.FloatField()
    df_val       = models.FloatField()
    ts_nit       = models.IntegerField()
    dts_val      = models.FloatField()
    dts_min      = models.FloatField()
    dts_max      = models.FloatField()
    dts_step     = models.FloatField()
    hdsafe       = models.BooleanField()
    xy_nit       = models.IntegerField()
    xy_dx        = models.FloatField()
    xy_nx        = models.IntegerField()
    dz           = models.FloatField()
    mindep       = models.FloatField()
    xy_nopt      = models.IntegerField()
    ib           = ArrayField(models.CharField(max_length=7))
    priorsdrm0   = ArrayField(models.FloatField())
    azp          = models.FloatField()
    med_val_flag = models.BooleanField()
    op_pa_flag   = models.BooleanField()
    ntr_flag     = models.BooleanField()
    ref_flag     = models.BooleanField()
    ps_flag      = models.BooleanField()

    # complementary information
    seed               = models.CharField(max_length=50, null=True)
    i_dmin             = models.FloatField(null=True)
    i_dmax             = models.FloatField(null=True)
    idec_2             = ArrayField(models.FloatField(null=True), null=True)
    idec_3             = ArrayField(models.FloatField(null=True), null=True)
    gfdir              = models.CharField(max_length=50, null=True)
    twptt              = models.IntegerField(null=True)
    p2p_fac_min        = models.FloatField(null=True)
    p2p_fac_max        = models.FloatField(null=True)
    tr_length_global   = models.IntegerField(null=True)
    tr_length_regional = models.IntegerField(null=True)
    tr_dlat            = models.FloatField(null=True)
    tr_dlon            = models.FloatField(null=True)
    tr_opdffile        = models.CharField(max_length=50, null=True)
    tr_ylimauto        = models.NullBooleanField()
    tr_ylimfixed       = ArrayField(models.IntegerField(null=True), null=True)
    tr_nc              = models.IntegerField(null=True)
    tr_nl              = models.IntegerField(null=True)

    # centroid moment tensor WCMT
    w_mrr           = models.FloatField()
    w_mtt           = models.FloatField()
    w_mpp           = models.FloatField()
    w_mrt           = models.FloatField()
    w_mrp           = models.FloatField()
    w_mtp           = models.FloatField()
    w_time_shift    = models.FloatField()
    w_half_duration = models.FloatField()
    w_latitude      = models.FloatField()
    w_longitude     = models.FloatField()
    w_depth         = models.FloatField()
    w_m0            = models.FloatField()
    w_mw            = models.FloatField()
    dc_flag         = models.BooleanField()

    # best nodal planes WCMT
    w_np1_strike = models.FloatField()
    w_np1_dip    = models.FloatField()
    w_np1_rake   = models.FloatField()
    w_np2_strike = models.FloatField()
    w_np2_dip    = models.FloatField()
    w_np2_rake   = models.FloatField()

    # eigenvalues WCMT
    w_eig_t = models.FloatField()
    w_eig_n = models.FloatField()
    w_eig_p = models.FloatField()
    w_azm_t  = models.FloatField()
    w_azm_n  = models.FloatField()
    w_azm_p  = models.FloatField()
    w_plg_t  = models.FloatField()
    w_plg_n  = models.FloatField()
    w_plg_p  = models.FloatField()

    # centroid moment tensor RCMT
    r_mrr           = models.FloatField()
    r_mtt           = models.FloatField()
    r_mpp           = models.FloatField()
    r_mrt           = models.FloatField()
    r_mrp           = models.FloatField()
    r_mtp           = models.FloatField()
    r_time_shift    = models.FloatField()
    r_half_duration = models.FloatField()
    r_latitude      = models.FloatField()
    r_longitude     = models.FloatField()
    r_depth         = models.FloatField()
    r_m0            = models.FloatField()
    r_mw            = models.FloatField()

    # best nodal planes RCMT
    r_np1_strike = models.FloatField()
    r_np1_dip    = models.FloatField()
    r_np1_rake   = models.FloatField()
    r_np2_strike = models.FloatField()
    r_np2_dip    = models.FloatField()
    r_np2_rake   = models.FloatField()

    # eigenvalues RCMT
    r_eig_t = models.FloatField()
    r_eig_n = models.FloatField()
    r_eig_p = models.FloatField()

    # filter parameters
    filt_order = models.IntegerField()
    filt_cf1   = models.FloatField()
    filt_cf2   = models.FloatField()
    filt_pass  = models.IntegerField()

    # screening parameters
    med_val = models.FloatField(null=True)
    p2p_med = models.FloatField(null=True)
    p2p_min = models.FloatField(null=True)
    p2p_max = models.FloatField(null=True)
    average = models.FloatField(null=True)

    # used data
    nb_stations          = models.IntegerField()
    nb_channels          = models.IntegerField()
    nb_rejected_channels = models.IntegerField()
    stations             = ArrayField(models.CharField(max_length=20))    
    wpwin                = ArrayField(models.FloatField())    
    dmin                 = models.FloatField()
    dmax                 = models.FloatField()
    wn                   = models.FloatField()
    we                   = models.FloatField()
    wz                   = models.FloatField()

    # inversion parameters
    command_line = models.CharField(max_length=50)
    ref_solution = models.CharField(max_length=20)
    cond_thre    = models.FloatField()
    damp_fac     = models.FloatField()

    # quality control
    wrms        = models.FloatField()
    wrms_r      = models.FloatField()
    gap         = models.FloatField()
    cond_number = models.FloatField(null=True)
    rrms        = models.FloatField()
    rrms_r      = models.FloatField()

    def __str__(self):
        exp_status = ""
        if "med" in self.status :
            exp_status = "Median Screening"
        if "th" in self.status :
            exp_status = "RMS Screening " + self.status[5:]
        if "ts" in self.status :
            exp_status = "Time-shift Gridsearch"
        if "z" in self.status :
            exp_status = "Depth Gridsearch"
        if "xy" in self.status :
            exp_status = "Lat-Lon Gridsearch"
        return self.event.__str__() +" - "+ exp_status

    def get_all_stations():
        all_stations = []
        for stations_list in Solution.objects.values_list('stations'):
            for stations in stations_list :
                for station in stations :
                    station = station.split('(')
                    if station[0] not in all_stations:
                        all_stations.append(station[0])
        return all_stations

    def plot(self,fname,npx=250,figsize=(3.,3.),colors=[[0.42,0.65,1.],[1.,1.,1.]]):
        '''
        Compute mechanism
        Args:
           * npx: number of points
           * colors: RGB colors for compressional and tensional quadrants
        '''
        
        # Mecanism
        meca = np.zeros((npx,npx))
    
        # x,y coordinates
        X,Y = np.meshgrid(np.linspace(-1,1,npx),np.linspace(-1,1,npx)[::-1])
    
        # distance, angles
        r  = np.sqrt(X*X+Y*Y)
        ta = 2. * np.arcsin(r/np.sqrt(2))
        az = np.arctan2(X,Y)
        
        # gamma vector
        ga = np.zeros((3,npx,npx))
        ga[0] = -np.cos(ta)
        ga[1] = -np.sin(ta)*np.cos(az)
        ga[2] =  np.sin(ta)*np.sin(az)

        # P-wave amplitude
        amp = self.w_mrr*ga[0]*ga[0] + self.w_mtt*ga[1]*ga[1] + self.w_mpp*ga[2]*ga[2]
        amp += 2*(self.w_mrt*ga[0]*ga[1] + self.w_mrp*ga[0]*ga[2] + self.w_mtp*ga[1]*ga[2])

        # Polarity
        i0,j0 = np.where(amp> 0.)
        i1,j1 = np.where(amp<=0.)
        i2,j2 = np.where((r>=0.98) & (r<=1))
        i3,j3 = np.where(r>1.)
        pol = np.zeros((npx,npx,3))
        pol[i0,j0] = colors[0]
        pol[i1,j1] = colors[1]
        pol[i2,j2] = [0.,0.,0.]
        pol[i3,j3] = [1.,1.,1.]
        pol=np.ma.masked_where(pol>=2.,pol)
        
        fig = plt.figure(figsize=figsize)
        ax  = fig.add_subplot(111)
        ax.imshow(pol)
        ax.set_axis_off()
        fig.savefig("media/"+fname)

        print("Picture saved")

    def get_centroid_time(self):
        origin_time = self.event.date()
        delta = timedelta(seconds=self.w_time_shift)
        return (origin_time + delta).time()
