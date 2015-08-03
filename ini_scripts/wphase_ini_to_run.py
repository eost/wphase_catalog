#!/usr/bin/env python
# wphase_ini_to_db.py
"""
Reads the ini file parsed as argument
and enters the corresponding data into db_wphase database

THIS PROGRAM IS MEANT TO TAKE PLACE AT THE WPHASE ROOT
MAKE THE ADEQUATE CHANGES IF YOU DECIDE TO MOVE IT
"""

import sys, os
import ConfigParser


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
    cfg.remove_section('prepare__dec_filt')
    s = cfg.sections()[0]

    # Creating run folder
    folder = "runs/" + cfg.get(s, 'eventid')
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Creating CMTSOLUTION

    capsule        = [" "] * 85
    capsule[1:4]   = cfg.get(s, 'EPI_agency')
    capsule[5:8]   = cfg.get(s, 'EPI_year')
    capsule[9]    = " "
    capsule[10:11] = cfg.get(s, 'EPI_month')
    capsule[12]    = " "
    capsule[13:14] = cfg.get(s, 'EPI_day')
    capsule[15]    = " "
    capsule[16:17] = cfg.get(s, 'EPI_hour')
    capsule[18]    = " "
    capsule[19:20] = cfg.get(s, 'EPI_minute')
    capsule[21]    = " "
    capsule[22:26] = cfg.get(s, 'EPI_second')
    capsule[27]    = " "
    capsule[28:35] = cfg.get(s, 'EPI_latitude')
    capsule[36]    = " "
    capsule[37:45] = cfg.get(s, 'EPI_longitude')
    capsule[46]    = " "
    capsule[47:51] = cfg.get(s, 'EPI_depth')
    capsule[52]    = " "
    capsule[53:55] = cfg.get(s, 'EPI_M1')
    capsule[56]    = " "
    capsule[57:59] = cfg.get(s, 'EPI_M2')
    capsule[60]    = " "
    capsule[61:]   = cfg.get(s, 'EPI_region')

    eventid       = cfg.get(s, 'eventid')
    time_shift    = cfg.get(s, 'R_time_shift')
    half_duration = cfg.get(s, 'R_half_duration')
    latitude      = cfg.get(s, 'R_latitude')
    longitude     = cfg.get(s, 'R_longitude')
    depth         = cfg.get(s, 'R_depth')
    mrr           = cfg.get(s, 'R_Mrr')
    mtt           = cfg.get(s, 'R_Mtt')
    mpp           = cfg.get(s, 'R_Mpp')
    mrt           = cfg.get(s, 'R_Mrt')
    mrp           = cfg.get(s, 'R_Mrp')
    mtp           = cfg.get(s, 'R_Mtp')

    cmttxt  = ''.join(capsule) + "\n"
    cmttxt += "event name:     " + eventid       + "\n"
    cmttxt += "time shift:     " + time_shift    + "\n"
    cmttxt += "half duration:  " + half_duration + "\n"
    cmttxt += "latitude:       " + latitude      + "\n"
    cmttxt += "longitude:      " + longitude     + "\n"
    cmttxt += "depth:          " + depth         + "\n"
    cmttxt += "Mrr:            " + mrr           + "\n"
    cmttxt += "Mtt:            " + mtt           + "\n"
    cmttxt += "Mpp:            " + mpp           + "\n"
    cmttxt += "Mrt:            " + mrt           + "\n"
    cmttxt += "Mrp:            " + mrp           + "\n"
    cmttxt += "Mtp:            " + mtp           + "\n"

    cmt_path = folder + "/CMTSOLUTION"
    cmt = open(cmt_path, "w");
    cmt.write(cmttxt)
    cmt.close()

    # Creating i_master

    evname      = cfg.get(s, 'EPI_region').replace(" ", "_")
    seed        = cfg.get(s, 'SEED')
    dmin        = cfg.get(s, 'i_DMIN')
    dmax        = cfg.get(s, 'i_DMAX')
    cmtfile     = cfg.get(s, 'cmtfile')
    filt_order  = cfg.get(s, 'filt_order')
    filt_cf1    = cfg.get(s, 'filt_cf1')
    filt_cf2    = cfg.get(s, 'filt_cf2')
    filt_pass   = cfg.get(s, 'filt_pass')
    idec_2      = cfg.get(s, 'IDEC_2').split()
    idec_3      = cfg.get(s, 'IDEC_3').split()
    gfdir       = cfg.get(s, 'GFDIR')
    wp_win      = cfg.get(s, 'WPWIN').split()
    twptt       = cfg.get(s, 'TWPTT')
    p2p_fac_min = cfg.get(s, 'p2p_fac_min')
    p2p_fac_max = cfg.get(s, 'p2p_fac_max')
    ts_nit      = cfg.get(s, 'ts_Nit')
    ts_dt       = cfg.get(s, 'dts_step')
    tsbounds    = [cfg.get(s, 'dts_min'), cfg.get(s, 'dts_max')]
    xy_nit      = cfg.get(s, 'xy_Nit')
    xy_dx       = cfg.get(s, 'xy_dx')
    xy_nx       = cfg.get(s, 'xy_nx')
    xy_nopt     = cfg.get(s, 'xy_nopt')
    ddep        = cfg.get(s, 'dz')
    mindep      = cfg.get(s, 'mindep')
    length_global   = cfg.get(s, 'tr_LENGTH_GLOBAL')
    length_regional = cfg.get(s, 'tr_LENGTH_REGIONAL')
    dlat = cfg.get(s, 'tr_DLAT')
    dlon = cfg.get(s, 'tr_DLON')
    opdffile = cfg.get(s, 'tr_OPDFFILE')
    ylimauto = cfg.get(s, 'tr_YLIMAUTO')
    ylimfixed = (cfg.get(s, 'tr_YLIMFIXED')).split('  ')
    nc = cfg.get(s, 'tr_NC')
    nl = cfg.get(s, 'tr_NL')

    imastxt  = "EVNAME:          " + evname      + "\n"
    imastxt += "SEED:            " + seed        + "\n"
    imastxt += "DMIN:            " + dmin        + "\n"
    imastxt += "DMAX:            " + dmax        + "\n"
    imastxt += "CMTFILE:         " + cmtfile     + "\n"
    imastxt += "\n"
    imastxt += "filt_order:      " + filt_order  + "\n"
    imastxt += "filt_cf1:        " + filt_cf1    + "\n"
    imastxt += "filt_cf2:        " + filt_cf2    + "\n"
    imastxt += "filt_pass:       " + filt_pass   + "\n"
    imastxt += "IDEC_2:          " 
    for val in idec_2 :
        imastxt += val + "   "
    imastxt += "\n"
    imastxt += "IDEC_3:          " 
    for val in idec_3 :
        imastxt += val + "   "
    imastxt += "\n\n"
    imastxt += "GFDIR:           " + gfdir[:-1]       + "\n"
    imastxt += "WP_WIN:          " 
    if wp_win[0] != "0.00" :
        imastxt += wp_win[0] + "   "
    if wp_win[1] != "0.00" :
        imastxt += wp_win[1] + "   "
    if wp_win[2] != "0.00" :
        imastxt += wp_win[2] + "   "
    if wp_win[3] != "180.00" :
        imastxt += wp_win[3] + "   "
    imastxt += "\n\n"
    if twptt != "1" :
        imastxt += "TWPTT:           " + twptt       + "\n"
    if p2p_fac_min != "0.1" :
        imastxt += "p2p_fac_min:     " + p2p_fac_min + "\n"
    if p2p_fac_max != "3.0" :
        imastxt += "p2p_fac_max:     " + p2p_fac_max + "\n\n"
    if ts_nit != "3" :
        imastxt += "TS_NIT:          " + ts_nit      + "\n"
    if ts_dt != "4.000000" :
        imastxt += "TS_DT:           " + ts_dt       + "\n"
    if tsbounds != ["1.000000", "168.000000"] :
        imastxt += "TSBOUNDS:        " 
        for val in tsbounds :
            imastxt += val + "   "
        imastxt += "\n"
    if "wp_z" in cfg.sections() :
        if xy_nit != "1" :
            imastxt += "XYZ_NIT:          " + xy_nit      + "\n"
        if xy_dx != "0.600000" :
            imastxt += "XYZ_DX:           " + xy_dx       + "\n"
        if xy_nx != "1" :
            imastxt += "XYZ_NX:           " + xy_nx       + "\n"
        if xy_nopt != "4" :
            imastxt += "XYZ_NOPT:         " + xy_nopt     + "\n"
        if ddep != "50.000000" :
            imastxt += "DDEP:             " + ddep        + "\n"
        if mindep != "11.500000" :
            imastxt += "MINDEP:           " + mindep      + "\n\n"
    else :
        if xy_nit != "3" :
            imastxt += "XY_NIT:           " + xy_nit      + "\n"
        if xy_dx != "0.400000" :
            imastxt += "XY_DX:            " + xy_dx       + "\n"
        if xy_nx != "3" :
            imastxt += "XY_NX:            " + xy_nx       + "\n"
        if xy_nopt != "5" :
            imastxt += "XY_NOPT:          " + ny_nopt     + "\n\n"

    if length_global != "3000" :
        imastxt += "LENGTH_GLOBAL:   " + length_global   + "\n"
    if length_regional != "1500" :
        imastxt += "LENGTH_REGIONAL: " + length_regional + "\n"
    if dlat != "20.000000" :
        imastxt += "DLAT:            " + dlat            + "\n"
    if dlon != "20.000000" :
        imastxt += "DLON:            " + dlon            + "\n"
    if opdffile != "wp_pages.pdf" :
        imastxt += "OPDFFILE:        " + opdffile        + "\n"
    if ylimauto != "True" :
        imastxt += "YLIM_AUTO:       " + length_global   + "\n"
    if ylimfixed != ["-9", "12"] :
        imastxt += "YLIMFIXED:       " 
        for val in ylimfixed :
            imastxt += val + "   "
        imastxt += "\n"
    if nc != "3" :
        imastxt += "NC:              " + nc              + "\n"
    if nl != "5" :
        imastxt += "NL:              " + nl              + "\n"

    imas_path = folder + "/i_master"
    imas = open(imas_path, "w");
    imas.write(imastxt)
    imas.close()


if __name__=='__main__':
    main(sys.argv)
