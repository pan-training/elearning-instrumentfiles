"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    Sword_Odin = instr.McStas_instr("Sword_Odin_generated")
    Sword_Odin.add_parameter("double", "chopper_mode", value=5.0)
    Sword_Odin.add_parameter("double", "Lambda", value=0.0)
    Sword_Odin.add_parameter("double", "Sample", value=1.0)
    Sword_Odin.add_parameter("double", "pinhole_diameter", value=0.1)
    Sword_Odin.add_parameter("double", "pinhole_detector_distance", value=10.0)
    Sword_Odin.add_parameter("double", "pinhole_sample_distance", value=9.0)
    Sword_Odin.add_parameter("double", "X_sample_pos", value=0.0)
    Sword_Odin.add_parameter("double", "Y_sample_pos", value=0.0)
    Sword_Odin.add_parameter("double", "angle", value=0.0)
    Sword_Odin.add_parameter("double", "Zoom", value=1.0)
    Sword_Odin.add_declare_var("double", "sword_height")
    Sword_Odin.add_declare_var("double", "rust_thickness")
    Sword_Odin.add_declare_var("double", "blade_mask_radius")
    Sword_Odin.add_declare_var("double", "blade_tip_mask_radius")
    Sword_Odin.add_declare_var("double", "cut_radius")
    Sword_Odin.add_declare_var("double", "cut_depth")
    Sword_Odin.add_declare_var("double", "sword_depth")
    Sword_Odin.add_declare_var("double", "sword_width")
    Sword_Odin.add_declare_var("double", "blade_start_width")
    Sword_Odin.add_declare_var("double", "blade_top_width")
    Sword_Odin.add_declare_var("double", "blade_tip_start_width")
    Sword_Odin.add_declare_var("double", "core_width_top")
    Sword_Odin.add_declare_var("double", "core_side_top_length")
    Sword_Odin.add_declare_var("double", "core_width_bottom")
    Sword_Odin.add_declare_var("double", "core_side_bottom_length")
    Sword_Odin.add_declare_var("double", "width_angle")
    Sword_Odin.add_declare_var("double", "cut_angle")
    Sword_Odin.add_declare_var("double", "radius_multiply")
    Sword_Odin.add_declare_var("double", "tip_x_multiplier")
    Sword_Odin.add_declare_var("double", "tip_height")
    Sword_Odin.add_declare_var("double", "blade_angle_deg")
    Sword_Odin.add_declare_var("double", "blade_angle_tip_deg")
    Sword_Odin.add_declare_var("char", "rust_string", array=128)
    Sword_Odin.add_declare_var("char", "spacial_resolution", array=128)
    Sword_Odin.add_declare_var("char", "wavelength_spectrum", array=128)
    Sword_Odin.add_declare_var("int", "rust_used")
    Sword_Odin.add_declare_var("double", "Fe3O4_content")
    Sword_Odin.add_declare_var("double", "Fe2O3_content")
    Sword_Odin.add_declare_var("double", "FeOOH_content")
    Sword_Odin.add_declare_var("double", "mixture")
    Sword_Odin.add_declare_var("double", "Dlambda")
    Sword_Odin.add_declare_var("double", "L_min")
    Sword_Odin.add_declare_var("double", "L_max")
    Sword_Odin.append_initialize("rust_used=1; ")
    Sword_Odin.append_initialize("Fe3O4_content = 0.34; ")
    Sword_Odin.append_initialize("Fe2O3_content = 0.33; ")
    Sword_Odin.append_initialize("FeOOH_content = 0.33; ")
    Sword_Odin.append_initialize("mixture=0.1; ")
    Sword_Odin.append_initialize("sword_width = 0.06; ")
    Sword_Odin.append_initialize("blade_start_width = 0.032; ")
    Sword_Odin.append_initialize("sword_depth = 0.015/2.0; ")
    Sword_Odin.append_initialize("sword_height = 0.6; ")
    Sword_Odin.append_initialize("rust_thickness = 0.002; ")
    Sword_Odin.append_initialize("blade_mask_radius = 0.07; ")
    Sword_Odin.append_initialize("cut_depth = 0.002/1.5; ")
    Sword_Odin.append_initialize("cut_radius = (0.5*blade_start_width*0.5*blade_start_width+cut_depth*cut_depth)/2.0/cut_depth; ")
    Sword_Odin.append_initialize("core_width_top = 0.032; ")
    Sword_Odin.append_initialize("core_side_top_length = core_width_top/sqrt(2); ")
    Sword_Odin.append_initialize("core_width_bottom = 0.0404; ")
    Sword_Odin.append_initialize("width_angle = 1.0/8.0; ")
    Sword_Odin.append_initialize("cut_angle = 1.0/6.0; ")
    Sword_Odin.append_initialize("blade_tip_start_width = -0.0; ")
    Sword_Odin.append_initialize("blade_tip_mask_radius = 0.07; ")
    Sword_Odin.append_initialize("core_side_bottom_length = core_width_bottom/sqrt(2); ")
    Sword_Odin.append_initialize("tip_height = 0.21; ")
    Sword_Odin.append_initialize("tip_x_multiplier = -0.5; ")
    Sword_Odin.append_initialize("radius_multiply = 1.0; ")
    Sword_Odin.append_initialize("blade_angle_deg = 180/3.14159*atan((core_width_bottom-core_width_top)/sword_height); ")
    Sword_Odin.append_initialize("blade_angle_tip_deg = 180/3.14159*atan((0.8*core_width_top)/tip_height); ")
    Sword_Odin.append_initialize("blade_top_width = blade_start_width - 2.0*(core_width_bottom-core_width_top); ")
    Sword_Odin.append_initialize("if (rust_used == 0){sprintf(rust_string, \"Fe3O4\");} ")
    Sword_Odin.append_initialize("if (rust_used == 1){sprintf(rust_string, \"Fe2O3\");} ")
    Sword_Odin.append_initialize("if (rust_used == 2){sprintf(rust_string, \"FeOOH\");} ")
    Sword_Odin.append_initialize("if (rust_used == 3){sprintf(rust_string, \"iron_mix\");} ")
    Sword_Odin.append_initialize("if (rust_used == 4){sprintf(rust_string, \"Fe_alpha\");} ")
    Sword_Odin.append_initialize("if (rust_used == 5){sprintf(rust_string, \"rust_mix\");} ")
    Sword_Odin.append_initialize("if (chopper_mode == 0){sprintf(wavelength_spectrum, \"Filters/I_lambda_C0.dat\"); Dlambda = 0.1;} ")
    Sword_Odin.append_initialize("if (chopper_mode == 1){sprintf(wavelength_spectrum, \"Filters/I_lambda_C1.dat\"); Dlambda = 0.05;} ")
    Sword_Odin.append_initialize("if (chopper_mode == 2){sprintf(wavelength_spectrum, \"Filters/I_lambda_C2.dat\"); Dlambda = 0.04;} ")
    Sword_Odin.append_initialize("if (chopper_mode == 3){sprintf(wavelength_spectrum, \"Filters/I_lambda_C3.dat\"); Dlambda = 0.03;} ")
    Sword_Odin.append_initialize("if (chopper_mode == 4){sprintf(wavelength_spectrum, \"Filters/I_lambda_C4.dat\"); Dlambda = 0.02;} ")
    Sword_Odin.append_initialize("if (chopper_mode == 5){sprintf(wavelength_spectrum, \"Filters/I_lambda_C5.dat\"); Dlambda = 0.25;} ")
    Sword_Odin.append_initialize("if (Lambda < 1.0){Lambda=0;} ")
    Sword_Odin.append_initialize("if (Lambda > 10.0){Lambda=0;} ")
    Sword_Odin.append_initialize("if (Lambda == 0){ ")
    Sword_Odin.append_initialize("L_min = 0.0; ")
    Sword_Odin.append_initialize("L_max = 10.0; ")
    Sword_Odin.append_initialize("} ")
    Sword_Odin.append_initialize("else{ ")
    Sword_Odin.append_initialize("L_min = Lambda-0.1; ")
    Sword_Odin.append_initialize("L_max = Lambda+0.1; ")
    Sword_Odin.append_initialize("} ")
    Sword_Odin.append_initialize("if (chopper_mode == 5){ ")
    Sword_Odin.append_initialize("L_min = 0.0; ")
    Sword_Odin.append_initialize("L_max = 10.0; ")
    Sword_Odin.append_initialize("} ")
    Sword_Odin.append_initialize("if (chopper_mode < 0){chopper_mode=5;} ")
    Sword_Odin.append_initialize("if (chopper_mode > 5){chopper_mode=5;} ")
    Sword_Odin.append_initialize("if (pinhole_detector_distance < 10){pinhole_detector_distance=10;} ")
    Sword_Odin.append_initialize("if (pinhole_detector_distance > 25){pinhole_detector_distance=25;} ")
    Sword_Odin.append_initialize("if (pinhole_sample_distance < 1){pinhole_sample_distance=1;} ")
    Sword_Odin.append_initialize("if (pinhole_sample_distance > 25){pinhole_sample_distance=25;} ")
    Sword_Odin.append_initialize("if (pinhole_diameter < 0.01){pinhole_diameter=0.01;} ")
    Sword_Odin.append_initialize("if (pinhole_diameter > 0.1){pinhole_diameter=0.1;} ")
    Sword_Odin.append_initialize("if (Sample < 0){Sample=0;} ")
    Sword_Odin.append_initialize("if (Sample > 1){Sample=0;} ")
    Sword_Odin.append_initialize("if (Zoom < 1){Zoom=1;} ")
    Sword_Odin.append_initialize("if (Zoom > 10){Zoom=10;} ")
    Sword_Odin.append_initialize("sprintf(spacial_resolution, \"Filters/2D_Filter_n600_25m.dat\"); ")

    a1 = Sword_Odin.add_component("a1", "Progress_bar")
    a1.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    source_gen = Sword_Odin.add_component("source_gen", "Source_gen")
    source_gen.flux_file = "wavelength_spectrum"
    source_gen.radius = "pinhole_diameter"
    source_gen.dist = "pinhole_detector_distance+0.01"
    source_gen.focus_xw = "0.3/Zoom"
    source_gen.focus_yh = "0.3/Zoom"
    source_gen.verbose = 1
    source_gen.Lmin = "L_min"
    source_gen.Lmax = "L_max"
    source_gen.set_AT(['0', ' 0', ' 0'], RELATIVE="a1")

    graph = Sword_Odin.add_component("graph", "Arm")
    graph.set_AT(['0', '0', '0.002'], RELATIVE="a1")
    graph.set_ROTATED(['0', '0', '0'], RELATIVE="a1")

    Lamb_Dif = Sword_Odin.add_component("Lamb_Dif", "Wavelength_Diffuser")
    Lamb_Dif.dlambda = "Dlambda"
    Lamb_Dif.set_AT(['0', '0', '0.003'], RELATIVE="a1")

    init = Sword_Odin.add_component("init", "Union_init")
    init.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Al_incoherent = Sword_Odin.add_component("Al_incoherent", "Incoherent_process")
    Al_incoherent.sigma = "4*0.0082"
    Al_incoherent.packing_factor = 1
    Al_incoherent.unit_cell_volume = 66.4
    Al_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Al_powder = Sword_Odin.add_component("Al_powder", "Powder_process")
    Al_powder.reflections = "\"Al.laz\""
    Al_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Al = Sword_Odin.add_component("Al", "Union_make_material")
    Al.process_string = "\"Al_incoherent,Al_powder\""
    Al.my_absorption = "100*4*0.231/66.4"
    Al.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe_incoherent = Sword_Odin.add_component("Fe_incoherent", "Incoherent_process")
    Fe_incoherent.sigma = "2*0.4"
    Fe_incoherent.packing_factor = 1
    Fe_incoherent.unit_cell_volume = 24.04
    Fe_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe_powder = Sword_Odin.add_component("Fe_powder", "Powder_process")
    Fe_powder.reflections = "\"Fe.laz\""
    Fe_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe = Sword_Odin.add_component("Fe", "Union_make_material")
    Fe.my_absorption = "100*2*2.56/24.04"
    Fe.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe_alpha_incoherent = Sword_Odin.add_component("Fe_alpha_incoherent", "Incoherent_process")
    Fe_alpha_incoherent.sigma = 0.80000
    Fe_alpha_incoherent.packing_factor = 1
    Fe_alpha_incoherent.unit_cell_volume = 23.55352
    Fe_alpha_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe_alpha_powder = Sword_Odin.add_component("Fe_alpha_powder", "Powder_process")
    Fe_alpha_powder.reflections = "\"alpha_Fe.laz\""
    Fe_alpha_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe_alpha = Sword_Odin.add_component("Fe_alpha", "Union_make_material")
    Fe_alpha.my_absorption = "100*5.12000/23.55352"
    Fe_alpha.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    cementite_incoherent = Sword_Odin.add_component("cementite_incoherent", "Incoherent_process")
    cementite_incoherent.sigma = 4.80398
    cementite_incoherent.packing_factor = 1
    cementite_incoherent.unit_cell_volume = 155.15118
    cementite_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    cementite_powder = Sword_Odin.add_component("cementite_powder", "Powder_process")
    cementite_powder.reflections = "\"cementite_300K.laz\""
    cementite_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    cementite = Sword_Odin.add_component("cementite", "Union_make_material")
    cementite.my_absorption = "100*30.73400/155.15118"
    cementite.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    mix_Fe_alpha_incoherent = Sword_Odin.add_component("mix_Fe_alpha_incoherent", "Incoherent_process")
    mix_Fe_alpha_incoherent.sigma = 0.80000
    mix_Fe_alpha_incoherent.packing_factor = "1.0-mixture"
    mix_Fe_alpha_incoherent.unit_cell_volume = 23.55352
    mix_Fe_alpha_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    mix_cementite_incoherent = Sword_Odin.add_component("mix_cementite_incoherent", "Incoherent_process")
    mix_cementite_incoherent.sigma = 4.80398
    mix_cementite_incoherent.packing_factor = "mixture"
    mix_cementite_incoherent.unit_cell_volume = 155.15118
    mix_cementite_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    mix_Fe_alpha_powder = Sword_Odin.add_component("mix_Fe_alpha_powder", "Powder_process")
    mix_Fe_alpha_powder.reflections = "\"alpha_Fe.laz\""
    mix_Fe_alpha_powder.packing_factor = "1.0-mixture"
    mix_Fe_alpha_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    mix_cementite_powder = Sword_Odin.add_component("mix_cementite_powder", "Powder_process")
    mix_cementite_powder.reflections = "\"cementite_300K.laz\""
    mix_cementite_powder.packing_factor = "mixture"
    mix_cementite_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    iron_mix = Sword_Odin.add_component("iron_mix", "Union_make_material")
    iron_mix.my_absorption = "mixture*100*30.73400/155.15118+(1.0-mixture)*100*5.12000/23.55352"
    iron_mix.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_incoherent = Sword_Odin.add_component("Fe3O4_incoherent", "Incoherent_process")
    Fe3O4_incoherent.sigma = 2.40639
    Fe3O4_incoherent.packing_factor = 1
    Fe3O4_incoherent.unit_cell_volume = 157.15089
    Fe3O4_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_powder = Sword_Odin.add_component("Fe3O4_powder", "Powder_process")
    Fe3O4_powder.reflections = "\"Fe3O4_mp-19306_computed.laz\""
    Fe3O4_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4 = Sword_Odin.add_component("Fe3O4", "Union_make_material")
    Fe3O4.process_string = "\"Fe3O4_incoherent,Fe3O4_powder\""
    Fe3O4.my_absorption = "100*15.36152/157.15089"
    Fe3O4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_incoherent = Sword_Odin.add_component("Fe2O3_incoherent", "Incoherent_process")
    Fe2O3_incoherent.sigma = 4.81438
    Fe2O3_incoherent.packing_factor = 1
    Fe2O3_incoherent.unit_cell_volume = 302.72198
    Fe2O3_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_powder = Sword_Odin.add_component("Fe2O3_powder", "Powder_process")
    Fe2O3_powder.reflections = "\"Fe2O3.laz\""
    Fe2O3_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3 = Sword_Odin.add_component("Fe2O3", "Union_make_material")
    Fe2O3.process_string = "\"Fe2O3_incoherent,Fe2O3_powder\""
    Fe2O3.my_absorption = "100*30.72342/302.72198"
    Fe2O3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_incoherent = Sword_Odin.add_component("FeOOH_incoherent", "Incoherent_process")
    FeOOH_incoherent.sigma = 322.63895
    FeOOH_incoherent.packing_factor = 1
    FeOOH_incoherent.unit_cell_volume = 302.72198
    FeOOH_incoherent.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_powder = Sword_Odin.add_component("FeOOH_powder", "Powder_process")
    FeOOH_powder.reflections = "\"FeOOH.laz\""
    FeOOH_powder.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH = Sword_Odin.add_component("FeOOH", "Union_make_material")
    FeOOH.process_string = "\"FeOOH_incoherent,FeOOH_powder\""
    FeOOH.my_absorption = "100*11.57192/302.72198"
    FeOOH.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_incoherent2 = Sword_Odin.add_component("Fe3O4_incoherent2", "Incoherent_process")
    Fe3O4_incoherent2.sigma = 2.40639
    Fe3O4_incoherent2.packing_factor = "Fe3O4_content"
    Fe3O4_incoherent2.unit_cell_volume = 157.15089
    Fe3O4_incoherent2.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_powder2 = Sword_Odin.add_component("Fe3O4_powder2", "Powder_process")
    Fe3O4_powder2.reflections = "\"Fe3O4_mp-19306_computed.laz\""
    Fe3O4_powder2.packing_factor = "Fe3O4_content"
    Fe3O4_powder2.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_incoherent2 = Sword_Odin.add_component("Fe2O3_incoherent2", "Incoherent_process")
    Fe2O3_incoherent2.sigma = 4.81438
    Fe2O3_incoherent2.packing_factor = "Fe2O3_content"
    Fe2O3_incoherent2.unit_cell_volume = 302.72198
    Fe2O3_incoherent2.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_powder2 = Sword_Odin.add_component("Fe2O3_powder2", "Powder_process")
    Fe2O3_powder2.reflections = "\"Fe2O3.laz\""
    Fe2O3_powder2.packing_factor = "Fe2O3_content"
    Fe2O3_powder2.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_incoherent2 = Sword_Odin.add_component("FeOOH_incoherent2", "Incoherent_process")
    FeOOH_incoherent2.sigma = 322.63895
    FeOOH_incoherent2.packing_factor = "FeOOH_content"
    FeOOH_incoherent2.unit_cell_volume = 302.72198
    FeOOH_incoherent2.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_powder2 = Sword_Odin.add_component("FeOOH_powder2", "Powder_process")
    FeOOH_powder2.reflections = "\"FeOOH.laz\""
    FeOOH_powder2.packing_factor = "FeOOH_content"
    FeOOH_powder2.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    rust_mix = Sword_Odin.add_component("rust_mix", "Union_make_material")
    rust_mix.process_string = "\"Fe3O4_incoherent2,Fe3O4_powder2,Fe2O3_incoherent2,Fe2O3_powder2,FeOOH_incoherent2,FeOOH_powder2\""
    rust_mix.my_absorption = "Fe3O4_content*100*15.36152/157.15089 + Fe2O3_content*100*30.72342/302.72198 + FeOOH_content*100*11.57192/302.72198"
    rust_mix.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_incoherent3 = Sword_Odin.add_component("Fe3O4_incoherent3", "Incoherent_process")
    Fe3O4_incoherent3.sigma = 2.40639
    Fe3O4_incoherent3.packing_factor = 0.25
    Fe3O4_incoherent3.unit_cell_volume = 157.15089
    Fe3O4_incoherent3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_powder3 = Sword_Odin.add_component("Fe3O4_powder3", "Powder_process")
    Fe3O4_powder3.reflections = "\"Fe3O4_mp-19306_computed.laz\""
    Fe3O4_powder3.packing_factor = 0.25
    Fe3O4_powder3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_incoherent3 = Sword_Odin.add_component("Fe2O3_incoherent3", "Incoherent_process")
    Fe2O3_incoherent3.sigma = 4.81438
    Fe2O3_incoherent3.packing_factor = 0.25
    Fe2O3_incoherent3.unit_cell_volume = 302.72198
    Fe2O3_incoherent3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_powder3 = Sword_Odin.add_component("Fe2O3_powder3", "Powder_process")
    Fe2O3_powder3.reflections = "\"Fe2O3.laz\""
    Fe2O3_powder3.packing_factor = 0.25
    Fe2O3_powder3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_incoherent3 = Sword_Odin.add_component("FeOOH_incoherent3", "Incoherent_process")
    FeOOH_incoherent3.sigma = 322.63895
    FeOOH_incoherent3.packing_factor = 0.5
    FeOOH_incoherent3.unit_cell_volume = 302.72198
    FeOOH_incoherent3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_powder3 = Sword_Odin.add_component("FeOOH_powder3", "Powder_process")
    FeOOH_powder3.reflections = "\"FeOOH.laz\""
    FeOOH_powder3.packing_factor = 0.5
    FeOOH_powder3.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    rust_mix_FeOOH_High = Sword_Odin.add_component("rust_mix_FeOOH_High", "Union_make_material")
    rust_mix_FeOOH_High.process_string = "\"Fe3O4_incoherent2,Fe3O4_powder2,Fe2O3_incoherent2,Fe2O3_powder2,FeOOH_incoherent2,FeOOH_powder2\""
    rust_mix_FeOOH_High.my_absorption = "0.25*100*15.36152/157.15089 + 0.25*100*30.72342/302.72198 + 0.5*100*11.57192/302.72198"
    rust_mix_FeOOH_High.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_incoherent4 = Sword_Odin.add_component("Fe3O4_incoherent4", "Incoherent_process")
    Fe3O4_incoherent4.sigma = 2.40639
    Fe3O4_incoherent4.packing_factor = 0.5
    Fe3O4_incoherent4.unit_cell_volume = 157.15089
    Fe3O4_incoherent4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe3O4_powder4 = Sword_Odin.add_component("Fe3O4_powder4", "Powder_process")
    Fe3O4_powder4.reflections = "\"Fe3O4_mp-19306_computed.laz\""
    Fe3O4_powder4.packing_factor = 0.25
    Fe3O4_powder4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_incoherent4 = Sword_Odin.add_component("Fe2O3_incoherent4", "Incoherent_process")
    Fe2O3_incoherent4.sigma = 4.81438
    Fe2O3_incoherent4.packing_factor = 0.25
    Fe2O3_incoherent4.unit_cell_volume = 302.72198
    Fe2O3_incoherent4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Fe2O3_powder4 = Sword_Odin.add_component("Fe2O3_powder4", "Powder_process")
    Fe2O3_powder4.reflections = "\"Fe2O3.laz\""
    Fe2O3_powder4.packing_factor = 0.25
    Fe2O3_powder4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_incoherent4 = Sword_Odin.add_component("FeOOH_incoherent4", "Incoherent_process")
    FeOOH_incoherent4.sigma = 322.63895
    FeOOH_incoherent4.packing_factor = 0.25
    FeOOH_incoherent4.unit_cell_volume = 302.72198
    FeOOH_incoherent4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    FeOOH_powder4 = Sword_Odin.add_component("FeOOH_powder4", "Powder_process")
    FeOOH_powder4.reflections = "\"FeOOH.laz\""
    FeOOH_powder4.packing_factor = 0.5
    FeOOH_powder4.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    rust_mix_Fe3O4_High = Sword_Odin.add_component("rust_mix_Fe3O4_High", "Union_make_material")
    rust_mix_Fe3O4_High.process_string = "\"Fe3O4_incoherent2,Fe3O4_powder2,Fe2O3_incoherent2,Fe2O3_powder2,FeOOH_incoherent2,FeOOH_powder2\""
    rust_mix_Fe3O4_High.my_absorption = "0.5*100*15.36152/157.15089 + 0.25*100*30.72342/302.72198 + 0.25*100*11.57192/302.72198"
    rust_mix_Fe3O4_High.set_AT(['0', '0', '0'], RELATIVE="ABSOLUTE")

    Turn_table_center = Sword_Odin.add_component("Turn_table_center", "Arm")
    Turn_table_center.set_AT(['X_sample_pos', 'Y_sample_pos', 'pinhole_sample_distance'], RELATIVE="graph")
    Turn_table_center.set_ROTATED(['0', 'angle', '0'], RELATIVE="graph")

    object_center = Sword_Odin.add_component("object_center", "Arm")
    object_center.set_AT(['0', '0', '0'], RELATIVE="Turn_table_center")
    object_center.set_ROTATED(['0', '0', '0'], RELATIVE="Turn_table_center")

    blade_rust_side_1 = Sword_Odin.add_component("blade_rust_side_1", "Union_sphere")
    blade_rust_side_1.material_string = "\"FeOOH\""
    blade_rust_side_1.priority = 100
    blade_rust_side_1.radius = 0.1
    blade_rust_side_1.set_AT(['sword_width+0.065', '-0.065', '0'], RELATIVE="object_center")
    blade_rust_side_1.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    blade_rust_side_2 = Sword_Odin.add_component("blade_rust_side_2", "Union_sphere")
    blade_rust_side_2.material_string = "\"FeOOH\""
    blade_rust_side_2.priority = 99
    blade_rust_side_2.radius = 0.10001
    blade_rust_side_2.set_AT(['sword_width+0.068', '0.065001', '0'], RELATIVE="object_center")
    blade_rust_side_2.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    blade_rust_side_3 = Sword_Odin.add_component("blade_rust_side_3", "Union_sphere")
    blade_rust_side_3.material_string = "\"FeOOH\""
    blade_rust_side_3.priority = 98
    blade_rust_side_3.radius = 0.10002
    blade_rust_side_3.set_AT(['sword_width+0.06', '0.0', '0'], RELATIVE="object_center")
    blade_rust_side_3.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    blade_iron_side_1 = Sword_Odin.add_component("blade_iron_side_1", "Union_box")
    blade_iron_side_1.material_string = "\"iron_mix\""
    blade_iron_side_1.priority = 90
    blade_iron_side_1.xwidth = 0.12002
    blade_iron_side_1.yheight = "sword_height+0.0002"
    blade_iron_side_1.zdepth = "sword_depth*2.0+0.0002"
    blade_iron_side_1.set_AT(['0.062', '0', '0'], RELATIVE="object_center")

    blade_mask_1 = Sword_Odin.add_component("blade_mask_1", "Union_cylinder")
    blade_mask_1.priority = 0
    blade_mask_1.radius = "radius_multiply*blade_mask_radius"
    blade_mask_1.yheight = "sword_height+0.10001"
    blade_mask_1.mask_string = "\"blade_rust_side_1,blade_rust_side_2,blade_rust_side_3,blade_iron_side_1\""
    blade_mask_1.mask_setting = "\"All\""
    blade_mask_1.set_AT(['blade_start_width*0.5', '0', 'blade_mask_radius-sword_depth*0.5'], RELATIVE="object_center")
    blade_mask_1.set_ROTATED(['width_angle', '0', 'blade_angle_deg'], RELATIVE="object_center")

    blade_mask_2 = Sword_Odin.add_component("blade_mask_2", "Union_cylinder")
    blade_mask_2.priority = 0
    blade_mask_2.radius = "radius_multiply*blade_mask_radius"
    blade_mask_2.yheight = "sword_height+0.10002"
    blade_mask_2.mask_string = "\"blade_rust_side_1,blade_rust_side_2,blade_rust_side_3,blade_iron_side_1\""
    blade_mask_2.mask_setting = "\"All\""
    blade_mask_2.set_AT(['blade_start_width*0.5', '0', '-blade_mask_radius+sword_depth*0.5'], RELATIVE="object_center")
    blade_mask_2.set_ROTATED(['-width_angle', '0', 'blade_angle_deg'], RELATIVE="object_center")

    blade_mask_25 = Sword_Odin.add_component("blade_mask_25", "Union_box")
    blade_mask_25.priority = 0
    blade_mask_25.xwidth = 0.6
    blade_mask_25.yheight = "sword_height+0.0001"
    blade_mask_25.zdepth = "sword_depth*3.0+0.0001"
    blade_mask_25.mask_string = "\"blade_rust_side_1,blade_rust_side_2,blade_rust_side_3,blade_iron_side_1\""
    blade_mask_25.mask_setting = "\"All\""
    blade_mask_25.set_AT(['blade_start_width', '0', '0'], RELATIVE="object_center")
    blade_mask_25.set_ROTATED(['width_angle', '0', 'blade_angle_deg'], RELATIVE="object_center")

    blade_rust_iron_core_side_1 = Sword_Odin.add_component("blade_rust_iron_core_side_1", "Union_box")
    blade_rust_iron_core_side_1.material_string = "\"iron_mix\""
    blade_rust_iron_core_side_1.priority = 200
    blade_rust_iron_core_side_1.xwidth = 0.12001
    blade_rust_iron_core_side_1.yheight = "sword_height+0.0001"
    blade_rust_iron_core_side_1.zdepth = "sword_depth*2.0+0.0001"
    blade_rust_iron_core_side_1.set_AT(['0.062', '0', '0'], RELATIVE="object_center")

    rust_mask_1 = Sword_Odin.add_component("rust_mask_1", "Union_cylinder")
    rust_mask_1.priority = 0
    rust_mask_1.radius = "blade_mask_radius*0.98"
    rust_mask_1.yheight = "0.5*sword_height+0.10001"
    rust_mask_1.mask_string = "\"blade_rust_iron_core_side_1\""
    rust_mask_1.mask_setting = "\"All\""
    rust_mask_1.set_AT(['blade_start_width*0.5', '0', 'blade_mask_radius-sword_depth*0.5'], RELATIVE="object_center")
    rust_mask_1.set_ROTATED(['width_angle', '0', 'blade_angle_deg'], RELATIVE="object_center")

    rust_mask_2 = Sword_Odin.add_component("rust_mask_2", "Union_cylinder")
    rust_mask_2.priority = 0
    rust_mask_2.radius = "blade_mask_radius*0.98"
    rust_mask_2.yheight = "0.5*sword_height+0.10002"
    rust_mask_2.mask_string = "\"blade_rust_iron_core_side_1\""
    rust_mask_2.mask_setting = "\"All\""
    rust_mask_2.set_AT(['blade_start_width*0.5', '0', '-blade_mask_radius+sword_depth*0.5'], RELATIVE="object_center")
    rust_mask_2.set_ROTATED(['-width_angle', '0', 'blade_angle_deg'], RELATIVE="object_center")

    blade_iron_side_2 = Sword_Odin.add_component("blade_iron_side_2", "Union_box")
    blade_iron_side_2.material_string = "\"iron_mix\""
    blade_iron_side_2.priority = 101
    blade_iron_side_2.xwidth = 0.12
    blade_iron_side_2.yheight = "sword_height"
    blade_iron_side_2.zdepth = "sword_depth*2.0"
    blade_iron_side_2.set_AT(['-0.061', '0', '0'], RELATIVE="object_center")

    blade_mask_3 = Sword_Odin.add_component("blade_mask_3", "Union_cylinder")
    blade_mask_3.priority = 0
    blade_mask_3.radius = "radius_multiply*blade_mask_radius"
    blade_mask_3.yheight = "sword_height+0.10003"
    blade_mask_3.mask_string = "\"blade_iron_side_2\""
    blade_mask_3.mask_setting = "\"All\""
    blade_mask_3.set_AT(['-blade_start_width*0.5', '0', 'blade_mask_radius-sword_depth*0.5'], RELATIVE="object_center")
    blade_mask_3.set_ROTATED(['width_angle', '0', '-blade_angle_deg'], RELATIVE="object_center")

    blade_mask_4 = Sword_Odin.add_component("blade_mask_4", "Union_cylinder")
    blade_mask_4.priority = 0
    blade_mask_4.radius = "radius_multiply*blade_mask_radius"
    blade_mask_4.yheight = "sword_height+0.10004"
    blade_mask_4.mask_string = "\"blade_iron_side_2\""
    blade_mask_4.mask_setting = "\"All\""
    blade_mask_4.set_AT(['-blade_start_width*0.5', '0', '-blade_mask_radius+sword_depth*0.5'], RELATIVE="object_center")
    blade_mask_4.set_ROTATED(['-width_angle', '0', '-blade_angle_deg'], RELATIVE="object_center")

    rust_core = Sword_Odin.add_component("rust_core", "Union_box")
    rust_core.material_string = "rust_string"
    rust_core.priority = 202
    rust_core.xwidth = "core_side_bottom_length"
    rust_core.yheight = "core_side_bottom_length"
    rust_core.zdepth = "sword_height-0.0001"
    rust_core.xwidth2 = "core_side_top_length"
    rust_core.yheight2 = "core_side_top_length"
    rust_core.set_AT(['0', '0', '0'], RELATIVE="object_center")
    rust_core.set_ROTATED(['-90', '0', '45'], RELATIVE="object_center")

    hard_core = Sword_Odin.add_component("hard_core", "Union_box")
    hard_core.material_string = "\"iron_mix\""
    hard_core.priority = 203
    hard_core.xwidth = "core_side_bottom_length-rust_thickness*2.0"
    hard_core.yheight = "core_side_bottom_length-rust_thickness*2.0"
    hard_core.zdepth = "sword_height-0.0002"
    hard_core.xwidth2 = "core_side_top_length-rust_thickness*2.0"
    hard_core.yheight2 = "core_side_top_length-rust_thickness*2.0"
    hard_core.set_AT(['0', '0', '0'], RELATIVE="object_center")
    hard_core.set_ROTATED(['-90', '0', '45'], RELATIVE="object_center")

    side_cut_1 = Sword_Odin.add_component("side_cut_1", "Union_cylinder")
    side_cut_1.material_string = "\"Vacuum\""
    side_cut_1.priority = 1000
    side_cut_1.radius = "cut_radius"
    side_cut_1.yheight = "sword_height+2*tip_height+0.2"
    side_cut_1.set_AT(['0', '0', 'cut_radius+sword_depth*0.5-cut_depth+0.0001'], RELATIVE="object_center")
    side_cut_1.set_ROTATED(['-cut_angle+0.00001', '0', '0'], RELATIVE="object_center")

    side_cut_2 = Sword_Odin.add_component("side_cut_2", "Union_cylinder")
    side_cut_2.material_string = "\"Vacuum\""
    side_cut_2.priority = 1001
    side_cut_2.radius = "cut_radius"
    side_cut_2.yheight = "sword_height+2*tip_height+0.1"
    side_cut_2.set_AT(['0', '0', '-cut_radius-sword_depth*0.5+cut_depth+0.0001'], RELATIVE="object_center")
    side_cut_2.set_ROTATED(['cut_angle+0.00002', '0', '0'], RELATIVE="object_center")

    blade_iron_side_tip_1 = Sword_Odin.add_component("blade_iron_side_tip_1", "Union_box")
    blade_iron_side_tip_1.material_string = "\"iron_mix\""
    blade_iron_side_tip_1.priority = 300
    blade_iron_side_tip_1.xwidth = "0.12-0.0002"
    blade_iron_side_tip_1.yheight = "tip_height"
    blade_iron_side_tip_1.zdepth = "sword_depth*2.0-0.001"
    blade_iron_side_tip_1.set_AT(['0.06', 'sword_height*0.5+tip_height*0.5-0.0001', '0'], RELATIVE="object_center")

    blade_mask_tip_1 = Sword_Odin.add_component("blade_mask_tip_1", "Union_cylinder")
    blade_mask_tip_1.priority = 0
    blade_mask_tip_1.radius = "blade_tip_mask_radius"
    blade_mask_tip_1.yheight = "tip_height+0.10001"
    blade_mask_tip_1.mask_string = "\"blade_iron_side_tip_1\""
    blade_mask_tip_1.mask_setting = "\"All\""
    blade_mask_tip_1.set_AT(['blade_top_width*0.5*tip_x_multiplier', 'sword_height*0.5+tip_height*0.5-0.0001', 'blade_tip_mask_radius-sword_depth*0.5*0.8'], RELATIVE="object_center")
    blade_mask_tip_1.set_ROTATED(['2.5*width_angle', '0', 'blade_angle_tip_deg'], RELATIVE="object_center")

    blade_mask_tip_2 = Sword_Odin.add_component("blade_mask_tip_2", "Union_cylinder")
    blade_mask_tip_2.priority = 0
    blade_mask_tip_2.radius = "blade_tip_mask_radius"
    blade_mask_tip_2.yheight = "tip_height+0.10002"
    blade_mask_tip_2.mask_string = "\"blade_iron_side_tip_1\""
    blade_mask_tip_2.mask_setting = "\"All\""
    blade_mask_tip_2.set_AT(['blade_top_width*0.5*tip_x_multiplier', 'sword_height*0.5+tip_height*0.5-0.0001', '-blade_tip_mask_radius+sword_depth*0.5*0.8'], RELATIVE="object_center")
    blade_mask_tip_2.set_ROTATED(['-2.5*width_angle', '0', 'blade_angle_tip_deg'], RELATIVE="object_center")

    blade_rust_side_tip_2 = Sword_Odin.add_component("blade_rust_side_tip_2", "Union_sphere")
    blade_rust_side_tip_2.material_string = "\"Fe2O3\""
    blade_rust_side_tip_2.priority = 291
    blade_rust_side_tip_2.radius = 0.044
    blade_rust_side_tip_2.set_AT(['-0.88*sword_width', '0.5*sword_height+0.5*tip_height', '0'], RELATIVE="object_center")
    blade_rust_side_tip_2.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    blade_rust_side_tip_3 = Sword_Odin.add_component("blade_rust_side_tip_3", "Union_sphere")
    blade_rust_side_tip_3.material_string = "\"Fe2O3\""
    blade_rust_side_tip_3.priority = 292
    blade_rust_side_tip_3.radius = 0.044
    blade_rust_side_tip_3.set_AT(['-0.83*sword_width', '0.55*sword_height+0.5*tip_height', '0'], RELATIVE="object_center")
    blade_rust_side_tip_3.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    blade_rust_side_tip_4 = Sword_Odin.add_component("blade_rust_side_tip_4", "Union_sphere")
    blade_rust_side_tip_4.material_string = "\"Fe2O3\""
    blade_rust_side_tip_4.priority = 293
    blade_rust_side_tip_4.radius = 0.045
    blade_rust_side_tip_4.set_AT(['-0.96*sword_width', '0.45*sword_height+0.5*tip_height', '0'], RELATIVE="object_center")
    blade_rust_side_tip_4.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    blade_iron_side_tip_2 = Sword_Odin.add_component("blade_iron_side_tip_2", "Union_box")
    blade_iron_side_tip_2.material_string = "\"iron_mix\""
    blade_iron_side_tip_2.priority = 290
    blade_iron_side_tip_2.xwidth = "0.12-0.0002"
    blade_iron_side_tip_2.yheight = "tip_height"
    blade_iron_side_tip_2.zdepth = "sword_depth*2.0-0.001"
    blade_iron_side_tip_2.set_AT(['-0.06', 'sword_height*0.5+tip_height*0.5-0.0001', '0'], RELATIVE="object_center")

    blade_mask_tip_3 = Sword_Odin.add_component("blade_mask_tip_3", "Union_cylinder")
    blade_mask_tip_3.priority = 0
    blade_mask_tip_3.radius = "blade_tip_mask_radius"
    blade_mask_tip_3.yheight = "tip_height+0.10003"
    blade_mask_tip_3.mask_string = "\"blade_iron_side_tip_2,blade_rust_side_tip_3,blade_rust_side_tip_4,blade_rust_side_tip_2\""
    blade_mask_tip_3.mask_setting = "\"All\""
    blade_mask_tip_3.set_AT(['-blade_top_width*0.5*tip_x_multiplier', 'sword_height*0.5+tip_height*0.5-0.0001', 'blade_tip_mask_radius-sword_depth*0.5*0.8'], RELATIVE="object_center")
    blade_mask_tip_3.set_ROTATED(['2.5*width_angle', '0', '-blade_angle_tip_deg'], RELATIVE="object_center")
    blade_mask_tip_4 = Sword_Odin.add_component("blade_mask_tip_4", "Union_cylinder")
    blade_mask_tip_4.priority = 0
    blade_mask_tip_4.radius = "blade_tip_mask_radius"
    blade_mask_tip_4.yheight = "tip_height+0.10004"
    blade_mask_tip_4.mask_string = "\"blade_iron_side_tip_2,blade_rust_side_tip_3,blade_rust_side_tip_4,blade_rust_side_tip_2\""
    blade_mask_tip_4.mask_setting = "\"All\""
    blade_mask_tip_4.set_AT(['-blade_top_width*0.5*tip_x_multiplier', 'sword_height*0.5+tip_height*0.5-0.0001', '-blade_tip_mask_radius+sword_depth*0.5*0.8'], RELATIVE="object_center")
    blade_mask_tip_4.set_ROTATED(['-2.5*width_angle', '0', '-blade_angle_tip_deg'], RELATIVE="object_center")

    blade_side_iron_core_tip_2 = Sword_Odin.add_component("blade_side_iron_core_tip_2", "Union_box")
    blade_side_iron_core_tip_2.material_string = "\"iron_mix\""
    blade_side_iron_core_tip_2.priority = 301
    blade_side_iron_core_tip_2.xwidth = "0.12-0.0003"
    blade_side_iron_core_tip_2.yheight = "tip_height+0.0001"
    blade_side_iron_core_tip_2.zdepth = "sword_depth*2.0-0.001"
    blade_side_iron_core_tip_2.set_AT(['-0.06', 'sword_height*0.5+tip_height*0.5+0.0001', '0'], RELATIVE="object_center")

    blade_mask_tip_5 = Sword_Odin.add_component("blade_mask_tip_5", "Union_cylinder")
    blade_mask_tip_5.priority = 0
    blade_mask_tip_5.radius = "blade_tip_mask_radius*0.99"
    blade_mask_tip_5.yheight = "0.75*tip_height+0.0003"
    blade_mask_tip_5.mask_string = "\"blade_side_iron_core_tip_2\""
    blade_mask_tip_5.mask_setting = "\"All\""
    blade_mask_tip_5.set_AT(['-blade_top_width*0.5*tip_x_multiplier', 'sword_height*0.5+tip_height*0.5-0.0001', 'blade_tip_mask_radius-sword_depth*0.5*0.8'], RELATIVE="object_center")
    blade_mask_tip_5.set_ROTATED(['2.5*width_angle', '0', '-blade_angle_tip_deg'], RELATIVE="object_center")

    blade_mask_tip_6 = Sword_Odin.add_component("blade_mask_tip_6", "Union_cylinder")
    blade_mask_tip_6.priority = 0
    blade_mask_tip_6.radius = "blade_tip_mask_radius*0.99"
    blade_mask_tip_6.yheight = "0.75*tip_height+0.0002"
    blade_mask_tip_6.mask_string = "\"blade_side_iron_core_tip_2\""
    blade_mask_tip_6.mask_setting = "\"All\""
    blade_mask_tip_6.set_AT(['-blade_top_width*0.5*tip_x_multiplier', 'sword_height*0.5+tip_height*0.5-0.0001', '-blade_tip_mask_radius+sword_depth*0.5*0.8'], RELATIVE="object_center")
    blade_mask_tip_6.set_ROTATED(['-2.5*width_angle', '0', '-blade_angle_tip_deg'], RELATIVE="object_center")

    rust_core_tip = Sword_Odin.add_component("rust_core_tip", "Union_box")
    rust_core_tip.material_string = "rust_string"
    rust_core_tip.priority = 302
    rust_core_tip.xwidth = "core_side_top_length-0.001"
    rust_core_tip.yheight = "core_side_top_length-0.001"
    rust_core_tip.zdepth = "tip_height-0.05"
    rust_core_tip.xwidth2 = "2.0*rust_thickness+0.0001"
    rust_core_tip.yheight2 = "2.0*rust_thickness+0.0001"
    rust_core_tip.set_AT(['0', 'sword_height*0.5+(tip_height-0.05)*0.5-0.0003', '0'], RELATIVE="object_center")
    rust_core_tip.set_ROTATED(['-90', '0', '45'], RELATIVE="object_center")

    hard_core_tip = Sword_Odin.add_component("hard_core_tip", "Union_box")
    hard_core_tip.material_string = "\"iron_mix\""
    hard_core_tip.priority = 303
    hard_core_tip.xwidth = "core_side_top_length-rust_thickness*2.0-0.001"
    hard_core_tip.yheight = "core_side_top_length-rust_thickness*2.0-0.001"
    hard_core_tip.zdepth = "tip_height-0.05"
    hard_core_tip.xwidth2 = 0.0001
    hard_core_tip.yheight2 = 0.0001
    hard_core_tip.set_AT(['0', 'sword_height*0.5+(tip_height-0.05)*0.5-0.0001', '0'], RELATIVE="object_center")
    hard_core_tip.set_ROTATED(['-90', 'sword_height*0.5-0.0001', '45'], RELATIVE="object_center")

    left_blade_guard = Sword_Odin.add_component("left_blade_guard", "Union_box")
    left_blade_guard.material_string = "\"iron_mix\""
    left_blade_guard.priority = 1050
    left_blade_guard.xwidth = 0.03
    left_blade_guard.yheight = 0.045
    left_blade_guard.zdepth = 0.09
    left_blade_guard.xwidth2 = 0.02
    left_blade_guard.yheight2 = 0.02
    left_blade_guard.set_AT(['0.0451', '-sword_height*0.5-0.015', '0'], RELATIVE="object_center")
    left_blade_guard.set_ROTATED(['0', '90', '0'], RELATIVE="object_center")

    right_blade_guard = Sword_Odin.add_component("right_blade_guard", "Union_box")
    right_blade_guard.material_string = "\"iron_mix\""
    right_blade_guard.priority = 1051
    right_blade_guard.xwidth = 0.03
    right_blade_guard.yheight = 0.045
    right_blade_guard.zdepth = 0.09
    right_blade_guard.xwidth2 = 0.02
    right_blade_guard.yheight2 = 0.02
    right_blade_guard.set_AT(['-0.0451', '-sword_height*0.5-0.015', '0'], RELATIVE="object_center")
    right_blade_guard.set_ROTATED(['0', '-90', '0'], RELATIVE="object_center")

    handle = Sword_Odin.add_component("handle", "Union_cylinder")
    handle.material_string = "\"iron_mix\""
    handle.priority = 1052
    handle.radius = 0.02
    handle.yheight = 0.15
    handle.set_AT(['0', '-sword_height*0.5-0.03-0.15*0.5', '0'], RELATIVE="object_center")
    handle.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    handle_end = Sword_Odin.add_component("handle_end", "Union_sphere")
    handle_end.material_string = "\"iron_mix\""
    handle_end.priority = 1053
    handle_end.radius = 0.03
    handle_end.set_AT(['0', '-sword_height*0.5-0.03-0.15', '0'], RELATIVE="object_center")
    handle_end.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_mount = Sword_Odin.add_component("sample_mount", "Union_box")
    sample_mount.material_string = "\"Al\""
    sample_mount.priority = 10000
    sample_mount.xwidth = "sword_width*0.5"
    sample_mount.yheight = "sword_height*1.5"
    sample_mount.zdepth = 0.01
    sample_mount.set_AT(['-sword_width*0.20', 'sword_height*0.3', '-sword_depth*0.50-0.0075'], RELATIVE="object_center")
    sample_mount.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    Holder_1 = Sword_Odin.add_component("Holder_1", "Union_box")
    Holder_1.material_string = "\"Al\""
    Holder_1.priority = 10002
    Holder_1.xwidth = "sword_width*3"
    Holder_1.yheight = 0.04
    Holder_1.zdepth = "sword_depth*3"
    Holder_1.xwidth2 = "sword_width*3"
    Holder_1.yheight2 = 0.04
    Holder_1.set_AT(['0', '0.0', '0'], RELATIVE="object_center")
    Holder_1.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_1_mask_1 = Sword_Odin.add_component("sample_holder_1_mask_1", "Union_box")
    sample_holder_1_mask_1.priority = 0
    sample_holder_1_mask_1.xwidth = 0.005
    sample_holder_1_mask_1.yheight = 0.02
    sample_holder_1_mask_1.zdepth = "0.0085*2"
    sample_holder_1_mask_1.mask_string = "\"Holder_1\""
    sample_holder_1_mask_1.mask_setting = "\"Any\""
    sample_holder_1_mask_1.set_AT(['0.042', '0.0', '0'], RELATIVE="object_center")
    sample_holder_1_mask_1.set_ROTATED(['0', '0.0', '0'], RELATIVE="object_center")

    sample_holder_1_mask_2 = Sword_Odin.add_component("sample_holder_1_mask_2", "Union_box")
    sample_holder_1_mask_2.priority = 0
    sample_holder_1_mask_2.xwidth = 0.005
    sample_holder_1_mask_2.yheight = 0.02
    sample_holder_1_mask_2.zdepth = "0.0085*2"
    sample_holder_1_mask_2.mask_string = "\"Holder_1\""
    sample_holder_1_mask_2.mask_setting = "\"Any\""
    sample_holder_1_mask_2.set_AT(['-0.042', '0.0', '0'], RELATIVE="object_center")
    sample_holder_1_mask_2.set_ROTATED(['0', '0.0', '0'], RELATIVE="object_center")

    sample_holder_1_mask_3 = Sword_Odin.add_component("sample_holder_1_mask_3", "Union_box")
    sample_holder_1_mask_3.priority = 0
    sample_holder_1_mask_3.xwidth = 0.09
    sample_holder_1_mask_3.yheight = 0.02
    sample_holder_1_mask_3.zdepth = 0.005
    sample_holder_1_mask_3.mask_string = "\"Holder_1\""
    sample_holder_1_mask_3.mask_setting = "\"Any\""
    sample_holder_1_mask_3.set_AT(['0', '0.0', '0.0065'], RELATIVE="object_center")
    sample_holder_1_mask_3.set_ROTATED(['0', '0.0', '0'], RELATIVE="object_center")

    sample_holder_1_mask_4 = Sword_Odin.add_component("sample_holder_1_mask_4", "Union_box")
    sample_holder_1_mask_4.priority = 0
    sample_holder_1_mask_4.xwidth = 0.09
    sample_holder_1_mask_4.yheight = 0.02
    sample_holder_1_mask_4.zdepth = 0.005
    sample_holder_1_mask_4.mask_string = "\"Holder_1\""
    sample_holder_1_mask_4.mask_setting = "\"Any\""
    sample_holder_1_mask_4.set_AT(['0', '0.0', '-0.0065'], RELATIVE="object_center")
    sample_holder_1_mask_4.set_ROTATED(['0', '0.0', '0'], RELATIVE="object_center")

    Holder_2 = Sword_Odin.add_component("Holder_2", "Union_box")
    Holder_2.material_string = "\"Al\""
    Holder_2.priority = 10003
    Holder_2.xwidth = "sword_width*3"
    Holder_2.yheight = 0.04
    Holder_2.zdepth = "sword_depth*3"
    Holder_2.xwidth2 = "sword_width*3"
    Holder_2.yheight2 = 0.04
    Holder_2.set_AT(['0', '0.25', '0'], RELATIVE="object_center")
    Holder_2.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_2_mask_1 = Sword_Odin.add_component("sample_holder_2_mask_1", "Union_box")
    sample_holder_2_mask_1.priority = 0
    sample_holder_2_mask_1.xwidth = 0.005
    sample_holder_2_mask_1.yheight = 0.02
    sample_holder_2_mask_1.zdepth = "sword_depth*2.0"
    sample_holder_2_mask_1.mask_string = "\"Holder_2\""
    sample_holder_2_mask_1.mask_setting = "\"Any\""
    sample_holder_2_mask_1.set_AT(['0.036', '0.25', '0'], RELATIVE="object_center")
    sample_holder_2_mask_1.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_2_mask_2 = Sword_Odin.add_component("sample_holder_2_mask_2", "Union_box")
    sample_holder_2_mask_2.priority = 0
    sample_holder_2_mask_2.xwidth = 0.005
    sample_holder_2_mask_2.yheight = 0.02
    sample_holder_2_mask_2.zdepth = "sword_depth*2.0"
    sample_holder_2_mask_2.mask_string = "\"Holder_2\""
    sample_holder_2_mask_2.mask_setting = "\"Any\""
    sample_holder_2_mask_2.set_AT(['-0.036', '0.25', '0'], RELATIVE="object_center")
    sample_holder_2_mask_2.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_2_mask_3 = Sword_Odin.add_component("sample_holder_2_mask_3", "Union_box")
    sample_holder_2_mask_3.priority = 0
    sample_holder_2_mask_3.xwidth = 0.078
    sample_holder_2_mask_3.yheight = 0.02
    sample_holder_2_mask_3.zdepth = 0.005
    sample_holder_2_mask_3.mask_string = "\"Holder_2\""
    sample_holder_2_mask_3.mask_setting = "\"Any\""
    sample_holder_2_mask_3.set_AT(['0', '0.25', '0.0055'], RELATIVE="object_center")
    sample_holder_2_mask_3.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_2_mask_4 = Sword_Odin.add_component("sample_holder_2_mask_4", "Union_box")
    sample_holder_2_mask_4.priority = 0
    sample_holder_2_mask_4.xwidth = 0.078
    sample_holder_2_mask_4.yheight = 0.02
    sample_holder_2_mask_4.zdepth = 0.005
    sample_holder_2_mask_4.mask_string = "\"Holder_2\""
    sample_holder_2_mask_4.mask_setting = "\"Any\""
    sample_holder_2_mask_4.set_AT(['0', '0.25', '-0.0055'], RELATIVE="object_center")
    sample_holder_2_mask_4.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    Holder_3 = Sword_Odin.add_component("Holder_3", "Union_box")
    Holder_3.material_string = "\"Al\""
    Holder_3.priority = 10004
    Holder_3.xwidth = "sword_width*3.0"
    Holder_3.yheight = 0.04
    Holder_3.zdepth = "sword_depth*3.0"
    Holder_3.xwidth2 = "sword_width*1.52"
    Holder_3.yheight2 = 0.04
    Holder_3.set_AT(['0', '-0.25', '0'], RELATIVE="object_center")
    Holder_3.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_3_mask_1 = Sword_Odin.add_component("sample_holder_3_mask_1", "Union_box")
    sample_holder_3_mask_1.priority = 0
    sample_holder_3_mask_1.xwidth = 0.005
    sample_holder_3_mask_1.yheight = 0.02
    sample_holder_3_mask_1.zdepth = "sword_depth*1.9"
    sample_holder_3_mask_1.mask_string = "\"Holder_3\""
    sample_holder_3_mask_1.mask_setting = "\"Any\""
    sample_holder_3_mask_1.set_AT(['0.047', '-0.25', '0'], RELATIVE="object_center")
    sample_holder_3_mask_1.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_3_mask_2 = Sword_Odin.add_component("sample_holder_3_mask_2", "Union_box")
    sample_holder_3_mask_2.priority = 0
    sample_holder_3_mask_2.xwidth = 0.005
    sample_holder_3_mask_2.yheight = 0.02
    sample_holder_3_mask_2.zdepth = "sword_depth*1.9"
    sample_holder_3_mask_2.mask_string = "\"Holder_3\""
    sample_holder_3_mask_2.mask_setting = "\"Any\""
    sample_holder_3_mask_2.set_AT(['-0.047', '-0.25', '0'], RELATIVE="object_center")
    sample_holder_3_mask_2.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_3_mask_3 = Sword_Odin.add_component("sample_holder_3_mask_3", "Union_box")
    sample_holder_3_mask_3.priority = 0
    sample_holder_3_mask_3.xwidth = 0.1
    sample_holder_3_mask_3.yheight = 0.02
    sample_holder_3_mask_3.zdepth = 0.005
    sample_holder_3_mask_3.mask_string = "\"Holder_3\""
    sample_holder_3_mask_3.mask_setting = "\"Any\""
    sample_holder_3_mask_3.set_AT(['0', '-0.25', '0.007'], RELATIVE="object_center")
    sample_holder_3_mask_3.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    sample_holder_3_mask_4 = Sword_Odin.add_component("sample_holder_3_mask_4", "Union_box")
    sample_holder_3_mask_4.priority = 0
    sample_holder_3_mask_4.xwidth = 0.1
    sample_holder_3_mask_4.yheight = 0.02
    sample_holder_3_mask_4.zdepth = 0.005
    sample_holder_3_mask_4.mask_string = "\"Holder_3\""
    sample_holder_3_mask_4.mask_setting = "\"Any\""
    sample_holder_3_mask_4.set_AT(['0', '-0.25', '-0.007'], RELATIVE="object_center")
    sample_holder_3_mask_4.set_ROTATED(['0', '0', '0'], RELATIVE="object_center")

    detector_exit = Sword_Odin.add_component("detector_exit", "Union_box")
    detector_exit.material_string = "\"Exit\""
    detector_exit.priority = 10000000
    detector_exit.xwidth = 0.3
    detector_exit.yheight = 0.3
    detector_exit.zdepth = 0.101
    detector_exit.set_AT(['0', '0', 'pinhole_detector_distance+0.05'], RELATIVE="graph")

    Sword = Sword_Odin.add_component("Sword", "Union_master")
    Sword.set_WHEN("Sample==1")
    Sword.set_AT(['0', '0', '0'], RELATIVE="a1")
    Sword.set_ROTATED(['0', '0', '0'], RELATIVE="a1")

    Stop = Sword_Odin.add_component("Stop", "Union_stop")
    Stop.set_AT(['0', '0', '0'], RELATIVE="a1")

    screen = Sword_Odin.add_component("screen", "PSD_monitor_Filter")
    screen.nx = 300
    screen.ny = 300
    screen.nL = 200
    screen.filter_pixels = 600
    screen.filename = "\"absoprtion_picture.dat\""
    screen.xwidth = 0.3
    screen.yheight = 0.3
    screen.restore_neutron = 0
    screen.TwoD_filename = "spacial_resolution"
    screen.L_filename = "wavelength_spectrum"
    screen.Lmin = 0
    screen.Lmax = 10
    screen.aply_xy_filter = 1
    screen.pinhol_filter_distance = 25.025
    screen.pinhol_detector_distance = "pinhole_detector_distance"
    screen.smoothing = 3.0
    screen.zoom = "Zoom"
    screen.set_AT(['0', '0', 'pinhole_detector_distance'], RELATIVE="graph")

    L_monitor = Sword_Odin.add_component("L_monitor", "L_monitor")
    L_monitor.nL = 200
    L_monitor.filename = "\"I_lambda.dat\""
    L_monitor.xwidth = 1
    L_monitor.yheight = 1
    L_monitor.Lmin = 0
    L_monitor.Lmax = 10
    L_monitor.restore_neutron = 1
    L_monitor.set_AT(['0.0', '0.0', 'pinhole_detector_distance'], RELATIVE="screen")

    return Sword_Odin
