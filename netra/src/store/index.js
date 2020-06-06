import Vue from 'vue'
import Vuex from 'vuex'

import gpsData from './modules/gpsData'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    gpsData
  }
})