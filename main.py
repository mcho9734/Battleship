from support.placement import PlacementUI
from support.computer import ComputerGameUI
from support.mode import ModeUI
from textual.coordinate import Coordinate

from src.computer_placement import place_ships
from src.easy_computer import easy_computer
from src.harder_computer import harder_computer

app = ModeUI()
mode = app.run()

app = PlacementUI()

output = place_ships()

comp_offsets = dict()
comp_coords = set()
comp_ships = dict()

for i, ship in enumerate(reversed(output)):
    if ship[0][0] == ship[1][0]:
        dir = 0
    else:
        dir = 1
    comp_offsets["s" + str(i + 1)] = (dir, (ship[0][0] * 10 + 2, ship[0][1] * 5 + 1))
    comp_ships["s" + str(i + 1)] = set()
    for coord in ship:
        comp_coords.add(Coordinate(coord[1], coord[0]))
        comp_ships["s" + str(i + 1)].add(Coordinate(coord[1], coord[0]))


if mode == "ec":
    (player_offsets, player_coords, player_ships) = app.run()

    app = ComputerGameUI(player_offsets, player_coords, player_ships, comp_offsets, comp_coords, comp_ships, easy_computer)
    outcome = app.run()
    print(outcome)

if mode == "hc":
    (player_offsets, player_coords, player_ships) = app.run()

    app = ComputerGameUI(player_offsets, player_coords, player_ships, comp_offsets, comp_coords, comp_ships, harder_computer)
    outcome = app.run()
    print(outcome)
