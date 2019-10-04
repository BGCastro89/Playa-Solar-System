from get_planet_positions import get_planetary_positions, PLANETS
from plot_planet_positions import generate_plot
import numpy as np

def format_planets(planets_data):
    '''
    Takes planet data and returns it formatted for... ?
    '''
    pass

def get_all_planet_pos():
    planet_data = []

    for planet in PLANETS:
        positions_table = get_planetary_positions(planet)
        data = np.array(positions_table)
        planet_data.append(data[0]) # pos of each planet at time 0
    return planet_data


def get_coords():
    '''
    gets planet positions for each solar system object
    '''
    planet_data = get_all_planet_pos()
    planet_data_reduced = [(pos[4], pos[2]) for pos in planet_data]
    theta = [rad[1] for rad in planet_data_reduced]
    r = [ang[0] for ang in planet_data_reduced]

    return (r, theta)

if __name__ == "__main__":
    r, theta = get_coords()
    generate_plot(r, theta)