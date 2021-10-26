#!/usr/bin/env python3
import csv
def main ():

    #vendorlist = []

    with open('vendor.csv', 'r') as vendorfile:
        vendorlist = csv.reader(vendorfile, delimiter=",")

        for row in vendorlist:
            print ("The IP " + row[2] + " driver " + row[3])

main()
