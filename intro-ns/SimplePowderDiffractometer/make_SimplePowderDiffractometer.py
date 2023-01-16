"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    SimplePowderDIffractometer = instr.McStas_instr("SimplePowderDIffractometer_generated")
    SimplePowderDIffractometer.add_parameter("double", "lambda0", value=1.0)
    SimplePowderDIffractometer.add_parameter("double", "dlambda", value=0.005)
    SimplePowderDIffractometer.add_parameter("double", "coll", value=120.0)
    SimplePowderDIffractometer.add_parameter("int", "container", value=0)
    SimplePowderDIffractometer.add_parameter("int", "sample", value=0)
    SimplePowderDIffractometer.add_declare_var("double", "L1", value=3.0)
    SimplePowderDIffractometer.add_declare_var("double", "LC", value=1.0)
    SimplePowderDIffractometer.add_declare_var("double", "sample_radius", value=0.005)
    SimplePowderDIffractometer.add_declare_var("double", "sample_height", value=0.05)
    SimplePowderDIffractometer.add_declare_var("double", "al_thickness", value=0.002)
    SimplePowderDIffractometer.add_declare_var("char", "samplestring", array=128)
    SimplePowderDIffractometer.append_initialize("if (sample==0) { ")
    SimplePowderDIffractometer.append_initialize("  sprintf(samplestring,\"Ni.laz\"); ")
    SimplePowderDIffractometer.append_initialize("} else if (sample==1) { ")
    SimplePowderDIffractometer.append_initialize("  sprintf(samplestring,\"Fe.laz\"); ")
    SimplePowderDIffractometer.append_initialize("} else if (sample==2) { ")
    SimplePowderDIffractometer.append_initialize("  sprintf(samplestring,\"SiO2_quartza.laz\"); ")
    SimplePowderDIffractometer.append_initialize("} else if (sample==3) { ")
    SimplePowderDIffractometer.append_initialize("  sprintf(samplestring,\"C_diamond.laz\"); ")
    SimplePowderDIffractometer.append_initialize("} else { ")
    SimplePowderDIffractometer.append_initialize("  sprintf(samplestring,\"NULL\"); ")
    SimplePowderDIffractometer.append_initialize("} ")

    Origin = SimplePowderDIffractometer.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    source = SimplePowderDIffractometer.add_component("source", "Source_simple")
    source.radius = 0.1
    source.dist = "L1"
    source.focus_xw = "2*sample_radius+2*al_thickness"
    source.focus_yh = "sample_height+2*al_thickness"
    source.lambda0 = "lambda0"
    source.dlambda = "dlambda"
    source.flux = 5e10
    source.gauss = 1
    source.set_AT(['0', ' 0', ' 0'], RELATIVE="Origin")

    collimator = SimplePowderDIffractometer.add_component("collimator", "Collimator_linear")
    collimator.xwidth = 0.2
    collimator.yheight = 0.2
    collimator.length = 0.2
    collimator.divergence = "coll"
    collimator.set_AT(['0', ' 0', ' LC'], RELATIVE="source")

    entry_side = SimplePowderDIffractometer.add_component("entry_side", "PowderN")
    entry_side.reflections = "\"Al.laz\""
    entry_side.radius = "sample_radius+al_thickness"
    entry_side.yheight = "sample_height +2*al_thickness"
    entry_side.thickness = "al_thickness"
    entry_side.p_transmit = 0.8
    entry_side.d_phi = 2
    entry_side.concentric = 1
    entry_side.barns = 1
    entry_side.set_WHEN("container >0")
    entry_side.set_AT(['0', ' 0', ' L1'], RELATIVE="source")

    sample = SimplePowderDIffractometer.add_component("sample", "PowderN")
    sample.reflections = "samplestring"
    sample.radius = "sample_radius"
    sample.yheight = "sample_height"
    sample.pack = 1
    sample.sigma_abs = -1
    sample.sigma_inc = -1
    sample.delta_d_d = 0
    sample.p_inc = 0
    sample.p_transmit = 0.1
    sample.DW = 0
    sample.d_phi = 2
    sample.barns = 1
    sample.set_AT(['0', ' 0', ' L1'], RELATIVE="source")

    exit_side = SimplePowderDIffractometer.copy_component("exit_side", "entry_side")
    exit_side.reflections = "\"Al.laz\""
    exit_side.radius = "sample_radius+al_thickness"
    exit_side.yheight = "sample_height +2*al_thickness"
    exit_side.thickness = "al_thickness"
    exit_side.p_transmit = 0.8
    exit_side.d_phi = 2
    exit_side.concentric = 1
    exit_side.barns = 1
    exit_side.set_WHEN("container >0")
    exit_side.set_AT(['0', ' 0', ' L1'], RELATIVE="source")

    Detector = SimplePowderDIffractometer.add_component("Detector", "Monitor_nD")
    Detector.xwidth = "L1"
    Detector.yheight = 0.20
    Detector.bins = 400
    Detector.min = 20
    Detector.max = 100
    Detector.restore_neutron = 1
    Detector.options = "\"banana, theta\""
    Detector.filename = "\"detector.dat\""
    Detector.set_AT(['0', '0', '0'], RELATIVE="sample")
    Detector.set_ROTATED(['0', '0', '180'], RELATIVE="sample")

    return SimplePowderDIffractometer
