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
    
    tw_clvt,tw_dsel,tw_dtod,tw_dca,tw_sc,DP_pw,DP_pwsl,Thr,P_kw,P_hp,P_hpSL = designpoint(DP_ws, DP_tw, alt, V, mtow, ar, C_Dmin, n, P_S, V_v, C_DTO, C_LTO, S_G, mu_gr, V_LOF, V_vx, alt_sc, alt_TO, V_stall, eta_prop)
    
    entry53.delete(0,99)
    entry54.delete(0,99)
    entry53.insert(tk.END, str(round(DP_pw,4)))
    entry54.insert(tk.END, str(DP_ws))
    
    label111 = tk.Label(frame1, text= 'label111-entry1 is: ' + str( entry1.get() ))
    label111.pack()
    label222 = tk.Label(frame1, text= 'label222-entry2 is: ' + str(entry2.get()))
    label222.pack()
    label333 = tk.Label(frame1, text= 'label333-entry3 is: ' + str(entry3.get()))
    label333.pack()
    label444 = tk.Label(frame1, text= 'label444-entry4 is: ' + str(entry4.get()))
    label444.pack()
    
    label13 = tk.Label(frame4, text=str( round(q,ndigits=2) ), borderwidth=2, relief="sunken")
    label13.grid(row=0, column=1, sticky="w")
    label14 = tk.Label(frame4, text=str( round(T,ndigits=2) ), borderwidth=2, relief="sunken")
    label14.grid(row=1, column=1, sticky="w")
    label15 = tk.Label(frame4, text=str( round(e,ndigits=2) ), borderwidth=2, relief="sunken")
    label15.grid(row=2, column=1, sticky="w")
    label16 = tk.Label(frame4, text=str( round(k,ndigits=2) ), borderwidth=2, relief="sunken")
    label16.grid(row=3, column=1, sticky="w")
    label50 = tk.Label(frame4, text=str( round(Thr,ndigits=2) ), borderwidth=2, relief="sunken")
    label50.grid(row=4, column=1, sticky="w")
    label52 = tk.Label(frame4, text=str( r.get() ), borderwidth=2, relief="sunken")
    label52.grid(row=5, column=1, sticky="w")
    
    showplotf()
#%% 04 GUI

root = tk.Tk()
root.title("root")
rootWidth = 1600
rootHeight = 720
root.geometry(str(rootWidth) + 'x' + str(rootHeight))

frame1Width = rootWidth/2
frame1Height = rootHeight/1
frame1 = tk.LabelFrame(root, text='frame1 input parameters here', width=frame1Width, height=frame1Height)
frame1.pack(side=tk.LEFT)
frame1.pack_propagate(0)
# frame1.grid(row=1, column=1, padx=10, pady=5)

frame2Width = rootWidth/2
frame2Height = rootHeight/1
frame2 = tk.LabelFrame(root,text='frame2', relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
frame2.pack()
# frame2.pack(side=tk.LEFT)
frame2.pack_propagate(1)
# frame2.grid(row=1, column=2, padx=10, pady=5)

frame3 = tk.LabelFrame(frame1, text="frame3text")
frame3.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady= 5, ipadx=0, ipady=0)
frame4 = tk.LabelFrame(frame1, text="frame4text")
frame4.pack(side=tk.RIGHT, anchor=tk.NE, padx=5, pady= 5, ipadx=0, ipady=0)

#---------------------------- INPUTS ----------------------------#
## ROW 0
label1 = tk.Label(frame3, text='label1-altitude',    borderwidth=2, relief="groove")
label1.grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(frame3)
entry1.insert(tk.END, '2438.4')
entry1.grid(row=0, column=1)
label5 = tk.Label(frame3, text='label5-[m]',  borderwidth=2, relief="ridge")
label5.grid(row=0, column=2, sticky="w")

## ROW 1
label2 = tk.Label(frame3, text='label2-velocity KTAS',       borderwidth=2, relief="groove")
label2.grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(frame3)
entry2.insert(tk.END, '77.16')
entry2.grid(row=1, column=1)
label6 = tk.Label(frame3, text='label6-m/s',   borderwidth=2, relief="ridge")
label6.grid(row=1, column=2, sticky="w")

## ROW 2
label3 = tk.Label(frame3, text='label3-mtow',       borderwidth=2, relief="groove")
label3.grid(row=2, column=0, sticky="w")
entry3 = tk.Entry(frame3)
entry3.insert(tk.END, '8896')
entry3.grid(row=2, column=1)
label7 = tk.Label(frame3, text='label7-N',  borderwidth=2, relief="ridge")
label7.grid(row=2, column=2, sticky="w")

