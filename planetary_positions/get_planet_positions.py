from astroquery.jplhorizons import Horizons
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

for planet in planets:
    print "\n",get_planetary_positions(planet)

for planet in minor_planets:
    print "\n",get_planetary_positions(planet,"smallbody")

# Future features
#   Pretty print/file output
#   Create map/diagram
#   Incorporate scaling? (possibly seperate program)