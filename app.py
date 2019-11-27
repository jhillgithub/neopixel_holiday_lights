from flask import Flask, render_template, request

import board
import neopixel

pixel_pin = board.D18
num_pixels = 50
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin,
    num_pixels,
    brightness=0.2,
    auto_write=False,
    pixel_order=ORDER
)

def all_color(pixels, color):
    """Sets all of the pixels to a single color.

    The color is specified by a RBG tuple from 0 to 255
    Example: color = (32, 0, 0) # Red
    """
    pixels.fill(color)
    pixels.show()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/set/all/<color>")
def set_all(color):
    all_color(pixels, color)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)