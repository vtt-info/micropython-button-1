from machine import Pin, Timer
from micropython import schedule


class Button:
    debounce_time_ms = 20

    def __init__(self, pin_num: int, up_state=0):
        self._callbacks = []
        self._pin = Pin(pin_num, Pin.IN)
        self._pin.irq(trigger=Pin.IRQ_FALLING, handler=self._on_press)
        self._debounce_timer = Timer(1)
        self._up_state = up_state

    def _on_press(self, pin):
        value = pin.value()
        if value == self._up_state:
            return

        self._value = value
        pin.irq(trigger=0)

        self._debounce_timer.init(
            period=Button.debounce_time_ms,
            mode=Timer.ONE_SHOT,
            callback=self._debounce
        )

    def _debounce(self, _):
        self._pin.irq(trigger=Pin.IRQ_FALLING, handler=self._on_press)
        if self._pin.value() == self._value:
            schedule(self._callback, None)

    def _callback(self, _):
        for callback in self._callbacks:
            callback()

    def register(self, callback):
        self._callbacks.append(callback)
