const state = {
  otherFlyingObjects: [
    {
      id: 1,
      name: "drone",
      latitude: 27.70323193557546,
      longitude: 85.31765898693936,
      speed: 20,
      pressure: 1,
      altitude: 50,
    },
    {
      id: 2,
      name: "drone",
      latitude: 27.70923194557546,
      longitude: 85.31765698693936,
      speed: 15,
      pressure: 1,
      altitude: 150,
    },
    {
      id: 3,
      name: "drone",
      latitude: 27.70923193557546,
      longitude: 85.31265898693936,
      speed: 5,
      pressure: 1,
      altitude: 250,
    },
    {
      id: 4,
      name: "drone",
      latitude: 27.70323193557546,
      longitude: 85.31665898693936,
      speed: 5,
      pressure: 1,
      altitude: 350,
    },
    {
      id: 5,
      name: "drone",
      latitude: 27.70423193557546,
      longitude: 85.31765898693936,
      speed: 5,
      pressure: 1,
      altitude: -350,
    },
  ],

  myFlyingObject: {
    id: 0,
    name: "drone",
    latitude: 27.70523193557546,
    longitude: 85.31165898693936,
    speed: 10,
    pressure: 1,
    altitude: 50,
  },

  restrictedAreas: [
    {
      id: 1,
      name: 'Ratna Park',
      type: 'Park',
      coordinates: [
        [85.31388882613281, 27.707164680527804],
        [85.31375484105061, 27.705323203556553],
        [85.31651748584035, 27.704905195253197],
        [85.31667699189056, 27.70675797663167],
        [85.31388882613281, 27.707164680527804],
      ]
    },
    {
      id: 2,
      name: 'Something',
      type: 'Something',
      coordinates: [
        [85.30102011265315, 27.712580264609523],
        [85.30971784939326, 27.712055175319694],
        [85.30987878193415, 27.708844738664233],
        [85.30195259346522, 27.70891122795547],
        [85.30102011265315, 27.712580264609523],
      ]
    }
  ]
};

const getters = {
  allOtherFlyingObjects: (state) => state.otherFlyingObjects,

  myFlyingObject: (state) => state.myFlyingObject,

  restrictedAreas: (state) => state.restrictedAreas,
};

const actions = {};

const mutations = {};

export default {
  state,
  getters,
  actions,
  mutations,
};
