"""
:file: main.py
:author: Paul Soma
:description: Main anomaly detection
"""
import adm_geocode
import adm_preproc
import adm_load
import os
import definitions
import time

if __name__ == '__main__':

    df = adm_load.transactions()

    print(definitions.ROOT_DIR)

    addr = adm_geocode.prep_addr(df)

    start = 0
    step = 10

    n = addr.shape[0]

    print(addr.isnull().values.any())


    add_strs = addr.loc[start:n,'CARDACCEPTORADDRESS']

    sv = addr.drop_duplicates()

    sv.to_csv('state_country')


   # gcode = adm_geocode.geocode_all(sv,start,step)







