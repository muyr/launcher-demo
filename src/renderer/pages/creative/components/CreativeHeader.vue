<template>
    <Header class="header">
        <div class="logo">
            <img class="logo-img" src="/static/images/icon-logo.png"/>
        </div>
        <ul>
            <li class="item">
                <Icon type="md-menu" size="24"/>
                <Badge dot :offset="[-12,5]">
                </Badge>
            </li>
            <li class="item">
                <Avatar src="/static/images/avatar.jpg"></Avatar>
            </li>
            <li class="item">
                <Icon type="ios-notifications" size="24"/>
                <Badge dot :offset="[-12,5]">
                </Badge>
            </li>
        </ul>
    </Header>
</template>

<script>
  export default {
    name: 'CreativeHeader'
  }
</script>

<style scoped>
    .header {
        padding: 0 12px;
        -webkit-app-region: drag;
        /*position: absolute;*/
        /*top: 0;*/
    }

    .item {
        color: #cacaca;
        display: inline-block;
        padding: 0 2px;
        cursor: pointer;
        float: right;
        margin-right: 10px;
    }

    .logo {
        float: left;
        width: 80px;
    }

    .logo-img {
        /*height: 40px;*/
        width: 100%;
    }

</style>
