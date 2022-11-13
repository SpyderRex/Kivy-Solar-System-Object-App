from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
import requests

class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class MyFeatureSpinner(Spinner):
    values = ["Is a Planet?", "Moons", "Semimajor Axis", "Perihelion", "Aphelion", "Eccentricity", "Inclination", "Mass", "Volume", "Density", "Gravity", "Escape Velocity", "Mean Radius", "Equatorial Radius", "Polar Radius", "Flattening", "Sidereal Orbit", "Sidereal Rotation", "Around Planet", "Discovered By", "Discovery Date", "Alternative Name", "Axial Tilt", "Average Temperature", "Mean Anomaly", "Argument of Periapsis", "Longitude of Ascending Node", "Body Type"]
    values.sort()
    

class MyObjectSpinner(Spinner):
    url = "https://api.le-systeme-solaire.net/rest/bodies"
    response = requests.get(url)
    object_list = response.json()["bodies"]
    name_list = [sub['englishName'] for sub in object_list]
    name_list.sort()
    values = name_list
    
class MyBoxlayout(BoxLayout):
    def object_spinner_clicked(self, value):
        self.ids.object_label_id.text = value
        self.ids.feature_label_id.text = "Pick a feature"

    def feature_spinner_clicked(self, value):
        url = "https://api.le-systeme-solaire.net/rest/bodies"
        response = requests.get(url)
        self.ids.feature_label_id.text = value
        object_list = response.json()["bodies"]
        name_list = [sub['englishName'] for sub in object_list]
        if value == "Is a Planet?":
            self.ids.feature_label_id.text = value  + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["isPlanet"])
        elif value == "Moons":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["moons"])
        elif value == "Semimajor Axis":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["semimajorAxis"]) + " " + "km"
        elif value == "Perihelion":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["perihelion"]) + " " + "km"
        elif value == "Aphelion":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["aphelion"]) + " " + "km"
        elif value == "Eccentricity":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["eccentricity"])
        elif value == "Inclination":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["inclination"]) + "°"
        elif value == "Mass":
            if response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["mass"] is not None:
                self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["mass"]["massValue"]) + " " + "x" + " " + "10^" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["mass"]["massExponent"]) + " " + "kg"
            else:
                self.ids.feature_label_id.text = value + ":" + "\nNone"
        elif value == "Volume":
            if response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["vol"] is not None:
                self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["vol"]["volValue"]) + " " + "x" + " " + "10^" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["vol"]["volExponent"]) + " " + "kg^3"
            else:
                self.ids.feature_label_id.text = value + ":" + "\nNone"
        elif value == "Density":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["density"]) + " " + "g/cm^3"
        elif value == "Gravity":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["gravity"]) + " " + "m/s^2"
        elif value == "Escape Velocity":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["escape"]) + " " + "m/s"
        elif value == "Mean Radius":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["meanRadius"]) + " " + "km"
        elif value == "Equatorial Radius":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["equaRadius"]) + " " + "km"
        elif value == "Polar Radius":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["polarRadius"]) + " " + "km"
        elif value == "Flattening":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["flattening"])
        elif value == "Sidereal Orbit":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["sideralOrbit"]) + " " + "days"
        elif value == "Sidereal Rotation":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["sideralRotation"]) + " " + "hours"
        elif value == "Around Planet":
            if response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["aroundPlanet"] is not None:
                self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["aroundPlanet"]["planet"])
            else:
                self.ids.feature_label_id.text = value + ":" + "\nNone"
        elif value == "Discovered By":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["discoveredBy"])
        elif value == "Discovery Date":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["discoveryDate"])
        elif value == "Alternative Name":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["alternativeName"])
        elif value == "Axial Tilt":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["axialTilt"]) + "°"
        elif value == "Average Temperature":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["avgTemp"]) + " " + "K"
        elif value == "Mean Anomaly":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["mainAnomaly"]) + "°"
        elif value == "Argument of Periapsis":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["argPeriapsis"]) + "°"
        elif value == "Longitude of Ascending Node":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["longAscNode"]) + "°"
        elif value == "Body Type":
            self.ids.feature_label_id.text = value + ":" + "\n" + str(response.json()["bodies"][name_list.index(self.ids.object_label_id.text)]["bodyType"])
          
        

class SolarSystemApp(App):
    def build(self):
        return MyBoxlayout()

if __name__ == "__main__":
    SolarSystemApp().run()