# meshtastic-mqtt-owntracks
A python script to translate Meshtastic MQTT location messages into a format that Owntracks can understand

There's a few config definitions at the top of meshtastic-mqtt.py that you'll need to change for your MQTT server.

This doesn't implement the decryption required, until that is working you'll need to modify your meshtastic gateway node to send decrypted payloads to MQTT.  In Router.cpp, in Router::send move the MQTT fragment (including the #if defined bits) to just above the call to perhapsEncode().

This is a nasty bodge but it does work!
