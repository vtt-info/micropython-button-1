from machine import Pin

from button import Button

boot_pin = Pin(0, Pin.IN)

boot_button = Button(boot_pin, release_value=1)


@boot_button.on_press
def boot_button_on_press():
    print('boot_button_on_press')


@boot_button.on_release
def boot_button_on_release():
    print('boot_button_on_release')


pin34 = Pin(34, Pin.IN)
pin35 = Pin(35, Pin.IN)
pin36 = Pin(36, Pin.IN)
pin39 = Pin(39, Pin.IN)

top_button = Button(pin34, release_value=1)
right_button = Button(pin35, release_value=1)
bottom_button = Button(pin36, release_value=1)
left_button = Button(pin39, release_value=1)


@top_button.on_press
def top_button_on_press():
    print('top_button_on_press')


@top_button.on_release
def top_button_on_release():
    print('top_button_on_release')


@right_button.on_press
def right_button_on_press():
    print('right_button_on_press')


@right_button.on_release
def right_button_on_release():
    print('right_button_on_release')


@bottom_button.on_press
def bottom_button_on_press():
    print('bottom_button_on_press')


@bottom_button.on_release
def bottom_button_on_release():
    print('bottom_button_on_release')


@left_button.on_press
def left_button_on_press():
    print('left_button_on_press')


@left_button.on_release
def left_button_on_release():
    print('left_button_on_release')