## ROW 3
label4 = tk.Label(frame3, text='label4-ar',     borderwidth=2, relief="groove")
label4.grid(row=3, column=0, sticky="w")
entry4 = tk.Entry(frame3)
entry4.insert(tk.END, '9')
entry4.grid(row=3, column=1)
label8 = tk.Label(frame3, text='label8-ul', borderwidth=2, relief="ridge")
label8.grid(row=3, column=2, sticky="w")

## ROW 4
label21 = tk.Label(frame3, text='label21-C_Dmin',     borderwidth=2, relief="groove")
label21.grid(row=4, column=0, sticky="w")
entry5 = tk.Entry(frame3)
entry5.insert(tk.END, '0.025')
entry5.grid(row=4, column=1)
label22 = tk.Label(frame3, text='label22-[ul]', borderwidth=2, relief="ridge")
label22.grid(row=4, column=2, sticky="w")

## ROW 5
label23 = tk.Label(frame3, text='label23-n',     borderwidth=2, relief="groove")
label23.grid(row=5, column=0, sticky="w")
entry6 = tk.Entry(frame3)
entry6.insert(tk.END, '2.00')
entry6.grid(row=5, column=1)
label24 = tk.Label(frame3, text='label24-[g]', borderwidth=2, relief="ridge")
label24.grid(row=5, column=2, sticky="w")

## ROW 6
label25 = tk.Label(frame3, text='label25-P_S',     borderwidth=2, relief="groove")
label25.grid(row=6, column=0, sticky="w")
entry7 = tk.Entry(frame3)
entry7.insert(tk.END, '6.10') # Condition specific energy at sustained turn | 6.10m/s = 20ft/s
entry7.grid(row=6, column=1)
label26 = tk.Label(frame3, text='label26-[m/s]', borderwidth=2, relief="ridge")
label26.grid(row=6, column=2, sticky="w")

## ROW 7
label27 = tk.Label(frame3, text='label27-V_v',     borderwidth=2, relief="groove")
label27.grid(row=7, column=0, sticky="w")
entry8 = tk.Entry(frame3)
entry8.insert(tk.END, '7.62') # Vertical velocity for climb | 7.62m/s = 1000ft/min
entry8.grid(row=7, column=1)
label28 = tk.Label(frame3, text='label28-[m/s]', borderwidth=2, relief="ridge")
label28.grid(row=7, column=2, sticky="w")

## ROW 8
label29 = tk.Label(frame3, text='label29-C_DTO',     borderwidth=2, relief="groove")
label29.grid(row=8, column=0, sticky="w")
entry9 = tk.Entry(frame3)
entry9.insert(tk.END, '0.04') # Drag coefficients at take-off
entry9.grid(row=8, column=1)
label30 = tk.Label(frame3, text='label30-[ul]', borderwidth=2, relief="ridge")
label30.grid(row=8, column=2, sticky="w")

## ROW 9
label31 = tk.Label(frame3, text='label31-C_LTO',     borderwidth=2, relief="groove")
label31.grid(row=9, column=0, sticky="w")
entry10 = tk.Entry(frame3)
entry10.insert(tk.END, '0.5') # Lift coefficients at take-off
entry10.grid(row=9, column=1)
label32 = tk.Label(frame3, text='label32-[ul]', borderwidth=2, relief="ridge")
label32.grid(row=9, column=2, sticky="w")

## ROW 10
label33 = tk.Label(frame3, text='label33-S_G',     borderwidth=2, relief="groove")
label33.grid(row=10, column=0, sticky="w")
entry11 = tk.Entry(frame3)
entry11.insert(tk.END, '274.32') # groundrun
entry11.grid(row=10, column=1)
label34 = tk.Label(frame3, text='label34-[m]', borderwidth=2, relief="ridge")
label34.grid(row=10, column=2, sticky="w")

## ROW 11
label35 = tk.Label(frame3, text='label35-mu_gr',     borderwidth=2, relief="groove")
label35.grid(row=11, column=0, sticky="w")
entry12 = tk.Entry(frame3)
entry12.insert(tk.END, '0.04') # Ground rolling friction coefficient
entry12.grid(row=11, column=1)
label36 = tk.Label(frame3, text='label36-[ul]', borderwidth=2, relief="ridge")
label36.grid(row=11, column=2, sticky="w")

## ROW 12
label37 = tk.Label(frame3, text='label37-V_LOF CAS@SL (=TAS)',     borderwidth=2, relief="groove")
label37.grid(row=12, column=0, sticky="w")
entry13 = tk.Entry(frame3)
entry13.insert(tk.END, '33.436') # Lift-off velocity [m/s] (idk why not "take-off"...)
entry13.grid(row=12, column=1)
label38 = tk.Label(frame3, text='label38-[m/s]', borderwidth=2, relief="ridge")
label38.grid(row=12, column=2, sticky="w")

