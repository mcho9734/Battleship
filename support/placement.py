from textual import on

from textual.app import App, ComposeResult, Binding
from textual.widgets import Footer, Static
from textual.containers import Horizontal, Vertical, Grid
from textual.coordinate import Coordinate
from textual.events import MouseDown, MouseMove
from textual.screen import ModalScreen
from textual.widget import NoMatches

from support.ship import ShipIMG
from support.board import BattleshipBoard

class PlacementUI(App):
    BINDINGS = [
        Binding("e", "rotate", "Rotate held Ship Counter-Clockwise"),
        Binding("q", "rotate", "Rotate held Ship Clockwise"),
        Binding("enter", "confirm", "Confirm your Ship Placements", priority=1),
    ]

    DEFAULT_CSS = """
        Screen {
            layers: below middle above above2 above3 above4 above5;
        }
        #box {
            width: 100%;
            height: 100%;
        }
        #board {
            height: 100;
            width: 100;
        }
        BattleshipBoard {
            layer: middle;
        }
        #s1 {
            layer: above;
        }
        #s2 {
            layer: above2;
        }
        #s3 {
            layer: above3;
        }
        #s4 {
            layer: above4;
        }
        #s5 {
            layer: above5;
        }
        RichLog {
            height: 5%;
        }
    """

    def __init__(self):
        super().__init__()
        self.curr_widget = None

    def compose(self) -> ComposeResult:
        ship1 = ShipIMG("assets/2-vertical.png", 2, id="s1")
        ship2 = ShipIMG("assets/3-vertical.png", 3, id="s2")
        ship3 = ShipIMG("assets/3-vertical.png", 3, id="s3")
        ship4 = ShipIMG("assets/4-vertical.png", 4, id="s4")
        ship5 = ShipIMG("assets/5-vertical.png", 5, id="s5")
        ship1.styles.offset = (2, 1)
        ship2.styles.offset = (22, 1)
        ship3.styles.offset = (42, 1)
        ship4.styles.offset = (62, 1)
        ship5.styles.offset = (82, 1)
        vertical = Vertical()
        vertical.styles.width = "30%"
        yield Horizontal(*[vertical, Vertical(*[BattleshipBoard(cursor_background_priority="renderable", cell_padding=0, header_height=1, id="board", zebra_stripes=True, show_cursor=False), ship1, ship2, ship3, ship4, ship5]), vertical], id="box")
        yield Footer()    

    def on_mouse_down(self, event: MouseDown) -> None:
        widget, _ = self.screen.get_widget_at(*event.screen_offset)
        if not isinstance(widget, ShipIMG):
            return
        self.curr_widget = widget
        widget.drag_start = event.screen_offset
        widget.start_offset = widget.styles.offset

    def on_mouse_move(self, event: MouseMove) -> None:
        if self.curr_widget is not None:
            self.curr_widget.styles.offset = (int((event.screen_offset.x - self.curr_widget.drag_start.x + self.curr_widget.start_offset.x.value)/10)*10 + self.curr_widget.x_offset, int((event.screen_offset.y - self.curr_widget.drag_start.y + self.curr_widget.start_offset.y.value)/5)*5 + self.curr_widget.y_offset)

    def on_mouse_up(self) -> None:
        if self.curr_widget is not None:
            self.curr_widget.drag_start = None
            self.curr_widget.start_offset = None
            self.curr_widget = None

    def action_rotate(self):
        if self.curr_widget is not None:
            self.curr_widget.rotate()
    
    def action_confirm(self):
        offsets = dict()
        coords = set()
        ships = dict()
        for i in range(5):
            try:
                ship = self.query_one("#s" + str(i + 1))
            except NoMatches:
                return
            offsets["s" + str(i + 1)] = (ship.dir, ship.styles.offset)
            ships["s" + str(i + 1)] = set()
            x_offset = ship.styles.offset.x.value
            y_offset = ship.styles.offset.y.value
            curr_coord = Coordinate(int(y_offset / 5), int(x_offset / 10))
            if ship.dir == 0:
                for _ in range(ship.len):
                    if curr_coord.column > 7 or curr_coord.column < 0 or curr_coord.row < 0 or curr_coord.row > 7:
                        self.app.push_screen(InvalidPlacementScreen())
                        return
                    coords.add(curr_coord)
                    ships["s" + str(i + 1)].add(curr_coord)
                    curr_coord = Coordinate(curr_coord.row + 1, curr_coord.column)
            else:
                for _ in range(ship.len):
                    if curr_coord.column > 7 or curr_coord.column < 0 or curr_coord.row < 0 or curr_coord.row > 7:
                        self.app.push_screen(InvalidPlacementScreen())
                        return
                    coords.add(curr_coord)
                    ships["s" + str(i + 1)].add(curr_coord)
                    curr_coord = Coordinate(curr_coord.row, curr_coord.column + 1) 
        if len(coords) != 17:
            self.app.push_screen(InvalidPlacementScreen())
            return
            
        self.exit(result=(offsets, coords, ships))

app = PlacementUI()
if __name__ == "__main__":
    app.run()

class InvalidPlacementScreen(ModalScreen[None]):
    BINDINGS = [
        Binding("escape", "dismiss", priority=1),
    ]

    DEFAULT_CSS = """
    InvalidPlacementScreen {
        align: center middle;
        height: 100%;
        width: 100%;
    }
    #dialog {
        width: 80%;
        height: auto;
        border: thick $background 80%;
        background: $surface;
        margin-bottom: 0;
    }
    #warn {
        color: red;
        align: center middle;
        text-align: center
    }
    """

    def __init__(self):
        super().__init__()

    def compose (self) -> ComposeResult:
        yield Grid(Static("You did not provide a valid placement of your ships.\nPlease make sure all ships are on the board and not overlapping.\n(Press Escape to Exit this Screen)", id="warn"), id="dialog")

