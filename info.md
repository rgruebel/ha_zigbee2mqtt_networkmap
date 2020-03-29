# ha_zigbee2mqtt_networkmap
Custom Component for Homeassistant to show the [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) Networkmap with [viz.js](https://github.com/mdaines/viz.js/).

[Forum link with Screenshot](https://community.home-assistant.io/t/zigbee2mqtt-show-the-networkmap-in-hassio/89116)

**Important:** you have to clear the browsercache after each update


**Instructions**
1. Add the following to your configuration.yaml. It is possible to update the map directly via button. If you want to use this functionality you also have to activate the webhook component. Otherwise you have to use the service "zigbee2mqtt_networkmap.update"

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
    
2. Restart Homeassistant
3. Test if everything is working