## ROW 13
label39 = tk.Label(frame3, text='label39-V_vx CAS@SL (=TAS)',       borderwidth=2, relief="groove")
label39.grid(row=13, column=0, sticky="w")
entry14 = tk.Entry(frame3)
entry14.insert(tk.END, '41.152')
entry14.grid(row=13, column=1)
label40 = tk.Label(frame3, text='label40-m/s',   borderwidth=2, relief="ridge")
label40.grid(row=13, column=2, sticky="w")

## ROW 14
label41 = tk.Label(frame3, text='label41-alt_sc',       borderwidth=2, relief="groove")
label41.grid(row=14, column=0, sticky="w")
entry15 = tk.Entry(frame3)
entry15.insert(tk.END, '6096')
entry15.grid(row=14, column=1)
label42 = tk.Label(frame3, text='label42-[m]',   borderwidth=2, relief="ridge")
label42.grid(row=14, column=2, sticky="w")

## ROW 15
label43 = tk.Label(frame3, text='label43-alt_TO',       borderwidth=2, relief="groove")
label43.grid(row=15, column=0, sticky="w")
entry16 = tk.Entry(frame3)
entry16.insert(tk.END, '0')
entry16.grid(row=15, column=1)
label44 = tk.Label(frame3, text='label44-[m]',   borderwidth=2, relief="ridge")
label44.grid(row=15, column=2, sticky="w")

## ROW 16
label45 = tk.Label(frame3, text='label45-V_stall CAS@SL (=TAS)',       borderwidth=2, relief="groove")
label45.grid(row=16, column=0, sticky="w")
entry17 = tk.Entry(frame3)
entry17.insert(tk.END, '31.3784')
entry17.grid(row=16, column=1)
label46 = tk.Label(frame3, text='label46-[m/s]',   borderwidth=2, relief="ridge")
label46.grid(row=16, column=2, sticky="w")

## ROW 17
label47 = tk.Label(frame3, text='label47-eta_prop',       borderwidth=2, relief="groove")
label47.grid(row=17, column=0, sticky="w")
entry18 = tk.Entry(frame3)
entry18.insert(tk.END, '0.80')
entry18.grid(row=17, column=1)
label48 = tk.Label(frame3, text='label48-[ul]',   borderwidth=2, relief="ridge")
label48.grid(row=17, column=2, sticky="w")

## ROW 51
labelDPTWin = tk.Label(frame3, text='labelDPTW-jet',    borderwidth=2, relief="groove")
labelDPTWin.grid(row=51, column=0, sticky="w")
entry51 = tk.Entry(frame3)
entry51.insert(tk.END, '0.38')
entry51.grid(row=51, column=1)
labelDPTWunit = tk.Label(frame3, text='labelDPTWunit-ul-jet', borderwidth=2, relief="ridge")
labelDPTWunit.grid(row=51, column=2, sticky="w")

## ROW 52
labelDPWSin = tk.Label(frame3, text='labelDPWS-jet',    borderwidth=2, relief="groove")
labelDPWSin.grid(row=52, column=0, sticky="w")
entry52 = tk.Entry(frame3)
entry52.insert(tk.END, '1077.3')
entry52.grid(row=52, column=1)
labelDPWSunit = tk.Label(frame3, text='labelDPWSunit-N/m2-jet', borderwidth=2, relief="ridge")
labelDPWSunit.grid(row=52, column=2, sticky="w")

## ROW 53
labelDPTWin = tk.Label(frame3, text='labelDPPW-prop',    borderwidth=2, relief="groove")
labelDPTWin.grid(row=53, column=0, sticky="w")
entry53 = tk.Entry(frame3)
entry53.insert(tk.END, '0.999')
entry53.grid(row=53, column=1)
labelDPTWunit = tk.Label(frame3, text='labelDPTWunit-ul-prop', borderwidth=2, relief="ridge")
labelDPTWunit.grid(row=53, column=2, sticky="w")

## ROW 54
labelDPWSin = tk.Label(frame3, text='labelDPWS-prop',    borderwidth=2, relief="groove")
labelDPWSin.grid(row=54, column=0, sticky="w")
entry54 = tk.Entry(frame3)
entry54.insert(tk.END, '999')
entry54.grid(row=54, column=1)
labelDPWSunit = tk.Label(frame3, text='labelDPWSunit-N/m2-prop', borderwidth=2, relief="ridge")
labelDPWSunit.grid(row=54, column=2, sticky="w")

