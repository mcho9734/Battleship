from textual import on

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label
from support.imageviewer import ImageViewer

class ModeUI(App):
    BINDINGS = [
    ]

    DEFAULT_CSS = """
        Static {
            content-align: center middle;
            height: 100;
        }
        Horizontal {
            height: 100;
            align: center middle;
        }
        Vertical {
            height: 100;
        }
        Button {
            width: 100;
        }
        ImageViewer {
            height: 30;
            width: 100%;
        }
    """

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Horizontal(*[Vertical(), Vertical(*[Label("Caltech CS1's Battleship", expand=True), ImageViewer("assets/logo.png", id="bleh"), Horizontal(*[Button("VS Easy Computer", id="ec"), Button ("VS Harder Computer", id="hc")])]), Vertical()])

    def on_button_pressed(self, event: Button.Pressed):
        self.exit(result=str(event.button.id))

app = ModeUI()
if __name__ == "__main__":
    app.run()
