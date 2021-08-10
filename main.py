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

#%% 02 Functions for Calculations

#%% 03 Functions for Tkinter
def button1fun():
    global label111
    global label222
    global label333
    global label444
    
    if 'label111' in globals():
        label111.destroy()
        label222.destroy()
        label333.destroy()
        label444.destroy()
    
    global ws
    global tw_clvt_list
    global tw_dsel_list
    global tw_droc_list
    global tw_dtod_list
    global tw_dca_list
    global tw_sc_list
    
    global pw_clvt_list
    global pw_dsel_list
    global pw_droc_list
    global pw_dtod_list
    global pw_dca_list
    global pw_sc_list
    
    global pwsl_clvt_list
    global pwsl_dsel_list
    global pwsl_droc_list
    global pwsl_dtod_list
    global pwsl_dca_list
    global pwsl_sc_list
    
    global S_list
    global t_clvt_mass_list
    global t_dsel_mass_list
    global t_dtod_mass_list
    global t_dca_mass_list
    global t_sc_mass_list
    
    global p_clvt_mass_list
    global p_dsel_mass_list
    global p_dtod_mass_list
    global p_dca_mass_list
    global p_sc_mass_list
    
    global psl_clvt_mass_list
    global psl_dsel_mass_list
    global psl_dtod_mass_list
    global psl_dca_mass_list
    global psl_sc_mass_list
    
    global DP_pw
    global DP_pwsl
    global Thr
    global P_hp
    global P_hpSL
    global DP_S
    
    "INPUTS"
    ws_params = [200,2960,553] # [start, stop, numsteps] 200,1000,553
    alt = float(entry1.get())
    V = float(entry2.get())
    mtow = float(entry3.get())
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
    V_vx = float(entry14.get())
    alt_sc = float(entry15.get())
    alt_TO = float(entry16.get())
    V_stall = float(entry17.get())
    eta_prop = float(entry18.get())
    DP_ws = float(entry52.get())
    DP_tw = float(entry51.get())
    
    T,p,rho,mu,a,V,q,e,k,ws,tw_clvt_list,tw_dsel_list,tw_dtod_list,tw_dca_list,tw_sc_list,pw_clvt_list,pwsl_clvt_list,t_clvt_mass_list,p_clvt_mass_list,psl_clvt_mass_list,pw_dsel_list,pwsl_dsel_list,t_dsel_mass_list,p_dsel_mass_list,psl_dsel_mass_list,pw_dtod_list,pwsl_dtod_list,t_dtod_mass_list,p_dtod_mass_list,psl_dtod_mass_list,pw_dca_list,pwsl_dca_list,t_dca_mass_list,p_dca_mass_list,psl_dca_mass_list,pw_sc_list,pwsl_sc_list,t_sc_mass_list,p_sc_mass_list,psl_sc_mass_list,S_list = mainparameters(ws_params,alt,V,mtow,ar,C_Dmin,n,P_S,V_v,C_DTO,C_LTO,S_G,mu_gr,V_LOF,V_vx,alt_sc,alt_TO,eta_prop)
    
    tw_clvt,tw_dsel,tw_dtod,tw_dca,tw_sc,DP_pw,DP_pwsl,Thr,P_kw,P_hp,P_hpSL,DP_S = designpoint(DP_ws, DP_tw, alt, V, mtow, ar, C_Dmin, n, P_S, V_v, C_DTO, C_LTO, S_G, mu_gr, V_LOF, V_vx, alt_sc, alt_TO, V_stall, eta_prop)
    
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
    label53 = tk.Label(frame5, text=str(round(DP_pw,4)),width=elw-2, borderwidth=1, relief="sunken")
    label53.grid(row=53, column=1, sticky="w")
    label54 = tk.Label(frame5, text=str(round(DP_pwsl,4)),width=elw-2, borderwidth=1, relief="sunken")
    label54.grid(row=54, column=1, sticky="w")
    label55 = tk.Label(frame5, text=str(round(Thr,1)),width=elw-2, borderwidth=1, relief="sunken")
    label55.grid(row=55, column=1, sticky="w")
    label56 = tk.Label(frame5, text=str(round(P_hp,1)),width=elw-2, borderwidth=1, relief="sunken")
    label56.grid(row=56, column=1, sticky="w")
    label57 = tk.Label(frame5, text=str(round(P_hpSL,1)),width=elw-2, borderwidth=1, relief="sunken")
    label57.grid(row=57, column=1, sticky="w")
    label58 = tk.Label(frame5, text=str(round(DP_S,2)),width=elw-2, borderwidth=1, relief="sunken")
    label58.grid(row=58, column=1, sticky="w")

    
    # label111 = tk.Label(frame1, text= 'label111-entry1 is: ' + str( entry1.get() ))
    # label111.pack()
    # label222 = tk.Label(frame1, text= 'label222-entry2 is: ' + str(entry2.get()))
    # label222.pack()
    # label333 = tk.Label(frame1, text= 'label333-entry3 is: ' + str(entry3.get()))
    # label333.pack()
    # label444 = tk.Label(frame1, text= 'label444-entry4 is: ' + str(entry4.get()))
    # label444.pack()
    
    label13 = tk.Label(frame4, text=str( round(q,ndigits=2) ), width=elw-2, borderwidth=1, relief="sunken")
    label13.grid(row=0, column=1, sticky="w")
    label14 = tk.Label(frame4, text=str( round(T,ndigits=2) ), width=elw-2, borderwidth=1, relief="sunken")
    label14.grid(row=1, column=1, sticky="w")
    label15 = tk.Label(frame4, text=str( round(e,ndigits=2) ), width=elw-2, borderwidth=1, relief="sunken")
    label15.grid(row=2, column=1, sticky="w")
    label16 = tk.Label(frame4, text=str( round(k,ndigits=2) ), width=elw-2, borderwidth=1, relief="sunken")
    label16.grid(row=3, column=1, sticky="w")
    label52 = tk.Label(frame4, text=str( r.get() ), width=elw-2, borderwidth=1, relief="sunken")
    label52.grid(row=5, column=1, sticky="w")
    
    showplotf()
