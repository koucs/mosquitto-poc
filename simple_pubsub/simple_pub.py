import paho.mqtt.publish as publish

publish.single("test/python", "hello from python", hostname="localhost")