from django.contrib import admin
from .models import Event, Solution

class SolutionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General information',         {'fields':['event', 'status', 'code_version', 'gf_path']}),
        ('Flags',                       {'fields':['o_covf', 'o_cmtf', 'cmtfile', 'th_val', 'rms_r_th', 'cth_val', 'df_val', 'ts_nit', 'dts_val', 'dts_min', 'dts_max', 'dts_step', 'hdsafe', 'xy_nit', 'xy_dx', 'xy_nx', 'dz', 'mindep', 'xy_nopt', 'ib', 'priorsdrm0', 'azp', 'med_val_flag', 'op_pa_flag', 'ntr_flag', 'ref_flag', 'ps_flag']}),
        ('Centroid moment tensor WCMT', {'fields':['w_mrr', 'w_mtt', 'w_mpp', 'w_mrt', 'w_mrp', 'w_mtp', 'w_time_shift', 'w_half_duration', 'w_latitude', 'w_longitude', 'w_depth', 'w_m0', 'w_mw', 'dc_flag']}),
        ('Best nodal planes WCMT',      {'fields':['w_np1_strike', 'w_np1_dip', 'w_np1_rake', 'w_np2_strike', 'w_np2_dip', 'w_np2_rake']}),
        ('Eigenvalues WCMT',            {'fields':['w_eig_t', 'w_eig_n', 'w_eig_p', 'w_azm_t', 'w_azm_n', 'w_azm_p', 'w_plg_t', 'w_plg_n', 'w_plg_p']}),
        ('Centroid moment tensor RCMT', {'fields':['r_mrr', 'r_mtt', 'r_mpp', 'r_mrt', 'r_mrp', 'r_mtp', 'r_time_shift', 'r_half_duration', 'r_latitude', 'r_longitude', 'r_depth', 'r_m0', 'r_mw']}),
        ('Best nodal planes RCMT',      {'fields':['r_np1_strike', 'r_np1_dip', 'r_np1_rake', 'r_np2_strike', 'r_np2_dip', 'r_np2_rake']}),
        ('Eigenvalues RCMT',            {'fields':['r_eig_t', 'r_eig_n', 'r_eig_p']}),
        ('Filter parameters',           {'fields':['filt_order', 'filt_cf1', 'filt_cf2', 'filt_pass']}),
        ('Screening parameters',        {'fields':['med_val', 'p2p_med', 'p2p_min', 'p2p_max', 'average']}),
        ('Used data',                   {'fields':['nb_stations', 'nb_channels', 'nb_rejected_channels', 'stations', 'wpwin', 'dmin', 'dmax', 'wn', 'we', 'wz']}),
        ('Inversion parameters',        {'fields':['command_line', 'ref_solution', 'cond_thre', 'damp_fac']}),
        ('Quality control',             {'fields':['wrms', 'wrms_r', 'gap', 'cond_number', 'rrms', 'rrms_r']}),
    ]
admin.site.register(Event)
admin.site.register(Solution, SolutionAdmin)
