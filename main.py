# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:39:01 2021

@author: Matko
"""
#%% 01 IMPORTS
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Implement the canvas thing, so Frame[Canvas[Subplot[Plot] ] ]
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk # Implement the Matplotlib toolbar
from matplotlib.backend_bases import key_press_handler # Implement the default Matplotlib key bindings
from matplotlib.figure import Figure
from parameters import mainparameters
from parameters import designpoint

#%% 02 Units Functions

def altitudeunits(value):
    global label5
    global label42
    global label44
    if value == 1:
        if label5.cget("text") == "[ft]":
            label5.grid_forget()
            label5 = tk.Label(frame3, text='[m]')
            label5.grid(row=0, column=2, sticky="w")
            a = str(round(float(entry1.get())*0.3048,1))
            entry1.delete(0,99)
            entry1.insert(tk.END, a)
            
            label42.grid_forget()
            label42 = tk.Label(frame3, text='[m]')
            label42.grid(row=14, column=2, sticky="w")
            b = str(round(float(entry15.get())*0.3048,1))
            entry15.delete(0,99)
            entry15.insert(tk.END, b)
            
            label44.grid_forget()
            label44 = tk.Label(frame3, text='[m]')
            label44.grid(row=15, column=2, sticky="w")
            c = str(round(float(entry16.get())*0.3048,1))
            entry16.delete(0,99)
            entry16.insert(tk.END, c)
        else:
            return
    if value == 2:
        if label5.cget("text") == "[m]":
            label5.grid_forget()
            label5 = tk.Label(frame3, text='[ft]', fg=col2)
            label5.grid(row=0, column=2, sticky="w")
            a = str(round(float(entry1.get())/0.3048))
            entry1.delete(0,99)
            entry1.insert(tk.END, a)
            
            label42.grid_forget()
            label42 = tk.Label(frame3, text='[ft]', fg=col2)
            label42.grid(row=14, column=2, sticky="w")
            b = str(round(float(entry15.get())/0.3048))
            entry15.delete(0,99)
            entry15.insert(tk.END, b)
            
            label44.grid_forget()
            label44 = tk.Label(frame3, text='[ft]', fg=col2)
            label44.grid(row=15, column=2, sticky="w")
            c = str(round(float(entry16.get())/0.3048))
            entry16.delete(0,99)
            entry16.insert(tk.END, c)
        else:
            return

def velocityunits(value):
    global label6
    global label38
    global label40
    global label46
    if value == 1:
        if label6.cget("text") == "[kn]":
            label6.grid_forget()
            label6 = tk.Label(frame3, text='[m/s]')
            label6.grid(row=1, column=2, sticky="w")
            a = str(round(float(entry2.get())*0.5144,2))
            entry2.delete(0,99)
            entry2.insert(tk.END, a)
            
            label38.grid_forget()
            label38 = tk.Label(frame3, text='[m/s]')
            label38.grid(row=12, column=2, sticky="w")
            b = str(round(float(entry13.get())*0.5144,2))
            entry13.delete(0,99)
            entry13.insert(tk.END, b)
            
            label40.grid_forget()
            label40 = tk.Label(frame3, text='[m/s]')
            label40.grid(row=13, column=2, sticky="w")
            c = str(round(float(entry14.get())*0.5144,2))
            entry14.delete(0,99)
            entry14.insert(tk.END, c)
            
            label46.grid_forget()
            label46 = tk.Label(frame3, text='[m/s]')
            label46.grid(row=16, column=2, sticky="w")
            d = str(round(float(entry17.get())*0.5144,2))
            entry17.delete(0,99)
            entry17.insert(tk.END, d)
            
            # label46 # v_vx
            # entry17
        else:
            return
    if value == 2:
        if label6.cget("text") == "[m/s]":
            label6.grid_forget()
            label6 = tk.Label(frame3, text='[kn]', fg=col1)
            label6.grid(row=1, column=2, sticky="w")
            a = str(round(float(entry2.get())/0.5144,1))
            entry2.delete(0,99)
            entry2.insert(tk.END, a)
            
            label38.grid_forget()
            label38 = tk.Label(frame3, text='[kn]', fg=col1)
            label38.grid(row=12, column=2, sticky="w")
            b = str(round(float(entry13.get())/0.5144,1))
            entry13.delete(0,99)
            entry13.insert(tk.END, b)
            
            label40.grid_forget()
            label40 = tk.Label(frame3, text='[kn]', fg=col1)
            label40.grid(row=13, column=2, sticky="w")
            c = str(round(float(entry14.get())/0.5144,1))
            entry14.delete(0,99)
            entry14.insert(tk.END, c)
            
            label46.grid_forget()
            label46 = tk.Label(frame3, text='[kn]', fg=col1)
            label46.grid(row=16, column=2, sticky="w")
            d = str(round(float(entry17.get())/0.5144,1))
            entry17.delete(0,99)
            entry17.insert(tk.END, d)
        else:
            return

col1 = '#0040ff' # blue good
col2 = '#00c030' # green
#%% 03 Functions for Tkinter
def button1fun():
    global label111, label222, label333, label444
    
    if 'label111' in globals():
        label111.destroy()
        label222.destroy()
        label333.destroy()
        label444.destroy()
    
    global ws, tw_clvt_list, tw_dsel_list, tw_droc_list, tw_dtod_list, tw_dca_list, tw_sc_list, clmax_list
    global pw_clvt_list, pw_dsel_list, pw_droc_list, pw_dtod_list, pw_dca_list, pw_sc_list
    global pwsl_clvt_list, pwsl_dsel_list, pwsl_droc_list, pwsl_dtod_list, pwsl_dca_list, pwsl_sc_list
    global S_list, t_clvt_mass_list, t_dsel_mass_list, t_dtod_mass_list, t_dca_mass_list, t_sc_mass_list
    global p_clvt_mass_list, p_dsel_mass_list, p_dtod_mass_list, p_dca_mass_list, p_sc_mass_list
    global psl_clvt_mass_list, psl_dsel_mass_list, psl_dtod_mass_list, psl_dca_mass_list, psl_sc_mass_list
    global DP_pw, DP_pwsl, Thr, P_hp, P_hpSL, DP_S, clmax
    
    "INPUTS"
    ws_params = [200,2960,553] # [start, stop, numsteps] 200,1000,553
    alt = float(entry1.get())
    if r2.get() == 2:
        alt = alt*0.3048
    V = float(entry2.get())
    if r3.get() == 2:
        V = V*0.5144
    mtow = float(entry3.get())*9.81
    ar = float(entry4.get())
    C_Dmin = float(entry5.get())
    n = float(entry6.get())
    P_S = float(entry7.get())
    V_v = float(entry8.get())
    C_DTO = float(entry9.get())
    C_LTO = float(entry10.get())
    S_G = float(entry11.get())
    mu_gr = float(entry12.get())
    V_LOF = float(entry13.get())
    if r3.get() == 2:
        V_LOF = V_LOF*0.5144
    V_vx = float(entry14.get())
    if r3.get() == 2:
        V_vx = V_vx*0.5144
    alt_sc = float(entry15.get())
    if r2.get() == 2:
        alt_sc = alt_sc*0.3048
    alt_TO = float(entry16.get())
    if r2.get() == 2:
        alt_TO = alt_TO*0.3048
    V_stall = float(entry17.get())
    if r3.get() == 2:
        V_stall = V_stall*0.5144
    eta_prop = float(entry18.get())
    DP_ws = float(entry52.get())
    DP_tw = float(entry51.get())
    
    T,p,rho,mu,a,V,q,e,k,ws,tw_clvt_list,tw_dsel_list,tw_dtod_list,tw_dca_list,tw_sc_list,pw_clvt_list,pwsl_clvt_list,t_clvt_mass_list,p_clvt_mass_list,psl_clvt_mass_list,pw_dsel_list,pwsl_dsel_list,t_dsel_mass_list,p_dsel_mass_list,psl_dsel_mass_list,pw_dtod_list,pwsl_dtod_list,t_dtod_mass_list,p_dtod_mass_list,psl_dtod_mass_list,pw_dca_list,pwsl_dca_list,t_dca_mass_list,p_dca_mass_list,psl_dca_mass_list,pw_sc_list,pwsl_sc_list,t_sc_mass_list,p_sc_mass_list,psl_sc_mass_list,S_list,clmax_list = mainparameters(ws_params,alt,V,mtow,ar,C_Dmin,n,P_S,V_v,C_DTO,C_LTO,S_G,mu_gr,V_LOF,V_vx,alt_sc,alt_TO,V_stall,eta_prop)
    
    tw_clvt,tw_dsel,tw_dtod,tw_dca,tw_sc,DP_pw,DP_pwsl,Thr,P_kw,P_hp,P_hpSL,DP_S,clmax = designpoint(DP_ws, DP_tw, alt, V, mtow, ar, C_Dmin, n, P_S, V_v, C_DTO, C_LTO, S_G, mu_gr, V_LOF, V_vx, alt_sc, alt_TO, V_stall, eta_prop)
    
    # entry53.delete(0,99)
    # entry54.delete(0,99)
    # entry55.delete(0,99)
    # entry56.delete(0,99)
    # entry57.delete(0,99)
    # entry58.delete(0,99)
    # entry53.insert(tk.END, str(round(DP_pw,4)))
    # entry54.insert(tk.END, str(round(DP_pwsl,4)))
    # entry55.insert(tk.END, str(round(Thr,1)))
    # entry56.insert(tk.END, str(round(P_hp,1)))
    # entry57.insert(tk.END, str(round(P_hpSL,1)))
    # entry58.insert(tk.END, str(round(DP_S,2)))
    label53 = tk.Label(frame5, text=str(round(DP_pw,4)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label53.grid(row=53, column=1, sticky="w")
    label54 = tk.Label(frame5, text=str(round(DP_pwsl,4)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label54.grid(row=54, column=1, sticky="w")
    label55 = tk.Label(frame5, text=str(round(Thr,1)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label55.grid(row=55, column=1, sticky="w")
    label56 = tk.Label(frame5, text=str(round(P_hp,1)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label56.grid(row=56, column=1, sticky="w")
    label57 = tk.Label(frame5, text=str(round(P_hpSL,1)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label57.grid(row=57, column=1, sticky="w")
    label58 = tk.Label(frame5, text=str(round(DP_S,2)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label58.grid(row=58, column=1, sticky="w")
    label59 = tk.Label(frame5, text=str(round(clmax,2)), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label59.grid(row=59, column=1, sticky="w")

    
    # label111 = tk.Label(frame1, text= 'label111-entry1 is: ' + str( entry1.get() ))
    # label111.pack()
    # label222 = tk.Label(frame1, text= 'label222-entry2 is: ' + str(entry2.get()))
    # label222.pack()
    # label333 = tk.Label(frame1, text= 'label333-entry3 is: ' + str(entry3.get()))
    # label333.pack()
    # label444 = tk.Label(frame1, text= 'label444-entry4 is: ' + str(entry4.get()))
    # label444.pack()
    
    # Atmosphere    
    label14rho = tk.Label(frame7, text=str( round(rho,ndigits=4) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14rho.grid(row=0, column=1, sticky="w")
    label14T = tk.Label(frame7, text=str( round(T-273.15,ndigits=1) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14T.grid(row=1, column=1, sticky="w")
    label14p = tk.Label(frame7, text=str( round(0.001*p,ndigits=3) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14p.grid(row=2, column=1, sticky="w")
    label14mu = tk.Label(frame7, text=str( round(1000000*mu,ndigits=2) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14mu.grid(row=3, column=1, sticky="w")
    label14a = tk.Label(frame7, text=str( round(a,ndigits=2) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label14a.grid(row=4, column=1, sticky="w")
    
    # Aerodynamics
    label13q = tk.Label(frame9, text=str( round(q,ndigits=1) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label13q.grid(row=0, column=1, sticky="w")
    label13Ma = tk.Label(frame9, text=str( round(V/a,ndigits=2) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label13Ma.grid(row=1, column=1, sticky="w")
    label15 = tk.Label(frame9, text=str( round(e,ndigits=4) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label15.grid(row=2, column=1, sticky="w")
    label16 = tk.Label(frame9, text=str( round(k,ndigits=4) ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    label16.grid(row=3, column=1, sticky="w")
    # label52 = tk.Label(frame4, text=str( r1.get() ), anchor="e", width=elw-1, borderwidth=1, relief="sunken")
    # label52.grid(row=5, column=1, sticky="w")
    
    showplotf()
#%% 04 GUI

root = tk.Tk()
root.title("root")
rootWidth = 1400
rootHeight = 800
root.geometry(str(rootWidth) + 'x' + str(rootHeight))
elw = 8 # Entry Label Width

frame1Width = rootWidth/2
frame1Height = rootHeight/1
frame1 = tk.LabelFrame(root, text='Flight Parameters', width=frame1Width, height=frame1Height)
frame1.pack(side=tk.LEFT)
frame1.pack_propagate(0)


frame2Width = rootWidth/2
frame2Height = rootHeight/1
frame2 = tk.LabelFrame(root,text='frame2', relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
frame2.pack()
frame2.pack(side=tk.TOP)
frame2.pack_propagate(1)



frame3 = tk.LabelFrame(frame1, text="frame3text")
frame3.grid(row=0,column=0, rowspan=2, sticky='nw')

frame8 = tk.LabelFrame(frame1, text="frame8units")
frame8.grid(row=0,column=1, sticky="nw")

frame4 = tk.LabelFrame(frame1, text="frame4text")
frame4.grid(row=0,column=2,sticky="nw")

frame5 = tk.LabelFrame(frame1, text="Design Point")
frame5.grid(row=1,column=1, columnspan=2, sticky="sw")

frame7 = tk.LabelFrame(frame1, text="frame7textAtmo")
frame7.grid(row=2,column=0, sticky="nw")

frame9 = tk.LabelFrame(frame1, text="frame9-Aero")
frame9.grid(row=2,column=1, columnspan=2, sticky="nw")


frame6 = tk.Frame(frame1,relief='flat')
frame6.grid(row=9,column=9)

#---------------------------- INPUTS ----------------------------#
## ROW 0
# label
label1 = tk.Label(frame3, text='alt')
label1.grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(frame3, width=elw)
entry1.insert(tk.END, '2438.4')
entry1.grid(row=0, column=1)
label5 = tk.Label(frame3, text='[m]')
label5.grid(row=0, column=2, sticky="w")
label1expl = tk.Label(frame3, text='Altitude')
label1expl.grid(row=0, column=3, sticky="w")

## ROW 1
label2 = tk.Label(frame3, text='V')
label2.grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(frame3, width=elw)
entry2.insert(tk.END, '77.16')
entry2.grid(row=1, column=1)
label6 = tk.Label(frame3, text='[m/s]')
label6.grid(row=1, column=2, sticky="w")
label2expl = tk.Label(frame3, text='Velocity (TAS)')
label2expl.grid(row=1, column=3, sticky="w")
# FONTn = 'Helvetica'
# FONTs = 9
# FONTt = 'regular'
## ROW 2
label3 = tk.Label(frame3, text='MTOM')
label3.grid(row=2, column=0, sticky="w")
entry3 = tk.Entry(frame3, width=elw)
entry3.insert(tk.END, '907')
entry3.grid(row=2, column=1)
label7 = tk.Label(frame3, text='[kg]')
label7.grid(row=2, column=2, sticky="w")
label3expl = tk.Label(frame3, text='Maximum Take-Off Mass')
label3expl.grid(row=2, column=3, sticky="w")

## ROW 3
label4 = tk.Label(frame3, text='AR')
label4.grid(row=3, column=0, sticky="w")
entry4 = tk.Entry(frame3, width=elw)
entry4.insert(tk.END, '9')
entry4.grid(row=3, column=1)
label8 = tk.Label(frame3, text='[-]')
label8.grid(row=3, column=2, sticky="w")
label4expl = tk.Label(frame3, text='Aspect Ratio')
label4expl.grid(row=3, column=3, sticky="w")

## ROW 4
label21 = tk.Label(frame3, text='C_Dmin')
label21.grid(row=4, column=0, sticky="w")
entry5 = tk.Entry(frame3, width=elw)
entry5.insert(tk.END, '0.025')
entry5.grid(row=4, column=1)
label22 = tk.Label(frame3, text='[-]')
label22.grid(row=4, column=2, sticky="w")
label21expl = tk.Label(frame3, text='Zero-lift drag')
label21expl.grid(row=4, column=3, sticky="w")

## ROW 5
label23 = tk.Label(frame3, text='n')
label23.grid(row=5, column=0, sticky="w")
entry6 = tk.Entry(frame3, width=elw)
entry6.insert(tk.END, '2.00')
entry6.grid(row=5, column=1)
label24 = tk.Label(frame3, text='[gee]')
label24.grid(row=5, column=2, sticky="w")
label23expl = tk.Label(frame3, text='Load factor')
label23expl.grid(row=5, column=3, sticky="w")

## ROW 6
label25 = tk.Label(frame3, text='P_S')
label25.grid(row=6, column=0, sticky="w")
entry7 = tk.Entry(frame3, width=elw)
entry7.insert(tk.END, '6.10') # Condition specific energy at sustained turn | 6.10m/s = 20ft/s
entry7.grid(row=6, column=1)
label26 = tk.Label(frame3, text='[m/s]')
label26.grid(row=6, column=2, sticky="w")
label25expl = tk.Label(frame3, text='Climb excess power (unused)')
label25expl.grid(row=6, column=3, sticky="w")

## ROW 7
label27 = tk.Label(frame3, text='V_v')
label27.grid(row=7, column=0, sticky="w")
entry8 = tk.Entry(frame3, width=elw)
entry8.insert(tk.END, '7.62') # Vertical velocity for climb | 7.62m/s = 1000ft/min
entry8.grid(row=7, column=1)
label28 = tk.Label(frame3, text='[m/s]')
label28.grid(row=7, column=2, sticky="w")
label27expl = tk.Label(frame3, text='Vertical velocity')
label27expl.grid(row=7, column=3, sticky="w")

## ROW 8
label29 = tk.Label(frame3, text='C_DTO')
label29.grid(row=8, column=0, sticky="w")
entry9 = tk.Entry(frame3, width=elw)
entry9.insert(tk.END, '0.04') # Drag coefficients at take-off
entry9.grid(row=8, column=1)
label30 = tk.Label(frame3, text='[-]')
label30.grid(row=8, column=2, sticky="w")
label29expl = tk.Label(frame3, text='Take-off drag coefficient')
label29expl.grid(row=8, column=3, sticky="w")

## ROW 9
label31 = tk.Label(frame3, text='C_LTO')
label31.grid(row=9, column=0, sticky="w")
entry10 = tk.Entry(frame3, width=elw)
entry10.insert(tk.END, '0.5') # Lift coefficients at take-off
entry10.grid(row=9, column=1)
label32 = tk.Label(frame3, text='[-]')
label32.grid(row=9, column=2, sticky="w")
label31expl = tk.Label(frame3, text='Take-off lift coefficient')
label31expl.grid(row=9, column=3, sticky="w")

## ROW 10
label33 = tk.Label(frame3, text='S_G')
label33.grid(row=10, column=0, sticky="w")
entry11 = tk.Entry(frame3, width=elw)
entry11.insert(tk.END, '274.32') # groundrun
entry11.grid(row=10, column=1)
label34 = tk.Label(frame3, text='[m]')
label34.grid(row=10, column=2, sticky="w")
label33expl = tk.Label(frame3, text='Ground run')
label33expl.grid(row=10, column=3, sticky="w")

## ROW 11
label35 = tk.Label(frame3, text='mu_gr')
label35.grid(row=11, column=0, sticky="w")
entry12 = tk.Entry(frame3, width=elw)
entry12.insert(tk.END, '0.04') # Ground rolling friction coefficient
entry12.grid(row=11, column=1)
label36 = tk.Label(frame3, text='[-]')
label36.grid(row=11, column=2, sticky="w")
label35expl = tk.Label(frame3, text='Rolling friction coefficient')
label35expl.grid(row=11, column=3, sticky="w")

## ROW 12
label37 = tk.Label(frame3, text='V_LOF')
label37.grid(row=12, column=0, sticky="w")
entry13 = tk.Entry(frame3, width=elw)
entry13.insert(tk.END, '33.436') # Lift-off velocity [m/s] (idk why not "take-off"...)
entry13.grid(row=12, column=1)
label38 = tk.Label(frame3, text='[m/s]')
label38.grid(row=12, column=2, sticky="w")
label37expl = tk.Label(frame3, text='Lift-off velocity, CAS@SL (=TAS)')
label37expl.grid(row=12, column=3, sticky="w")

## ROW 13
label39 = tk.Label(frame3, text='V_vx')
label39.grid(row=13, column=0, sticky="w")
entry14 = tk.Entry(frame3, width=elw)
entry14.insert(tk.END, '41.152')
entry14.grid(row=13, column=1)
label40 = tk.Label(frame3, text='[m/s]')
label40.grid(row=13, column=2, sticky="w")
label39expl = tk.Label(frame3, text='Level-turn horiz velocity, CAS@SL (=TAS)')
label39expl.grid(row=13, column=3, sticky="w")

## ROW 14
label41 = tk.Label(frame3, text='alt_sc')
label41.grid(row=14, column=0, sticky="w")
entry15 = tk.Entry(frame3, width=elw)
entry15.insert(tk.END, '6096')
entry15.grid(row=14, column=1)
label42 = tk.Label(frame3, text='[m]')
label42.grid(row=14, column=2, sticky="w")
label41expl = tk.Label(frame3, text='Service ceiling altitude')
label41expl.grid(row=14, column=3, sticky="w")

## ROW 15
label43 = tk.Label(frame3, text='alt_TO')
label43.grid(row=15, column=0, sticky="w")
entry16 = tk.Entry(frame3, width=elw)
entry16.insert(tk.END, '0')
entry16.grid(row=15, column=1)
label44 = tk.Label(frame3, text='[m]')
label44.grid(row=15, column=2, sticky="w")
label43expl = tk.Label(frame3, text='Take-off altitude')
label43expl.grid(row=15, column=3, sticky="w")

## ROW 16
label45 = tk.Label(frame3, text='V_stall')
label45.grid(row=16, column=0, sticky="w")
entry17 = tk.Entry(frame3, width=elw)
entry17.insert(tk.END, '31.3784')
entry17.grid(row=16, column=1)
label46 = tk.Label(frame3, text='[m/s]')
label46.grid(row=16, column=2, sticky="w")
label45expl = tk.Label(frame3, text='Stall velocity, CAS@SL (=TAS)')
label45expl.grid(row=16, column=3, sticky="w")

## ROW 17
label47 = tk.Label(frame3, text='eta_prop')
label47.grid(row=17, column=0, sticky="w")
entry18 = tk.Entry(frame3, width=elw)
entry18.insert(tk.END, '0.80')
entry18.grid(row=17, column=1)
label48 = tk.Label(frame3, text='[-]')
label48.grid(row=17, column=2, sticky="w")
label47expl = tk.Label(frame3, text='Propeller efficiency')
label47expl.grid(row=17, column=3, sticky="w")

## ROW 51
labelDPTWin = tk.Label(frame5, text='T/W')
labelDPTWin.grid(row=51, column=0, sticky="w")
entry51 = tk.Entry(frame5, width=elw)
entry51.insert(tk.END, '0.135')
entry51.grid(row=51, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=51, column=2, sticky="w")
labelDPTWinexpl = tk.Label(frame5, text='Thrust-to-weight ratio')
labelDPTWinexpl.grid(row=51, column=3, sticky="w")

## ROW 52
labelDPWSin = tk.Label(frame5, text='W/S')
labelDPWSin.grid(row=52, column=0, sticky="w")
entry52 = tk.Entry(frame5, width=elw)
entry52.insert(tk.END, '1077.3')
entry52.grid(row=52, column=1)
labelDPWSunit = tk.Label(frame5, text='[N/m2]')
labelDPWSunit.grid(row=52, column=2, sticky="w")
labelDPWSinexpl = tk.Label(frame5, text='Wing loading')
labelDPWSinexpl.grid(row=52, column=3, sticky="w")

## ROW 53
labelDPPW = tk.Label(frame5, text='P/W')
labelDPPW.grid(row=53, column=0, sticky="w")
label53 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label53.grid(row=53, column=1, sticky="w")
# entry53 = tk.Entry(frame5, width=elw)
# entry53.insert(tk.END, '0.000')
# entry53.grid(row=53, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=53, column=2, sticky="w")
labelDPPWexpl = tk.Label(frame5, text='Power-to-weight ratio')
labelDPPWexpl.grid(row=53, column=3, sticky="w")

## ROW 54
labelDPPW = tk.Label(frame5, text='P/W @SL')
labelDPPW.grid(row=54, column=0, sticky="w")
label54 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label54.grid(row=54, column=1, sticky="w")
# entry54 = tk.Entry(frame5, width=elw)
# entry54.insert(tk.END, '0.000')
# entry54.grid(row=54, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=54, column=2, sticky="w")
labelDPPWexpl = tk.Label(frame5, text='Power-to-weight ratio at sea level')
labelDPPWexpl.grid(row=54, column=3, sticky="w")

## ROW 55
labelDPThr = tk.Label(frame5, text='T')
labelDPThr.grid(row=55, column=0, sticky="w")
label55 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label55.grid(row=55, column=1, sticky="w")
# entry55 = tk.Entry(frame5, width=elw)
# entry55.insert(tk.END, '0')
# entry55.grid(row=55, column=1)
labelDPWSunit = tk.Label(frame5, text='[N]')
labelDPWSunit.grid(row=55, column=2, sticky="w")
labelDPThrexpl = tk.Label(frame5, text='Thrust')
labelDPThrexpl.grid(row=55, column=3, sticky="w")

## ROW 56
labelDPPow = tk.Label(frame5, text='P')
labelDPPow.grid(row=56, column=0, sticky="w")
label56 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label56.grid(row=56, column=1, sticky="w")
# entry56 = tk.Entry(frame5, width=elw)
# entry56.insert(tk.END, '0')
# entry56.grid(row=56, column=1)
labelDPWSunit = tk.Label(frame5, text='[HP]')
labelDPWSunit.grid(row=56, column=2, sticky="w")
labelDPPowexpl = tk.Label(frame5, text='Power')
labelDPPowexpl.grid(row=56, column=3, sticky="w")

## ROW 57
labelDPPowsl = tk.Label(frame5, text='P @SL')
labelDPPowsl.grid(row=57, column=0, sticky="w")
label57 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label57.grid(row=57, column=1, sticky="w")
# entry57 = tk.Entry(frame5, width=elw)
# entry57.insert(tk.END, '0')
# entry57.grid(row=57, column=1)
labelDPPowslunit = tk.Label(frame5, text='[HP]')
labelDPPowslunit.grid(row=57, column=2, sticky="w")
labelDPPowslexpl = tk.Label(frame5, text='Power at sea level')
labelDPPowslexpl.grid(row=57, column=3, sticky="w")

## ROW 58
labelDPS = tk.Label(frame5, text='S_ref')
labelDPS.grid(row=58, column=0, sticky="w")
label58 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label58.grid(row=58, column=1, sticky="w")
# entry58 = tk.Entry(frame5, width=elw)
# entry58.insert(tk.END, '0.0')
# entry58.grid(row=58, column=1)
labelDPSunit = tk.Label(frame5, text='[m2]')
labelDPSunit.grid(row=58, column=2, sticky="w")
labelDPSexpl = tk.Label(frame5, text='Wing surface (reference)')
labelDPSexpl.grid(row=58, column=3, sticky="w")

## ROW 59
labelDPclmax = tk.Label(frame5, text='C_Lmax')
labelDPclmax.grid(row=59, column=0, sticky="w")
label59 = tk.Label(frame5, text='', width=elw-1, borderwidth=1, relief="sunken")
label59.grid(row=59, column=1, sticky="w")
# entry58 = tk.Entry(frame5, width=elw)
# entry58.insert(tk.END, '0.0')
# entry58.grid(row=58, column=1)
labelDPclmaxunit = tk.Label(frame5, text='[-]')
labelDPclmaxunit.grid(row=59, column=2, sticky="w")
labelDPclmaxexpl = tk.Label(frame5, text='Required C_Lmax')
labelDPclmaxexpl.grid(row=59, column=3, sticky="w")

## ROW 59
# samplettxt = tk.Text(frame5, width=5, height=2, borderwidth=0)
# samplettxt.tag_configure("subscript", offset=-4, font=('Calibri',6))
# samplettxt.tag_configure("superscript", offset=6, font=('Calibri',6))
# samplettxt.insert("insert", "H", "", "2", "subscript", "O", "", "2", "superscript")
# samplettxt.grid(row=59,column=0)

#---------------------------- ATMOSPHERE ----------------------------#

## ROW 0
label10rho = tk.Label(frame7, text='ρ')
label10rho.grid(row=0, column=0, sticky="w")
label14rho = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14rho.grid(row=0, column=1, sticky="w")
label18rho = tk.Label(frame7, text='[kg/m3]')
label18rho.grid(row=0, column=2, sticky="w")
label10rhoexpl = tk.Label(frame7, text='Density')
label10rhoexpl.grid(row=0, column=3, sticky="w")

## ROW 1
label10T = tk.Label(frame7, text='T')
label10T.grid(row=1, column=0, sticky="w")
label14T = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14T.grid(row=1, column=1, sticky="w")
label18T = tk.Label(frame7, text='[°C]')
label18T.grid(row=1, column=2, sticky="w")
label10Texpl = tk.Label(frame7, text='Temperature')
label10Texpl.grid(row=1, column=3, sticky="w")

## ROW 2
label10p = tk.Label(frame7, text='p')
label10p.grid(row=2, column=0, sticky="w")
label14p = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14p.grid(row=2, column=1, sticky="w")
label18p = tk.Label(frame7, text='[kPa]')
label18p.grid(row=2, column=2, sticky="w")
label10pexpl = tk.Label(frame7, text='Pressure')
label10pexpl.grid(row=2, column=3, sticky="w")

## ROW 3
label10mu = tk.Label(frame7, text='μ')
label10mu.grid(row=3, column=0, sticky="w")
label14mu = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14mu.grid(row=3, column=1, sticky="w")
label18mu = tk.Label(frame7, text='[μPa s]')
label18mu.grid(row=3, column=2, sticky="w")
label10muexpl = tk.Label(frame7, text='Dynamic viscosity')
label10muexpl.grid(row=3, column=3, sticky="w")

## ROW 4
label10a = tk.Label(frame7, text='a')
label10a.grid(row=4, column=0, sticky="w")
label14a = tk.Label(frame7, text='', width=elw-1, borderwidth=1, relief="sunken")
label14a.grid(row=4, column=1, sticky="w")
label18a = tk.Label(frame7, text='[m/s]')
label18a.grid(row=4, column=2, sticky="w")
label10aexpl = tk.Label(frame7, text='Speed of sound')
label10aexpl.grid(row=4, column=3, sticky="w")

#---------------------------- AERODYNAMICS ----------------------------#
## ROW 0
label9q = tk.Label(frame9, text='q')
label9q.grid(row=0, column=0, sticky="w")
label13q = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label13q.grid(row=0, column=1, sticky="w")
label17q = tk.Label(frame9, text='[Pa]')
label17q.grid(row=0, column=2, sticky="w")
label9qexpl = tk.Label(frame9, text='Dynamic pressure')
label9qexpl.grid(row=0, column=3, sticky="w")

## ROW 0
label9Ma = tk.Label(frame9, text='Ma')
label9Ma.grid(row=1, column=0, sticky="w")
label13Ma = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label13Ma.grid(row=1, column=1, sticky="w")
label17Ma = tk.Label(frame9, text='[-]')
label17Ma.grid(row=1, column=2, sticky="w")
label9Maexpl = tk.Label(frame9, text='Mach number')
label9Maexpl.grid(row=1, column=3, sticky="w")

## ROW 2
label11 = tk.Label(frame9, text="e")
label11.grid(row=2, column=0, sticky="w")
label15 = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label15.grid(row=2, column=1, sticky="w")
label19 = tk.Label(frame9, text='[-]')
label19.grid(row=2, column=2, sticky="w")
label11expl = tk.Label(frame9, text="Oswald's efficiency")
label11expl.grid(row=2, column=3, sticky="w")

## ROW 3
label12 = tk.Label(frame9, text='k')
label12.grid(row=3, column=0, sticky="w")
label16 = tk.Label(frame9, text='', width=elw-1, borderwidth=1, relief="sunken")
label16.grid(row=3, column=1, sticky="w")
label20 = tk.Label(frame9, text='[-]')
label20.grid(row=3, column=2, sticky="w")
label12expl = tk.Label(frame9, text='Lift-induced drag constant')
label12expl.grid(row=3, column=3, sticky="w")

## ROW 5 radio buttons for plots
plotsRadios = tk.Label(frame4, text='Sizing diagram type:').grid(row=5, column=0, columnspan=4, sticky="w")
r1 = tk.IntVar()
r1.set(1)
tk.Radiobutton(frame4, text='T/W (Jet)',    variable=r1, value=1).grid(row=6, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='T/W@SL (Jet)',  variable=r1, value=2, state=tk.DISABLED).grid(row=7, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='P/W (Prop)',   variable=r1, value=3).grid(row=8, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='P/W@SL (Prop)', variable=r1, value=4).grid(row=9, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Thrust (Jet)',     variable=r1, value=5).grid(row=6, column=2, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Thrust@SL (Jet)',   variable=r1, value=6, state=tk.DISABLED).grid(row=7, column=2, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Power (Prop)',    variable=r1, value=7).grid(row=8, column=2, columnspan=2, sticky="w")
tk.Radiobutton(frame4, text='Power@SL (Prop)',  variable=r1, value=8).grid(row=9, column=2, columnspan=2, sticky="w")

## ROW 14 radio buttons for units
altUnitsRadios = tk.Label(frame8, text='Altitude units:').grid(row=14, column=0, columnspan=4, sticky="w")
r2 = tk.IntVar()
r2.set(1)
tk.Radiobutton(frame8, text='meters', variable=r2, value=1, command=lambda: altitudeunits(r2.get())).grid(row=15, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame8, text='feet',   variable=r2, value=2, command=lambda: altitudeunits(r2.get())).grid(row=16, column=0, columnspan=2, sticky="w")
    

## ROW 17 radio buttons for velocities
velUnitsRadios = tk.Label(frame8, text='x Velocity units:').grid(row=17, column=0, columnspan=4, sticky="w")
r3 = tk.IntVar()
r3.set(1)
tk.Radiobutton(frame8, text='m/s', variable=r3, value=1, command=lambda: velocityunits(r3.get())).grid(row=18, column=0, columnspan=2, sticky="w")
tk.Radiobutton(frame8, text='kn',  variable=r3, value=2, command=lambda: velocityunits(r3.get())).grid(row=19, column=0, columnspan=2, sticky="w")


'Label(self, text=text, justify=LEFT, anchor="w").grid(sticky = W, column=0,row=0)'

# Calculate Button
button1 = tk.Button(frame6, text='calculate\nand plot',font=('Helvetica',14), command=button1fun)
button1.pack()
# button1.grid(row=0,column=1)

#%% PLOTTING MAGIC
def keypress1(heppening1):
    global keypress_label1
    if 'keypress_label1' in globals():
        keypress_label1.pack_forget()
    keypress_label1 = tk.Label(frame2, text='you pressed1 {}'.format(heppening1.key))
    keypress_label1.pack( side=tk.RIGHT, anchor=tk.NE )
    key_press_handler(heppening1, plotcanvas1, bar_of_tools1)
    # key_press_handler(event=heppening1, canvas=plotcanvas2, toolbar=bar_of_tools2)


def showplotf():
    global frame2
    global fig1
    if 'fig1' in globals():
        print('fig1 exists in GLOBALS')
        frame2.destroy()
        frame2 = tk.Frame(root, relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
        frame2.pack(side=tk.TOP)
        frame2.pack_propagate(1)
        del fig1
    DP_ws = float(entry52.get())
    DP_tw = float(entry51.get())
    DP_pow = P_hp
    DP_powSL = P_hpSL
    #---------------------------- Figure 1 ----------------------------#
    fig1 = Figure(figsize=(6,7),dpi=100) # see more args here
    if r1.get() == 1:
        maxtw = max( max(tw_clvt_list),max(tw_dsel_list),max(tw_dtod_list),max(tw_dca_list),max(tw_sc_list) )
        fig1.add_subplot(2,1,1,xlim=[min(ws),max(ws)],ylim=[0,maxtw],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='Thrust-to-Weight [N/N]').plot(ws,tw_clvt_list,'b-',
                                                                                                                                                 ws,tw_dsel_list,'b--',
                                                                                                                                                 ws,tw_dtod_list,'k--',
                                                                                                                                                 ws,tw_dca_list,'k-',
                                                                                                                                                 ws,tw_sc_list,'k:',
                                                                                                                                                 [DP_ws,DP_ws],[0,1.2*DP_tw],'r--',
                                                                                                                                                 [0,1.3*DP_ws],[DP_tw,DP_tw],'r--',
                                                                                                                                                 DP_ws,DP_tw,'ro')
    elif r1.get() == 3:
        maxpw = max( max(pw_clvt_list),max(pw_dsel_list),max(pw_dtod_list),max(pw_dca_list),max(pw_sc_list) )
        fig1.add_subplot(2,1,1,xlim=[min(ws),max(ws)],ylim=[0,maxpw],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='Power loading P/W [HP/N]').plot(ws,pw_clvt_list,'b-',
                                                                                                                                              ws,pw_dsel_list,'b--',
                                                                                                                                              ws,pw_dtod_list,'k--',
                                                                                                                                              ws,pw_dca_list,'k-',
                                                                                                                                              ws,pw_sc_list,'k:',
                                                                                                                                              [DP_ws,DP_ws],[0,1.2*DP_pw],'r--',
                                                                                                                                              [0,1.3*DP_ws],[DP_pw,DP_pw],'r--',
                                                                                                                                              DP_ws,DP_pw,'ro')
    elif r1.get() == 4:
        maxpwsl = max( max(pwsl_clvt_list),max(pwsl_dsel_list),max(pwsl_dtod_list),max(pwsl_dca_list),max(pwsl_sc_list) )
        fig1.add_subplot(2,1,1,xlim=[min(ws),max(ws)],ylim=[0,maxpwsl],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='Power loading@SL P/W [HP/N]').plot(ws,pwsl_clvt_list,'b-',
                                                                                                                                                   ws,pwsl_dsel_list,'b--',
                                                                                                                                                   ws,pwsl_dtod_list,'k--',
                                                                                                                                                   ws,pwsl_dca_list,'k-',
                                                                                                                                                   ws,pwsl_sc_list,'k:',
                                                                                                                                                   [DP_ws,DP_ws],[0,1.2*DP_pwsl],'r--',
                                                                                                                                                   [0,1.3*DP_ws],[DP_pwsl,DP_pwsl],'r--',
                                                                                                                                                   DP_ws,DP_pwsl,'ro')
    elif r1.get() == 5:
        maxt = max( max(t_clvt_mass_list),max(t_dsel_mass_list),max(t_dtod_mass_list),max(t_dca_mass_list),max(t_sc_mass_list) )
        fig1.add_subplot(2,1,1,xlim=[min(S_list),max(S_list)],ylim=[0,maxt],xlabel='$S_{ref}$ $[m^2]$',ylabel='Thrust [N]').plot(S_list,t_clvt_mass_list,'b-',
                                                                                                                                 S_list,t_dsel_mass_list,'b--',
                                                                                                                                 S_list,t_dtod_mass_list,'k--',
                                                                                                                                 S_list,t_dca_mass_list,'k-',
                                                                                                                                 S_list,t_sc_mass_list,'k:',
                                                                                                                                 [DP_S,DP_S],[0,1.2*Thr],'r--',
                                                                                                                                 [0,1.3*DP_S],[Thr,Thr],'r--',
                                                                                                                                 DP_S,Thr,'ro')
    elif r1.get() == 7:
        maxp = max( max(p_clvt_mass_list),max(p_dsel_mass_list),max(p_dtod_mass_list),max(p_dca_mass_list),max(p_sc_mass_list) )
        fig1.add_subplot(2,1,1,xlim=[min(S_list),max(S_list)],ylim=[0,maxp],xlabel='$S_{ref}$ $[m^2]$',ylabel='Power [HP]').plot(S_list,p_clvt_mass_list,'b-',
                                                                                                                         S_list,p_dsel_mass_list,'b--',
                                                                                                                         S_list,p_dtod_mass_list,'k--',
                                                                                                                         S_list,p_dca_mass_list,'k-',
                                                                                                                         S_list,p_sc_mass_list,'k:',
                                                                                                                         [DP_S,DP_S],[0,1.2*DP_pow],'r--',
                                                                                                                         [0,1.3*DP_S],[DP_pow,DP_pow],'r--',
                                                                                                                         DP_S,DP_pow,'ro')
    elif r1.get() == 8:
        maxpsl = max( max(psl_clvt_mass_list),max(psl_dsel_mass_list),max(psl_dtod_mass_list),max(psl_dca_mass_list),max(psl_sc_mass_list) )
        fig1.add_subplot(2,1,1,xlim=[min(S_list),max(S_list)],ylim=[0,maxpsl],xlabel='$S_{ref}$ $[m^2]$',ylabel='Power@SL [HP]').plot(S_list,psl_clvt_mass_list,'b-',
                                                                                                                              S_list,psl_dsel_mass_list,'b--',
                                                                                                                              S_list,psl_dtod_mass_list,'k--',
                                                                                                                              S_list,psl_dca_mass_list,'k-',
                                                                                                                              S_list,psl_sc_mass_list,'k:',
                                                                                                                              [DP_S,DP_S],[0,1.2*DP_powSL],'r--',
                                                                                                                              [0,1.3*DP_S],[DP_powSL,DP_powSL],'r--',
                                                                                                                              DP_S,DP_powSL,'ro')
    if r1.get() == 1 or r1.get() == 2 or r1.get() == 3 or r1.get() == 4:
        fig1.add_subplot(2,1,2,xlim=[min(ws),max(ws)],ylim=[0,max(clmax_list)],xlabel='Wing loading $W/S$ $[N/m^2]$',ylabel='$C_{Lmax}$').plot(ws,clmax_list,'k-',
                                                                                                                                     [DP_ws,DP_ws],[0,1.2*clmax],'r--',
                                                                                                                                     [0,1.15*DP_ws],[clmax,clmax],'r--',
                                                                                                                                     DP_ws,clmax,'ro')
    if r1.get() == 5 or r1.get() == 6 or r1.get() == 7 or r1.get() == 8:
        fig1.add_subplot(2,1,2,xlim=[min(S_list),max(S_list)],ylim=[0,max(clmax_list)],xlabel='$S_{ref}$ $[m^2]$',ylabel='$C_{Lmax}$').plot(S_list,clmax_list,'k-',
                                                                                                                               [DP_S,DP_S],[0,1.2*clmax],'r--',
                                                                                                                               [0,1.15*DP_S],[clmax,clmax],'r--',
                                                                                                                               DP_S,clmax,'ro')
    
    labbb = ['clvt','dsel','dtod','dca','sc','DP']
    fig1.legend(labbb,loc=[0.73,0.80])
    global plotcanvas1
    global bar_of_tools1, bar_of_tools2
    
    plotcanvas1 = FigureCanvasTkAgg(fig1, master=frame2)
    plotcanvas1.draw()
    plotcanvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    bar_of_tools1 = NavigationToolbar2Tk(plotcanvas1, frame2)
    bar_of_tools1.update()
    
    plotcanvas1.mpl_connect('key_press_event', keypress1)
    plotcanvas1.mpl_disconnect(plotcanvas1)
    

def _quit():
    root.quit()
    root.destroy()


button3 = tk.Button(frame6,width=4, text='EXIT', font=('Helvetica',28), command=_quit)
# button3.grid(row=1,column=1)
button3.pack()

# label200 = tk.Label(frame2, text='label200')
# label200.pack( side=tk.LEFT, anchor=tk.NW )

root.resizable(True, True)
tk.mainloop()
