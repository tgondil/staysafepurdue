import React, { useState, useEffect, useRef } from 'react';
import { Map, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import 'ol/ol.css';

function MapComponent() {
    

    useEffect(() => {
        const osmLayer = new TileLayer({
            preload: Infinity,
            source: new OSM(),
        })

        const map = new Map({
            target: "map",
            layers: [osmLayer],
            view: new View({
                projection: 'EPSG:4326',
                center: [-86.92, 40.4290],
                zoom: 17,
              }),
          });
      return () => map.setTarget(null)
    }, []);

    return (
      <div style={{height:'100vh',width:'100%'}} id="map" className="map-container" />
    );
}

export default MapComponent;