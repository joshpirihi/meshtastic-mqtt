# Note: you shouldn't need to run this script manually.
# It is run implicitly by the pip3 install command.
"""setup for package"""

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="meshtastic_mqtt",
    version="1.0.1",
    description="A python script to translate Meshtastic MQTT location messages into a format that Traccar can understand.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshpirihi/meshtastic-mqtt",
    author="joshpirihi",
    #author_email="tbd",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    #include_package_data=True,
    install_requires=["protobuf>=3.13.0", "pypubsub>=4.0.3", "requests", "paho-mqtt"],
    python_requires='>=3.6',
    packages=["meshtastic_mqtt"],
    entry_points={
        "console_scripts": [
            "meshtastic-mqtt = meshtastic_mqtt.meshtastic_mqtt:main",
        ]
    },
)
