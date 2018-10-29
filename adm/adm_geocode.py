"""
:file: adm_geocode.py
:author: Paul Soma
:description: Functions for geocoding
"""

import definitions

import googlemaps
import geopy
import os
import geopandas

def prep_addr(df, fill_na = True):
    """
    function to take prepare an address to be converted to latitude and longitude
    in case of missing values, use:
         the center of the state
         the center of the country
         the previous transaction location

    :param df: pd.DataFrame of transactions
    :return: addr: pd.Series of address strings
    """

    # dataframe of address strings
    add_df = df.loc[:, ['CARDACCEPTORSTREET', 'CARDACCEPTORCITY', 'CARDACCEPTORSTATE', 'CARDACCEPTORCOUNTRY']]

    # number of all null columns
    print(add_df.shape[0] - add_df.dropna().shape[0])

    add_df = add_df.fillna(method='ffill')

    # add_df['CARDACCEPTORSTREET'].map(str) \
    #                                 + "," +
    #add_df['CARDACCEPTORCITY'].map(str) \
    # + ", " +
    add_df['CARDACCEPTORADDRESS'] = add_df['CARDACCEPTORSTATE'].map(str) \
                                + ", " + add_df['CARDACCEPTORCOUNTRY'].map(str)

    add_df = add_df.drop(['CARDACCEPTORSTATE', 'CARDACCEPTORCOUNTRY'],axis=1)

    addrs = add_df.drop_duplicates()

    return addrs

def geocode_one(addr):
    """
    Geocode just one address
    :param addr:
    :return:
    """
    gmaps = googlemaps.Client(key=definitions.GOOGLE_API_KEY)

    geocode_result = gmaps.geocode(addr)[0]

    lat = geocode_result['geometry']['location']['lat']
    lon = geocode_result['geometry']['location']['lng']

    return [lat,lon]

def geocode_all(addresses,i,step):
    """
    function to convert an address to latitude and longitude

    :param addresses: address string
    :return: latlon: latitude and longitude as [lat,long]
    """

#    geocoder = geopy.geocoders.GoogleV3(api_key=definitions.GOOGLE_API_KEY)

    res = geopandas.tools.geocode(addresses, provider='google',
                                  api_key = definitions.GOOGLE_API_KEY,
                                  timeout=10)

#    addresses['GEOCODE'] = addresses['CARDACCEPTORADDRESS'].apply(rate_limiter)

    fname = 'state_locs.csv'

    save_path = os.path.join(definitions.ROOT_DIR, 'data', fname)

    res.to_csv(save_path)

    return res