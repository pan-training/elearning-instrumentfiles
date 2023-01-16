"""
This McStasScript file was generated from a
McStas instrument file. It is advised to check
the content to ensure it is as expected.
"""
from mcstasscript.interface import instr, plotter, functions

def make():
    ESS_HEIMDAL = instr.McStas_instr("ESS_HEIMDAL_generated")
    ESS_HEIMDAL.add_parameter("double", "HighRes", value=0.0)
    ESS_HEIMDAL.add_parameter("double", "T", value=25.0)
    ESS_HEIMDAL.add_parameter("double", "tau", value=0.0)
    ESS_HEIMDAL.add_parameter("double", "dmin", value=0.5)
    ESS_HEIMDAL.add_parameter("double", "dmax", value=5.5)
    ESS_HEIMDAL.add_declare_var("double", "tof")
    ESS_HEIMDAL.add_declare_var("double", "tofmin")
    ESS_HEIMDAL.add_declare_var("double", "tofmax")
    ESS_HEIMDAL.add_declare_var("double", "det_rad")
    ESS_HEIMDAL.add_declare_var("double", "det_Linst")
    ESS_HEIMDAL.add_declare_var("double", "det_t0")
    ESS_HEIMDAL.add_declare_var("double", "det_th1")
    ESS_HEIMDAL.add_declare_var("double", "det_th2")
    ESS_HEIMDAL.add_declare_var("double", "hm", value="2*PI*K2V")
    ESS_HEIMDAL.add_declare_var("double", "samplechoice", value=0.0)
    ESS_HEIMDAL.add_declare_var("double", "Tc", value=525.0)
    ESS_HEIMDAL.add_declare_var("double", "lam0")
    ESS_HEIMDAL.add_declare_var("double", "dlam")
    ESS_HEIMDAL.add_declare_var("double", "dPulse")
    ESS_HEIMDAL.add_declare_var("double", "lmin", value=0.65)
    ESS_HEIMDAL.add_declare_var("double", "lmax", value=2.35)
    ESS_HEIMDAL.add_declare_var("double", "use_CoFe2O4", value=1.0)
    ESS_HEIMDAL.add_declare_var("double", "use_CoFe", value=1.0)
    ESS_HEIMDAL.add_declare_var("double", "use_magn", value=1.0)
    ESS_HEIMDAL.add_declare_var("double", "f1", value=0.5)
    ESS_HEIMDAL.add_declare_var("double", "f2", value=1.0)
    ESS_HEIMDAL.add_declare_var("double", "f3", value=1.0)
    ESS_HEIMDAL.add_declare_var("double", "dfactor", value=1.0)
    ESS_HEIMDAL.add_declare_var("int", "dbins")
    ESS_HEIMDAL.add_declare_var("char", "monopts", array=256)
    ESS_HEIMDAL.add_declare_var("char", "monopts2", array=256)
    ESS_HEIMDAL.append_declare("  struct pieceswisepars {")
    ESS_HEIMDAL.append_declare("    double min;")
    ESS_HEIMDAL.append_declare("    double max;")
    ESS_HEIMDAL.append_declare("    double* uppers;")
    ESS_HEIMDAL.append_declare("    double* slopes;")
    ESS_HEIMDAL.append_declare("    double* consts;")
    ESS_HEIMDAL.append_declare("  };")
    ESS_HEIMDAL.append_declare("")
    ESS_HEIMDAL.add_declare_var("double", "Itime_CoFe2O4")
    ESS_HEIMDAL.add_declare_var("double", "Itime_CoFe")
    ESS_HEIMDAL.append_declare("  struct pieceswisepars pars_CoFe2O4;")
    ESS_HEIMDAL.append_declare("  struct pieceswisepars pars_CoFe;")
    ESS_HEIMDAL.append_declare("  int piecewiselin(double x, double* val, struct pieceswisepars* fct, int sz);")
    ESS_HEIMDAL.append_declare("")
    ESS_HEIMDAL.append_declare("  //")
    ESS_HEIMDAL.append_declare("  // determine Itime_CoFe2O4 and Itime_CoFe")
    ESS_HEIMDAL.append_declare("  int piecewiselin(double x, double* val, struct pieceswisepars* fct, int sz) {")
    ESS_HEIMDAL.append_declare("    // NOTE: the user is responsible")
    ESS_HEIMDAL.append_declare("    double* u = fct->uppers;")
    ESS_HEIMDAL.append_declare("    double* s = fct->slopes;")
    ESS_HEIMDAL.append_declare("    double* c = fct->consts;")
    ESS_HEIMDAL.append_declare("    double min = fct->min;")
    ESS_HEIMDAL.append_declare("")
    ESS_HEIMDAL.append_declare("    // use first found segment")
    ESS_HEIMDAL.append_declare("    int i = 0;")
    ESS_HEIMDAL.append_declare("    double low, high;")
    ESS_HEIMDAL.append_declare("    for (i=0;i<sz;i++) {")
    ESS_HEIMDAL.append_declare("      // determine segment lower limit")
    ESS_HEIMDAL.append_declare("      if (i==0) low = min;")
    ESS_HEIMDAL.append_declare("      else low = u[i-1];")
    ESS_HEIMDAL.append_declare("")
    ESS_HEIMDAL.append_declare("      // determine segment upper limit")
    ESS_HEIMDAL.append_declare("      high = u[i];")
    ESS_HEIMDAL.append_declare("      if (low<=x && x<=high) {")
    ESS_HEIMDAL.append_declare("        fprintf(stdout, \"\\nl:%1f h:%1f s:%1f c:%1f x:%1f\", low, high, s[i], c[i], x);")
    ESS_HEIMDAL.append_declare("        *val = s[i]*x + c[i];")
    ESS_HEIMDAL.append_declare("        return s[i]*x + c[i];")
    ESS_HEIMDAL.append_declare("        //return 0;")
    ESS_HEIMDAL.append_declare("      }")
    ESS_HEIMDAL.append_declare("    }")
    ESS_HEIMDAL.append_declare("    return 1;")
    ESS_HEIMDAL.append_declare("  }")
    ESS_HEIMDAL.append_declare("")
    ESS_HEIMDAL.append_initialize("det_th1 = 10; ")
    ESS_HEIMDAL.append_initialize("det_th2 = 170; ")
    ESS_HEIMDAL.append_initialize("det_rad = 1.5; ")
    ESS_HEIMDAL.append_initialize("det_Linst = 150+det_rad; ")
    ESS_HEIMDAL.append_initialize("tof = det_Linst/hm*lam0*1e6; ")
    ESS_HEIMDAL.append_initialize("tofmin = det_Linst/hm*lmin*1e6; ")
    ESS_HEIMDAL.append_initialize("tofmax = det_Linst/hm*lmax*1e6; ")
    ESS_HEIMDAL.append_initialize("lam0 = (lmax+lmin)/2.0; ")
    ESS_HEIMDAL.append_initialize("dlam = (lmax-lmin)/2.0; ")
    ESS_HEIMDAL.append_initialize("dbins = ceil((dmax-dmin)/0.002); ")
    ESS_HEIMDAL.append_initialize("  ")
    ESS_HEIMDAL.append_initialize("dfactor = 0.02*T/Tc + 1; ")
    ESS_HEIMDAL.append_initialize("double min = 0; ")
    ESS_HEIMDAL.append_initialize("double u[2] = {50, 600}; ")
    ESS_HEIMDAL.append_initialize("double s[2] = {0, 1/250.0}; ")
    ESS_HEIMDAL.append_initialize("double c[2] = {0, -50*1/250.0}; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe.min = min; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe.uppers = u; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe.slopes = s; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe.consts = c; ")
    ESS_HEIMDAL.append_initialize("piecewiselin(tau, &Itime_CoFe, &pars_CoFe, 2); ")
    ESS_HEIMDAL.append_initialize("double min2 = 0; ")
    ESS_HEIMDAL.append_initialize("double u2[1] = {300}; ")
    ESS_HEIMDAL.append_initialize("double s2[1] = {-0.4/300}; ")
    ESS_HEIMDAL.append_initialize("double c2[1] = {0.4}; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe2O4.min = min2; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe2O4.uppers = u2; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe2O4.slopes = s2; ")
    ESS_HEIMDAL.append_initialize("pars_CoFe2O4.consts = c2; ")
    ESS_HEIMDAL.append_initialize("piecewiselin(tau, &Itime_CoFe2O4, &pars_CoFe2O4, 1); ")
    ESS_HEIMDAL.append_initialize(" if (HighRes==0) { ")
    ESS_HEIMDAL.append_initialize("   dPulse=3.86e-3*0.05; ")
    ESS_HEIMDAL.append_initialize(" } else { ")
    ESS_HEIMDAL.append_initialize("   dPulse=3.86e-3*0.0017; ")
    ESS_HEIMDAL.append_initialize(" } ")
    ESS_HEIMDAL.append_initialize(" sprintf(monopts,\"banana theta limits=[%g %g] bins=600, tof limits=[%g %g] bins=800\",det_th1, det_th2, 0.95*tofmin/1e6, tofmax*1.05/1e6); ")
    ESS_HEIMDAL.append_initialize(" sprintf(monopts2,\"banana theta limits=[%g %g] bins=600, tof limits=[%g %g] bins=800\",-170.0, -55.0, 0.95*tofmin/1e6, tofmax*1.05/1e6); ")

    origin = ESS_HEIMDAL.add_component("origin", "Progress_bar")
    origin.set_AT(['0', ' 0', ' 0'], RELATIVE="ABSOLUTE")

    source = ESS_HEIMDAL.add_component("source", "Source_simple")
    source.focus_xw = 0.01
    source.focus_yh = 0.07
    source.lambda0 = "lam0"
    source.dlambda = "dlam"
    source.flux = 1e14
    source.target_index = 3
    source.append_EXTEND("samplechoice=rand01();")
    source.append_EXTEND("t=rand01()*dPulse;")
    source.append_EXTEND("p*=dPulse/3.86e-3;")
    source.set_AT(['0', '0', '0'], RELATIVE="PREVIOUS")

    SampleArm = ESS_HEIMDAL.add_component("SampleArm", "Arm")
    SampleArm.set_SPLIT(32)
    SampleArm.set_AT(['0', ' 0', ' 150'], RELATIVE="source")
    
    sample_2 = ESS_HEIMDAL.add_component("sample_2", "PowderN_dspace_factor")
    sample_2.reflections = "\"CoFe_56273.txt\""
    sample_2.radius = 0.005
    sample_2.yheight = 0.07
    sample_2.p_transmit = 0
    sample_2.d_phi = 10
    sample_2.dspace_factor = "dfactor"
    sample_2.append_EXTEND("p *= Itime_CoFe;")
    sample_2.append_EXTEND("p *= f1;")
    sample_2.set_WHEN("samplechoice>=0.43 && samplechoice<0.86 && use_CoFe==1")
    sample_2.set_AT(['0', ' 0', ' 150'], RELATIVE="source")

    sample_1 = ESS_HEIMDAL.add_component("sample_1", "PowderN_dspace_factor")
    sample_1.reflections = "\"CoFe2O4_109044.txt\""
    sample_1.radius = 0.005
    sample_1.yheight = 0.07
    sample_1.p_transmit = 0
    sample_1.d_phi = 10
    sample_1.dspace_factor = "dfactor"
    sample_1.append_EXTEND("p *= Itime_CoFe2O4;")
    sample_1.append_EXTEND("p *= f2;")
    sample_1.set_WHEN("samplechoice<0.43 && use_CoFe2O4==1")
    sample_1.set_AT(['0', ' 0', ' 150'], RELATIVE="source")

    Magnet = ESS_HEIMDAL.add_component("Magnet", "PowderN_dspace_factor")
    Magnet.reflections = "\"magnetic_peak.txt\""
    Magnet.radius = 0.001
    Magnet.yheight = 0.07
    Magnet.p_inc = 0
    Magnet.p_transmit = 0
    Magnet.d_phi = 10
    Magnet.dspace_factor = "dfactor"
    Magnet.append_EXTEND("if (INSTRUMENT_GETPAR(T)<Tc && INSTRUMENT_GETPAR(T)>=0) {")
    Magnet.append_EXTEND("p *= (Tc-INSTRUMENT_GETPAR(T))/(Tc);")
    Magnet.append_EXTEND("p *= f3;")
    Magnet.append_EXTEND("p *= Itime_CoFe2O4;")
    Magnet.append_EXTEND("}")
    Magnet.append_EXTEND("else")
    Magnet.append_EXTEND("ABSORB;")
    Magnet.set_WHEN("samplechoice>=0.86")
    Magnet.set_AT(['0', ' 0', ' 150'], RELATIVE="source")

    psdtof = ESS_HEIMDAL.add_component("psdtof", "NPI_tof_theta_monitor")
    psdtof.filename = "\"tof_theta.dat\""
    psdtof.radius = 1.5
    psdtof.yheight = 1
    psdtof.tmin = "0.95*tofmin"
    psdtof.tmax = "tofmax*1.05"
    psdtof.amin = "det_th1"
    psdtof.amax = "det_th2"
    psdtof.restore_neutron = 1
    psdtof.verbose = 0
    psdtof.nt = 800
    psdtof.na = 600
    psdtof.set_AT(['0', ' 0', ' 0'], RELATIVE="sample_1")

    npi_tof_dhkl_detector = ESS_HEIMDAL.add_component("npi_tof_dhkl_detector", "NPI_tof_dhkl_detector")
    npi_tof_dhkl_detector.filename = "\"dhkl.dat\""
    npi_tof_dhkl_detector.radius = "det_rad"
    npi_tof_dhkl_detector.yheight = 1.0
    npi_tof_dhkl_detector.zdepth = 0.01
    npi_tof_dhkl_detector.amin = "det_th1"
    npi_tof_dhkl_detector.amax = "det_th2"
    npi_tof_dhkl_detector.nd = "dbins"
    npi_tof_dhkl_detector.d_min = "dmin"
    npi_tof_dhkl_detector.d_max = "dmax"
    npi_tof_dhkl_detector.time0 = 0
    npi_tof_dhkl_detector.Linst = 152
    npi_tof_dhkl_detector.Lc = 0
    npi_tof_dhkl_detector.res_x = 0.002
    npi_tof_dhkl_detector.res_y = 0.005
    npi_tof_dhkl_detector.res_t = 1e-6
    npi_tof_dhkl_detector.mu = 1.0
    npi_tof_dhkl_detector.mod_shift = 0
    npi_tof_dhkl_detector.modulation = 0
    npi_tof_dhkl_detector.mod_dt = 0
    npi_tof_dhkl_detector.mod_twidth = "dPulse"
    npi_tof_dhkl_detector.mod_d0_table = "\"dhkl.tab\""
    npi_tof_dhkl_detector.restore_neutron = 1
    npi_tof_dhkl_detector.set_AT(['0', ' 0', ' 0'], RELATIVE="sample_1")

    return ESS_HEIMDAL
