# Comprehensive Cost Estimation Script Using Original Function with Break-Even Analysis and Visualization

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set global font to Calibri
rcParams['font.family'] = 'Calibri'

# ---------------------------- Quantity Discount Factor ---------------------------- #
def quantity_discount_factor(F_EXP, N):
    """
    Calculates the Quantity Discount Factor (QDF) based on experience effectiveness and production quantity.

    Parameters:
    - F_EXP: Experience effectiveness factor (0.01-0.99)
    - N: Number of units produced.

    Returns:
    - QDF: Quantity Discount Factor.
    """
    return F_EXP ** (1.4427 * np.log(N))

def dev_cost_GA(cost_input_dict):
        # W_airframe, V_H, N, f_comp,
        # yrs,
        # R_ENG,
        # N_P,
        # R_TOOL,
        # R_MFG,
        # N_PP,
        # CPIyear,
        # unit_sales_price, QDF, insurance=50000,
        # tapered='yes',
        # pressurized='yes', certificate='EASA', flap='simple', gear='retractable',
        # engine_type='turbofan',P_BHP=0,P_SHP=0,T=0,
        # prop_type='no_prop',D_P=0,
        # n_wwpy=48,n_whpw=40
    """
    Snorri 2.2.2 Development Cost of a GA Aircraft - the Eastlake Model
    (pg 37-43)
    The costs are calculated assuming the cost of living in the year 2012.
    That means the factor CPI is taken for the year 2012, and for year
    e.g. 2022 CPI must be updated.
    CPI - Consumer Price Index (aka cost-of-living index)
    For more information and updated values see footnote at pg 37 (or
    visit http://www.bls.gov/data/inflation_calculator.htm )
    
    CPI defined down there (CTRL+F "Jan 1986")

    Parameters
    ----------
    factor1 : TYPE
        DESCRIPTION.
    factor2 : TYPE
        DESCRIPTION.

    Returns dict with values
    -------
    None.

    """
    N           = cost_input_dict['N_units']
    W_airframe  = cost_input_dict['W_airframe']
    yrs         = cost_input_dict['yrs']
    f_comp      = cost_input_dict['f_comp']
    usdeur      = cost_input_dict['usdeur']
    unit_sales_price    = cost_input_dict['unit_sales_price'] * usdeur
    N_P         = cost_input_dict['N_P']
    R_ENG       = cost_input_dict['R_ENG'] * usdeur
    R_TOOL      = cost_input_dict['R_TOOL'] * usdeur
    R_MFG       = cost_input_dict['R_MFG'] * usdeur
    N_PP        = cost_input_dict['N_PP']
    insurance   = cost_input_dict['insurance'] * usdeur
    D_P         = cost_input_dict['D_P'] / 0.3048
    n_wwpy      = cost_input_dict['n_wwpy']
    n_whpw      = cost_input_dict['n_whpw']
    CPIyear     = cost_input_dict['CPIyear']
    certificate = cost_input_dict['certificate']
    flap        = cost_input_dict['flap']
    gear        = cost_input_dict['gear']
    pressurized = cost_input_dict['pressurized']
    tapered     = cost_input_dict['tapered']
    engine_type = cost_input_dict['engine_type']
    prop_type   = cost_input_dict['prop_type']
    PP_val      = cost_input_dict['PP_val']
    V_H         = cost_input_dict['V_H'] / 0.5144
    QDF         = cost_input_dict['QDF']
    
    return_dict = dict()
    W_airframe = W_airframe / 4.448 # because these estimates take lbf
    #%% Number of Engineering Man-Hours
    # Number of engineering man-hours required to design the aircraft and
    # perform the necessary RDT&E (Research, Development, Tests, and Evaluation)
    if pressurized == 'yes':
        F_PRESS1 = 1.03
    elif pressurized == 'no':
        F_PRESS1 = 1.0
    if certificate == 'EASA':
        F_CERT1 = 1.0
    elif certificate == 'FAA':
        F_CERT1 = 0.67
    if flap == 'simple':
        F_CF1 = 1
    elif flap == 'complex':
        F_CF1 = 1.03
    F_COMP1 = 1+f_comp
    H_ENG = 0.0396 * W_airframe**0.791 * V_H**1.526 * N**0.183 * F_CERT1 * F_CF1 * F_COMP1 * F_PRESS1 # equation (2-2)
    return_dict['H_ENG'] = round(H_ENG)
    """
    W_airframe  - weight of structural skeleton* (65% of operational empty weight)
    V_H         - maximum level airspeed in KTAS
    N           - number of aircraft to be produced over a 5-year period
    F_CERT1     - =0.67 if certified as LSA, =1 if certified as a 14 CFR Part 23
    F_CF1       - =1.03 if complex flap, =1 if simple flap
    F_COMP1 = 1+f_comp  - a factor to account for the use of composites in the airframe
    f_comp      - fraction of airframe made from composites (0=no composites, 1=full composite)
    F_PRESS1    - =1 if unpressurized, =1.03 if pressurized
    
    *structural skeleton weighs far less than the empty weight of the aircraft.
     This weight can be approximated by considering the empty weight minus
     engines, avionics, seats, furnishing, control system, and other.
     If unknown, assume ~65% of empty weight
     """
     
    #%% Number of Tooling Man-hours
    # Number of man-hours required to design and build tools, fixtures, jigs, molds, etc
    if pressurized == 'yes':
        F_PRESS2 = 1.01
    elif pressurized == 'no':
        F_PRESS2 = 1.0
    if flap == 'simple':
        F_CF2 = 1
    elif flap == 'complex':
        F_CF2 = 1.02
    if tapered == 'yes':
        F_TAPER = 1
    elif tapered == 'no':
        F_TAPER = 0.95
    Q_m = round(N/(12*yrs),2)
    H_TOOL = 1.0032 * W_airframe**0.764 * V_H**0.899 * N**0.178 * Q_m**0.066 * F_TAPER * F_CF2 * F_COMP1 * F_PRESS2 # equation (2-3)
    return_dict['H_TOOL'] = round(H_TOOL)
    """
    Q_m         - estimated production rate in aircraft per month (=N/60 for 60 months i.e. 5 years)
    F_TAPER     - =0.95 for no taper, =1 for tapered wing
    F_CF2       - =1.02 if complex flap, =1 if simple flap
    F_PRESS2    - =1 if unpressurized, =1.01 if pressurized
    """
    #%% Number of Manufacturing Labor Man-hours
    # Number of man-hours required to build the aircraft
    if certificate == 'EASA':
        F_CERT2 = 1.0
    elif certificate == 'FAA':
        F_CERT2 = 0.75
    if flap == 'simple':
        F_CF3 = 1
    elif flap == 'complex':
        F_CF3 = 1.01
    F_COMP2 = 1 + 0.25*f_comp
    H_MFG = 9.6613 * W_airframe**0.74 * V_H**0.543 * N**0.524 * F_CERT2 * F_CF3 * F_COMP2 # equation (2-4)
    return_dict['H_MFG'] = round(H_MFG)
    """
    F_CERT2     - =0.75 if certified as LSA, =1 if certified as a 14 CFR Part 23
    F_CF3       - =1.01 if complex flap, =1 if simple flap
    F_COMP2 = 1+0.25*f_comp - a factor to account for the use of composites in the airframe
    """
    
    
    
    
    #%% Total Cost of Engineering
    CPI2021 = CPIyear # 2.0969 #2.496049 # Jan 1986 --> Aug 2021
    CPI = CPI2021
    C_ENG = CPI * H_ENG * R_ENG # equation (2-5)
    return_dict['C_ENG'] = round(C_ENG/usdeur)
    """
    R_ENG       - rate of engineering labor in $/h (e.g. $92/h)
    CPI         - Consumer Price Index for 2021 relative to 1986
    """
    
    #%% Total Cost of Development Support
    # The cost of overheads, administration, logistics, HR, facilities maintenance personell, etc
    CPI2012 = 2.0969 # CPI ratio is required --> CPI2021/CPI2012
    
    if certificate == 'EASA':
        F_CERT3 = 1.0
    elif certificate == 'FAA':
        F_CERT3 = 0.5
    F_COMP3 = 1 + 0.5*f_comp
    C_DEV = 0.06458 * W_airframe**0.873 * V_H**1.89 * N_P**0.346 * (CPI2021/CPI2012) * F_CERT3 * F_CF3 * F_COMP3 * F_PRESS1
    return_dict['C_DEV'] = round(C_DEV/usdeur)
    """
    N_P         - number of prototypes
    F_CERT3     - =0.5 if certified as LSA, =1 if certified as a 14 CFR Part 23
    F_COMP3 = 1+0.5*f_comp  - a factor to account for the use of composites in the airframe
    """
    
    #%% Total Cost of Flight Test Operations
    # Total cost of completing the development and certification flight-test program
    # CPI ratio is required --> CPI2021/CPI2012
    if certificate == 'EASA':
        F_CERT4 = 1.0
    elif certificate == 'FAA':
        F_CERT4 = 10.0
    C_FT = 0.009646 * W_airframe**1.16 * V_H**1.3718 * N_P**1.281 * (CPI2021/CPI2012) * F_CERT4 # equation (2-7)
    return_dict['C_FT'] = round(C_FT/usdeur)
    """
    F_CERT4     - =10 if certified as LSA, =1 if certified as a 14 CFR Part 23
    """
    
    #%% Total Cost of Tooling
    # Cost of designing, fabricating, and maintaining jigs, fixtures, molds, ...
    # Tooling requires industrial and manufacturing engineers for the design
    # work and technicians to fabricate and maintain
    C_TOOL = CPI * H_TOOL * R_TOOL # equation (2-8)
    return_dict['C_TOOL'] = round(C_TOOL/usdeur)
    """
    R_TOOL      - rate of tooling labor in $/h (e.g. $61/h)
    """
    
    #%% Total Cost of Manufacturing
    # Cost of manufacturing labor required to produce the aircraft
    C_MFG = CPI * H_MFG * R_MFG # equation (2-9)
    return_dict['C_MFG'] = round(C_MFG/usdeur)
    """
    R_MFG       - rate of manufacturing labor in $/h (e.g. $53/h)
    """
    
    #%% Total Cost of Quality Control
    # Cost of technicians and the equipment required to demonstrate that the
    # product being manufactured is inded the airplane shown in the drawing package
    C_QC = 0.13 * C_MFG * F_CERT3 * F_COMP3
    return_dict['C_QC'] = round(C_QC/usdeur)
    
    #%% Total Cost of Materials
    # Cost of raw material (aluminium sheets, pre-impregnated composites,
    # landing gear, avionics, etc.) required to fabricate the airplane
    C_MAT = 24.896 * W_airframe**0.689 * V_H**0.624 * N**0.792 * (CPI2021/CPI2012) * F_CERT2 * F_CF2 * F_PRESS2
    return_dict['C_MAT'] = round(C_MAT/usdeur)
    
    #%% Total Cost to Certify
    # Sum of costs of Engineering, Development Support, Flight Test, and Tooling
    C_CERT = C_ENG + C_DEV + C_FT + C_TOOL
    return_dict['C_CERT'] = round(C_CERT/usdeur)
    
    #%% Cost of Retractable Landing Gear per Airplane
    # Already included in the DAPCA-IV (this) formulation, so an adjustment
    # is made only if the airplane has fixed landing gear. If so, subtract
    # $7500 per airplane
    if gear == 'retractable':
        gear_val = 0
    elif gear == 'fixed':
        gear_val = -7500
    return_dict['gear_val'] = round(gear_val/usdeur)
    
    #%% Cost of Avionics
    # In the absence of more accurate information, in 2012 US dollars (that's why CPI ratio),
    # add $15000 per airplane if it's certified to 14 CFR Part 23 (EASA), or add $4500 per
    # airplane if it's certified as an LSA (Light Sport Aircraft) (FAA)
    if certificate == 'EASA':
        avionics = 15000 * (CPI2021/CPI2012)
    elif certificate == 'FAA':
        avionics = 4500 * (CPI2021/CPI2012)
    return_dict['avionics'] = round(avionics/usdeur)
    #%% Cost of Power Plant (engines, propellers)
    # The cost of the engine depends on the number of (N_PP) and type of engine
    # (piston, turboprop, turbojet, or turbofan). For piston and turboprop engines
    # the cost depends on the rated brake-horsepower (P_BHP) or shaft-horsepower
    # (P_SHP). For turbojets and turbofans it is based on the rated thrust (T).
    if engine_type == 'Piston':
        C_PP = 174.0 * N_PP * PP_val * (CPI2021/CPI2012) # equation (2-13)
    elif engine_type == 'Turboprop':
        C_PP = 377.4 * N_PP * PP_val * (CPI2021/CPI2012) # equation (2-14)
    elif engine_type == 'Turbojet':
        C_PP = 868.1 * N_PP * PP_val**0.8356 * (CPI2021/CPI2012) # equation (2-15)
    elif engine_type == 'Turbofan':
        C_PP = 1035.9 * N_PP * PP_val**0.8356 * (CPI2021/CPI2012) # equation (2-16)
    elif engine_type == 'No engine':
        C_PP = 0
    return_dict['C_PP'] = round(C_PP/usdeur)
    
    # Since piston and turboprop engines also require propellers, this cost must
    # be determined as well. The two most common types are the fixed-pitch and
    # the constant speed propellers. The typical fixed-pitch propeller cost
    # around $3145 in 2012. However constant-speed propellers are more expensive
    # and an expression that takes into account the diameter of the propeller
    # (D_P [ft]) and P_SHP has been derived.
    if engine_type == 'Piston' or engine_type == 'Turboprop':
        if prop_type == 'Fixed pitch':
            C_prop = 3145 * N_PP * (CPI2021/CPI2012) # equation (2-17)
        elif prop_type == 'Constant speed':
            P_SHP = PP_val
            C_prop = 209.69 * N_PP * (CPI2021/CPI2012) * D_P**2 * (P_SHP/D_P)**0.12 # equation (2-18)
        elif prop_type == 'No propeller':
            C_prop = 0
    else:
        C_prop = 0
    return_dict['C_prop'] = round(C_prop/usdeur)
    
    #%% Number of engineers
    # Number of engineers needed to develop the aircraft over a period of eng_yrs years
    eng_yrs = 3/5 * yrs
    N_ENG = ( H_ENG )/( eng_yrs * n_wwpy * n_whpw )
    return_dict['N_ENG'] = round(N_ENG)
    """
    eng_yrs     - time for only development, roughly 60% of total time
    n_wwpy      - number of WorkWeeks Per Year (generally 48)
    n_whpw      - number of Working Hours Per Week (generally 40)
    """
    
    #%% Time to manufacture a single unit [hours]
    t_AC = H_MFG / N
    return_dict['t_AC'] = round(t_AC)
    
    #%% Break-even Analysis
    # How many units must be produced before revenue equals the cost incurred.
    # Using the standard cost-volume-profit-analysis equation (2-19) is used.
    total_fixed_cost = C_CERT
    unit_variable_cost = (C_MFG + C_QC + C_MAT)/N + (gear_val+C_PP+C_prop+avionics)*QDF + insurance
    return_dict['unit_variable_cost'] = round(unit_variable_cost/usdeur)
    min_usp = round(unit_variable_cost*1.2)
    a = len(str(min_usp))
    sfg = 2 # significant figures (generally 3)
    
    return_dict['min_unit_sales_price'] = round(min_usp*10**(-(a-sfg)))*10**(a-sfg)
    # return_dict['min_unit_sales_price'] = round(unit_variable_cost*1.2)
    N_BE = ( total_fixed_cost )/( unit_sales_price - unit_variable_cost ) # equation (2-19)
    return_dict['N_BE'] = round(N_BE)
    """
    total_fixed_cost    - generally certification cost C_CERT
    unit_variable_cost  - sum of manufacturing labor, quality control,
                          materials/equipment, landing gear, engines,
                          propellers, avionics, and manufacturer's liability
                          insurance divided by the number of units produced
    unit_sales_price    - how much would you sell your aircraft for?
    """
    return return_dict
