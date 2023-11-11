import network

def do_connect(SSID, SSI_PASSWORD, sta_if):
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.connect(SSID, SSI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    return sta_if

