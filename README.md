# Note: only functions with old v1.2 meshtastic device firmware
The newer version 2 of the device firmware supports JSON MQTT packets natively, so there is no need for this script.


# meshtastic-mqtt
A python script to translate Meshtastic MQTT location messages into a plain format that other systems can easily understand.  Currently takes position data and submits it to a Traccar instance, also publishes user info packets, battery levels and environmental plugin temperatures and humidity readings to mqtt as raw values.

The latest build of Meshtastic-device has support for publishing decrypted payloads, which you'll need in order to use this script.

There's a few config definitions at the top of meshtastic-mqtt.py that you'll need to change for your MQTT server.

# Installation

Clone the repo
`git clone https://github.com/joshpirihi/meshtastic-mqtt`
`cd meshtastic-mqtt`

Edit the main script and enter your broker and/or traccar host details
`nano meshtastic_mqtt/meshtastic_mqtt.py`

Install to your systen with pip
`pip install .`

Run
`meshtastic-mqtt`

There are some comments in meshtastic-mqtt.py that detail the tweaks needed to make this run under AppDaemon in Home Assistant.
