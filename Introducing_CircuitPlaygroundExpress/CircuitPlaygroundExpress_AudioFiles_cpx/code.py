# SPDX-FileCopyrightText: 2017 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.play_file("rimshot.wav")
    elif cpx.button_b:
        cpx.play_file("laugh.wav")
