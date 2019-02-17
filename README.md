# Environment
* ubuntu16.04
* sumo-1.1.0
* python (higher than 2.7)
* matplotlib
* pyproj
* rtree

# Setup
## set environment value
if you use bash
```
echo "export SUMO_HOME=/usr/share/sumo" >> ~/.bashrc
source ~/.bashrc
```

## Install matplotlib
```
# if you use python on system, you need `sudo -H` 
pip install matplotlib
```

## Install rtree and pyproj
rtree need spatialindex
```
wget http://download.osgeo.org/libspatialindex/spatialindex-src-1.8.5.tar.gz
cd spatialindex-src-1.8.5
mkdir build
cd build
cmake ..
make -j 4
sudo make install
sudo ldconfig
# if you use python on system, you need `sudo -H` 
pip install pyproj
pip install rtree
```

# How to use
## make grid map
```
./gridnetgen.sh
```

## draw net
```
./draw_net.py -n gridmap/map.net.xml
```

## run simple simulation
```
./runner.py gridmap
# or
./runner.sh gridmap
```

## plot net speed
```
./plot_net_speed.sh
```

# How to SUMO?
It is difficult to use SUMO, if you first try.

There are 4 steps.

## Index
### 1. Prepare Map
There are three method.
* netgenerate
* OpenStreatMap
* netedit
### 2. Demand Modeling
* random Trips
### 3. Route generate
* duarouter
### 4. Simulation
* sumo
* sumo-gui
# 1. Prepare Map
## netgenerate
If you want to create simple map easy, you should use netgenerate.

netgenerate has three types map.

* gridmap
```
./gridnetgen.sh
./draw_net.py -n gridmap/map.net.xml
```
<img src="https://github.com/minaminoki/gusumo/blob/master/img/draw_gridmap.png" width="640">

* spidermap
```
./spidernetgen.sh
./draw_net.py -n spidermap/map.net.xml
```
<img src="https://github.com/minaminoki/gusumo/blob/master/img/draw_spidermap.png" width="640">

* randommap
```
./randamnetgen.sh
./draw_net.py -n randommap/map.net.xml
```
<img src="https://github.com/minaminoki/gusumo/blob/master/img/draw_randommap.png" width="640">

## OpenStreatMap

## MEMO
map.net.xml
```
...
    <location netOffset="0.00,0.00" convBoundary="0.00,0.00,60.00,60.00" origBoundary="0.00,0.00,60.00,60.00" projParameter="!"/>
...
```
convBoundary is important

you use this number in plot\_net\_speed.py
```
...
 --xlim 0,60 --ylim 0,60 \
...
```

