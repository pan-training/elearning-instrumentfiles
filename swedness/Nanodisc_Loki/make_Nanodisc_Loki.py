"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    Loki = instr.McStas_instr("Loki_generated")
    Loki.add_parameter("int", "Instrument_Mode", value=0)
    Loki.add_parameter("double", "Detector_Distance", value=2.0)
    Loki.add_parameter("int", "SAMPLE", value=0)
    Loki.add_parameter("double", "Solvent_Fraction", value=1.0)
    Loki.add_parameter("double", "Mix_Fraction", value=0.0)
    Loki.add_parameter("int", "Incoherent_Solvent", value=0)
    Loki.add_declare_var("double", "DetectorRadius")
    Loki.add_declare_var("double", "DetectorSize")
    Loki.add_declare_var("double", "Mix_Chance")
    Loki.add_declare_var("char", "virtualoutput_filename", array=256)
    Loki.add_declare_var("char", "calibration_filename", array=256)
    Loki.add_declare_var("char", "mcploutput_filename", array=256)
    Loki.add_declare_var("char", "Sample_String", array=256)
    Loki.add_declare_var("int", "Sam")
    Loki.add_declare_var("int", "SAMPLE_HOLD")
    Loki.add_declare_var("int", "SAMPLE_HOLD2")
    Loki.add_declare_var("int", "SAMPLE_Select")
    Loki.add_declare_var("int", "Repeat_Number")
    Loki.add_declare_var("int", "Plot_Frac")
    Loki.add_declare_var("int", "Beamstop")
    Loki.add_declare_var("double", "Rmin")
    Loki.add_declare_var("double", "T_min")
    Loki.add_declare_var("double", "T_max")
    Loki.add_declare_var("double", "P_Interact")
    Loki.add_declare_var("double", "sigma_Head_Deutorated")
    Loki.add_declare_var("double", "sigma_CH2_Deutorated")
    Loki.add_declare_var("double", "sigma_CH3_Deutorated")
    Loki.add_declare_var("double", "sigma_Head_Hydrated")
    Loki.add_declare_var("double", "sigma_CH2_Hydrated")
    Loki.add_declare_var("double", "sigma_CH3_Hydrated")
    Loki.add_declare_var("double", "sigma_Head_Mixed")
    Loki.add_declare_var("double", "sigma_CH2_Mixed")
    Loki.add_declare_var("double", "sigma_CH3_Mixed")
    Loki.add_declare_var("double", "RhoH2O")
    Loki.add_declare_var("double", "RhoD2O")
    Loki.add_declare_var("double", "RhoSolv")
    Loki.add_declare_var("double", "AxisRatio")
    Loki.add_declare_var("double", "N_Lipids")
    Loki.add_declare_var("double", "AreaPrHead")
    Loki.add_declare_var("double", "H_1MSP")
    Loki.add_declare_var("double", "V_1MSP")
    Loki.add_declare_var("double", "V_1MSPE3")
    Loki.add_declare_var("double", "V_1Headgruope")
    Loki.add_declare_var("double", "V_1CH2Tail")
    Loki.add_declare_var("double", "V_1CH3Tail")
    Loki.add_declare_var("double", "SLD_1MSP")
    Loki.add_declare_var("double", "SLD_1MSPE3")
    Loki.add_declare_var("double", "Rough")
    Loki.add_declare_var("double", "Conc")
    Loki.add_declare_var("double", "AbsCrossection")
    Loki.add_declare_var("double", "sigma_abs_H2O")
    Loki.add_declare_var("double", "sigma_inc_H2O")
    Loki.add_declare_var("double", "sigma_abs_D2O")
    Loki.add_declare_var("double", "sigma_inc_D2O")
    Loki.add_declare_var("double", "sigma_abs_solvent")
    Loki.add_declare_var("double", "sigma_inc_solvent")
    Loki.add_declare_var("double", "RhoSolv_Inc")
    Loki.append_initialize("Repeat_Number=5; ")
    Loki.append_initialize("DetectorSize = 1.0; ")
    Loki.append_initialize("Beamstop = 0; ")
    Loki.append_initialize("P_Interact = 0.0; ")
    Loki.append_initialize("Sam = 999; ")
    Loki.append_initialize("Rmin = sqrt(0.07*0.07+0.07*0.07); ")
    Loki.append_initialize("if(Instrument_Mode < 0){Instrument_Mode = 0;} ")
    Loki.append_initialize("if(Instrument_Mode > 5){Instrument_Mode = 0;} ")
    Loki.append_initialize("if(Instrument_Mode > 2){Repeat_Number = 2;} ")
    Loki.append_initialize("if(Detector_Distance == 2.0){ ")
    Loki.append_initialize("    if(Instrument_Mode == 0){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C3_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal0_2.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 1){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C5_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal1_2.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 2){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C8_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal2_2.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 3){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C3_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal3_2.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 4){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C5_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal4_2.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 5){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C8_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal5_2.dat\");} ")
    Loki.append_initialize("} ")
    Loki.append_initialize("else if(Detector_Distance == 10.0){ ")
    Loki.append_initialize("    if(Instrument_Mode == 0){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C3_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal0_10.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 1){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C5_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal1_10.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 2){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C8_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal2_10.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 3){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C3_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal3_10.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 4){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C5_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal4_10.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 5){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C8_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal5_10.dat\");} ")
    Loki.append_initialize("} ")
    Loki.append_initialize("else{ ")
    Loki.append_initialize("    if(Instrument_Mode == 0){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C3_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal0_5.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 1){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C5_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal1_5.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 2){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C8_L115.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal2_5.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 3){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C3_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal3_5.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 4){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C5_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal4_5.dat\");} ")
    Loki.append_initialize("    if(Instrument_Mode == 5){ ")
    Loki.append_initialize("        sprintf(virtualoutput_filename,\"inputs/C8_L214.mcpl.gz\"); ")
    Loki.append_initialize("        sprintf(calibration_filename,\"calibrations/cal5_5.dat\");} ")
    Loki.append_initialize("} ")
    Loki.append_initialize("T_min=22000.0; ")
    Loki.append_initialize("T_max=170000.0; ")
    Loki.append_initialize("DetectorRadius = sqrt((DetectorSize*DetectorSize) + (DetectorSize*DetectorSize)); ")
    Loki.append_initialize("SAMPLE_HOLD = SAMPLE; ")
    Loki.append_initialize("SAMPLE_HOLD2 = SAMPLE; ")
    Loki.append_initialize("AxisRatio=1.2; ")
    Loki.append_initialize("AreaPrHead=60.13; ")
    Loki.append_initialize("H_1MSP=24.0; ")
    Loki.append_initialize("N_Lipids=120.0; ")
    Loki.append_initialize("V_1MSP=27146.4; ")
    Loki.append_initialize("SLD_1MSP=9.23E-10; ")
    Loki.append_initialize("V_1Headgruope=319.0; ")
    Loki.append_initialize("V_1CH2Tail=754.2; ")
    Loki.append_initialize("V_1CH3Tail=108.6; ")
    Loki.append_initialize("Rough=2.0; ")
    Loki.append_initialize("Conc=50.0; ")
    Loki.append_initialize("AbsCrossection=0.0; ")
    Loki.append_initialize("sigma_Head_Deutorated = 247.55E-13*(1-0.5 * Mix_Fraction) + 60.06E-13 * 0.5 * Mix_Fraction; ")
    Loki.append_initialize("sigma_CH2_Deutorated = 479.91E-13*(1-0.5 * Mix_Fraction) -20.05E-13 * 0.5 * Mix_Fraction; ")
    Loki.append_initialize("sigma_CH3_Deutorated = 53.34E-13*(1-0.5 * Mix_Fraction) -9.16E-13 * 0.5 * Mix_Fraction; ")
    Loki.append_initialize("sigma_Head_Hydrated = 60.06E-13*(1-0.5 * Mix_Fraction) + 247.55E-13 * 0.5 * Mix_Fraction; ")
    Loki.append_initialize("sigma_CH2_Hydrated = -20.05E-13*(1-0.5 * Mix_Fraction) + 479.91E-13 * 0.5 * Mix_Fraction; ")
    Loki.append_initialize("sigma_CH3_Hydrated = -9.16E-13*(1-0.5 * Mix_Fraction) + 53.34E-13 * 0.5 * Mix_Fraction; ")
    Loki.append_initialize("sigma_Head_Mixed = 153.80E-13; ")
    Loki.append_initialize("sigma_CH2_Mixed = 229.93E-13; ")
    Loki.append_initialize("sigma_CH3_Mixed = 22.09E-13; ")
    Loki.append_initialize("RhoH2O = -1.678E-13/30.; ")
    Loki.append_initialize("RhoD2O = 19.15E-13/30.; ")
    Loki.append_initialize("RhoSolv = RhoH2O*(1.0-Solvent_Fraction) + RhoD2O*Solvent_Fraction; ")
    Loki.append_initialize("sigma_abs_H2O = 2*0.3326+0.00019; ")
    Loki.append_initialize("sigma_inc_H2O = 2*80.27+0.0; ")
    Loki.append_initialize("sigma_abs_D2O = 2*0.000519+0.00019; ")
    Loki.append_initialize("sigma_inc_D2O = 2*2.05+0.0; ")
    Loki.append_initialize("sigma_abs_solvent = sigma_abs_H2O*(1.0-Solvent_Fraction) + sigma_abs_D2O*Solvent_Fraction; ")
    Loki.append_initialize("sigma_inc_solvent = sigma_inc_H2O*(1.0-Solvent_Fraction) + sigma_inc_D2O*Solvent_Fraction; ")
    Loki.append_initialize("RhoSolv_Inc = sigma_inc_solvent/30.; ")
    Loki.append_initialize("if(Incoherent_Solvent == 1){ ")
    Loki.append_initialize("  Conc = 0.0; ")
    Loki.append_initialize("} ")
    Loki.append_initialize("if(Incoherent_Solvent == 2){ ")
    Loki.append_initialize("  RhoSolv_Inc = 0.0; ")
    Loki.append_initialize("} ")
    
    Origin = Loki.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")
    
    virtual_input = Loki.add_component("virtual_input", "MCPL_input")
    virtual_input.filename = "virtualoutput_filename"
    virtual_input.verbose = 1
    virtual_input.repeat_count = "Repeat_Number"
    virtual_input.E_smear = 0.01
    virtual_input.pos_smear = 0.0001
    virtual_input.dir_smear = 0.0001
    virtual_input.append_EXTEND("if(SAMPLE_HOLD2 == 2){")
    virtual_input.append_EXTEND("SAMPLE_Select = rand() % 2;")
    virtual_input.append_EXTEND("SAMPLE_HOLD = SAMPLE_Select;")
    virtual_input.append_EXTEND("}")
    virtual_input.set_AT(['0', '0', '0'], RELATIVE="Origin")

    l_monitor_before_sample = Loki.add_component("l_monitor_before_sample", "L_monitor")
    l_monitor_before_sample.nL = 100
    l_monitor_before_sample.filename = "\"Lambda_before_sample\""
    l_monitor_before_sample.xwidth = "DetectorRadius"
    l_monitor_before_sample.yheight = "DetectorRadius"
    l_monitor_before_sample.Lmin = 0.0
    l_monitor_before_sample.Lmax = 23.0
    l_monitor_before_sample.restore_neutron = 1
    l_monitor_before_sample.set_AT(['0', ' 0', ' 0.004'], RELATIVE="virtual_input")

    Hydrated_Disc = Loki.add_component("Hydrated_Disc", "SANSNanodiscsFast_Loki")
    Hydrated_Disc.AxisRatio = "AxisRatio"
    Hydrated_Disc.NumberOfLipids = "N_Lipids"
    Hydrated_Disc.AreaPerLipidHeadgroup = "AreaPrHead"
    Hydrated_Disc.HeightOfMSP = "H_1MSP"
    Hydrated_Disc.VolumeOfOneMSP = "V_1MSP"
    Hydrated_Disc.VolumeOfHeadgroup = "V_1Headgruope"
    Hydrated_Disc.VolumeOfCH2Tail = "V_1CH2Tail"
    Hydrated_Disc.VolumeOfCH3Tail = "V_1CH3Tail"
    Hydrated_Disc.ScatteringLengthOfOneMSP = "SLD_1MSP"
    Hydrated_Disc.ScatteringLengthOfHeadgroup = "sigma_Head_Hydrated"
    Hydrated_Disc.ScatteringLengthOfCH2Tail = "sigma_CH2_Hydrated"
    Hydrated_Disc.ScatteringLengthOfCH3Tail = "sigma_CH3_Hydrated"
    Hydrated_Disc.Roughness = "Rough"
    Hydrated_Disc.Concentration = "Conc"
    Hydrated_Disc.RhoSolvent = "RhoSolv"
    Hydrated_Disc.RhoSolventIncoherent = "RhoSolv_Inc"
    Hydrated_Disc.AbsorptionCrosssection = "AbsCrossection"
    Hydrated_Disc.AbsorptionCrosssectionSolvent = "sigma_abs_solvent"
    Hydrated_Disc.xwidth = 0.1
    Hydrated_Disc.yheight = 0.1
    Hydrated_Disc.zdepth = 0.005
    Hydrated_Disc.SampleToDetectorDistance = "Detector_Distance"
    Hydrated_Disc.DetectorRadius = "DetectorRadius"
    Hydrated_Disc.qMin = 0.0
    Hydrated_Disc.qMax = 10.0
    Hydrated_Disc.beamwidth_x = 0.01
    Hydrated_Disc.beamwidth_y = 0.01
    Hydrated_Disc.set_WHEN("SAMPLE_HOLD==0")
    Hydrated_Disc.set_AT(['0', ' 0', ' 0.005'], RELATIVE="virtual_input")

    Deutorated_Disc = Loki.add_component("Deutorated_Disc", "SANSNanodiscsFast_Loki")
    Deutorated_Disc.AxisRatio = "AxisRatio"
    Deutorated_Disc.NumberOfLipids = "N_Lipids"
    Deutorated_Disc.AreaPerLipidHeadgroup = "AreaPrHead"
    Deutorated_Disc.HeightOfMSP = "H_1MSP"
    Deutorated_Disc.VolumeOfOneMSP = "V_1MSP"
    Deutorated_Disc.VolumeOfHeadgroup = "V_1Headgruope"
    Deutorated_Disc.VolumeOfCH2Tail = "V_1CH2Tail"
    Deutorated_Disc.VolumeOfCH3Tail = "V_1CH3Tail"
    Deutorated_Disc.ScatteringLengthOfOneMSP = "SLD_1MSP"
    Deutorated_Disc.ScatteringLengthOfHeadgroup = "sigma_Head_Deutorated"
    Deutorated_Disc.ScatteringLengthOfCH2Tail = "sigma_CH2_Deutorated"
    Deutorated_Disc.ScatteringLengthOfCH3Tail = "sigma_CH3_Deutorated"
    Deutorated_Disc.Roughness = "Rough"
    Deutorated_Disc.Concentration = "Conc"
    Deutorated_Disc.RhoSolvent = "RhoSolv"
    Deutorated_Disc.RhoSolventIncoherent = "RhoSolv_Inc"
    Deutorated_Disc.AbsorptionCrosssection = "AbsCrossection"
    Deutorated_Disc.AbsorptionCrosssectionSolvent = "sigma_abs_solvent"
    Deutorated_Disc.xwidth = 0.1
    Deutorated_Disc.yheight = 0.1
    Deutorated_Disc.zdepth = 0.005
    Deutorated_Disc.SampleToDetectorDistance = "Detector_Distance"
    Deutorated_Disc.DetectorRadius = "DetectorRadius"
    Deutorated_Disc.qMin = 0.0
    Deutorated_Disc.qMax = 10.0
    Deutorated_Disc.beamwidth_x = 0.01
    Deutorated_Disc.beamwidth_y = 0.01
    Deutorated_Disc.set_WHEN("SAMPLE_HOLD==1")
    Deutorated_Disc.set_AT(['0', ' 0', ' 0.005'], RELATIVE="virtual_input")

    beamstop = Loki.add_component("beamstop", "Beamstop")
    beamstop.xwidth = 0.012
    beamstop.yheight = 0.012
    beamstop.set_WHEN("Beamstop==1")
    beamstop.set_AT(['0', '0', '1'], RELATIVE="virtual_input")

    tof_sans_monitor = Loki.add_component("tof_sans_monitor", "TOF_SANS_spacial_monitor")
    tof_sans_monitor.nr = 200
    tof_sans_monitor.nt = 1000
    tof_sans_monitor.nq = 500
    tof_sans_monitor.qFilename = "\"QDetector\""
    tof_sans_monitor.filename = "\"TOF_SANS\""
    tof_sans_monitor.calibration_file = "calibration_filename"
    tof_sans_monitor.rmax = "DetectorRadius"
    tof_sans_monitor.rmin = "Rmin"
    tof_sans_monitor.tmin = "T_min"
    tof_sans_monitor.tmax = "T_max"
    tof_sans_monitor.SDD = "Detector_Distance+0.005"
    tof_sans_monitor.restore_neutron = 1
    tof_sans_monitor.instrumentlength = "Detector_Distance+0.005+23.5"
    tof_sans_monitor.set_AT(['0', ' 0', ' Detector_Distance+0.005'], RELATIVE="virtual_input")

    return Loki
