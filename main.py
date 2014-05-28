from datetime import datetime

import requests


DATA_URL = "http://marsweather.ingenology.com/v1/latest/"


class MarsWeather(object):
    def __init__(self):
        super(MarsWeather, self).__init__()
        self.__data = None

    def _retrieve(self):
        response = requests.get(DATA_URL)
        try:
            self.__data = response.json()["report"]
        except:
            raise Exception("Data retrieval failed. Check your internet connection.")

    @property
    def _data(self):
        if self.__data is None:
            self._retrieve()

        return self.__data

    @property
    def terrestrial_date(self):
        st = self._data['terrestrial_date']
        return datetime.strptime(st, "%Y-%m-%d")

    @property
    def sol(self):
        return self._data['sol']

    @property
    def ls(self):
        return self._data['ls']

    @property
    def min_temp(self):
        return self._data['min_temp']

    @property
    def min_temp_fahrenheit(self):
        return self._data['min_temp_fahrenheit']

    @property
    def max_temp(self):
        return self._data['max_temp']

    @property
    def max_temp_fahrenheit(self):
        return self._data['max_temp_fahrenheit']

    @property
    def pressure(self):
        return self._data['pressure']

    @property
    def pressure_string(self):
        return self._data['pressure_string']

    @property
    def abs_humidity(self):
        return self._data['abs_humidity']

    @property
    def wind_speed(self):
        return self._data['wind_speed']

    @property
    def wind_direction(self):
        return self._data['wind_direction']

    @property
    def atmo_opacity(self):
        return self._data['atmo_opacity']

    @property
    def season(self):
        return self._data['season']

    @property
    def sunrise(self):
        st = self._data['sunrise']
        dt = datetime.strptime(st, "%Y-%m-%dT%H:%M:%SZ")
        return dt

    @property
    def sunset(self):
        st = self._data['sunset']
        dt = datetime.strptime(st, "%Y-%m-%dT%H:%M:%SZ")
        return dt


def format_label(label):
    label = label.replace("_", " ")
    return label.capitalize() + " : "


def main():
    obj = MarsWeather()
    labels = dir(obj)
    for label in labels:
        if not label.startswith('_'):
            print format_label(label), getattr(obj, label)


if __name__ == "__main__":
    main()