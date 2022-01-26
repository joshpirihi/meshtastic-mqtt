# meshtastic-mqtt
A python script to translate Meshtastic MQTT location messages into a format that Traccar can understand
Also publishes battery levels and environmental plugin temperatures and humidity readings to mqtt.

There's a few config definitions at the top of meshtastic-mqtt.py that you'll need to change for your MQTT server.

This doesn't implement the decryption required, you'll either need to disable encryption on your meshtastic nodes, or modify your meshtastic gateway node to send decrypted payloads to MQTT.  In Router.cpp, in Router::send move the MQTT fragment (including the #if defined bits) to just above the call to perhapsEncode().

There are some comments in meshtastic-mqtt.py that detail the tweaks needed to make this run under AppDaemon in Home Assistant.
