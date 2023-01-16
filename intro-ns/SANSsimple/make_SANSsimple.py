"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    SANSsimple = instr.McStas_instr("SANSsimple_generated")
    SANSsimple.add_parameter("double", "pinhole_rad", value=0.004)
    SANSsimple.add_parameter("double", "LC", value=3.0)
    SANSsimple.add_parameter("double", "LD", value=3.0)
    SANSsimple.add_parameter("double", "Lambda", value=6.0)
    SANSsimple.add_parameter("double", "DLambda", value=0.6)
    SANSsimple.add_parameter("double", "R", value=400.0)
    SANSsimple.add_parameter("double", "dR", value=0.0)
    SANSsimple.add_parameter("double", "dbilayer", value=35.0)
    SANSsimple.add_parameter("double", "PHI", value=0.01)
    SANSsimple.add_parameter("double", "Delta_Rho", value=0.6)
    SANSsimple.add_parameter("double", "Qmax", value=0.3)
    SANSsimple.add_parameter("double", "BEAMSTOP", value=1.0)
    SANSsimple.add_parameter("double", "SAMPLE", value=1.0)
    SANSsimple.add_parameter("double", "Sigma_a", value=0.0)
    SANSsimple.add_declare_var("double", "nm", value=1e-09)
    SANSsimple.add_declare_var("double", "Rdet")
    SANSsimple.append_initialize("Rdet=0.5; ")

    Origin = SANSsimple.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', ' 0', ' 0'], RELATIVE="ABSOLUTE")

    source = SANSsimple.add_component("source", "Source_Maxwell_3")
    source.size = "2*pinhole_rad"
    source.Lmin = "Lambda-DLambda"
    source.Lmax = "Lambda+DLambda"
    source.dist = "LC"
    source.focus_xw = "pinhole_rad"
    source.focus_yh = "pinhole_rad"
    source.T1 = 150.42
    source.T2 = 38.74
    source.T3 = 14.84
    source.I1 = 3.67e11
    source.I2 = 3.64e11
    source.I3 = 0.95e11
    source.set_AT(['0', ' 0', ' 0'], RELATIVE="Origin")

    ArmSlit1 = SANSsimple.add_component("ArmSlit1", "Arm")
    ArmSlit1.set_AT(['0', '0', '6-LC+0.001'], RELATIVE="source")

    CircSlit1 = SANSsimple.add_component("CircSlit1", "Slit")
    CircSlit1.radius = "pinhole_rad"
    CircSlit1.set_AT(['0', ' 0', ' 0'], RELATIVE="ArmSlit1")

    ArmSlit2 = SANSsimple.add_component("ArmSlit2", "Arm")
    ArmSlit2.set_AT(['0', '0', '6'], RELATIVE="source")

    CircSlit2 = SANSsimple.add_component("CircSlit2", "Slit")
    CircSlit2.radius = "pinhole_rad"
    CircSlit2.set_AT(['0', ' 0', ' 0'], RELATIVE="ArmSlit2")

    SampleArm = SANSsimple.add_component("SampleArm", "Arm")
    SampleArm.set_AT(['0', '0', '0.05'], RELATIVE="ArmSlit2")

    sampleB = SANSsimple.add_component("sampleB", "Sans_liposomes_new")
    sampleB.R = "R"
    sampleB.dR = "dR"
    sampleB.Phi = "PHI"
    sampleB.Delta_rho = "DeltaRho"
    sampleB.sigma_a = 0.5
    sampleB.qmax = "Qmax"
    sampleB.xwidth = "4*pinhole_rad"
    sampleB.yheight = "4*pinhole_rad"
    sampleB.dist = "LD"
    sampleB.Rdet = "Rdet"
    sampleB.set_WHEN("SAMPLE==1")
    sampleB.set_AT(['0', '0', '0'], RELATIVE="SampleArm")

    beamstop = SANSsimple.add_component("beamstop", "Beamstop")
    beamstop.radius = "3*pinhole_rad"
    beamstop.set_WHEN("BEAMSTOP")
    beamstop.set_AT(['0', '0', 'LD-0.01'], RELATIVE="ArmSlit2")

    PSD = SANSsimple.add_component("PSD", "PSD_monitor")
    PSD.nx = 128
    PSD.ny = 128
    PSD.restore_neutron = 1
    PSD.filename = "\"PSD.dat\""
    PSD.xwidth = 1
    PSD.yheight = 1
    PSD.set_AT(['0', '0', 'LD-0.01'], RELATIVE="ArmSlit2")

    q_monitor = SANSsimple.add_component("q_monitor", "SANSQMonitor")
    q_monitor.RFilename = "\"rdetector.dat\""
    q_monitor.qFilename = "\"qdetector.dat\""
    q_monitor.NumberOfBins = 100
    q_monitor.restore_neutron = 1
    q_monitor.RadiusDetector = "Rdet"
    q_monitor.DistanceFromSample = "LD"
    q_monitor.LambdaMin = "Lambda"
    q_monitor.Lambda0 = "Lambda"
    q_monitor.set_AT(['0', '0', 'LD-0.01'], RELATIVE="ArmSlit2")

    return SANSsimple
