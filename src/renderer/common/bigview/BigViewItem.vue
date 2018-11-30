<template>
    <Card style="width:120px" :padding=10 @click="handleClick" :icon="icon">
        <p slot="title">{{content.name}}</p>
        <div style="text-align:center">
            <img :src="icon">
        </div>
    </Card>
</template>

<script>
  export default {
    name: 'BigViewItem',
    props: [
      'icon',
      'content'
    ],
    methods: {
      handleClick () {
        this.emit()
      }
    }
  }
</script>

<style scoped>
    img {
        width: 100%
    }
</style>
