# Brian Castro 2019

from astroquery.jplhorizons import Horizons
import numpy as np

# AstroQuery library info
# github: https://github.com/astropy/astroquery
# docs: https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html

epochs = {'start':'2020-08-30', 'stop':'2020-09-07','step':'1d'}
location = '@sun' #center of the sun

# Each planet can be referred to by System Gravitational Barycenter or planetary center, number specifies planetary center
planets = [
    '199', # Mercury
    '299', # Venus
    '399', # Earth
    '499', # Mars
    '599', # Jupiter
    '699', # Saturn
    '799', # Uranus
    '899', # Neptune
    '999', # Pluto (like it or not, a planet according to JPL HORIZONS)
]

minor_planets = [
    'Ceres',
]

def get_planetary_positions(target,type='majorbody'):
    planet_pos_data = Horizons(id=target, id_type=type, location=location, epochs=epochs)
    eph = planet_pos_data.ephemerides()
    eph['r'].convert_unit_to('km')
    return eph['targetname','datetime_str','EclLon','EclLat','r']

# for planet in planets:
#     print("\n",get_planetary_positions(planet))

# for planet in minor_planets:
#     print("\n",get_planetary_positions(planet,"smallbody"))

def format_planets():
    planetary_coords = []

    for planet in planets:
        positions_table = get_planetary_positions(planet)
        # print(type(planet_pos))
        # print(planet_pos.colnames)
        # print(planet_pos.columns)
        # print(planet_pos[0])
        data = np.array(positions_table)
        # print data

        planetary_coords.append(data[0]) # pos of each planet at time 0

    return planetary_coords


    # for planet in minor_planets:
    #     planet_pos = get_planetary_positions(planet,"smallbody")

def get_coords():
    data = format_planets() # call each separetly?
    planet_pos_reduced = [(pos[4], pos[2]) for pos in data]
    theta = [rad[1] for rad in planet_pos_reduced]
    r = [ang[0] for ang in planet_pos_reduced]

    return (r, theta)

if __name__ == "__main__":
    data = format_planets() # call each separetly?
    r, theta = data[4], data[2]

# Future features
#   Pretty print/file output
#   Create map/diagram
#   Incorporate scaling? (possibly seperate program)