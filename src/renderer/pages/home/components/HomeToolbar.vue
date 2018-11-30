<template>
    <Menu active-name="1-2" theme="light" width="auto" :open-names="['1']"
          @on-select="handleSubmenuClicked">
        <Submenu :name="index" v-for="(section, index) in dataList" :key="index">
            <template slot="title">
                <Icon type="ios-navigate"></Icon>
                {{section.title}}
            </template>
            <MenuItem :name="item.name" v-for="item in section.data">
                <Avatar size="small" shape="square" :src="item.icon" class="icon"/>
                {{item.name}}
            </MenuItem>
        </Submenu>
    </Menu>
</template>

<script>
  export default {
    name: 'HomeToolbar',
    props: [
      'dataList'
    ],
    methods: {
      handleSubmenuClicked (tabName) {
        this.$emit('menu-item-clicked', tabName)
      }
    }
  }
</script>

<style scoped>
    .icon {
        margin-right: 5px;
        margin-left: -5px;
    }
</style>
