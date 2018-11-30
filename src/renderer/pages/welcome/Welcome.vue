<template>
    <div class="welcome-container">
        <div class="subtitle">最近打开的软件 ...</div>
        <big-view :dataList="recentToolList"></big-view>
        <div class="subtitle">最近打开的文件 ...</div>
        <Table stripe size="small"
               no-data-text="空空如也"
               :columns="recentFileHeaderList"
               :data="recentFileList"></Table>
    </div>
</template>

<script>
  import BigView from 'common/bigview/BigView'

  export default {
    name: 'Welcome',
    components: {
      BigView
    }
  }
</script>

<style scoped>

</style>
