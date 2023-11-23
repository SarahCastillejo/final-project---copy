def on_button_pressed_a():
    global _4digit, strip
    _4digit = grove.create_display(DigitalPin.P0, DigitalPin.P1)
    _4digit.show(time)
    strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
    strip.show_rainbow(1, 360)
input.on_button_pressed(Button.A, on_button_pressed_a)

_4digit: grove.TM1637 = None
strip: neopixel.Strip = None
time = 0
time = 1
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.RED))
strip.show()
strip.clear()
basic.show_icon(IconNames.NO)
basic.pause(2000)
basic.clear_screen()
while True:
    basic.show_number(time)
    time += 1
    if time >= 5 and time <= 30:
        music.play(music.string_playable("G F E E F G F E ", 340),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        music.stop_melody(MelodyStopOptions.BACKGROUND)
        strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
        strip.show_rainbow(1, 360)
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
strip.show()
basic.show_icon(IconNames.YES)