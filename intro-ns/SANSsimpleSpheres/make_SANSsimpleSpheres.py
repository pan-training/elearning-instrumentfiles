"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    SANSsimpleSpheres = instr.McStas_instr("SANSsimpleSpheres_generated")
    SANSsimpleSpheres.add_parameter("double", "pinhole_rad", value=0.004)
    SANSsimpleSpheres.add_parameter("double", "LC", value=3.0)
    SANSsimpleSpheres.add_parameter("double", "LD", value=3.0)
    SANSsimpleSpheres.add_parameter("double", "Lambda", value=6.0)
    SANSsimpleSpheres.add_parameter("double", "DLambda", value=0.001)
    SANSsimpleSpheres.add_parameter("double", "R", value=400.0)
    SANSsimpleSpheres.add_parameter("double", "dR", value=0.0)
    SANSsimpleSpheres.add_parameter("double", "PHI", value=0.01)
    SANSsimpleSpheres.add_parameter("double", "Delta_Rho", value=0.6)
    SANSsimpleSpheres.add_parameter("double", "BEAMSTOP", value=1.0)
    SANSsimpleSpheres.add_parameter("double", "SAMPLE", value=1.0)
    SANSsimpleSpheres.add_declare_var("double", "nm", value=1e-09)
    SANSsimpleSpheres.add_declare_var("double", "Rdet")
    SANSsimpleSpheres.add_declare_var("double", "Na", value=6.02214129e+23)
    SANSsimpleSpheres.add_declare_var("double", "VAA")
    SANSsimpleSpheres.add_declare_var("double", "V")
    SANSsimpleSpheres.add_declare_var("double", "Vm")
    SANSsimpleSpheres.add_declare_var("double", "conc")
    SANSsimpleSpheres.add_declare_var("double", "DeltaRho")
    SANSsimpleSpheres.append_initialize("Rdet=0.5; ")
    SANSsimpleSpheres.append_initialize("if (DLambda==0){ ")
    SANSsimpleSpheres.append_initialize("printf(\" \\n Warning: Monochromatic source, setting automatic bandwidth DLambda=0.001 AA.\\n \\n\"); ")
    SANSsimpleSpheres.append_initialize("DLambda=0.001; ")
    SANSsimpleSpheres.append_initialize("} ")
    SANSsimpleSpheres.append_initialize("VAA =   4.0 / 3.0 * PI * pow(R, 3) ; ")
    SANSsimpleSpheres.append_initialize("V = VAA*1e-27; ")
    SANSsimpleSpheres.append_initialize("Vm = V*NA*1e-3; ")
    SANSsimpleSpheres.append_initialize("conc = PHI / Vm; ")
    SANSsimpleSpheres.append_initialize("printf(\" \\n Concentration of sample = %g mmol/L \\n\",conc); ")
    SANSsimpleSpheres.append_initialize("DeltaRho = Delta_Rho*1e-13; ")

    Origin = SANSsimpleSpheres.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    source = SANSsimpleSpheres.add_component("source", "Source_Maxwell_3")
    source.size = "2*pinhole_rad"
    source.Lmin = "Lambda-DLambda"
    source.Lmax = "Lambda+DLambda"
    source.dist = "LC"
    source.focus_xw = "pinhole_rad"
    source.focus_yh = "pinhole_rad"
    source.T1 = 150.42
    source.T2 = 38.74
    source.T3 = 14.84
    source.I1 = 3.67
    source.I2 = 3.64e11
    source.I3 = 0.95e11
    source.set_AT(['0', ' 0', ' 0'], RELATIVE="Origin")

    ArmSlit1 = SANSsimpleSpheres.add_component("ArmSlit1", "Arm")
    ArmSlit1.set_AT(['0', ' 0', ' 6-LC+0.001'], RELATIVE="source")

    CircSlit1 = SANSsimpleSpheres.add_component("CircSlit1", "Slit")
    CircSlit1.radius = "pinhole_rad"
    CircSlit1.set_AT(['0', ' 0', ' 0'], RELATIVE="ArmSlit1")

    ArmSlit2 = SANSsimpleSpheres.add_component("ArmSlit2", "Arm")
    ArmSlit2.set_AT(['0', '0', '6'], RELATIVE="source")

    CircSlit2 = SANSsimpleSpheres.add_component("CircSlit2", "Slit")
    CircSlit2.radius = "pinhole_rad"
    CircSlit2.set_AT(['0', ' 0', ' 0'], RELATIVE="ArmSlit2")

    SampleArm = SANSsimpleSpheres.add_component("SampleArm", "Arm")
    SampleArm.set_AT(['0', '0', '0.05'], RELATIVE="ArmSlit2")

    sample = SANSsimpleSpheres.add_component("sample", "SANSSpheresPolydisperse")
    sample.R = "R"
    sample.dR = "dR"
    sample.Concentration = "conc"
    sample.DeltaRho = "DeltaRho"
    sample.AbsorptionCrosssection = 0.5
    sample.xwidth = "4*pinhole_rad"
    sample.yheight = "4*pinhole_rad"
    sample.zdepth = 0.005
    sample.SampleToDetectorDistance = "LD"
    sample.DetectorRadius = "1.03*Rdet"
    sample.set_WHEN("SAMPLE")
    sample.set_AT(['0', '0', '0'], RELATIVE="SampleArm")

    beamstop = SANSsimpleSpheres.add_component("beamstop", "Beamstop")
    beamstop.radius = "3*pinhole_rad"
    beamstop.set_WHEN("BEAMSTOP")
    beamstop.set_AT(['0', '0', 'LD-0.01'], RELATIVE="ArmSlit2")

    PSD = SANSsimpleSpheres.add_component("PSD", "PSD_monitor")
    PSD.nx = 128
    PSD.ny = 128
    PSD.restore_neutron = 1
    PSD.filename = "\"PSD.dat\""
    xwidth = 1
    PSD.yheight = 1
    PSD.set_AT(['0', '0', 'LD-0.01'], RELATIVE="ArmSlit2")

    q_monitor = SANSsimpleSpheres.add_component("q_monitor", "SANSQMonitor")
    q_monitor.RFilename = "\"rdetector.dat\""
    q_monitor.qFilename = "\"qdetector.dat\""
    q_monitor.NumberOfBins = 100
    q_monitor.restore_neutron = 1
    q_monitor.RadiusDetector = "Rdet"
    q_monitor.DistanceFromSample = "LD"
    q_monitor.LambdaMin = "Lambda"
    q_monitor.Lambda0 = "Lambda"
    q_monitor.set_AT(['0', '0', 'LD-0.01'], RELATIVE="ArmSlit2")

    return SANSsimpleSpheres
