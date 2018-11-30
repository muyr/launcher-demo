<template>
    <div class="container">
        <big-view-item
                class="item"
                v-for="item of dataList"
                :icon="item.icon"
                :content="item.content"/>
    </div>
</template>

<script>
  import BigViewItem from 'common/bigview/BigViewItem'

  export default {
    name: 'BigView',
    components: {
      BigViewItem
    },
    props: [
      'dataList'
    ]
  }
</script>

<style scoped>
    .container {
        background-color: #eee;
        padding: 10px;
    }

    .item {
        display: inline-block;
        margin: 4px;
    }
</style>
