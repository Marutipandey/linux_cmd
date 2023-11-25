<template>
  <Welcome :display="true"></Welcome>
  <!-- <Input></Input> -->
</template>

<script>
import Welcome from '@/components/Welcome.vue';
// import Input from '@/components/Input.vue';
export default {
  name: 'IndexPage',
  components: {
    Welcome,
    // Input,
  },
}
</script>
