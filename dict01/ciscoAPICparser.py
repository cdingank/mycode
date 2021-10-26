#!/usr/bin/env python3
"""parsing json"""
import json # working with JSON data

def main():
    with open("ciscoAPIC.json", "r") as jsonfile:
        x = json.load(jsonfile)
        print("The number of instances: ", len(x['imdata']))
        for instances in x['imdata']:
            print("Firmware version running - ", instances.get('firmwareCtrlrRunning').get('attributes').get('version'))

main()
