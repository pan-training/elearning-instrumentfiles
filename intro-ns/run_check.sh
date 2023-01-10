#!/bin/sh

rm -r data_folder
rm -r debug
rm -r logs

mcrun_path=/Applications/McStas-3.2build.app/Contents/Resources/mcstas/3.2build/bin/

cp -r SANSsimple SANSsimple_run
cp -r SANSsimpleSpheres SANSsimpleSpheres_run
cp -r SimplePowderDiffractometer SimplePowderDiffractometer_run
cp -r Radiography_absorbing_edge Radiography_absorbing_edge_run
cp -r reflectometer reflectometer_run

python reproduce_examples.py -f SANSsimple -i SANSsimple_run -p $mcrun_path -s 312 -n 1E6
python reproduce_examples.py -f SANSsimpleSpheres -i SANSsimpleSpheres_run -p $mcrun_path  -s 312 -n 1E6
python reproduce_examples.py -f SimplePowderDiffractometer -i SimplePowderDiffractometer_run -p $mcrun_path  -s 312 -n 1E6
python reproduce_examples.py -f Radiography_absorbing_edge -i Radiography_absorbing_edge_run -p $mcrun_path  -s 312 -n 1E6
python reproduce_examples.py -f reflectometer -i reflectometer_run -p $mcrun_path  -s 312 -n 1E6
