# meshtastic-mqtt
A python script to translate Meshtastic MQTT location messages into a plain format that other systems can easily understand.  Currently takes position data and submits it to a Traccar instance, also publishes battery levels and environmental plugin temperatures and humidity readings to mqtt as raw values.

The latest build of Meshtastic-device has support for publishing decrypted payloads, which you'll need in order to use this script.

There's a few config definitions at the top of meshtastic-mqtt.py that you'll need to change for your MQTT server.



There are some comments in meshtastic-mqtt.py that detail the tweaks needed to make this run under AppDaemon in Home Assistant.
