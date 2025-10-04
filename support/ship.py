from support.imageviewer import ImageViewer

from PIL import Image

HEIGHT = 5
WIDTH = 10

class ShipIMG(ImageViewer):
    def __init__(self, path, len, id=None, dir=0):
        super().__init__(path, id=id, zoom=False)
        self.drag_start = None
        self.start_offset = None
        self.x_offset = 2
        self.y_offset = 1
        self.dir = dir
        self.len = len
        self.styles.width, self.styles.height = WIDTH, self.len * HEIGHT
        if dir == 1:
            self.dir = 0
            self.rotate()

    def rotate(self):
        self.dir = (self.dir + 1) % 2
        self.change("assets/" +  str(self.len) + "-" + ("vertical" if self.dir == 0 else "horizontal") + ".png")
        if self.dir == 0:
            self.styles.width, self.styles.height = WIDTH, self.len * HEIGHT
            self.x_offset = 2
            self.y_offset = 1
        else:
            self.styles.width, self.styles.height = self.len * WIDTH, HEIGHT
            self.x_offset = 2
            self.y_offset = 1
        self.styles.refresh()
        self.refresh()