# ---------------------------- Cost Estimation Function ---------------------------- #
def cost_estimation(N_units_range, cost_input_dict):
    """
    Calculate cost components, unit costs, and break-even point for varying production quantities.

    Parameters:
    - N_units_range: tuple (start, end, step) for units produced.
    - cost_input_dict: dictionary containing all input variables.

    Returns:
    - results: dictionary with vectors of calculated cost components and costs at the break-even point.
    - break_even_units: units at break-even point.
    """
    units_list = []
    unit_costs, total_costs, dev_costs, fixed_costs, program_costs = [], [], [], [], []
    break_even_cost_components = {}

    start, end, step = N_units_range

    for N in range(start, end + 1, step):
        cost_input_dict['N_units'] = N
        cost_input_dict['QDF'] = quantity_discount_factor(cost_input_dict['F_EXP'], N)

        # Call the provided development cost function
        result = dev_cost_GA(cost_input_dict)

        # Calculate total and unit costs
        total_cost = (result['C_ENG'] + result['C_DEV'] + result['C_FT'] + result['C_TOOL'] +
                      result['C_MFG'] + result['C_QC'] + result['C_MAT'] + 
                      result['gear_val'] + result['avionics'] + result['C_PP'] + result['C_prop'] +
                      cost_input_dict['insurance'])

        fixed_cost = (result['C_ENG'] + result['C_DEV'] + result['C_FT'] + result['C_TOOL'] ) / N
        dev_cost = (result['C_MFG'] + result['C_QC'] + result['C_MAT'] + +
                      result['gear_val'] + result['avionics'] + result['C_PP'] + result['C_prop'] +
                      cost_input_dict['insurance']) / N
        program_cost = result['C_ENG'] + result['C_DEV'] + result['C_FT'] + result['C_TOOL']

        unit_cost = fixed_cost + dev_cost

        # Store results
        units_list.append(N)
        total_costs.append(total_cost)
        unit_costs.append(unit_cost)
        dev_costs.append(dev_cost)
        fixed_costs.append(fixed_cost)
        program_costs.append(program_cost)

        # Check for break-even point and store cost components at that point
        if not break_even_cost_components and unit_cost <= cost_input_dict['unit_sales_price']:
            break_even_cost_components = {
                'C_ENG': result['C_ENG'],
                'C_DEV': result['C_DEV'],
                'C_FT': result['C_FT'],
                'C_TOOL': result['C_TOOL'],
                'C_MFG': result['C_MFG'],
                'C_QC': result['C_QC'],
                'C_MAT': result['C_MAT'],
                'C_CERT': result['C_CERT'],
                'gear_val': result['gear_val'],
                'avionics': result['avionics'],
                'C_PP': result['C_PP'],
                'C_prop': result['C_prop'],
                'insurance': cost_input_dict['insurance'],
                'total_cost': total_cost,
                'unit_cost': unit_cost,
                'dev_cost': dev_cost,
                'fixed_cost': fixed_cost,
                'program_cost': program_cost,
                'units_produced': N
            }

    break_even_units = break_even_cost_components.get('units_produced', None)

    results = {
        'units_produced': units_list,
        'unit_costs': unit_costs,
        'total_costs': total_costs,
        'unit_sales_price': cost_input_dict['unit_sales_price'],
        'break_even_units': break_even_units,
        'dev_costs': dev_costs,
        'fixed_costs': fixed_costs,
        'program_costs': program_costs,
        'break_even_cost_components': break_even_cost_components
    }

    return results, break_even_units, break_even_cost_components



