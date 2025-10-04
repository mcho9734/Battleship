import math

from PIL import Image
from textual import events
from textual.app import RenderResult
from textual.widget import Widget

from support.image import ImageView

"""
Original code written by Adam Viola and distributed at the following link:

https://github.com/adamviola/textual-imageview/tree/main/textual_imageview

Course staff have adapted it to fit the needs of the assignment.
"""

class ImageViewer(Widget):
    DEFAULT_CSS = """
    ImageViewer{
        min-height: 1;
        min-width: 1;
    }
    """

    def __init__(self, path, id=None, zoom=True):
        super().__init__(id=id)
        self.zoom = zoom

        self.image = ImageView(Image.open(path))
        self.mouse_down = False

    def on_show(self):
        w, h = self.size.width, self.size.height
        img_w, img_h = self.image.size

        # Compute zoom such that image fits in container
        if self.zoom:
            zoom_w = math.log(max(w, 1) / img_w, self.image.ZOOM_RATE)
            zoom_h = math.log((max(h, 1) * 2) / img_h, self.image.ZOOM_RATE)
            zoom = max(0, math.ceil(max(zoom_w, zoom_h)))
            self.image.set_zoom(zoom)

            # Position image in center of container
            img_w, img_h = self.image.zoomed_size
        self.image.origin_position = (-round((w - img_w) / 2), -round(h - img_h / 2))
        self.image.set_container_size(w, h, maintain_center=False)

        self.refresh()

    def on_resize(self, event: events.Resize):
        self.image.set_container_size(event.size.width, event.size.height)
        self.refresh()

    def render(self) -> RenderResult:
        return self.image
    
    def change(self, path):
        self.image = ImageView(Image.open(path))
        self.image.set_container_size(*self.container_size)
        self.on_show()
