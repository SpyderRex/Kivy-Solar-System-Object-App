# Kivy-Solar-System-Object-App
See features for major objects in the solar system 

This Kivy app uses two spinners, one to list
more than 250 objects in the solar system, such 
as moons, planets, and asteroids; and another
to list almost 30 features of those bodies, such
as escape velocity, volume, mass, and which planet
it orbits, if any. It uses the Solar System OpenData
API (see https://api.le-systeme-solaire.net/en/).
I generated the APK on Colab and installed the
app on mobile. A wrinkle in the code, which I haven't
figured out how to get around, is that once one 
selects a body and then a feature, if one wishes 
to select the same feature for a different body,
one has to first select the new body, then select 
a different feature, and then go back to the 
initial feature. 
