from tkinter import Canvas
from turtle import RawTurtle
from .base import Widget

class Turtle(Widget, RawTurtle):

    def __init__(
        self, 
        master, 
        width=100, 
        height=100, 
        grid=None, 
        align=None, 
        visible=True, 
        enabled=None):

        description = "[Turtle] object"

        tk = Canvas(master.tk)

        super(Turtle, self).__init__(master, tk, description, grid, align, visible, enabled, width, height)

        RawTurtle.__init__(self, tk)