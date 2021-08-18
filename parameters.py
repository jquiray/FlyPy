# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:19:18 2021

@author: Matko
"""
# imports are defined IN the .py file they are used in, BEFORE definig func
import numpy as np
from ISAfunction import ISAfunny
from func_b2_constraint_analysis import tw_constant_level_velocity_turn
from func_b2_constraint_analysis import tw_desired_specific_energy_level
from func_b2_constraint_analysis import tw_desired_rate_of_climb
from func_b2_constraint_analysis import tw_desired_TO_distance
from func_b2_constraint_analysis import tw_desired_cruise_airspeed
from func_b2_constraint_analysis import tw_service_ceiling
from func_b2_constraint_analysis import clmax_ws_func
# 
def mainparameters(ws_params,alt,V,mtow,ar,C_Dmin,n,P_S,V_v,C_DTO,C_LTO,S_G,mu_gr,V_LOF,V_vx,alt_sc,alt_TO,V_stall,eta_prop):
    """
    Main parameters function

    Parameters
    ----------
    alt : float
        Altitude in [m].
    mach : float
        Velocity in Mach.
    mtow : float
        Maximum Take-Off Weight in [N].
    ar : float
        Aspect Ratio of wings.
    C_Dmin : float
        Zero-lift drag.
    P_S : float
        Turn excess energy.

    Returns
    -------
    All other necessary stuff.

    """
    # Atmosphere
    T,p,rho,mu,a = ISAfunny(alt)
    
    # Velocity, TAS [m/s]
    V = V # V = mach*a
    
    # Weight, [N]
    W = mtow
    
    # Dynamic pressure
    q = 0.5*rho*V**2
    
    # Oswald's wing efficiency factor
    e = 1.78*(1-0.045*ar**0.68)-0.64
    
    # Lift-induced drag component
    k = 1/(np.pi*ar*e)
    
    T_TO,P_TO,rho_TO,mu_TO,a_TO = ISAfunny(alt_TO)
    q2 = 0.5*rho_TO*V_vx**2
    n2 = 1
    
    V3 = V_LOF/ (2**0.5)
    q3 = 0.5*rho_TO*V3**2
    
    T_sc,P_sc,rho_sc,mu_sc,a_sc = ISAfunny(alt_sc)
    
    # ws range
    ws = np.linspace(ws_params[0],ws_params[1],ws_params[2])
    tw_clvt_list = []
    tw_dsel_list = []
    tw_droc_list = []
    tw_dtod_list = []
    tw_dca_list = []
    tw_sc_list = []
    clmax_list = []
    
    S_list = []
    for ind, val in enumerate(ws):
        tw_clvt = tw_constant_level_velocity_turn(q, C_Dmin, ws[ind], k, n)
        tw_clvt_list.append(tw_clvt)
        
        tw_dsel = tw_desired_specific_energy_level(q2, C_Dmin, ws[ind], k, n2, V_v, V_vx)
        tw_dsel_list.append(tw_dsel)
        
        # tw_droc = tw_desired_rate_of_climb(q, C_Dmin, ws[ind], k, V_v, rho)
        # tw_droc_list.append(tw_droc)
        
        tw_dtod = tw_desired_TO_distance(q3, C_DTO, C_LTO, ws[ind], S_G, mu_gr, V_LOF)
        tw_dtod_list.append(tw_dtod)
        
        tw_dca = tw_desired_cruise_airspeed(q, C_Dmin, ws[ind], k)
        tw_dca_list.append(tw_dca)
        
        tw_sc = tw_service_ceiling(C_Dmin, ws[ind], k, rho_sc)
        tw_sc_list.append(tw_sc)
        
        clmax = clmax_ws_func(ws[ind], rho_TO, V_stall)
        clmax_list.append(clmax)
        
        S = W/ws[ind]
        S_list.append(S)
    
    tohp = 1.341
    #--------------------------------------------------
    pw_clvt_list = []
    pwsl_clvt_list = []
    t_clvt_mass_list = []
    p_clvt_mass_list = []
    psl_clvt_mass_list = []
    for tw in tw_clvt_list:
        
        pw = 0.001*(tw*V)/eta_prop*1.341
        pwSL = pw / ( 1.132*rho/rho_TO - 0.132 )
        pw_clvt_list.append(pw)
        pwsl_clvt_list.append(pwSL)
        t_clvt_mass = tw*W
        t_clvt_mass_list.append(t_clvt_mass)
        p_clvt_mass = pw * W
        p_clvt_mass_list.append(p_clvt_mass)
        psl_clvt_mass = pwSL * W
        psl_clvt_mass_list.append(psl_clvt_mass)
    #--------------------------------------------------
    pw_dsel_list = []
    pwsl_dsel_list = []
    t_dsel_mass_list = []
    p_dsel_mass_list = []
    psl_dsel_mass_list = []
    for tw in tw_dsel_list:
        
        pw = 0.001*(tw*V_vx)/eta_prop*1.341
        pwSL = pw / ( 1.132*rho_TO/rho_TO - 0.132 )
        pw_dsel_list.append(pw)
        pwsl_dsel_list.append(pwSL)
        t_dsel_mass = tw*W
        t_dsel_mass_list.append(t_dsel_mass)
        p_dsel_mass = pw * W
        p_dsel_mass_list.append(p_dsel_mass)
        psl_dsel_mass = pwSL * W
        psl_dsel_mass_list.append(psl_dsel_mass)
    #--------------------------------------------------
    pw_dtod_list = []
    pwsl_dtod_list = []
    t_dtod_mass_list = []
    p_dtod_mass_list = []
    psl_dtod_mass_list = []
    
    for tw in tw_dtod_list:
        # thr = (item*W)
        pw = 0.001*(tw*V_vx)/eta_prop*1.341
        pwSL = pw / ( 1.132*rho_TO/rho_TO - 0.132 )
        pw_dtod_list.append(pw)
        pwsl_dtod_list.append(pwSL)
        t_dtod_mass = tw*W
        t_dtod_mass_list.append(t_dtod_mass)
        p_dtod_mass = pw * W
        p_dtod_mass_list.append(p_dtod_mass)
        psl_dtod_mass = pwSL * W
        psl_dtod_mass_list.append(psl_dtod_mass)
    #--------------------------------------------------
    pw_dca_list = []
    pwsl_dca_list = []
    t_dca_mass_list = []
    p_dca_mass_list = []
    psl_dca_mass_list = []
    
    for tw in tw_dca_list:
        # thr = (item*W)
        pw = 0.001*(tw*V)/eta_prop*1.341
        pwSL = pw / ( 1.132*rho/rho_TO - 0.132 )
        pw_dca_list.append(pw)
        pwsl_dca_list.append(pwSL)
        t_dca_mass = tw*W
        t_dca_mass_list.append(t_dca_mass)
        p_dca_mass = pw * W
        p_dca_mass_list.append(p_dca_mass)
        psl_dca_mass = pwSL * W
        psl_dca_mass_list.append(psl_dca_mass)
    #--------------------------------------------------
    pw_sc_list = []
    pwsl_sc_list = []
    t_sc_mass_list = []
    p_sc_mass_list = []
    psl_sc_mass_list = []
    
    for tw in tw_sc_list:
        # thr = (item*W)
        pw = 0.001*(tw*V)/eta_prop*1.341
        pwSL = pw / ( 1.132*rho_sc/rho_TO - 0.132 )
        pw_sc_list.append(pw)
        pwsl_sc_list.append(pwSL)
        t_sc_mass = tw*W
        t_sc_mass_list.append(t_sc_mass)
        p_sc_mass = pw * W
        p_sc_mass_list.append(p_sc_mass)
        psl_sc_mass = pwSL * W
        psl_sc_mass_list.append(psl_sc_mass)
    #--------------------------------------------------
    #--------------------------------------------------
    
    
    return T,p,rho,mu,a,V,q,e,k,ws,tw_clvt_list,tw_dsel_list,tw_dtod_list,tw_dca_list,tw_sc_list,pw_clvt_list,pwsl_clvt_list,t_clvt_mass_list,p_clvt_mass_list,psl_clvt_mass_list,pw_dsel_list,pwsl_dsel_list,t_dsel_mass_list,p_dsel_mass_list,psl_dsel_mass_list,pw_dtod_list,pwsl_dtod_list,t_dtod_mass_list,p_dtod_mass_list,psl_dtod_mass_list,pw_dca_list,pwsl_dca_list,t_dca_mass_list,p_dca_mass_list,psl_dca_mass_list,pw_sc_list,pwsl_sc_list,t_sc_mass_list,p_sc_mass_list,psl_sc_mass_list,S_list,clmax_list

def designpoint(DP_ws,DP_tw,alt,V,mtow,ar,C_Dmin,n,P_S,V_v,C_DTO,C_LTO,S_G,mu_gr,V_LOF,V_vx,alt_sc,alt_TO,V_stall,eta_prop):
    """
    

    Parameters
    ----------
    DP_ws : TYPE
        DESCRIPTION.
    DP_tw : TYPE
        DESCRIPTION.
    alt : TYPE
        DESCRIPTION.
    V : TYPE
        DESCRIPTION.
    mtow : TYPE
        DESCRIPTION.
    ar : TYPE
        DESCRIPTION.
    C_Dmin : TYPE
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.
    P_S : TYPE
        DESCRIPTION.
    V_v : TYPE
        DESCRIPTION.
    C_DTO : TYPE
        DESCRIPTION.
    C_LTO : TYPE
        DESCRIPTION.
    S_G : TYPE
        DESCRIPTION.
    mu_gr : TYPE
        DESCRIPTION.
    V_LOF : TYPE
        DESCRIPTION.
    V_vx : TYPE
        DESCRIPTION.
    alt_sc : TYPE
        DESCRIPTION.
    alt_TO : TYPE
        DESCRIPTION.
    V_stall : TYPE
        DESCRIPTION.
    eta_prop : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # Atmosphere
    T,p,rho,mu,a = ISAfunny(alt)
    
    # Velocity, TAS [m/s]
    V = V # V = mach*a
    
    # Dynamic pressure
    q = 0.5*rho*V**2
    
    # Oswald's wing efficiency factor
    e = 1.78*(1-0.045*ar**0.68)-0.64
    
    # Lift-induced drag component
    k = 1/(np.pi*ar*e)
    
    T_TO,P_TO,rho_TO,mu_TO,a_TO = ISAfunny(alt_TO)
    q2 = 0.5*rho_TO*V_vx**2
    n2 = 1
    
    V3 = V_LOF/ (2**0.5)
    q3 = 0.5*rho_TO*V3**2
    
    T_sc,P_sc,rho_sc,mu_sc,a_sc = ISAfunny(alt_sc)
    
    tw_clvt = tw_constant_level_velocity_turn(q, C_Dmin, DP_ws, k, n)
    tw_dsel = tw_desired_specific_energy_level(q2, C_Dmin, DP_ws, k, n2, V_v, V_vx)
    # tw_droc = tw_desired_rate_of_climb(q, C_Dmin, DP_ws, k, V_v, rho)
    tw_dtod = tw_desired_TO_distance(q3, C_DTO, C_LTO, DP_ws, S_G, mu_gr, V_LOF)
    tw_dca = tw_desired_cruise_airspeed(q, C_Dmin, DP_ws, k)
    tw_sc = tw_service_ceiling(C_Dmin, DP_ws, k, rho_sc)
    
    DP_pw = 0.001*(DP_tw*V)/eta_prop*1.341
    DP_pwsl = DP_pw / ( 1.132*rho/rho_TO - 0.132 )
    Thr = DP_tw*mtow
    P_watt = (Thr*V)/eta_prop
    P_kw = 0.001*P_watt
    P_hp = P_kw*1.341
    
    sigma = rho/rho_TO
    P_hpSL = P_hp / ( 1.132*sigma - 0.132 ) # Gagg and Ferrar model for pistoned propellers, snorri equation (7-16)
    
    DP_S = mtow/DP_ws
    
    clmax = clmax_ws_func(DP_ws, rho_TO, V_stall)
    
    return tw_clvt,tw_dsel,tw_dtod,tw_dca,tw_sc,DP_pw,DP_pwsl,Thr,P_kw,P_hp,P_hpSL,DP_S,clmax