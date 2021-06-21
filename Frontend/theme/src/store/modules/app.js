// Pathify
import { make } from 'vuex-pathify'

// Data
const state = {
  drawer: null,
  drawerImage: true,
  mini: false,
  items: [
    {
      title: 'Dashboard',
      icon: 'mdi-view-dashboard',
      to: '/',
    },
    // {
    //   title: 'User Profile',
    //   icon: 'mdi-account',
    //   to: '/components/profile/',
    // },
    {
      title: 'Doctor Table',
      icon: 'mdi-account-plus-outline',
      to: '/tables/doctor/',
    },
    {
      title: 'Clinic Table',
      icon: 'mdi-ambulance',
      to: '/tables/clinic/',
    },
    {
      title: 'Patient Table',
      icon: 'mdi-account-multiple-plus',
      to: '/tables/patient/',
    },
    {
      title: 'Appointment Table',
      icon: 'mdi-alarm-plus',
      to: '/tables/appointment/',
    },
    {
      title: 'Appointment Details',
      icon: 'mdi-clipboard-outline',
      to: '/tables/appointmentinfo/',
    },
    // {
    //   title: 'Register',
    //   icon: 'mdi-clipboard-outline',
    //   to: '/register',
    // },
    // {
    //   title: 'Login',
    //   icon: 'mdi-clipboard-outline',
    //   to: '/login',
    // },
    // {
    //   title: 'Typography',
    //   icon: 'mdi-format-font',
    //   to: '/components/typography/',
    // },
    // {
    //   title: 'Icons',
    //   icon: 'mdi-chart-bubble',
    //   to: '/components/icons/',
    // },
    // {
    //   title: 'Google Maps',
    //   icon: 'mdi-map-marker',
    //   to: '/maps/google/',
    // },
    // {
    //   title: 'Notifications',
    //   icon: 'mdi-bell',
    //   to: '/components/notifications/',
    // },
  ],
}

const mutations = make.mutations(state)

const actions = {
  ...make.actions(state),
  init: async ({ dispatch }) => {
    //
  },
}

const getters = {}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
