input.onButtonPressed(Button.A, function () {
    _4digit = grove.createDisplay(DigitalPin.P0, DigitalPin.P1)
    _4digit.show(time)
    strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
    strip.showRainbow(1, 360)
})
let _4digit: grove.TM1637 = null
let strip: neopixel.Strip = null
let time = 0
time = 1
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Red))
strip.show()
strip.clear()
basic.showIcon(IconNames.No)
basic.pause(2000)
basic.clearScreen()
while (true) {
    basic.showNumber(time)
    time += 1
    if (time >= 5 && time <= 30) {
        music.play(music.stringPlayable("G F E E F G F E ", 340), music.PlaybackMode.LoopingInBackground)
        music.stopMelody(MelodyStopOptions.Background)
        strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
        strip.showRainbow(1, 360)
    }
}
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Green))
strip.show()
basic.showIcon(IconNames.Yes)
