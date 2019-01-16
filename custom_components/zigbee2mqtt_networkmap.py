import homeassistant.loader as loader
from datetime import datetime

DOMAIN = 'zigbee2mqtt_networkmap'

DEPENDENCIES = ['mqtt']

CONF_TOPIC = 'topic'
DEFAULT_TOPIC = 'zigbee2mqtt'


def setup(hass, config):
    """Set up the Hello MQTT component."""
    mqtt = hass.components.mqtt
    topic = config[DOMAIN].get(CONF_TOPIC, DEFAULT_TOPIC)
    entity_id = 'zigbee2mqtt_networkmap.map_last_update'

    # Listener to be called when we receive a message.
    def message_received(topic, payload, qos):
        """Handle new MQTT messages."""
        # Save Response as JS variable in source.js
        f = open(hass.config.path('www', 'zigbee2mqtt_networkmap', 'source.js'),"w")
        f.write("var graph = \'"+payload.replace('\n', ' ').replace('\r', '')+"\'")
        f.close()
        hass.states.set(entity_id, datetime.now())

    # Subscribe our listener to the networkmap topic.
    mqtt.subscribe(topic+'/bridge/networkmap/graphviz', message_received)

    # Set the initial state.
    hass.states.set(entity_id, None)

    # Service to publish a message on MQTT.
    def update_service(call):
        """Service to send a message."""
        mqtt.publish(topic+'/bridge/networkmap', 'graphviz')

    hass.services.register(DOMAIN, 'update', update_service)
    
    return True
