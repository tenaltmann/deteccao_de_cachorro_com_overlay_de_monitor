import mss
import numpy as np


class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()