import mypackage.mymodule

today = mypackage.mymodule.get_weather()
print(today)

from mypackage import mymodule
today = mymodule.get_weather()
print(today)
