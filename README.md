# ha_zigbee2mqtt_networkmap
Custom Component for Homeassistant to show the [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) Networkmap with [viz.js](https://github.com/mdaines/viz.js/).

[Forum link with Screenshot](https://community.home-assistant.io/t/zigbee2mqtt-show-the-networkmap-in-hassio/89116)

![map|658x499](map.gif)

**Important:** you have to clear the browsercache after each update


**Instructions**
1. Download or clone [https://github.com/rgruebel/ha_zigbee2mqtt_networkmap](https://github.com/rgruebel/ha_zigbee2mqtt_networkmap)
2. Copy "custom_components/zigbee2mqtt_networkmap" and content to your "custom_components" folder.
3. Add the following to your configuration.yaml. It is possible to update the map directly via button. If you want to use this functionality you also have to activate the webhook component. Otherwise you have to use the service "zigbee2mqtt_networkmap.update"

        webhook:
        
        zigbee2mqtt_networkmap:
          #topic: your topic (optional, default zigbee2mqtt)
        panel_iframe:
          networkmap:
            title: 'Zigbee Map'
            url: '/local/community/zigbee2mqtt_networkmap/map.html'
            icon: 'mdi:graphql'
    You can set the graphviz engine via URL Parameter: 
    map.html?engine=circo (Default: circo, [Supported Engines](https://github.com/mdaines/viz.js/wiki/Supported-Graphviz-Features))  
    
4. Restart Homeassistant
5. Test if everything is working


