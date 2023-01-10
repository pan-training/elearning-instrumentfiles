"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():

    reflectometer = instr.McStas_instr("reflectometer_generated")
    reflectometer.add_parameter("double", "lambda_min", value=5.3, comment="[AA]   Minimum wavelength from source")
    reflectometer.add_parameter("double", "lambda_max", value=5.45, comment="[AA]   Maximum wavelength from source")
    reflectometer.add_parameter("double", "slittranslation", value=0.0, comment="[m]    Translation of slit (horizontal)")
    reflectometer.add_parameter("double", "sampletranslation", value=0.0, comment="[m]    Sample translation (horizontal)")
    reflectometer.add_parameter("double", "slitwidth", value=0.001, comment="[m]    Width of slit pinholes")
    reflectometer.add_parameter("double", "slitheight", value=0.002, comment="[m]    Height of slit pinholes")
    reflectometer.add_parameter("double", "dist_source2slit", value=1.0, comment="[m]    Distance between source and first slit")
    reflectometer.add_parameter("double", "dist_slit2slit", value=3.2, comment="[m]    Distance between slits")
    reflectometer.add_parameter("double", "dist_slit2sample", value=0.18, comment="[m]    Distance between second slit and sample")
    reflectometer.add_parameter("double", "dist_sample2detector", value=2.0, comment="[m]    Distance between sample and detector")
    sample_type = reflectometer.add_parameter("double", "sampletype", value=1.0, comment="[1]    Sample type: 0 none, 1 mirror, 2+ multilayer")
    sample_type.add_option([0, 1, 2, 3, 4, 5, 6, 7], True)
    reflectometer.add_parameter("double", "samplesize", value=0.15, comment="[m]    Side-length of the (quadratic) sample plate")
    reflectometer.add_parameter("double", "substratethickness", value=0.003, comment="[m]    Thickness of the substrate")
    reflectometer.add_parameter("double", "MR_Qc", value=0.15, comment="[AA]   Critical Q-vector length of mirror sample")
    reflectometer.add_parameter("double", "sampleangle", value=2.5, comment="[deg]  Rotation angle of sample (theta)")
    reflectometer.add_parameter("double", "detectorangle", value=5.0, comment="[deg]  Rotation angle of detector (2 theta)")
    
    reflectometer.add_declare_var("double", "blocktranslation")
    reflectometer.append_initialize("blocktranslation = -slittranslation; ")

    Origin = reflectometer.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Source = reflectometer.add_component("Source", "Source_Maxwell_3")
    Source.size = 0.12
    Source.Lmin = "lambda_min"
    Source.Lmax = "lambda_max"
    Source.dist = "dist_source2slit+dist_slit2slit"
    Source.focus_xw = "slitwidth"
    Source.focus_yh = "slitheight"
    Source.T1 = 150.42
    Source.T2 = 38.72
    Source.T3 = 14.84
    Source.I1 = 3.67E11
    Source.I2 = 3.64E11
    Source.I3 = 0.95E11
    Source.set_AT(['0', ' 0', ' 0'], RELATIVE="Origin")

    mon_PSD_atSource = reflectometer.add_component("mon_PSD_atSource", "PSD_monitor")
    mon_PSD_atSource.nx = 100
    mon_PSD_atSource.ny = 100
    mon_PSD_atSource.filename = "\"mon_PSD_atSource.dat\""
    mon_PSD_atSource.xwidth = 0.2
    mon_PSD_atSource.yheight = 0.2
    mon_PSD_atSource.restore_neutron = 1
    mon_PSD_atSource.set_AT(['0', ' 0', ' 0.01'], RELATIVE="Source")

    mon_div_atSource = reflectometer.add_component("mon_div_atSource", "Divergence_monitor")
    mon_div_atSource.nh = 100
    mon_div_atSource.nv = 100
    mon_div_atSource.filename = "\"mon_div_atSource\""
    mon_div_atSource.xwidth = 0.2
    mon_div_atSource.yheight = 0.2
    mon_div_atSource.maxdiv_h = 10
    mon_div_atSource.maxdiv_v = 10
    mon_div_atSource.restore_neutron = 1
    mon_div_atSource.set_AT(['0', ' 0', ' 1e-6'], RELATIVE="PREVIOUS")

    mon_Lmon_atSource = reflectometer.add_component("mon_Lmon_atSource", "L_monitor")
    mon_Lmon_atSource.nL = 100
    mon_Lmon_atSource.filename = "\"mon_Lmon_atSource.dat\""
    mon_Lmon_atSource.xwidth = 0.2
    mon_Lmon_atSource.yheight = 0.2
    mon_Lmon_atSource.Lmin = 0
    mon_Lmon_atSource.Lmax = 22
    mon_Lmon_atSource.restore_neutron = 1
    mon_Lmon_atSource.set_AT(['0', ' 0', ' 1e-6'], RELATIVE="PREVIOUS")

    Slit1 = reflectometer.add_component("Slit1", "Slit")
    Slit1.xwidth = "slitwidth"
    Slit1.yheight = "slitheight"
    Slit1.set_AT(['0', ' 0', ' dist_source2slit'], RELATIVE="Source")

    mon_PSD_afterSlit1 = reflectometer.add_component("mon_PSD_afterSlit1", "PSD_monitor")
    mon_PSD_afterSlit1.nx = 100
    mon_PSD_afterSlit1.ny = 100
    mon_PSD_afterSlit1.filename = "\"mon_PSD_afterslit1.dat\""
    mon_PSD_afterSlit1.xwidth = "slitwidth+0.1"
    mon_PSD_afterSlit1.yheight = "slitheight+0.1"
    mon_PSD_afterSlit1.restore_neutron = 1
    mon_PSD_afterSlit1.set_AT(['0', ' 0', ' 0.01'], RELATIVE="Slit1")

    mon_div_afterSlit1 = reflectometer.add_component("mon_div_afterSlit1", "Divergence_monitor")
    mon_div_afterSlit1.nh = 100
    mon_div_afterSlit1.nv = 100
    mon_div_afterSlit1.filename = "\"mon_div_afterSlit1\""
    mon_div_afterSlit1.xwidth = "slitwidth+0.1"
    mon_div_afterSlit1.yheight = "slitheight+0.1"
    mon_div_afterSlit1.maxdiv_h = 10
    mon_div_afterSlit1.maxdiv_v = 10
    mon_div_afterSlit1.restore_neutron = 1
    mon_div_afterSlit1.set_AT(['0', ' 0', ' 1e-6'], RELATIVE="PREVIOUS")

    mon_Lmon_afterSlit1 = reflectometer.add_component("mon_Lmon_afterSlit1", "L_monitor")
    mon_Lmon_afterSlit1.nL = 100
    mon_Lmon_afterSlit1.filename = "\"mon_Lmon_afterSlit1.dat\""
    mon_Lmon_afterSlit1.xwidth = "slitwidth+0.1"
    mon_Lmon_afterSlit1.yheight = "slitheight+0.1"
    mon_Lmon_afterSlit1.Lmin = 0
    mon_Lmon_afterSlit1.Lmax = 22
    mon_Lmon_afterSlit1.restore_neutron = 1
    mon_Lmon_afterSlit1.set_AT(['0', ' 0', ' 1e-6'], RELATIVE="PREVIOUS")

    Slit2 = reflectometer.add_component("Slit2", "Slit")
    Slit2.xwidth = "slitwidth"
    Slit2.yheight = "slitheight"
    Slit2.set_AT(['0', ' 0', ' dist_slit2slit'], RELATIVE="Slit1")

    mon_PSD_afterSlit2 = reflectometer.add_component("mon_PSD_afterSlit2", "PSD_monitor")
    mon_PSD_afterSlit2.nx = 100
    mon_PSD_afterSlit2.ny = 100
    mon_PSD_afterSlit2.filename = "\"mon_PSD_afterslit2.dat\""
    mon_PSD_afterSlit2.xwidth = "slitwidth+0.1"
    mon_PSD_afterSlit2.yheight = "slitheight+0.1"
    mon_PSD_afterSlit2.restore_neutron = 1
    mon_PSD_afterSlit2.set_AT(['0', ' 0', ' 0.01'], RELATIVE="Slit2")

    mon_div_afterSlit2 = reflectometer.add_component("mon_div_afterSlit2", "Divergence_monitor")
    mon_div_afterSlit2.nh = 100
    mon_div_afterSlit2.nv = 100
    mon_div_afterSlit2.filename = "\"mon_div_afterSlit2\""
    mon_div_afterSlit2.xwidth = "slitwidth+0.1"
    mon_div_afterSlit2.yheight = "slitheight+0.1"
    mon_div_afterSlit2.maxdiv_h = 10
    mon_div_afterSlit2.maxdiv_v = 10
    mon_div_afterSlit2.restore_neutron = 1
    mon_div_afterSlit2.set_AT(['0', ' 0', ' 1e-6'], RELATIVE="PREVIOUS")

    mon_Lmon_afterSlit2 = reflectometer.add_component("mon_Lmon_afterSlit2", "L_monitor")
    mon_Lmon_afterSlit2.nL = 100
    mon_Lmon_afterSlit2.filename = "\"mon_Lmon_afterSlit2.dat\""
    mon_Lmon_afterSlit2.xwidth = "slitwidth+0.1"
    mon_Lmon_afterSlit2.yheight = "slitheight+0.1"
    mon_Lmon_afterSlit2.Lmin = 0
    mon_Lmon_afterSlit2.Lmax = 22
    mon_Lmon_afterSlit2.restore_neutron = 1
    mon_Lmon_afterSlit2.set_AT(['0', ' 0', ' 1e-6'], RELATIVE="PREVIOUS")

    Arm_sampleNOROTNOTRANS = reflectometer.add_component("Arm_sampleNOROTNOTRANS", "Arm")
    Arm_sampleNOROTNOTRANS.set_AT(['blocktranslation', ' 0', ' dist_slit2sample'], RELATIVE="Slit2")

    Arm_sampleNOROT = reflectometer.add_component("Arm_sampleNOROT", "Arm")
    Arm_sampleNOROT.set_AT(['sampletranslation', ' 0', ' 0'], RELATIVE="Arm_sampleNOROTNOTRANS")

    Arm_sample = reflectometer.add_component("Arm_sample", "Arm")
    Arm_sample.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sampleNOROT")
    Arm_sample.set_ROTATED(['0', ' sampleangle', ' 0'], RELATIVE="Arm_sampleNOROT")

    Sample_Mirror = reflectometer.add_component("Sample_Mirror", "Mirror")
    Sample_Mirror.xwidth = "samplesize"
    Sample_Mirror.yheight = "samplesize"
    Sample_Mirror.R0 = 0.99
    Sample_Mirror.Qc = "MR_Qc"
    Sample_Mirror.alpha = 6.07
    Sample_Mirror.m = 1
    Sample_Mirror.W = 0.003
    Sample_Mirror.center = 1
    Sample_Mirror.set_WHEN("sampletype == 1")
    Sample_Mirror.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Mirror.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Sample_Mirror_backside = reflectometer.add_component("Sample_Mirror_backside", "Isotropic_Sqw")
    Sample_Mirror_backside.xwidth = "samplesize"
    Sample_Mirror_backside.yheight = "samplesize"
    Sample_Mirror_backside.zdepth = "substratethickness"
    Sample_Mirror_backside.rho = "1/13.827"
    Sample_Mirror_backside.sigma_abs = 500.08
    Sample_Mirror_backside.sigma_coh = 0
    Sample_Mirror_backside.sigma_inc = 4.935
    Sample_Mirror_backside.set_WHEN("sampletype == 1")
    Sample_Mirror_backside.set_AT(['0', ' 0', ' -substratethickness/2-1e-6'], RELATIVE="Sample_Mirror")

    Sample_Multilayer1 = reflectometer.add_component("Sample_Multilayer1", "Mirror")
    Sample_Multilayer1.reflect = "\"d54DMPC-D2O.dat\""
    Sample_Multilayer1.xwidth = "samplesize"
    Sample_Multilayer1.yheight = "samplesize"
    Sample_Multilayer1.center = 1
    Sample_Multilayer1.set_WHEN("sampletype == 2")
    Sample_Multilayer1.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Multilayer1.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Sample_Multilayer2 = reflectometer.add_component("Sample_Multilayer2", "Mirror")
    Sample_Multilayer2.reflect = "\"d54DMPC-H2O.dat\""
    Sample_Multilayer2.xwidth = "samplesize"
    Sample_Multilayer2.yheight = "samplesize"
    Sample_Multilayer2.center = 1
    Sample_Multilayer2.set_WHEN("sampletype == 3")
    Sample_Multilayer2.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Multilayer2.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Sample_Multilayer3 = reflectometer.add_component("Sample_Multilayer3", "Mirror")
    Sample_Multilayer3.reflect = "\"hDMPC-D2O.dat\""
    Sample_Multilayer3.xwidth = "samplesize"
    Sample_Multilayer3.yheight = "samplesize"
    Sample_Multilayer3.center = 1
    Sample_Multilayer3.set_WHEN("sampletype == 5")
    Sample_Multilayer3.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Multilayer3.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Sample_Multilayer4 = reflectometer.add_component("Sample_Multilayer4", "Mirror")
    Sample_Multilayer4.reflect = "\"hDMPC-H2O.dat\""
    Sample_Multilayer4.xwidth = "samplesize"
    Sample_Multilayer4.yheight = "samplesize"
    Sample_Multilayer4.center = 1
    Sample_Multilayer4.set_WHEN("sampletype == 6")
    Sample_Multilayer4.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Multilayer4.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Sample_Multilayer5 = reflectometer.add_component("Sample_Multilayer5", "Mirror")
    Sample_Multilayer5.reflect = "\"silicon-D2O.dat\""
    Sample_Multilayer5.xwidth = "samplesize"
    Sample_Multilayer5.yheight = "samplesize"
    Sample_Multilayer5.center = 1
    Sample_Multilayer5.set_WHEN("sampletype == 6")
    Sample_Multilayer5.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Multilayer5.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Sample_Multilayer6 = reflectometer.add_component("Sample_Multilayer6", "Mirror")
    Sample_Multilayer6.reflect = "\"silicon-H2O.dat\""
    Sample_Multilayer6.xwidth = "samplesize"
    Sample_Multilayer6.yheight = "samplesize"
    Sample_Multilayer6.center = 1
    Sample_Multilayer6.set_WHEN("sampletype == 7")
    Sample_Multilayer6.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sample")
    Sample_Multilayer6.set_ROTATED(['0', ' 90', ' 0'], RELATIVE="Arm_sample")

    Arm_detectorONLYROT = reflectometer.add_component("Arm_detectorONLYROT", "Arm")
    Arm_detectorONLYROT.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_sampleNOROTNOTRANS")
    Arm_detectorONLYROT.set_ROTATED(['0', ' detectorangle', ' 0'], RELATIVE="Source")

    Arm_detector = reflectometer.add_component("Arm_detector", "Arm")
    Arm_detector.set_AT(['0', ' 0', ' dist_sample2detector'], RELATIVE="Arm_detectorONLYROT")

    Detector = reflectometer.add_component("Detector", "PSD_monitor")
    Detector.nx = 200
    Detector.ny = 200
    Detector.filename = "\"mon_detector\""
    Detector.xwidth = 0.025
    Detector.yheight = 0.05
    Detector.restore_neutron = 1
    Detector.set_AT(['0', ' 0', ' 0'], RELATIVE="Arm_detector")
    
    return reflectometer
