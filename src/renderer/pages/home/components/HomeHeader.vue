<template>
    <Menu mode="horizontal" theme="dark" active-name="1" style="width:200px">
        <div class="layout-logo">
            <img class="logo" src="/static/images/icon-logo.png"/>
        </div>
        <div class="layout-nav">
            <MenuItem name="0">
                <Icon type="md-log-out" size="24"/>
                退出
            </MenuItem>
            <MenuItem name="1">
                <Avatar src="/static/images/avatar.jpg"></Avatar>
                <Badge text="new" :offset="[15,0]">
                    个人中心
                </Badge>
            </MenuItem>
            <MenuItem name="2">
                <Icon type="ios-notifications" size="24"/>
                <Badge :count="2" :offset="[15,-10]">
                    通知
                </Badge>
            </MenuItem>
        </div>
    </Menu>
</template>

<script>
  export default {
    name: 'HomeHeader'
  }
</script>

<style scoped>

    .layout-logo {
        width: 100px;
        height: 40px;
        /*background: #5b6270;*/
        /*border-radius: 3px;*/
        float: left;
        position: relative;
        /*top: 5px;*/
        /*left: 20px;*/
    }

    .logo {
        width: 100%;
    }

    .layout-nav {
        width: 550px;
        margin: 0 auto;
    }
</style>
