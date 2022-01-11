from pyowm import OWM



def weather():
    owm = OWM('KEY')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Москва,Ru')
    w = observation.weather

    return w

print(weather())
