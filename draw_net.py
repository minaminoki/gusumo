#!/usr/bin/env python

# @file		lonlat2xy.py
# @author	Yuji Ogusu
# @date		2019-02-17

import sys
import os
import matplotlib.pyplot as plt
import matplotlib 

## Get SUMO Environment information
if 'SUMO_HOME' in os.environ:
    SUMO_PATH = os.environ['SUMO_HOME']
    TOOLS_PATH = os.path.join(SUMO_PATH, 'tools')
    BIN_PATH = os.path.join(SUMO_PATH,'bin')
    sys.path.append(TOOLS_PATH)
else:   
    sys.exit("please declare environment variable 'SUMO_HOME'")

import sumolib
from sumolib.visualization import helpers

def main(args=None):
    ## Set Argument Parser
    from optparse import OptionParser
    optParser = OptionParser()
    optParser.add_option("-n", "--net", dest="net", metavar="FILE",
                         help="Defines the network to read")
    optParser.add_option("--edge-width", dest="defaultWidth",
                         type="float", default=1, help="Defines the edge width")
    optParser.add_option("--edge-color", dest="defaultColor",
                         default='k', help="Defines the edge color")
    optParser.add_option("-v", "--verbose", dest="verbose", action="store_true",
                         default=False, help="If set, the script says what it's doing")
    ## standard plot options
    helpers.addInteractionOptions(optParser)
    helpers.addPlotOptions(optParser)
    ## parse
    options, remaining_args = optParser.parse_args(args=args)
    ## Set Simulation Environment
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    if options.net is None:
        print("Error: a network to load must be given.")
        return 1
    if options.verbose:
        print("Reading network from '%s'" % options.net)
    NET_FILE = options.net
    ## Show infomation
    print('script          : '+__file__)
    print('base            : '+BASE_PATH)
    print('sumo home       : '+SUMO_PATH)
    print('bin path        : '+BIN_PATH)
    print('tools path      : '+TOOLS_PATH)
    print('net file        : '+NET_FILE)
    ## Read Net
    net = sumolib.net.readNet(NET_FILE)
    ## Open Figure
    fig, ax = helpers.openFigure(options)
    ax.set_aspect("equal", None, 'C')
    ## Plot Net
    helpers.plotNet(net, {}, {}, options)
    options.nolegend = True
    ## Close Figure
    helpers.closeFigure(fig, ax, options)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

