<template>
  <div>
    <Header @display_view="getData" /> 
    <div class = "greener">ID: {{did}}</div><div v-bind:class="{redder: isRestricted, greener: !isRestricted}"><u>{{restricted}}</u></div><br>
    <div class="main-div">
      <div id="map" class="map-div">
        <!-- map will be injected here :) -->
      </div>
      <div id="mymodal" v-bind:class="{ visible: !isVisible }">
        <h3>
          <div style="color: white; ">Fleet ID:</div>
          <input v-model="fleet_id" /><br />
          <div style="color: white; ">Object1 ID:</div>
          <input v-model="drone1" /><br />
          <div style="color: white; ">Extra for Fleetmate:</div>
          <div style="color: skyblue; ">{{ drone2 }}</div>
        </h3>
        <button class="btn btn-primary" @click="sendDataFleet()" style="margin-left:45%">OK</button>
      </div>
      <div class="info-div">
        <div class="my-obj-div">
          <a href="#" id="toggle" @click="toggle_mode"> {{ mode }} </a>
          <label class="label-heading">Your data</label>
          <div class="my-info-card card">
            <!-- oops! same code repeated, why dont you use a function ? -->
            <!-- yeah i'm lazy, Sorry! "dont argue just modify"-->
            <!--  make a list and iterate -->
            <p>
              <label class="label-inside">LAT {{ user.latitude }}</label>
            </p>
            <p>
              <label class="label-inside">LON {{ user.longitude }}</label>
            </p>
            <p>
              <label class="label-inside">ALT {{ user.altitude }}</label>
            </p>
            <p>
              <label class="label-inside">TEMP {{ user.temperature }}</label>
            </p>
            <p>
              <label class="label-inside">ATM {{ myFlyingObject.pressure }}</label>
            </p>
          </div>
        </div>
        <div class="other-obj-div">
          <label class="label-heading">Nearby data</label>
          <div class="other-info-card card" v-bind:key="user._id" v-for="user in allUsersData">
            <p>
              <label class="label-inside">LAT {{ user.latitude }}</label>
            </p>
            <p>
              <label class="label-inside">LON {{ user.longitude }}</label>
            </p>
            <p>
              <label class="label-inside">ALT {{ user.altitude }}</label>
            </p>
            <p>
              <label class="label-inside">TEMP {{ user.temperature }}</label>
            </p>
            <p>
              <label class="label-inside">ATM 1</label>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import axios from "axios";
import mapboxgl from "mapbox-gl/dist/mapbox-gl.js";

import Header from "./Header";

import redDrone from "../assets/drones/redDrone.png";
import blackDrone from "../assets/drones/blackDrone.png";
import blueDrone from "../assets/drones/blueDrone.png";
import yellowDrone from "../assets/drones/yellowDrone.png";
import greenDrone from "../assets/drones/greenDrone.png";
import whiteDrone from "../assets/drones/whiteDrone.png";

mapboxgl.accessToken =
  "pk.eyJ1Ijoic2F1cmF2bmlyYXVsYSIsImEiOiJja2F5eHd2Y3AwOGMzMnNxYno3M2xmMXdkIn0.QeVxe4rfaHG4KsgQ7FbZqA";

var map = null;
var initSocket = null;

