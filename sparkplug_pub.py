#! /usr/bin/python3

import sparkplugb_pb2
import random

ALLOWED_PARAMETER_NAMES = ["temperate", "pressure", "light_sensor", "humidity"]

'''
EoN Node Spec: 
Software
    System Software Overview:
        System Version: macOS 12.6.1 (21G217)
        Kernel Version: Darwin 21.6.0
        Boot Volume: Macintosh HD
        Boot Mode: Normal
        Computer Name: SoundsMacBookPro
        User Name: chirag
        Secure Virtual Memory: Enabled
Hardware
    Hardware Overview
        Model Name: MacBook Pro
        Model Identifier: MacBookPro13,3
        Processor Name: Quad-Core Intel Core i7
        Processor Speed: 2.6 GHz
        Number of Processors: 1
        Total Number of Cores: 4
        L2 Cache (per Core): 256 KB
        L3 Cache: 6 MB
        Hyper-Threading Technology: Enabled
        Memory: 16 GB
        System Firmware Version: 499.40.2.0.0
        OS Loader Version: 540.120.3~22
        SMC Version (system): 2.38f12
        Serial Number (system): C02SW4UXGTFL
        Hardware UUID: 55D9103D-F307-5ACA-8616-7A0451FC5E94
        Provisioning UDID: 55D9103D-F307-5ACA-8616-7A0451FC5E94
'''

def generate_parameter():
    # TODO
    return None

def generate_template():
    parameter = generate_parameter()

def generate_data_set_value():
    return 

def generate_data_set():
    data_set_value = generate_data_set_value()

def generate_payload():
    message = generate_template()
    data_set = generate_data_set()

def generate_sparkplugb_payload():
    sparkplugb = sparkplugb_pb2.Payload


generate_sparkplugb_payload()