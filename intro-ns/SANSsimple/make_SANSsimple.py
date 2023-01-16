"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    SANS2_liposomes = instr.McStas_instr("SANS2_liposomes_generated")
    SANS2_liposomes.add_parameter("double", "pinhole_rad", value=0.004)
    SANS2_liposomes.add_parameter("double", "LC", value=3.0)
    SANS2_liposomes.add_parameter("double", "LD", value=3.0)
    SANS2_liposomes.add_parameter("double", "Lambda", value=6.0)
    SANS2_liposomes.add_parameter("double", "DLambda", value=0.6)
    SANS2_liposomes.add_parameter("double", "R", value=400.0)
    SANS2_liposomes.add_parameter("double", "dR", value=0.0)
    SANS2_liposomes.add_parameter("double", "dbilayer", value=35.0)
    SANS2_liposomes.add_parameter("double", "PHI", value=0.01)
    SANS2_liposomes.add_parameter("double", "Delta_Rho", value=0.6)
    SANS2_liposomes.add_parameter("double", "Qmax", value=0.3)
    SANS2_liposomes.add_parameter("double", "BEAMSTOP", value=1.0)
    SANS2_liposomes.add_parameter("double", "SAMPLE", value=1.0)
    SANS2_liposomes.add_parameter("double", "Sigma_a", value=0.0)
    SANS2_liposomes.add_declare_var("double", "nm", value=1e-09)
    SANS2_liposomes.add_declare_var("double", "Rdet")
    SANS2_liposomes.append_initialize("Rdet=0.5; ")

    Origin = SANS2_liposomes.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', ' 0', ' 0'], RELATIVE="ABSOLUTE")

    source = SANS2_liposomes.add_component("source", "Source_Maxwell_3")
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

    ArmSlit1 = SANS2_liposomes.add_component("ArmSlit1", "Arm")
    ArmSlit1.set_AT(['0', '0', '6-LC+0.001'], RELATIVE="source")

    CircSlit1 = SANS2_liposomes.add_component("CircSlit1", "Slit")
    CircSlit1.radius = "pinhole_rad"
    CircSlit1.set_AT(['0', ' 0', ' 0'], RELATIVE="ArmSlit1")

    ArmSlit2 = SANS2_liposomes.add_component("ArmSlit2", "Arm")
    ArmSlit2.set_AT(['0', '0', '6'], RELATIVE="source")

    CircSlit2 = SANS2_liposomes.add_component("CircSlit2", "Slit")
    CircSlit2.radius = "pinhole_rad"
    CircSlit2.set_AT(['0', ' 0', ' 0'], RELATIVE="ArmSlit2")

    SampleArm = SANS2_liposomes.add_component("SampleArm", "Arm")
    SampleArm.set_AT(['0', '0', '0.05'], RELATIVE="ArmSlit2")

    return SANS2_liposomes
