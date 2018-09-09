class Camera:
    def __init__(self, producer="Canon", memory=1028, zoom_ratio=1.0):
        self.producer = producer
        self.memory = memory
        self.zoom_ratio = zoom_ratio

    def __str__(self):
        return "Producer: " + self.producer + ", Memory: " + str(self.memory) + ", Zoom ratio: " + str(self.zoom_ratio)