# ---------------------------- Visualization Function ---------------------------- #

    """Plot unit costs vs. units produced with break-even point."""
    units = results['units_produced']
    unit_costs = results['unit_costs']
    sales_price = results['unit_sales_price']
    break_even_units = results['break_even_units']

    plt.figure(figsize=(12, 8))
    plt.plot(units, unit_costs, label='Unit Cost', color='blue', marker='o', linewidth=2)
    plt.axhline(y=sales_price, color='red', linestyle='--', label=f'Sales Price (€{sales_price:,.0f})')

    if break_even_units:
        plt.axvline(x=break_even_units, color='green', linestyle='--', label=f'Break-even at {break_even_units} units')
        plt.scatter(break_even_units, sales_price, color='green', s=100, zorder=5)

    plt.title('Unit Cost vs. Number of Units Produced', fontsize=16)
    plt.xlabel('Number of Units Produced', fontsize=14)
    plt.ylabel('Cost per Unit (EUR)', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
 
def plot_costs(results, break_even_result, save_path='cost_analysis.svg'):
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    """
    Plot unit costs (left Y-axis) and total program cost (right Y-axis) vs. units produced with 
    shaded areas for development and fixed costs. Save the plot as an SVG file.
    """
    units = results['units_produced']
    dev_costs = results['dev_costs']
    fixed_costs = results['fixed_costs']
    unit_costs = results['unit_costs']
    total_program_costs = results['total_costs']
    sales_price = results['unit_sales_price']
    break_even_units = results['break_even_units']
    program_costs = results['program_costs']

    fig, ax1 = plt.subplots(figsize=(14, 9))
    # Remove margins around the plot
    ax1.margins(x=0, y=0)
    

    # Left Y-axis: Unit costs
    ax1.fill_between(units, 0, [d / 1_000_000 for d in dev_costs], color='skyblue', alpha=0.6, label='Development Costs per Unit')
    ax1.fill_between(units, [d / 1_000_000 for d in dev_costs], 
                     [(d + f) / 1_000_000 for d, f in zip(dev_costs, fixed_costs)], 
                     color='lightgreen', alpha=0.6, label='Fixed Costs per Unit')

    ax1.plot(units, [uc / 1_000_000 for uc in unit_costs], label='Total Unit Cost', color='blue', linewidth=2)
    ax1.axhline(y=sales_price / 1_000_000, color='black', linestyle='--', linewidth=2, )

    if break_even_units:
        ax1.axvline(x=break_even_units, color='black', linestyle='--', linewidth=2,)

    ax1.set_xlabel('Number of Units Produced', fontsize=18)
    ax1.set_ylabel('Cost per Unit [Million USD]', fontsize=18)

    ax1.tick_params(axis='y',labelsize = 14)
    ax1.tick_params(axis='x', labelsize=14)
    # Right Y-axis: Total program costs
    ax2 = ax1.twinx()
    
    ax2.plot(units, [tpc / 1_000_000 for tpc in program_costs], label='Development Cost', color='red', linestyle='-', linewidth=2)
    ax2.set_ylabel('Development Cost [Million USD]', fontsize=18, color='red')
    
    ax2.tick_params(axis='y', labelcolor='red',labelsize=14)
    ax2.axhline(y=2_000_000_00 / 1_000_000, color='red', linestyle='--', linewidth=2)
    ax2.set_ylim(0, 350)  # Set Y-axis limits for the red line between 0 and 350 million USD
    ax2.margins(x=0, y=0)
    # Legends and grid
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=12)

   
    ax1.grid(True)
    plt.tight_layout()

    # Save plot as SVG
    plt.savefig(save_path, format='svg')
    plt.show()


