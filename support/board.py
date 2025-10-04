from rich.text import Text
from rich.style import Style
from rich.padding import Padding

from textual.widgets import DataTable

ROWS = [[x + " "*9 for x in ("A","B","C","D","E","F","G","H")]]

for i in range(len(ROWS[0])):
    row = []
    for j in range(len(ROWS[0])):
        row.append(Padding(Text(""), (3, 3),  style=Style(color="green")))
    ROWS.append(row)

class BattleshipBoard(DataTable):
    DEFAULT_CSS = """
    BattleshipBoard {
        height: auto;
        width: auto;
    }
    BattleshipBoard > .datatable--header {
        border-title-align: center;
    }
    BattleshipBoard > .datatable--hover {
        background: $secondary 0%;
    }
    BattleshipBoard > .datatable--odd-row {
        border: orange;
    }
    """

    def on_data_table_cell_selected(self, msg):
        return
    
    def on_mount(self) -> None:
        self.add_columns(*ROWS[0])
        for number, row in enumerate(ROWS[1:], start=1):
            label = Padding(Text('0' + str(number - 1), style=Style(color="white")), (0, 0))
            self.add_row(*row, label=label, height=5)