export default {
  name: "Map",

  components: {
    Header,
  },

  data() {
    return {
      baseUrl: "http://68.183.89.213",
      wsBaseUrl: "ws://68.183.89.213/ws",

      userLocation: [27.70523193557546, 85.31165898693936],
      allUsers: {}, // Nearby users

      // allUsersList: [],
      user: {},
      allUsersData: {},

      mapStyle: "mapbox://styles/mapbox/streets-v11",
      // center: [this.myFlyingObject.longitude, this.myFlyingObject.latitude],  // look at mounted
      zoom: 14, // mounted
      maxZoom: 19, // mounted
      offset: 0.01, // mounted  1 long ~= 110km
      howMuchToMove: 0.0001,
      isLocationAllowed: true,
      droneColors: [
        // at returnFeatures
        "match",
        ["get", "eachColor"],
        "White",
        "whiteDrone",
        "Black",
        "blackDrone",
        "Blue",
        "blueDrone",
        "Green",
        "greenDrone",
        "Red",
        "redDrone",
        "Yellow",
        "yellowDrone",
        "#ccc", // but why ? > for declaring the type
      ],
      droneSize: ["match", ["get", "eachSize"], "others", 0.03, "mine", 0.05, 0], // at returnFeatures
      mode: "Mono Mode",
      isVisible: false,
      fleet_id: "",
      drone1: "",
      drone2: "",
      mono_mode: true,
      restricted: "Safe Zone",
      isRestricted: false,
      did: ""
    };
  },

  methods: {
    afterGettingId(id) {
      // is the main function of websocket
      console.log(id);
      this.did = id;

      setTimeout(() => {
        // idk why bt i think it takes time to get id so
        initSocket = new WebSocket(`${this.wsBaseUrl}/connection/${id}/`);

        initSocket.onopen = () => {
          console.log("Connection Successful!");

          this.sendData(initSocket);
        };

        initSocket.onmessage = (e) => {
          this.allUsers = JSON.parse(e.data);

          // this.allUsersList = this.allUsers['user_arr']

          if (this.allUsers["user_arr"].length > 1) {
            // console.log("Length longer than 1");

            this.afterReceivingUsers(this.allUsers["user_arr"]);
          }
        };
      }, 1000);
    },

    afterReceivingUsers(users) {
      var dataSocket = new WebSocket(`${this.wsBaseUrl}/data/${this.id}/`);

      dataSocket.onopen = () => {
        console.log("data Socket opened");
      };

      dataSocket.onmessage = (e) => {
        this.sendData(dataSocket);
        let data = JSON.parse(e.data);
        this.user = data;
        // console.log("own-data = ", data);
      };

      this.getOthersData(users);
    },

    getOthersData(users) {
      window.setInterval(() => {
        // resetting data to start fresh in every 10 sec
        this.allUsersData = {}; // dont do this and we dont need this on bots
      }, 10000);

      users.forEach((user) => {
        if (user !== this.id) {
           new WebSocket(`${this.wsBaseUrl}/data/${user}/`).onmessage = (e) => {
            let data = JSON.parse(e.data);

            if (data.type == "messenger") {
              this.allUsersData[user] = data;
            }

            // console.log("Received data = ", data);
          };
        }
      });
    },

    sendData(socket) {
      let obj = {
        status: 200,
        _id: this.id,
        longitude: this.userLocation[1],
        latitude: this.userLocation[0],
        temperature: 20,
        altitude: 100,
        obstruction: 123,
      };
      socket.send(JSON.stringify(obj));
    },

    // getUserLocation() {
    //   if (!navigator.geolocation) {
    //     alert("Geolocation is not supported in your browser");
    //   } else {
    //     navigator.geolocation.getCurrentPosition(this.gotPosition, this.gotError);
    //   }
    // },

    // gotPosition(pos) {
    //   this.isLocationAllowed = true;
    //   this.userLocation = [pos.coords.latitude, pos.coords.longitude];
    // },

    // gotError(error) {
    //   switch (error.code) {
    //     case error.PERMISSION_DENIED:
    //       this.isLocationAllowed = false;
    //       // console.log("Please Allow location");
    //       break;
    //     case error.POSITION_UNAVAILABLE:
    //       console.log("Location information is unavailable.");
    //       break;
    //     case error.TIMEOUT:
    //       console.log("request timed out.");
    //       break;
    //     case error.UNKNOWN_ERROR:
    //       console.log("An unknown error occurred.");
    //       break;
    //     default:
    //       console.log("Error occured");
    //   }
    // },

    //////////////////////  MAP ////////////////////

    MapMain() {
      map.on("load", () => {
        // lines layer

        map.addSource("lines", {
          type: "geojson",
          data: {
            type: "FeatureCollection",
            features: [],
          },
        });

        map.addLayer({
          id: "lines",
          type: "line",
          source: "lines",
          layout: {
            "line-join": "round",
            "line-cap": "round",
          },
          paint: {
            "line-color": "#9400D3",
            "line-width": 3,
          },
        });
        // drones layer

        map.addSource("drones", {
          type: "geojson",
          data: {
            type: "FeatureCollection",
            features: [],
            // this.returnDroneFeatures(this.allUsersData, this.user),
          },
        });

        map.addLayer({
          id: "drones",
          type: "symbol",
          source: "drones",
          layout: {
            "icon-image": this.droneColors,
            "icon-size": this.droneSize,
            "icon-allow-overlap": true,
          },
        });

        this.windowInterval = window.setInterval(() => {
          // Why didn't i use flyto to make our drone always be on center of boundary ?
          //because youre a box of shit ;>
          // console.log("up");
          this.setBoundary(this.userLocation);
          this.updateLine();
          this.updateMapData();
        }, 1000); // smaller than this doesnot make sense

        // restricted ares layer

        map.addSource("resAreas", {
          type: "geojson",
          data: {
            type: "FeatureCollection",
            features: this.returnRestrictedAreasFeatures(this.restrictedAreas),
          },
        });
        map.addLayer({
          id: "resArea",
          type: "fill",
          source: "resAreas",
          layout: {},
          paint: {
            "fill-color": "#ff5500",
            "fill-opacity": 0.8,
          },
        });
      });
    },


    restricted_checker(){
      console.log("reached here")
      if (this.userLocation[1] > 85.31388882613281 && this.userLocation[1] < 85.31667699189056 && this.userLocation[0] > 27.704905195253197 &&  this.userLocation[0] < 27.707164680527804){
        console.log("also here")
        this.restricted = "Restricted Zone"
        this.isRestricted = !this.isRestricted
      }
      else{
        this.restricted = "Safe Zone"
        this.isRestricted = !this.isRestricted
      }
    },

    updateMapData() {
      let features = this.returnDroneFeatures(this.allUsersData, this.user);

      map.getSource("drones").setData({
        type: "FeatureCollection",
        features,
      });
    },

    updateLine() {
      let features = this.returnLineFeatures(this.allUsersData);
      map.getSource("lines").setData({
        type: "FeatureCollection",
        features,
      });
    },

    onKeyDown() {
      window.addEventListener("keydown", (e) => {
        // if (!this.isLocationAllowed) {
        switch (e.keyCode) {
          case 38: // up
            this.userLocation[0] += this.howMuchToMove;
            break;

          case 40: // down
            this.userLocation[0] -= this.howMuchToMove;
            break;

          case 37: //left
            this.userLocation[1] -= this.howMuchToMove;
            break;

          case 39: //right
            this.userLocation[1] += this.howMuchToMove;
        }
        this.updateMapData();
        this.updateLine();

        this.restricted_checker();
        // }
      });
    },

    // when mouse enter event is called

    onMouseEnter() {
      var popup = new mapboxgl.Popup({
        closeButton: false,
        closeOnClick: true,
      });

      var mouseEnter = (enterOn) => {
        map.on("mouseenter", enterOn, function(e) {
          // Change the cursor style as a UI indicator.
          // map.getCanvas().style.cursor = "pointer";    // really ? aren't u kidding ?

          var coordinates = [];

          if (enterOn == "drones") {
            // ohh not again "extra code for handling two types of coords"
            coordinates = e.features[0].geometry.coordinates.slice();
          } else if (enterOn == "resArea") {
            let coordsList = e.features[0].geometry.coordinates[0];

            // to put popup on center of resarea "just ignore"

            let getLong = (coordsList[0][0] + coordsList[2][0]) / 2;
            let getLat = (coordsList[0][1] + coordsList[2][1]) / 2;

            coordinates = [getLong, getLat];
          }

          let description = e.features[0].properties.description;

          // Ensure that if the map is zoomed out such that multiple
          // copies of the feature are visible, the popup appears
          // over the copy being pointed to.
          while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
          }

          // Populate the popup and set its coordinates
          // based on the feature found.
          popup
            .setLngLat(coordinates)
            .setHTML(description)
            .addTo(map);
        });
      };

      mouseEnter("drones");
      mouseEnter("resArea");
    },

    // returns features according given allOtherFlyingObjects and myFlyingObjects

    returnDroneFeatures(objs, myobj) {
      var features = [];
      // other objects feature
      for (var obj in objs) {
        features.push({
          type: "Feature",
          properties: {
            eachColor: this.returnColor(objs[obj].altitude),
            eachSize: "others",
            description: this.returnDroneDescription(objs[obj]),
          },
          geometry: {
            type: "Point",
            coordinates: [objs[obj].longitude, objs[obj].latitude],
          },
        });
      }

      // my obj feature

      features.push({
        type: "Feature",
        properties: {
          eachColor: this.returnColor(myobj.altitude),
          eachSize: "mine",
          description: this.returnDroneDescription(myobj),
        },
        geometry: {
          type: "Point",
          coordinates: [this.userLocation[1], this.userLocation[0]],
        },
      });

      return features;
    },

    returnLineFeatures(otherUsers) {
      let features = [];

      for (var each in otherUsers) {
        features.push({
          type: "Feature",
          geometry: {
            type: "LineString",
            coordinates: [
              [this.userLocation[1], this.userLocation[0]],
              [otherUsers[each].longitude, otherUsers[each].latitude],
            ],
          },
        });
      }

      return features;
    },

    returnRestrictedAreasFeatures(areas) {
      var features = [];

      areas.forEach((area) => {
        features.push({
          type: "Feature",
          properties: {
            description: this.returnRestrictedAreasDescription(area),
          },
          geometry: {
            type: "Polygon",
            coordinates: [area.coordinates],
          },
        });
      });

      return features;
    },

    setBoundary(userLocation) {
      // boundary of map according to my drone center

      this.bounds = [
        [userLocation[1] - this.offset, userLocation[0] - this.offset], // [west, south]
        [userLocation[1] + this.offset, userLocation[0] + this.offset], // [east, north]
      ];

      // this should be called every time socket sends data
      map.setMaxBounds(this.bounds); // just setting the boundaries (:
    },

    // returns color according to altitude

    returnColor(altitude) {
      if (altitude < 0) return "Black";
      else if (altitude >= 0 && altitude < 100) return "Blue";
      else if (altitude >= 100 && altitude < 200) return "Green";
      else if (altitude >= 200 && altitude < 300) return "Yellow";
      else return "Red";
    },

    // popUp message on hover

    returnDroneDescription(obj) {
      return `
              <p>
                <strong>LAT</strong> ${obj.latitude}
              </p>
              <p>
                <strong>LON</strong> ${obj.longitude}
              </p>
              <p>
                <strong>ALT</strong> ${obj.altitude}
              </p>
              `;
    },

    returnRestrictedAreasDescription(obj) {
      return `<strong>
                Restricted Area
              </strong>
              <p>
                ${obj.type}
              </p>
              <p>
                ${obj.name}
              </p>
              `;
    },

    // loads image in mapbox

    loadImage(imageName, giveThisName) {
      map.loadImage(imageName, function(error, image) {
        if (error) throw error;
        map.addImage(giveThisName, image);
      });
    },

    display_view(value) {
      console.log(value);
    },
    alert_data(data) {
      console.log(data);
      this.isVisible = !this.isVisible;
      this.fleet_id = data["fleet_id"];
      this.drone1 = data["ids"][0];
      this.drone2 = data["ids"][1];
    },
    toggle_mode() {
      if (this.mode != "Fleet Mode") {
        this.mode = "Fleet Mode";
        axios.get("http://68.183.89.213/fleet/3").then((response) => this.alert_data(response.data));
      } else {
        this.mode = "Mono Mode";
      }
    },

    getData(){
      axios
      .get(this.baseUrl + "/id")
      .then((res) => {
        this.id = res.data._id;
        this.afterGettingId(res.data._id);
      }) // and websocket thing starts
      .catch((err) => console.log(err));
    },
    sendDataFleet() {
      this.isVisible = !this.isVisible;
      var fleetSock = new WebSocket(
        "ws://" + "68.183.89.213" + "/ws/fleet/" + this.fleet_id + "/" + this.drone1 + "/"
      );

      fleetSock.onopen = () => {
        
        window.clearInterval(this.windowInterval);
        map.setMaxBounds(null)
        map.setZoom(0)
        map.setMaxZoom(null)
        map.setMinZoom(null);

        

        fleetSock.send(
          JSON.stringify({
            status: 200,
            fleet_id: this.fleet_id,
            _id: this.drone1,
            longitude: 23.23423,
            latitude: 34.23423412,
            temperature: 12,
            altitude: 234,
            obstruction: 123,
          })
        );
      };

      fleetSock.onmessage = (e) => {
        // map.setMaxBounds = undefined;
        
        const data = JSON.parse(e.data);
        console.log(data);
        if (data._id == this.drone1) {
          this.userLocation = [data.latitude, data.longitude];
          this.user.latitude = data.latitude;
          this.user.longitude = data.longitude;
          this.user.altitude = data.altitude;
          this.user.temperature = data.temperature;
          this.user.presuure = 1;

          this.updateLine()
          this.updateMapData()

          // jst to center drone we will remove this

          // map.flyTo({center: [data.longitude, data.latitude]})
          // this.setBoundary(null)

          fleetSock.send(
            JSON.stringify({
              status: 200,
              fleet_id: this.fleet_id,
              _id: this.drone1,
              longitude: 23.23423,
              latitude: 34.23423412,
              temperature: 12,
              altitude: 234,
              obstruction: 123,
            })
          );
        } else {
          this.allUsersData = [
            {
              latitude: data.latitude,
              longitude: data.longitude,
              altitude: data.altitude,
              temperature: data.temperature,
            },
          ];
        }
      };
    },
  },

  computed: {
    ...mapGetters(["allOtherFlyingObjects", "myFlyingObject", "restrictedAreas"]),
  },

  created() {
    // window.setInterval(() => {
    //   // get location every .5 sec
    //   this.getUserLocation();
    // }, 500);

    this.getData()
    // initSocket = new WebSocket(`${this.wsBaseUrl}/connection/`)
  },

  mounted() {
    map = new mapboxgl.Map({
      container: "map",
      style: this.mapStyle,
      // zoom: this.zoom,
      maxZoom: this.maxZoom,
      center: [this.userLocation[1], this.userLocation[0]],
      keyboard: false,
    });

    console.log(this.restrictedAreas)

    this.onKeyDown();

    // calls loadImage method and load Image giving a name "used in features"

    this.loadImage(redDrone, "redDrone");
    this.loadImage(whiteDrone, "whiteDrone");
    this.loadImage(blueDrone, "blueDrone");
    this.loadImage(greenDrone, "greenDrone");
    this.loadImage(blackDrone, "blackDrone");
    this.loadImage(yellowDrone, "yellowDrone");

    // calls Map on Load function

    this.MapMain();

    // calls Map onmouseenter

    this.onMouseEnter();
  },
};
</script>

