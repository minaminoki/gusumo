# Environment
* ubuntu16.04
* sumo-1.1.0
* python (higher than 2.7)
* matplotlib
* pyproj
* rtree
* overpy
* folium
* dill

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

## Install packages for check spot scripts

```
pip install overpy
pip install folium
pip install dill
```

# How to SUMO?
It is difficult to use SUMO, if you first try.

There are 3 steps.

## 1. Prepare Map
There are three method.
* netgenerate
* OpenStreatMap
* netedit
## 2. Demand Modeling
### create trips
* random Trips
### Route generate
* duarouter
## 3. Simulation
* sumo
* sumo-gui

# Simple map simulation
## prepare map
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

## demand modeling and run

```
./runner.py gridmap
```

This script include randomTrips and duarouter and sumo-gui.

<img src="https://github.com/minaminoki/gusumo/blob/master/img/gridmap.gif" width="640">

# Real map simulation
If you want to use real map, you should use a osmWebWizard tool.

```
./osmWebWizard.sh
```

<img src="https://github.com/minaminoki/gusumo/blob/master/img/osmWebWizard.png" width="640">

You set a your favarite location.
I set "Tokyo".

Push car icon, then push like this.

<img src="https://github.com/minaminoki/gusumo/blob/master/img/traffic_setting.png" width="270">

Also push Generate Scenario.
It takes a few minutes.
If this successed, appear sumo-gui.

You push Start button.

<img src="https://github.com/minaminoki/gusumo/blob/master/img/Tokyo.gif" width="1280">

# GUSUMO Tools
## Where is The Closest Edge?

This is a tools to find closeset edge from longitude and latitude.  

```
./getNeighboringEdges.py -n osm/Tokyo/osm.net.xml --lon 139.765 --lat 35.68
```

Red point is a point you set (lon lat).  
Blue edge is a closest edge line.  
<img src="https://github.com/minaminoki/gusumo/blob/master/img/closestEdge.png" width="720">  
Console output closest edge and distance

```
net file        : osm/Tokyo/osm.net.xml
(lon,lat)       : (139.765, 35.68)
(x,y)           : (8618.109951582097, 3573.570724199526)
closest edge    : <edge id="363564525#2" from="3677320551" to="3925244022"/>
distance        : 18.126912151173638
```

## Check Spot for Demand Modeling

Check convenience store in erea.  
Save *.pkl file.  

```
./check_spots/save_pkl.py
```

Check in browser.  

```
./check_spots/load_pkl.py
firefox map.html
```

<img src="https://github.com/minaminoki/gusumo/blob/master/img/check_spot.png" width="720">  

# MEMO
## location
map.net.xml

```
...
    <location netOffset="0.00,0.00" convBoundary="0.00,0.00,60.00,60.00" origBoundary="0.00,0.00,60.00,60.00" projParameter="!"/>
...
```

convBoundary is important.

you use this number in plot\_net\_speed.py

```
...
 --xlim 0,60 --ylim 0,60 \
...
```

## unicode ERROR in osmWebWizard.py
Python3 is not difined unicode.

```
calling route2trips
Traceback (most recent call last):
  File "/usr/share/sumo/tools/osmWebWizard.py", line 432, in build
    builder.build()
  File "/usr/share/sumo/tools/osmWebWizard.py", line 304, in build
    (randomTripsPath, " ".join(map(quoted_str, self.getRelative(opts)))))
  File "/usr/share/sumo/tools/osmWebWizard.py", line 164, in getRelative
    if type(o) in [str, unicode] and o[0:l] == dirname:
NameError: name 'unicode' is not defined
```

So you need repair this error.

Before  
osmWebWizard.py
```
159     def getRelative(self, options):
160         result = []
161         dirname = self.tmp
162         l = len(dirname)
163         for o in options:
164             if type(o) in [str, unicode] and o[0:l] == dirname:
165                 remove = o[:l+1]
166                 result.append(o.replace(remove, ''))
167             else:
168                 result.append(o)
169         return result
```

After  

```
159     def getRelative(self, options):
160         result = []
161         dirname = self.tmp
162         l = len(dirname)
163         for o in options:
164             try:
165                 UNICODE_EXISTS = bool(type(unicode))
166             except NameError:
167                unicode = lambda s: str(s)
168             if type(o) in [str, unicode] and o[0:l] == dirname:
169                 remove = o[:l+1]
170                 result.append(o.replace(remove, ''))
171             else:
172                 result.append(o)
173         return result
```

# Reference
## Sumo
* https://sumo.dlr.de/wiki/Simulation_of_Urban_MObility_-_Wiki

## Sumo Tools Visualization
* https://sumo.dlr.de/wiki/Tools/Visualization

## Sumolib
* https://sumo.dlr.de/wiki/Tools/Sumolib
* https://sumo.dlr.de/pydoc/sumolib.net.html

## OpenStreatMap
* https://qiita.com/tags/openstreetmap

## OpenStreatMap Tag infomation
* https://taginfo.openstreetmap.org/

## Overpass
* https://wiki.openstreetmap.org/wiki/Overpass_API/Installation
* http://overpass-turbo.eu/
* https://wiki.openstreetmap.org/wiki/JA:Overpass_API/%E8%A8%80%E8%AA%9E%E3%82%AC%E3%82%A4%E3%83%89

* [New York fuel station](http://overpass-turbo.eu/s/GbE)

## Overpy
* https://pypi.org/project/overpy/
* http://nao-y.hatenablog.com/entry/2018/04/26/181029
* https://python-overpy.readthedocs.io/en/latest/example.html

## TraCI
* https://sumo.dlr.de/wiki/TraCI
* https://sumo.dlr.de/wiki/TraCI/Interfacing_TraCI_from_Python

## osmnx
* https://geoffboeing.com/2016/11/osmnx-python-street-networks/
* https://githubja.com/gboeing/osmnx

## Dataset
* https://developer.wmata.com/

## Leaflet
* https://leafletjs.com/

## folium
* https://qiita.com/momota10/items/3b878f01d489a32e40c3
* https://blog.prototypr.io/interactive-maps-with-python-part-1-aa1563dbe5a9
* https://python-visualization.github.io/folium/docs-v0.6.0/quickstart.html
* http://sinhrks.hatenablog.com/entry/2015/12/26/231000