#---------------------------- OUTPUTS ----------------------------#
## ROW 0
label9 = tk.Label(frame4, text='label9-dynpress',            borderwidth=2, relief="groove")
label9.grid(row=0, column=0, sticky="w")
label13 = tk.Label(frame4, text='label13', borderwidth=2, relief="sunken")
label13.grid(row=0, column=1, sticky="w")
label17 = tk.Label(frame4, text='label17-Pa s', borderwidth=2, relief="groove")
label17.grid(row=0, column=2, sticky="w")

## ROW 1
label10 = tk.Label(frame4, text='label10-temp',              borderwidth=2, relief="groove")
label10.grid(row=1, column=0, sticky="w")
label14 = tk.Label(frame4, text='label14', borderwidth=2, relief="sunken")
label14.grid(row=1, column=1, sticky="w")
label18 = tk.Label(frame4, text='label18-K', borderwidth=2, relief="groove")
label18.grid(row=1, column=2, sticky="w")

## ROW 2
label11 = tk.Label(frame4, text='label11-oswald',            borderwidth=2, relief="groove")
label11.grid(row=2, column=0, sticky="w")
label15 = tk.Label(frame4, text='label15', borderwidth=2, relief="sunken")
label15.grid(row=2, column=1, sticky="w")
label19 = tk.Label(frame4, text='label19-ul', borderwidth=2, relief="groove")
label19.grid(row=2, column=2, sticky="w")

## ROW 3
label12 = tk.Label(frame4, text='label12-lift induced drag', borderwidth=2, relief="groove")
label12.grid(row=3, column=0, sticky="w")
label16 = tk.Label(frame4, text='label16', borderwidth=2, relief="sunken")
label16.grid(row=3, column=1, sticky="w")
label20 = tk.Label(frame4, text='label20-ul', borderwidth=2, relief="groove")
label20.grid(row=3, column=2, sticky="w")

## ROW 4
label49 = tk.Label(frame4, text='label49-thrust', borderwidth=2, relief="groove")
label49.grid(row=4, column=0, sticky="w")
label50 = tk.Label(frame4, text='label50', borderwidth=2, relief="sunken")
label50.grid(row=4, column=1, sticky="w")
label51 = tk.Label(frame4, text='label51-[N]', borderwidth=2, relief="groove")
label51.grid(row=4, column=2, sticky="w")

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
button1 = tk.Button(frame1, text='calculate\nand plot',font=('Helvetica',14,), command=button1fun)
button1.pack()

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
        print('fig exists in GLOBALS')
        frame2.pack_forget()
        frame2 = tk.Frame(root, relief=tk.RIDGE, borderwidth=5, width=frame2Width, height=frame2Height)
        frame2.pack(side=tk.LEFT)
        frame2.pack_propagate(1)
    DP_ws = float(entry52.get())
    DP_tw = float(entry51.get())
    DP_pw = float(entry53.get())
    
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
                                                                                                                      [DP_ws,DP_ws],[0,1.2*DP_pw],'r--',
                                                                                                                      [0,1.3*DP_ws],[DP_pw,DP_pw],'r--',
                                                                                                                      DP_ws,DP_pw,'ro')
    elif r.get() == 5:
        fig.add_subplot(1,1,1,xlabel='Sref [N2]',ylabel='Thrust').plot(S_list,t_clvt_mass_list,'b-',
                                                                       S_list,t_dsel_mass_list,'b--',
                                                                       S_list,t_dtod_mass_list,'k--',
                                                                       S_list,t_dca_mass_list,'k-',
                                                                       S_list,t_sc_mass_list,'k:')
    elif r.get() == 7:
        fig.add_subplot(1,1,1,xlabel='Sref [m2]',ylabel='Power [HP]').plot(S_list,p_clvt_mass_list,'b-',
                                                                           S_list,p_dsel_mass_list,'b--',
                                                                           S_list,p_dtod_mass_list,'k--',
                                                                           S_list,p_dca_mass_list,'k-',
                                                                           S_list,p_sc_mass_list,'k:')
    elif r.get() == 8:
        fig.add_subplot(1,1,1,xlabel='Sref [m2]',ylabel='Power@SL [HP]').plot(S_list,psl_clvt_mass_list,'b-',
                                                                              S_list,psl_dsel_mass_list,'b--',
                                                                              S_list,psl_dtod_mass_list,'k--',
                                                                              S_list,psl_dca_mass_list,'k-',
                                                                              S_list,psl_sc_mass_list,'k:')
    
    
    
    
    
    
    
    
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
button3 = tk.Button(frame1, text='EXIT', font=('Helvetica',28), command=_quit)
button3.pack()

label200 = tk.Label(frame2, text='label200')
label200.pack( side=tk.LEFT, anchor=tk.NW )

root.resizable(True, True)
tk.mainloop()
