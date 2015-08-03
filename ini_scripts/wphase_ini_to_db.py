#!/usr/bin/env python
# wphase_ini_to_db.py
"""
Reads the ini file parsed as argument
and enters the corresponding data into db_wphase database
"""

import sys, os
import ConfigParser
import psycopg2


def main(argv):
    # Argument control
    if len(argv[1:]) != 1 :
        sys.stderr.write("Use : " + os.path.basename(argv[0]) + " ini_file \n")
        exit(1)
    else :
        ini = argv[1]

    # File control
    if not os.path.isfile(ini) :
        sys.stderr.write("File was not found.\n")
        exit(1)

    # Opening ini file
    cfg = ConfigParser.ConfigParser()
    cfg.read(ini)

    # Connecting to the database
    usr  = os.environ['POSTGRES_DB_USER']
    pwd  = os.environ['POSTGRES_DB_PASSWORD']
    conn = psycopg2.connect(database='db_wphase', user=usr, password=pwd, host='localhost')

    # Creating a psycopg cursor
    cur = conn.cursor()

    #nb_channel_dec           = cfg.get('prepare__dec_filt', 'nb_channel_dec')
    #nb_rejected_channels_dec = cfg.get('prepare__dec_filt', 'nb_rejected_channels_dec')
    cfg.remove_section('prepare__dec_filt')
    sections = cfg.sections()

    for s in sections :    
        # Reading EVENT data from ini
        eventid       = cfg.get(s, 'eventid')
        EPI_agency    = cfg.get(s, 'EPI_agency')
        EPI_year      = cfg.getint(s, 'EPI_year')
        EPI_month     = cfg.getint(s, 'EPI_month')
        EPI_day       = cfg.getint(s, 'EPI_day')
        EPI_hour      = cfg.getint(s, 'EPI_hour')
        EPI_minute    = cfg.getint(s, 'EPI_minute')
        EPI_second    = cfg.getfloat(s, 'EPI_second')
        EPI_latitude  = cfg.getfloat(s, 'EPI_latitude')
        EPI_longitude = cfg.getfloat(s, 'EPI_longitude')
        EPI_depth     = cfg.getfloat(s, 'EPI_depth')
        EPI_M1        = cfg.getfloat(s, 'EPI_M1')
        EPI_M2        = cfg.getfloat(s, 'EPI_M2')
        EPI_region    = cfg.get(s, 'EPI_region')
        nb_com        = cfg.getint(s, 'nb_comments')
        comments      = []
        for i in range(nb_com):
            key = "Comment" + `i`
            comments.append(cfg.get(s, key))


        # Entering EVENT data into database
        cur.execute("""SELECT eventid FROM wphase_event""")
        rows = cur.fetchall()
        if eventid not in str(rows) :
            query = "INSERT INTO wphase_event VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            data = (eventid, EPI_agency, EPI_year, EPI_month, EPI_day, EPI_hour, EPI_minute, EPI_second, EPI_latitude, EPI_longitude, EPI_depth, EPI_M1, EPI_M2, EPI_region, comments)
            cur.execute(query, data)
            conn.commit()
            print "Event added to database"
        else:
            print "Event already existed in database"


        # Reading SOLUTION data from ini
        status       = s
        code_version = cfg.getint(s, 'code_version')
        gf_path      = cfg.get(s, 'gf_path')

        #       flags
        o_covf       = cfg.get(s, 'o_covf')
        o_cmtf       = cfg.get(s, 'o_cmtf')
        cmtfile      = cfg.get(s, 'cmtfile')
        th_val       = cfg.getfloat(s, 'th_val')
        rms_r_th     = cfg.getfloat(s, 'rms_r_th')
        cth_val      = cfg.getfloat(s, 'cth_val')
        df_val       = cfg.getfloat(s, 'df_val')
        ts_nit       = cfg.getint(s, 'ts_nit')
        dts_val      = cfg.getfloat(s, 'dts_val')
        dts_min      = cfg.getfloat(s, 'dts_min')
        dts_max      = cfg.getfloat(s, 'dts_max')
        dts_step     = cfg.getfloat(s, 'dts_step')
        hdsafe       = cfg.getboolean(s, 'hdsafe')
        xy_nit       = cfg.getint(s, 'xy_nit')
        xy_dx        = cfg.getfloat(s, 'xy_dx')
        xy_nx        = cfg.getint(s, 'xy_nx')
        dz           = cfg.getfloat(s, 'dz')
        mindep       = cfg.getfloat(s, 'mindep')
        xy_nopt      = cfg.getint(s, 'xy_nopt')
        ib           = (cfg.get(s, 'ib')).split(' ')
        priorsdrm0   = [float(val) for val in(cfg.get(s, 'priorsdrm0')).split()]
        azp          = cfg.getfloat(s, 'azp')
        med_val_flag = cfg.getboolean(s, 'med_val_flag')
        op_pa_flag   = cfg.getboolean(s, 'op_pa_flag')
        ntr_flag     = cfg.getboolean(s, 'ntr_flag')
        ref_flag     = cfg.getboolean(s, 'ref_flag')
        ps_flag      = cfg.getboolean(s, 'ps_flag')

        #       centroid moment tensor WCMT
        w_mrr           = cfg.getfloat(s, 'W_Mrr')
        w_mtt           = cfg.getfloat(s, 'W_Mtt')
        w_mpp           = cfg.getfloat(s, 'W_Mpp')
        w_mrt           = cfg.getfloat(s, 'W_Mrt')
        w_mrp           = cfg.getfloat(s, 'W_Mrp')
        w_mtp           = cfg.getfloat(s, 'W_Mtp')
        w_time_shift    = cfg.getfloat(s, 'W_time_shift')
        w_half_duration = cfg.getfloat(s, 'W_half_duration')
        w_latitude      = cfg.getfloat(s, 'W_latitude')
        w_longitude     = cfg.getfloat(s, 'W_longitude')
        w_depth         = cfg.getfloat(s, 'W_depth')
        w_m0            = cfg.getfloat(s, 'W_M0')
        w_mw            = cfg.getfloat(s, 'W_Mw')
        dc_flag         = cfg.getboolean(s, 'DC_FLAG')

        #       best nodal planes WCMT
        w_np1_strike = cfg.getfloat(s, 'W_NP1_strike')
        w_np1_dip    = cfg.getfloat(s, 'W_NP1_dip')
        w_np1_rake   = cfg.getfloat(s, 'W_NP1_rake')
        w_np2_strike = cfg.getfloat(s, 'W_NP2_strike')
        w_np2_dip    = cfg.getfloat(s, 'W_NP2_dip')
        w_np2_rake   = cfg.getfloat(s, 'W_NP2_rake')

        #       eigenvalues WCMT
        w_eig_t = cfg.getfloat(s, 'W_eig_T')
        w_eig_n = cfg.getfloat(s, 'W_eig_N')
        w_eig_p = cfg.getfloat(s, 'W_eig_P')
        w_azm_t = cfg.getfloat(s, 'W_azm_T')
        w_azm_n = cfg.getfloat(s, 'W_azm_N')
        w_azm_p = cfg.getfloat(s, 'W_azm_P')
        w_plg_t = cfg.getfloat(s, 'W_plg_T')
        w_plg_n = cfg.getfloat(s, 'W_plg_N')
        w_plg_p = cfg.getfloat(s, 'W_plg_P')

        #       centroid moment tensor RCMT
        r_mrr           = cfg.getfloat(s, 'R_Mrr')
        r_mtt           = cfg.getfloat(s, 'R_Mtt')
        r_mpp           = cfg.getfloat(s, 'R_Mpp')
        r_mrt           = cfg.getfloat(s, 'R_Mrt')
        r_mrp           = cfg.getfloat(s, 'R_Mrp')
        r_mtp           = cfg.getfloat(s, 'R_Mtp')
        r_time_shift    = cfg.getfloat(s, 'R_time_shift')
        r_half_duration = cfg.getfloat(s, 'R_half_duration')
        r_latitude      = cfg.getfloat(s, 'R_latitude')
        r_longitude     = cfg.getfloat(s, 'R_longitude')
        r_depth         = cfg.getfloat(s, 'R_depth')
        r_m0            = cfg.getfloat(s, 'R_M0')
        r_mw            = cfg.getfloat(s, 'R_Mw')

        #       best nodal planes RCMT
        r_np1_strike = cfg.getfloat(s, 'R_NP1_strike')
        r_np1_dip    = cfg.getfloat(s, 'R_NP1_dip')
        r_np1_rake   = cfg.getfloat(s, 'R_NP1_rake')
        r_np2_strike = cfg.getfloat(s, 'R_NP2_strike')
        r_np2_dip    = cfg.getfloat(s, 'R_NP2_dip')
        r_np2_rake   = cfg.getfloat(s, 'R_NP2_rake')

        #       eigenvalues RCMT
        r_eig_t = cfg.getfloat(s, 'R_eig_T')
        r_eig_n = cfg.getfloat(s, 'R_eig_N')
        r_eig_p = cfg.getfloat(s, 'R_eig_P')

        #       filter parameters
        filt_order = cfg.getint(s, 'filt_order')
        filt_cf1   = cfg.getfloat(s, 'filt_cf1')
        filt_cf2   = cfg.getfloat(s, 'filt_cf2')
        filt_pass  = cfg.getint(s, 'filt_pass')

        #       screening parameters
        if s == 'wp_med':
            med_val = cfg.getfloat(s, 'med_val')
            p2p_med = cfg.getfloat(s, 'p2p_med')
            p2p_min = cfg.getfloat(s, 'p2p_min')
            p2p_max = cfg.getfloat(s, 'p2p_max')
            average = cfg.getfloat(s, 'average')
        else:
            med_val = None
            p2p_med = None
            p2p_min = None
            p2p_max = None
            average = None

        #       used data
        nb_stations          = cfg.getint(s, 'nb_stations')
        nb_channels          = cfg.getint(s, 'nb_channels')
        nb_rejected_channels = cfg.getint(s, 'nb_rejected_channels')
        stations             = (cfg.get(s, 'stations')).split(' ')
        wpwin                = [float(val) for val in(cfg.get(s, 'WPWIN')).split()]
        dmin                 = cfg.getfloat(s, 'Dmin')
        dmax                 = cfg.getfloat(s, 'Dmax')
        wn                   = cfg.getfloat(s, 'wN')
        we                   = cfg.getfloat(s, 'wE')
        wz                   = cfg.getfloat(s, 'wZ')

        #       inversion parameters
        command_line = cfg.get(s, 'command_line')
        ref_solution = cfg.get(s, 'ref_solution')
        cond_thre    = cfg.getfloat(s, 'cond_thre')
        damp_fac     = cfg.getfloat(s, 'damp_fac')

        #       quality control
        wrms        = cfg.getfloat(s, 'WRMS')
        wrms_r      = cfg.getfloat(s, 'WRMS_r')
        gap         = cfg.getfloat(s, 'Gap')
        if dc_flag :
            cond_number = cfg.getfloat(s, 'Cond_number')
        else :
            cond_number = None
        rrms        = cfg.getfloat(s, 'RRMS')
        rrms_r      = cfg.getfloat(s, 'RRMS_r')

        # Entering SOLUTION data into database
        test_query = """SELECT id 
                        FROM wphase_solution 
                        WHERE event_id=%s AND status=%s"""
        test_data  = (eventid, status)
        cur.execute(test_query, test_data)
        rows = cur.fetchall()
        if rows :
            # Deleting existing solution from database
            clean_query = """ DELETE FROM wphase_solution
                              WHERE event_id=%s AND status=%s"""
            clean_data = (eventid, status)
            cur.execute(clean_query, clean_data)
            print ("A solution was deleted to be replaced")
            # Deleting existing picture (standard format)
            file_path = '/home/lucile/wphase_catalog/media/' +eventid+ '_' +status+ '.png'
            if os.path.isfile(file_path):
                os.remove(file_path)
                print ("The solution's picture was removed")

        query = """INSERT INTO wphase_solution(event_id, status, code_version, gf_path,
                                   o_covf, o_cmtf, cmtfile, th_val, rms_r_th, cth_val, df_val,
                                   ts_nit, dts_val, dts_min, dts_max, dts_step, hdsafe, 
                                   xy_nit, xy_dx, xy_nx, dz, mindep, xy_nopt, ib, priorsdrm0,
                                   azp, med_val_flag, op_pa_flag, ntr_flag, ref_flag, ps_flag,
                                   w_mrr, w_mtt, w_mpp, w_mrt, w_mrp, w_mtp, 
                                   w_time_shift, w_half_duration, w_latitude, w_longitude, w_depth, 
                                   w_m0, w_mw, dc_flag,
                                   w_np1_strike, w_np1_dip, w_np1_rake, w_np2_strike, w_np2_dip, w_np2_rake,
                                   w_eig_t, w_eig_n, w_eig_p,
                                   w_azm_t, w_azm_n, w_azm_p, w_plg_t, w_plg_n, w_plg_p,
                                   r_mrr, r_mtt, r_mpp, r_mrt, r_mrp, r_mtp,
                                   r_time_shift, r_half_duration, r_latitude, r_longitude, r_depth,
                                   r_m0, r_mw,
                                   r_np1_strike, r_np1_dip, r_np1_rake, r_np2_strike, r_np2_dip, r_np2_rake,
                                   r_eig_t, r_eig_n, r_eig_p,
                                   filt_order, filt_cf1, filt_cf2, filt_pass,
                                   med_val, p2p_med, p2p_min, p2p_max, average,
                                   nb_stations, nb_channels, nb_rejected_channels, 
                                   stations, wpwin, dmin, dmax, wn, we, wz,
                                   command_line, ref_solution, cond_thre, damp_fac,
                                   wrms, wrms_r, gap, cond_number, rrms, rrms_r)
                       VALUES (%s, %s, %s, %s, 
                               %s, %s, %s, %s, %s, %s, 
                               %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, 
                               %s, %s, %s,
                               %s, %s, %s, %s, %s, %s,
                               %s, %s, %s,
                               %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s, %s,
                               %s, %s,
                               %s, %s, %s, %s, %s, %s,
                               %s, %s, %s,
                               %s, %s, %s, %s,
                               %s, %s, %s, %s, %s,
                               %s, %s, %s, 
                               %s, %s, %s, %s, %s, %s, %s,
                               %s, %s, %s, %s,
                               %s, %s, %s, %s, %s, %s)"""
        data = (eventid, status, code_version, gf_path,
               o_covf, o_cmtf, cmtfile, th_val, rms_r_th, cth_val, df_val,
               ts_nit, dts_val, dts_min, dts_max, dts_step, hdsafe, 
               xy_nit, xy_dx, xy_nx, dz, mindep, xy_nopt, ib, priorsdrm0,
               azp, med_val_flag, op_pa_flag, ntr_flag, ref_flag, ps_flag,
               w_mrr, w_mtt, w_mpp, w_mrt, w_mrp, w_mtp, 
               w_time_shift, w_half_duration, w_latitude, w_longitude, w_depth, 
               w_m0, w_mw, dc_flag,
               w_np1_strike, w_np1_dip, w_np1_rake, w_np2_strike, w_np2_dip, w_np2_rake,
               w_eig_t, w_eig_n, w_eig_p,
               w_azm_t, w_azm_n, w_azm_p, w_plg_t, w_plg_n, w_plg_p,
               r_mrr, r_mtt, r_mpp, r_mrt, r_mrp, r_mtp,
               r_time_shift, r_half_duration, r_latitude, r_longitude, r_depth,
               r_m0, r_mw,
               r_np1_strike, r_np1_dip, r_np1_rake, r_np2_strike, r_np2_dip, r_np2_rake,
               r_eig_t, r_eig_n, r_eig_p,
               filt_order, filt_cf1, filt_cf2, filt_pass,
               med_val, p2p_med, p2p_min, p2p_max, average,
               nb_stations, nb_channels, nb_rejected_channels, 
               stations, wpwin, dmin, dmax, wn, we, wz,
               command_line, ref_solution, cond_thre, damp_fac,
               wrms, wrms_r, gap, cond_number, rrms, rrms_r)
        cur.execute(query, data)
        conn.commit()


    cur.close()
    conn.close()
    print "Data successfully entered into database !"


if __name__=='__main__':
    main(sys.argv)