#%% 04 GUI

root = tk.Tk()
root.title("root")
rootWidth = 1600
rootHeight = 720
root.geometry(str(rootWidth) + 'x' + str(rootHeight))
elw = 8 # Entry Label Width

frame1Width = rootWidth/2
frame1Height = rootHeight/1
frame1 = tk.LabelFrame(root, text='Flight Parameters', width=frame1Width, height=frame1Height)
frame1.pack(side=tk.LEFT)
frame1.pack_propagate(0)
# frame1.grid(row=1, column=1, padx=10, pady=5)

frame2Width = rootWidth/2
frame2Height = rootHeight/1
frame2 = tk.LabelFrame(root,text='frame2', relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
frame2.pack()
frame2.pack(side=tk.LEFT)
frame2.pack_propagate(1)
# frame2.grid(row=1, column=2, padx=10, pady=5)

frame3 = tk.LabelFrame(frame1, text="frame3text")
frame3.grid(row=0,column=0)
# frame3.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady= 5, ipadx=0, ipady=0)
frame4 = tk.LabelFrame(frame1, text="frame4text")
# frame4.pack(side=tk.RIGHT, anchor=tk.NE, padx=5, pady= 5, ipadx=0, ipady=0)
frame4.grid(row=0,column=2,sticky="n")
frame5 = tk.LabelFrame(frame1, text="Design Point")
frame5.grid(row=1,column=0)
frame6 = tk.Frame(frame1,relief='flat')
frame6.grid(row=1,column=2)

#---------------------------- INPUTS ----------------------------#
## ROW 0
label1 = tk.Label(frame3, text='Altitude, alt')
label1.grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(frame3, width=elw)
entry1.insert(tk.END, '2438.4')
entry1.grid(row=0, column=1)
label5 = tk.Label(frame3, text='[m]')
label5.grid(row=0, column=2, sticky="w")

## ROW 1
label2 = tk.Label(frame3, text='Velocity (TAS), V')
label2.grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(frame3, width=elw)
entry2.insert(tk.END, '77.16')
entry2.grid(row=1, column=1)
label6 = tk.Label(frame3, text='[m/s]')
label6.grid(row=1, column=2, sticky="w")

## ROW 2
label3 = tk.Label(frame3, text='MTOW')
label3.grid(row=2, column=0, sticky="w")
entry3 = tk.Entry(frame3, width=elw)
entry3.insert(tk.END, '8896')
entry3.grid(row=2, column=1)
label7 = tk.Label(frame3, text='[N]')
label7.grid(row=2, column=2, sticky="w")

## ROW 3
label4 = tk.Label(frame3, text='Aspect Ratio, AR')
label4.grid(row=3, column=0, sticky="w")
entry4 = tk.Entry(frame3, width=elw)
entry4.insert(tk.END, '9')
entry4.grid(row=3, column=1)
label8 = tk.Label(frame3, text='[-]')
label8.grid(row=3, column=2, sticky="w")

## ROW 4
label21 = tk.Label(frame3, text='Zero-lift drag, C_Dmin')
label21.grid(row=4, column=0, sticky="w")
entry5 = tk.Entry(frame3, width=elw)
entry5.insert(tk.END, '0.025')
entry5.grid(row=4, column=1)
label22 = tk.Label(frame3, text='[-]')
label22.grid(row=4, column=2, sticky="w")

## ROW 5
label23 = tk.Label(frame3, text='Load factor, n')
label23.grid(row=5, column=0, sticky="w")
entry6 = tk.Entry(frame3, width=elw)
entry6.insert(tk.END, '2.00')
entry6.grid(row=5, column=1)
label24 = tk.Label(frame3, text='[gee]')
label24.grid(row=5, column=2, sticky="w")

## ROW 6
label25 = tk.Label(frame3, text='Climb excess power (unused), P_S')
label25.grid(row=6, column=0, sticky="w")
entry7 = tk.Entry(frame3, width=elw)
entry7.insert(tk.END, '6.10') # Condition specific energy at sustained turn | 6.10m/s = 20ft/s
entry7.grid(row=6, column=1)
label26 = tk.Label(frame3, text='[m/s]')
label26.grid(row=6, column=2, sticky="w")

## ROW 7
label27 = tk.Label(frame3, text='Vertical velocity, V_v')
label27.grid(row=7, column=0, sticky="w")
entry8 = tk.Entry(frame3, width=elw)
entry8.insert(tk.END, '7.62') # Vertical velocity for climb | 7.62m/s = 1000ft/min
entry8.grid(row=7, column=1)
label28 = tk.Label(frame3, text='[m/s]')
label28.grid(row=7, column=2, sticky="w")

## ROW 8
label29 = tk.Label(frame3, text='Take-off drag coefficient, C_DTO')
label29.grid(row=8, column=0, sticky="w")
entry9 = tk.Entry(frame3, width=elw)
entry9.insert(tk.END, '0.04') # Drag coefficients at take-off
entry9.grid(row=8, column=1)
label30 = tk.Label(frame3, text='[-]')
label30.grid(row=8, column=2, sticky="w")

## ROW 9
label31 = tk.Label(frame3, text='Take-off lift coefficient, C_LTO')
label31.grid(row=9, column=0, sticky="w")
entry10 = tk.Entry(frame3, width=elw)
entry10.insert(tk.END, '0.5') # Lift coefficients at take-off
entry10.grid(row=9, column=1)
label32 = tk.Label(frame3, text='[-]')
label32.grid(row=9, column=2, sticky="w")

## ROW 10
label33 = tk.Label(frame3, text='Ground run, S_G')
label33.grid(row=10, column=0, sticky="w")
entry11 = tk.Entry(frame3, width=elw)
entry11.insert(tk.END, '274.32') # groundrun
entry11.grid(row=10, column=1)
label34 = tk.Label(frame3, text='[m]')
label34.grid(row=10, column=2, sticky="w")

## ROW 11
label35 = tk.Label(frame3, text='Rolling friction coefficient, mu_gr')
label35.grid(row=11, column=0, sticky="w")
entry12 = tk.Entry(frame3, width=elw)
entry12.insert(tk.END, '0.04') # Ground rolling friction coefficient
entry12.grid(row=11, column=1)
label36 = tk.Label(frame3, text='[-]')
label36.grid(row=11, column=2, sticky="w")

## ROW 12
label37 = tk.Label(frame3, text='Lift-off velocity, V_LOF CAS@SL (=TAS)')
label37.grid(row=12, column=0, sticky="w")
entry13 = tk.Entry(frame3, width=elw)
entry13.insert(tk.END, '33.436') # Lift-off velocity [m/s] (idk why not "take-off"...)
entry13.grid(row=12, column=1)
label38 = tk.Label(frame3, text='[m/s]')
label38.grid(row=12, column=2, sticky="w")

## ROW 13
label39 = tk.Label(frame3, text='Level-turn horiz velocity, V_vx CAS@SL (=TAS)')
label39.grid(row=13, column=0, sticky="w")
entry14 = tk.Entry(frame3, width=elw)
entry14.insert(tk.END, '41.152')
entry14.grid(row=13, column=1)
label40 = tk.Label(frame3, text='[m/s]')
label40.grid(row=13, column=2, sticky="w")

## ROW 14
label41 = tk.Label(frame3, text='Service ceiling altitude, alt_sc')
label41.grid(row=14, column=0, sticky="w")
entry15 = tk.Entry(frame3, width=elw)
entry15.insert(tk.END, '6096')
entry15.grid(row=14, column=1)
label42 = tk.Label(frame3, text='label42-[m]')
label42.grid(row=14, column=2, sticky="w")

## ROW 15
label43 = tk.Label(frame3, text='Take-off altitude, alt_TO')
label43.grid(row=15, column=0, sticky="w")
entry16 = tk.Entry(frame3, width=elw)
entry16.insert(tk.END, '0')
entry16.grid(row=15, column=1)
label44 = tk.Label(frame3, text='[m]')
label44.grid(row=15, column=2, sticky="w")

## ROW 16
label45 = tk.Label(frame3, text='Stall velocity, V_stall CAS@SL (=TAS)')
label45.grid(row=16, column=0, sticky="w")
entry17 = tk.Entry(frame3, width=elw)
entry17.insert(tk.END, '31.3784')
entry17.grid(row=16, column=1)
label46 = tk.Label(frame3, text='[m/s]')
label46.grid(row=16, column=2, sticky="w")

## ROW 17
label47 = tk.Label(frame3, text='Propeller efficiency, eta_prop')
label47.grid(row=17, column=0, sticky="w")
entry18 = tk.Entry(frame3, width=elw)
entry18.insert(tk.END, '0.80')
entry18.grid(row=17, column=1)
label48 = tk.Label(frame3, text='[-]')
label48.grid(row=17, column=2, sticky="w")

## ROW 51
labelDPTWin = tk.Label(frame5, text='Thrust-to-weight, T-W')
labelDPTWin.grid(row=51, column=0, sticky="w")
entry51 = tk.Entry(frame5, width=elw)
entry51.insert(tk.END, '0.135')
entry51.grid(row=51, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=51, column=2, sticky="w")

## ROW 52
labelDPWSin = tk.Label(frame5, text='Wing loading, W/S')
labelDPWSin.grid(row=52, column=0, sticky="w")
entry52 = tk.Entry(frame5, width=elw)
entry52.insert(tk.END, '1077.3')
entry52.grid(row=52, column=1)
labelDPWSunit = tk.Label(frame5, text='[N/m2]')
labelDPWSunit.grid(row=52, column=2, sticky="w")

## ROW 53
labelDPPW = tk.Label(frame5, text='Power-to-weight, P-W')
labelDPPW.grid(row=53, column=0, sticky="w")
label53 = tk.Label(frame5, text='', width=elw-2, borderwidth=1, relief="sunken")
label53.grid(row=53, column=1, sticky="w")
# entry53 = tk.Entry(frame5, width=elw)
# entry53.insert(tk.END, '0.000')
# entry53.grid(row=53, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=53, column=2, sticky="w")

## ROW 54
labelDPPW = tk.Label(frame5, text='Power-to-weight ASL')
labelDPPW.grid(row=54, column=0, sticky="w")
label54 = tk.Label(frame5, text='', width=elw-2, borderwidth=1, relief="sunken")
label54.grid(row=54, column=1, sticky="w")
# entry54 = tk.Entry(frame5, width=elw)
# entry54.insert(tk.END, '0.000')
# entry54.grid(row=54, column=1)
labelDPTWunit = tk.Label(frame5, text='[-]')
labelDPTWunit.grid(row=54, column=2, sticky="w")

## ROW 55
labelDPPow = tk.Label(frame5, text='Thrust')
labelDPPow.grid(row=55, column=0, sticky="w")
label55 = tk.Label(frame5, text='', width=elw-2, borderwidth=1, relief="sunken")
label55.grid(row=55, column=1, sticky="w")
# entry55 = tk.Entry(frame5, width=elw)
# entry55.insert(tk.END, '0')
# entry55.grid(row=55, column=1)
labelDPWSunit = tk.Label(frame5, text='[N]')
labelDPWSunit.grid(row=55, column=2, sticky="w")

## ROW 56
labelDPPow = tk.Label(frame5, text='Power')
labelDPPow.grid(row=56, column=0, sticky="w")
label56 = tk.Label(frame5, text='', width=elw-2, borderwidth=1, relief="sunken")
label56.grid(row=56, column=1, sticky="w")
# entry56 = tk.Entry(frame5, width=elw)
# entry56.insert(tk.END, '0')
# entry56.grid(row=56, column=1)
labelDPWSunit = tk.Label(frame5, text='[HP]')
labelDPWSunit.grid(row=56, column=2, sticky="w")

## ROW 57
labelDPS = tk.Label(frame5, text='Power ASL')
labelDPS.grid(row=57, column=0, sticky="w")
label57 = tk.Label(frame5, text='', width=elw-2, borderwidth=1, relief="sunken")
label57.grid(row=57, column=1, sticky="w")
# entry57 = tk.Entry(frame5, width=elw)
# entry57.insert(tk.END, '0')
# entry57.grid(row=57, column=1)
labelDPSunit = tk.Label(frame5, text='[HP]')
labelDPSunit.grid(row=57, column=2, sticky="w")

## ROW 58
labelDPS = tk.Label(frame5, text='Wing surface, S_ref')
labelDPS.grid(row=58, column=0, sticky="w")
label58 = tk.Label(frame5, text='', width=elw-2, borderwidth=1, relief="sunken")
label58.grid(row=58, column=1, sticky="w")
# entry58 = tk.Entry(frame5, width=elw)
# entry58.insert(tk.END, '0.0')
# entry58.grid(row=58, column=1)
labelDPSunit = tk.Label(frame5, text='[m2]')
labelDPSunit.grid(row=58, column=2, sticky="w")

## ROW 59
samplettxt = tk.Text(frame5, width=5, height=2, borderwidth=0)
samplettxt.tag_configure("subscript", offset=-4, font=('Calibri',6))
samplettxt.tag_configure("superscript", offset=6, font=('Calibri',6))
samplettxt.insert("insert", "H", "", "2", "subscript", "O", "", "2", "superscript")
samplettxt.grid(row=59,column=0)

#---------------------------- OUTPUTS ----------------------------#
## ROW 0
label9 = tk.Label(frame4, text='Dynamic pressure, q')
label9.grid(row=0, column=0, sticky="w")
label13 = tk.Label(frame4, text='', width=elw-2, borderwidth=1, relief="sunken")
label13.grid(row=0, column=1, sticky="w")
label17 = tk.Label(frame4, text='[Pa s]', )
label17.grid(row=0, column=2, sticky="w")

## ROW 1
label10 = tk.Label(frame4, text='Temperature, T')
label10.grid(row=1, column=0, sticky="w")
label14 = tk.Label(frame4, text='', width=elw-2, borderwidth=1, relief="sunken")
label14.grid(row=1, column=1, sticky="w")
label18 = tk.Label(frame4, text='[K]', )
label18.grid(row=1, column=2, sticky="w")

## ROW 2
label11 = tk.Label(frame4, text="Oswald's efficiency, e")
label11.grid(row=2, column=0, sticky="w")
label15 = tk.Label(frame4, text='', width=elw-2, borderwidth=1, relief="sunken")
label15.grid(row=2, column=1, sticky="w")
label19 = tk.Label(frame4, text='[-]', )
label19.grid(row=2, column=2, sticky="w")

## ROW 3
label12 = tk.Label(frame4, text='Lift-induced drag constant, k')
label12.grid(row=3, column=0, sticky="w")
label16 = tk.Label(frame4, text='', width=elw-2, borderwidth=1, relief="sunken")
label16.grid(row=3, column=1, sticky="w")
label20 = tk.Label(frame4, text='[-]', )
label20.grid(row=3, column=2, sticky="w")

## ROW 5 radio button
r = tk.IntVar()
r.set(1)
tk.Radiobutton(frame4, text='Jet - tw plot', variable=r, value=1).grid(row=5, column=0, sticky="w")
tk.Radiobutton(frame4, text='Jet - twSL plot', variable=r, value=2, state=tk.DISABLED).grid(row=6, column=0, sticky="w")
tk.Radiobutton(frame4, text='Prop - pw plot', variable=r, value=3).grid(row=7, column=0, sticky="w")
tk.Radiobutton(frame4, text='Prop - pwSL plot', variable=r, value=4).grid(row=8, column=0, sticky="w")
tk.Radiobutton(frame4, text='Jet - t plot', variable=r, value=5).grid(row=9, column=0, sticky="w")
tk.Radiobutton(frame4, text='Jet - tSL plot', variable=r, value=6, state=tk.DISABLED).grid(row=10, column=0, sticky="w")
tk.Radiobutton(frame4, text='Prop - p plot', variable=r, value=7).grid(row=11, column=0, sticky="w")
tk.Radiobutton(frame4, text='Prop - pSL plot', variable=r, value=8).grid(row=12, column=0, sticky="w")


'Label(self, text=text, justify=LEFT, anchor="w").grid(sticky = W, column=0,row=0)'

# Calculate Button
button1 = tk.Button(frame6, text='calculate\nand plot',font=('Helvetica',14), command=button1fun)
button1.pack()
# button1.grid(row=0,column=1)

#%% PLOTTING MAGIC
def keypress(heppening):
    global keypress_label
    if 'keypress_label' in globals():
        keypress_label.pack_forget()
    keypress_label = tk.Label(frame2, text='you pressed {}'.format(heppening.key))
    keypress_label.pack( side=tk.RIGHT, anchor=tk.NE )
    key_press_handler(heppening, plotcanvas, bar_of_tools)

def showplotf():
    global frame2
    if 'fig' in globals():
        # print('fig exists in GLOBALS')
        frame2.pack_forget()
        frame2 = tk.Frame(root, relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
        frame2.pack(side=tk.LEFT)
        frame2.pack_propagate(1)
    DP_ws = float(entry52.get())
    DP_tw = float(entry51.get())
    # DP_pw = float(entry53.get())
    # DP_pwsl = float(entry54.get())
    # Thr = float(entry55.get())
    DP_pow = P_hp
    DP_powSL = P_hpSL
    # DP_S = float(entry58.get())
    
    global fig
    fig = Figure(figsize=(6,4),dpi=100) # see more args here
    if r.get() == 1:
        fig.add_subplot(1,1,1,xlabel='Wing loading W/S [N/m2]',ylabel='Thrust-to-Weight',xlim=(200,2900),ylim=(0,0.5),title='titlehere').plot(ws,tw_clvt_list,'b-',
                                                                                                                      ws,tw_dsel_list,'b--',
                                                                                                                      ws,tw_dtod_list,'k--',
                                                                                                                      ws,tw_dca_list,'k-',
                                                                                                                      ws,tw_sc_list,'k:',
                                                                                                                      [DP_ws,DP_ws],[0,1.2*DP_tw],'r--',
                                                                                                                      [0,1.3*DP_ws],[DP_tw,DP_tw],'r--',
                                                                                                                      DP_ws,DP_tw,'ro')
    elif r.get() == 3:
        fig.add_subplot(1,1,1,xlabel='Wing loading W/S [N/m2]',ylabel='Power loading P/W [HP/N]',xlim=(200,2900),title='titlehere').plot(ws,pw_clvt_list,'b-',
                                                                                                                      ws,pw_dsel_list,'b--',
                                                                                                                      ws,pw_dtod_list,'k--',
                                                                                                                      ws,pw_dca_list,'k-',
                                                                                                                      ws,pw_sc_list,'k:',
                                                                                                                      [DP_ws,DP_ws],[0,1.2*DP_pw],'r--',
                                                                                                                      [0,1.3*DP_ws],[DP_pw,DP_pw],'r--',
                                                                                                                      DP_ws,DP_pw,'ro')
    elif r.get() == 4:
        fig.add_subplot(1,1,1,xlabel='Wing loading W/S [N/m2]',ylabel='Power loading@SL P/W [HP/N]',xlim=(200,2900),title='titlehere').plot(ws,pwsl_clvt_list,'b-',
                                                                                                                      ws,pwsl_dsel_list,'b--',
                                                                                                                      ws,pwsl_dtod_list,'k--',
                                                                                                                      ws,pwsl_dca_list,'k-',
                                                                                                                      ws,pwsl_sc_list,'k:',
                                                                                                                      [DP_ws,DP_ws],[0,1.2*DP_pwsl],'r--',
                                                                                                                      [0,1.3*DP_ws],[DP_pwsl,DP_pwsl],'r--',
                                                                                                                      DP_ws,DP_pwsl,'ro')
    elif r.get() == 5:
        fig.add_subplot(1,1,1,xlabel='Sref [m2]',ylabel='Thrust').plot(S_list,t_clvt_mass_list,'b-',
                                                                       S_list,t_dsel_mass_list,'b--',
                                                                       S_list,t_dtod_mass_list,'k--',
                                                                       S_list,t_dca_mass_list,'k-',
                                                                       S_list,t_sc_mass_list,'k:',
                                                                       [DP_S,DP_S],[0,1.2*Thr],'r--',
                                                                       [0,1.3*DP_S],[Thr,Thr],'r--',
                                                                       DP_S,Thr,'ro')
    elif r.get() == 7:
        fig.add_subplot(1,1,1,xlabel='Sref [m2]',ylabel='Power [HP]').plot(S_list,p_clvt_mass_list,'b-',
                                                                           S_list,p_dsel_mass_list,'b--',
                                                                           S_list,p_dtod_mass_list,'k--',
                                                                           S_list,p_dca_mass_list,'k-',
                                                                           S_list,p_sc_mass_list,'k:',
                                                                           [DP_S,DP_S],[0,1.2*DP_pow],'r--',
                                                                           [0,1.3*DP_S],[DP_pow,DP_pow],'r--',
                                                                           DP_S,DP_pow,'ro')
    elif r.get() == 8:
        fig.add_subplot(1,1,1,xlabel='Sref [m2]',ylabel='Power@SL [HP]').plot(S_list,psl_clvt_mass_list,'b-',
                                                                              S_list,psl_dsel_mass_list,'b--',
                                                                              S_list,psl_dtod_mass_list,'k--',
                                                                              S_list,psl_dca_mass_list,'k-',
                                                                              S_list,psl_sc_mass_list,'k:',
                                                                              [DP_S,DP_S],[0,1.2*DP_powSL],'r--',
                                                                              [0,1.3*DP_S],[DP_powSL,DP_powSL],'r--',
                                                                              DP_S,DP_powSL,'ro')
    labbb = ['clvt','dsel','dtod','dca','sc','DP']
    fig.legend(labbb,loc=[0.73,0.56])
    global plotcanvas
    global bar_of_tools
    plotcanvas = FigureCanvasTkAgg(fig, master=frame2)
    plotcanvas.draw()
    plotcanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    bar_of_tools = NavigationToolbar2Tk(plotcanvas, frame2)
    bar_of_tools.update()
    
    plotcanvas.mpl_connect('key_press_event', keypress)

def _quit():
    root.quit()
    root.destroy()

# helv36 = tk.Font.Font(family='Helvetica', size=36, weight='bold')
button3 = tk.Button(frame6,width=4, text='EXIT', font=('Helvetica',28), command=_quit)
# button3.grid(row=1,column=1)
button3.pack()

# label200 = tk.Label(frame2, text='label200')
# label200.pack( side=tk.LEFT, anchor=tk.NW )

root.resizable(True, True)
tk.mainloop()