# ---------------------------- Example Usage ---------------------------- #
if __name__ == "__main__":
    # Inputs from provided function and GUI screenshot
    cost_input_dict = {
        'F_EXP': 0.7,
        'N_units': 1,
        'W_airframe': 25799.685368,
        'yrs': 5,
        'f_comp': 0.0,
        'unit_sales_price': 12_000_000,
        'N_P': 2,
        'R_ENG': 65,
        'R_TOOL': 45,
        'R_MFG': 35,
        'N_PP': 1,
        'insurance': 43_073.56,
        'CPIyear': 2.8,
        'usdeur': 0.95,
        'D_P': 2.7,
        'certificate': 'FAA',
        'flap': 'simple',
        'gear': 'retractable',
        'pressurized': 'yes',
        'tapered': 'no',
        'engine_type': 'Turboprop',
        'prop_type': 'Constant speed',
        'PP_val': 1600,
        'V_H':280,
        'n_wwpy': 48,
        'n_whpw': 40
    }

    # Production range for analysis
    N_units_range = (5, 100, 1)

    # Run cost estimation
    results, break_even_result,break_even_cost_components = cost_estimation(N_units_range, cost_input_dict)

    # Plot results
    plot_costs(results,break_even_result, save_path='unit_and_program_cost_analysis.svg')

    # Output break-even point
    # Output break-even details
    if break_even_result:
     print(f"✅ Break-even occurs at: {break_even_result['units_to_break_even']} units.")
     print("Break-even cost details:")
     for key, value in break_even_result.items():
         print(f"  {key}: {value:,.2f}")
    else:
     print("⚠️ No break-even point found.")