<template>
  <v-app>
    <default-bar v-if="$route.name != 'Login' && $route.name != 'Clinic Register' && $route.name != 'Doctor Register' && $route.name != 'Patient Register'">
    </default-bar>

    <default-drawer
      v-if="$route.name != 'Login' && $route.name != 'Clinic Register' && $route.name != 'Doctor Register' && $route.name != 'Patient Register'"
    />

    <default-view />

    <default-footer v-if="$route.name != 'Login' && $route.name != 'Clinic Register' && $route.name != 'Doctor Register' && $route.name != 'Patient Register'" />

    <default-settings v-if="$route.name != 'Login' && $route.name != 'Clinic Register' && $route.name != 'Doctor Register' && $route.name != 'Patient Register'" />
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",

  components: {
    DefaultBar: () =>
      import(
        /* webpackChunkName: "default-app-bar" */
        "./AppBar"
      ),
    DefaultDrawer: () =>
      import(
        /* webpackChunkName: "default-drawer" */
        "./Drawer"
      ),
    DefaultFooter: () =>
      import(
        /* webpackChunkName: "default-footer" */
        "./Footer"
      ),
    DefaultSettings: () =>
      import(
        /* webpackChunkName: "default-settings" */
        "./Settings"
      ),
    DefaultView: () =>
      import(
        /* webpackChunkName: "default-view" */
        "./View"
      ),
  },
  created() {
    console.log(this.$route.name);
  },
};
</script>
