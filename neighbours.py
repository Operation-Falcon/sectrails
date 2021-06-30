import argparse
import sys
from banner.banner import banner_design
from function import *
banner=banner_design()


parser=argparse.ArgumentParser(description="Subdomain enumeration", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i", "--ip", help="ip address", type=str, required=True)
parser.add_argument("-o","--output", help="output filename to save the results", type=str, required=True)
parser.add_argument("-a", "--api", help="Security trails api key", type=str, required=True)
args=parser.parse_args()

if len(sys.argv) <7:
    sys.exit()
elif sys.argv[2]==args.ip and sys.argv[4]==args.api and sys.argv[6]==args.output:
    neighbours(args.ip, args.api, args.output)