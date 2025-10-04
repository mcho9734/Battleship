from textual import on
from rich.padding import Padding
from rich.text import Text
from rich.style import Style

from textual.app import App, ComposeResult, Binding
from textual.widgets import Static, Label
from textual.containers import Horizontal, Vertical, Container, Grid
from textual.coordinate import Coordinate
from textual.events import MouseDown
from textual.screen import ModalScreen

from support.ship import ShipIMG
from support.board import BattleshipBoard

from src.shot import Shot

class ComputerGameUI(App):
    BINDINGS = [
    ]

    DEFAULT_CSS = """
        Screen {
            layers: below1 below2 below3 below4 below5 middle above1 above2 above3 above4 above5 top eabove1 eabove2 eabove3 eabove4 eabove5;
        }
        #p_box {
            layer: middle;
            width: 100%;
            height: auto;
        }
        #p_board {
            layer: middle;
            width: 83;
        }
        #p_s1 {
            layer: above1;
        }
        #p_s2 {
            layer: above2;
        }
        #p_s3 {
            layer: above3;
        }
        #p_s4 {
            layer: above4;
        }
        #p_s5 {
            layer: above5;
        }
        #p_es1 {
            layer: below1;
        }
        #p_es2 {
            layer: below2;
        }
        #p_es3 {
            layer: below3;
        }
        #p_es4 {
            layer: below4;
        }
        #p_es5 {
            layer: below5;
        }
        RichLog {
            height: 5%;
        }
        Vertical, Container {
            layer: middle;
            height: auto;
        }
        #p_enemyboard {
            layer: top;
        }
        .hit-square {
            layer: top;
            visibility: hidden;
            background: red;
            color: red;
            width: 10;
            height: 5;
        }
    """

    def __init__(self, p_offsets, p_coords, p_ships, comp_offsets, comp_coords, comp_ships, bot):
        super().__init__()
        self.p_offsets = p_offsets
        self.p_coords = p_coords
        self.p_ships = p_ships
        self.comp_offsets = comp_offsets
        self.comp_coords = comp_coords
        self.comp_ships = comp_ships
        self.p_shots = []
        self.comp_shots = []
        def bot_wrapper(shots):
            result = bot(shots)
            assert result not in [x[0] for x in shots] 
            return result
        self.bot = bot_wrapper

    def compose(self) -> ComposeResult:
        p_ship1 = ShipIMG("assets/2-vertical.png", 2, id="p_s1", dir=self.p_offsets["s1"][0])
        p_ship2 = ShipIMG("assets/3-vertical.png", 3, id="p_s2", dir=self.p_offsets["s2"][0])
        p_ship3 = ShipIMG("assets/3-vertical.png", 3, id="p_s3", dir=self.p_offsets["s3"][0])
        p_ship4 = ShipIMG("assets/4-vertical.png", 4, id="p_s4", dir=self.p_offsets["s4"][0])
        p_ship5 = ShipIMG("assets/5-vertical.png", 5, id="p_s5", dir=self.p_offsets["s5"][0])
        p_ship5_hits = []
        for i, (x, y) in enumerate(list(self.p_coords)):
            p_ship5_hits.append(Static("", classes="hit-square", id="p_hit_" + str(x) + "_" + str(y)))
            p_ship5_hits[-1].styles.offset = (2 + y*10, -(i * 5) + x * 5 + 1)
        p_ship1.styles.offset = self.p_offsets["s1"][1]
        p_ship2.styles.offset = self.p_offsets["s2"][1]
        p_ship3.styles.offset = self.p_offsets["s3"][1]
        p_ship4.styles.offset = self.p_offsets["s4"][1]
        p_ship5.styles.offset = self.p_offsets["s5"][1]
        p_eship1 = ShipIMG("assets/2-vertical-op.png", 2, id="p_es1", dir=self.comp_offsets["s1"][0])
        p_eship2 = ShipIMG("assets/3-vertical-op.png", 3, id="p_es2", dir=self.comp_offsets["s2"][0])
        p_eship3 = ShipIMG("assets/3-vertical-op.png", 3, id="p_es3", dir=self.comp_offsets["s3"][0])
        p_eship4 = ShipIMG("assets/4-vertical.png", 4, id="p_es4", dir=self.comp_offsets["s4"][0])
        p_eship5 = ShipIMG("assets/5-vertical.png", 5, id="p_es5", dir=self.comp_offsets["s5"][0])
        p_eship1.styles.offset = self.comp_offsets["s1"][1]
        p_eship2.styles.offset = self.comp_offsets["s2"][1]
        p_eship3.styles.offset = self.comp_offsets["s3"][1]
        p_eship4.styles.offset = self.comp_offsets["s4"][1]
        p_eship5.styles.offset = self.comp_offsets["s5"][1]
        vertical = Vertical()
        vertical.styles.width = "5%"
        yield Horizontal(*[vertical, Vertical(*([BattleshipBoard(cursor_background_priority="renderable", cell_padding=0, header_height=1, id="p_board", zebra_stripes=True, show_cursor=False), p_ship1, p_ship2, p_ship3, p_ship4, p_ship5] + p_ship5_hits)), vertical, Vertical(*[BattleshipBoard(cursor_background_priority="renderable", cell_padding=0, header_height=1, zebra_stripes=True, show_cursor=False, id="p_enemyboard"), p_eship1, p_eship2, p_eship3, p_eship4, p_eship5]), vertical], id="p_box")

    def on_mouse_down(self, event: MouseDown):
        def check_ship_sink(shots, enemy_ships):
            for ship in enemy_ships:
                ship_coords = enemy_ships[ship]
                if ship_coords - set([x[0] for x in shots]) == set():
                    return ship
            return None

        if self.app.get_widget_at(event.screen_offset.x, event.screen_offset.y)[0].id != "p_enemyboard":
            return
        x_offset = event.offset.x
        y_offset = event.offset.y
        coord = Coordinate(int((y_offset - 1) / 5), int((x_offset - 3) / 10))
        if coord in self.comp_coords:
            self.p_shots.append((coord, Shot.HIT))
            self.query_one("#p_enemyboard").update_cell_at(coord, Padding(Text(""), (6, 5),  style=Style(color="red", bgcolor="red")))
            result = check_ship_sink(self.p_shots, self.comp_ships)
            if result is not None:
                self.query_one("#p_e" + result).styles.layer = "eabove" + result.split("s")[1]
                del self.comp_ships[result]
            if len(self.comp_ships) == 0:
                self.exit(result="The Player Won!")
            return
        self.p_shots.append((coord, Shot.MISS))
        self.query_one("#p_enemyboard").update_cell_at(coord, Padding(Text(""), (6, 5),  style=Style(color="white", bgcolor="white")))
        coord = Coordinate(*self.bot(self.comp_shots))
        while coord in self.p_coords:
            self.comp_shots.append((coord, Shot.HIT))
            self.query_one("#p_board").update_cell_at(coord, Label(Text(""), classes="hit-square"))
            self.query_one("#p_hit_" + str(coord[0]) + "_" + str(coord[1])).styles.visibility = "visible"
            ship = check_ship_sink(self.comp_shots, self.p_ships)
            if ship is not None:
                sunk_coords = self.p_ships[ship]
                for coord in sunk_coords:
                    index = [x[0] for x in self.comp_shots].index(coord)
                    self.comp_shots[index] = (self.comp_shots[index][0], Shot.SUNK)
                del self.p_ships[ship]
                if len(self.p_ships) == 0:
                    self.exit(result="The Computer Won!")
                    break
            coord = Coordinate(*self.bot(self.comp_shots))
        self.query_one("#p_board").update_cell_at(coord, Padding(Text(""), (6, 5),  style=Style(color="white", bgcolor="white")))
        self.comp_shots.append((coord, Shot.MISS))
        
