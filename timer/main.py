from machine import Timer, Pin

led = Pin("LED", Pin.OUT)
temporizador = Timer()

def tempo(timer):
    global led
    led.toggle()
    print(f"LED: {led.value()}, execute toggle") 
    

temporizador.init(freq=1, mode=Timer.PERIODIC, callback=tempo)