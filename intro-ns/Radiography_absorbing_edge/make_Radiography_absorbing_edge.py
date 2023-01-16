"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    Radiography_absorbing_edge = instr.McStas_instr("Radiography_absorbing_edge_generated")
    Radiography_absorbing_edge.add_parameter("double", "D", value=0.01)
    Radiography_absorbing_edge.add_parameter("double", "L", value=5.0)
    Radiography_absorbing_edge.add_parameter("double", "l", value=0.1)
    Radiography_absorbing_edge.add_parameter("double", "sigma_abs", value=5.08)
    Radiography_absorbing_edge.add_parameter("double", "Vc", value=13.827)
    Radiography_absorbing_edge.add_parameter("double", "sample_z", value=0.01)
    Radiography_absorbing_edge.add_declare_var("double", "L0", value=5.0)
    Radiography_absorbing_edge.add_declare_var("double", "sample_xoff")
    Radiography_absorbing_edge.add_declare_var("double", "det_w", value=0.1)
    Radiography_absorbing_edge.add_declare_var("double", "det_h", value=0.1)
    Radiography_absorbing_edge.add_declare_var("double", "sample_x", value=0.1)
    Radiography_absorbing_edge.add_declare_var("double", "sample_y", value=0.1)
    Radiography_absorbing_edge.add_declare_var("double", "sigma_inc", value=0.0001)
    Radiography_absorbing_edge.add_declare_var("double", "sqrt2", value=1.414214)
    Radiography_absorbing_edge.add_declare_var("double", "frac_interact", value=1e-06)
    Radiography_absorbing_edge.append_initialize("  ")
    Radiography_absorbing_edge.append_initialize("  sample_xoff  = sample_x/2*sqrt(2); /* Sample x offset */ ")
    Radiography_absorbing_edge.append_initialize("      ")

    Origin = Radiography_absorbing_edge.add_component("Origin", "Progress_bar")
    Origin.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    source = Radiography_absorbing_edge.add_component("source", "Source_gen")
    source.dist = "L0"
    source.focus_xw = "D"
    source.focus_yh = "D"
    source.lambda0 = 3
    source.dlambda = 1
    source.I1 = 1
    source.yheight = 0.1
    source.xwidth = 0.1
    source.target_index = 1
    source.set_AT(['0', ' 0', ' 0'], RELATIVE="Origin")

    pinhole = Radiography_absorbing_edge.add_component("pinhole", "Slit")
    pinhole.radius = "D/2"
    pinhole.set_AT(['0', ' 0', ' L0'], RELATIVE="source")

    samplearm = Radiography_absorbing_edge.add_component("samplearm", "Arm")
    samplearm.set_AT(['0', '0', 'L'], RELATIVE="pinhole")
    samplearm.set_ROTATED(['0', '0', '0'], RELATIVE="pinhole")

    edge_sample = Radiography_absorbing_edge.add_component("edge_sample", "Incoherent")
    edge_sample.xwidth = "sample_x"
    edge_sample.yheight = "sample_y"
    edge_sample.zdepth = "sample_z"
    edge_sample.target_x = "det_w"
    edge_sample.target_y = "det_h"
    edge_sample.target_index = 1
    edge_sample.p_interact = "frac_interact"
    edge_sample.sigma_abs = "sigma_abs"
    edge_sample.sigma_inc = "sigma_inc"
    edge_sample.Vc = "Vc"
    edge_sample.set_AT(['sample_x/2', ' 0', ' 0'], RELATIVE="samplearm")
    edge_sample.set_ROTATED(['0', ' 0', ' 0'], RELATIVE="samplearm")

    PSD_1cm_detector_50mum = Radiography_absorbing_edge.add_component("PSD_1cm_detector_50mum", "PSD_monitor")
    PSD_1cm_detector_50mum.nx = 200
    PSD_1cm_detector_50mum.ny = 200
    PSD_1cm_detector_50mum.filename = "\"PSD_1cm_detector_50mum\""
    PSD_1cm_detector_50mum.xwidth = 0.01
    PSD_1cm_detector_50mum.yheight = 0.01
    PSD_1cm_detector_50mum.restore_neutron = 1
    PSD_1cm_detector_50mum.set_AT(['0', ' 0', ' L+l'], RELATIVE="pinhole")

    edge_monitor_50mum = Radiography_absorbing_edge.add_component("edge_monitor_50mum", "PSDlin_diff_monitor")
    edge_monitor_50mum.nx = 200
    edge_monitor_50mum.filename = "\"edge_monitor_50mum\""
    edge_monitor_50mum.xwidth = 0.01
    edge_monitor_50mum.yheight = "det_h"
    edge_monitor_50mum.set_AT(['0', ' 0', ' L+l'], RELATIVE="pinhole")

    return Radiography_absorbing_edge