<style scoped>
/* mapbox css */

.mapboxgl-popup {
  max-width: 400px;
  font: 12px/20px "Helvetica Neue", Arial, Helvetica, sans-serif;
}

.main-div {
  font-family: "Poppins", sans-serif;
  display: grid;
  grid-template-columns: 5fr 1fr;
  grid-column-gap: 10px;
  max-width: 100%;
  /* max-height: 90vh; */
  margin: 10px 10px 0 10px;
}

.map-div {
  max-height: 90vh;
  min-height: 90vh;
}

.my-obj-div {
  margin: 10px 0 10px 0;
}

.info-div {
  background-color: rgb(255, 255, 255);
  border-radius: 5px;
  color: rgb(68, 68, 68);
  padding: 1px 1px 1px 1px;
  text-align: center;
}

.label-heading {
  color: black;
  font-size: 30px;
  font-weight: bold;
}

.card {
  padding: 10px 0 10px 0;
  border-radius: 5px;
}

.my-info-card {
  background-color: rgb(202, 202, 202);
  color: black;
  font-weight: 400;
  font-size: 18px;
}

.other-info-card {
  border: 1px solid rgb(255, 255, 255);
  background-color: rgb(228, 228, 228);
  margin: 2px;
  margin-bottom: 5px;
}

#toggle {
  padding: 5px 5px 5px 5px;
  border: black solid 1px;
  border-radius: 5px;
  text-decoration: none;
  display: block;
}

#toggle:hover {
  color: white;
  background-color: brown;
  font-weight: bolder;
}

#mymodal {
  height: 250px;
  width: 500px;
  position: absolute;
  float: right;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  background-color: brown;
  margin-left: 25%;
}
.visible {
  display: none;
}

.redder{
 color: red;
 font-size: 30px;
}
.greener{
  color: green;
  font-size: 30px;
}

@media screen and (max-width: 1000px) {
  .main-div {
    display: block;
  }
  .map-div {
    max-height: 85vh;
    min-height: 80vh;
    margin-bottom: 10px;
  }
}
</style>
