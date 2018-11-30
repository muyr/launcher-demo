<template>
    <div class="app-container">
        <div class="banner">
            <Carousel v-model="value1" loop>
                <CarouselItem>
                    <div class="demo-carousel">1</div>
                </CarouselItem>
                <CarouselItem>
                    <div class="demo-carousel">2</div>
                </CarouselItem>
                <CarouselItem>
                    <div class="demo-carousel">3</div>
                </CarouselItem>
                <CarouselItem>
                    <div class="demo-carousel">4</div>
                </CarouselItem>
            </Carousel>
        </div>
        <div class="app-list-container">
            <ul>
                <li v-for="(item, key) in appList" :key="key" class="app-item-container">
                    <Avatar class="icon" :src="item.name | iconPath" shape="square" size="large"></Avatar>
                    <div class="text-container">
                        <div class="app-name">{{item.name | title}} {{item.version}}</div>
                        <div class="description">{{item.description}}</div>
                    </div>
                    <Button class="operator" shape="circle"
                            @click="openApp"
                            :type="item.operator | role">{{item.operator}}
                    </Button>
                </li>
                <Divider><span class="bottom-info">做人是有底线的</span></Divider>
            </ul>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'Apps',
    filters: {
      title: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      },
      iconPath: function (value) {
        return '/static/images/app-' + value.toLowerCase() + '.png'
      },
      role: (value) => {
        let setting = {'安装': 'success', '更新': 'warning', '启动': 'primary'}
        return setting[value]
      }
    },
    methods: {
      openApp (nodesc) {
        this.$Message.success('软件启动成功')
      }
    },
    data () {
      return {
        value1: 0,
        appList: [
          {
            name: 'Maya',
            version: '2018',
            operator: '启动',
            description: '这里是关于软件的描述'
          },
          {
            name: 'Nuke',
            version: '11.1v2',
            operator: '启动',
            description: '影视后期二维领域一霸'
          },
          {
            name: 'Houdini',
            version: '16.3.3232',
            operator: '启动',
            description: '这里是关于软件的描述'
          },
          {
            name: 'Mari',
            version: '16.3.3232',
            operator: '启动',
            description: '这里是关于软件的描述'
          },
          {
            name: 'Hiero',
            version: '7.3.0',
            operator: '启动',
            description: '这里是关于软件的描述'
          },
          {
            name: 'RV',
            version: '7.3.0',
            operator: '更新',
            description: '这里是关于软件的描述'
          },
          {
            name: 'Shotgun',
            version: '7.3.0',
            operator: '启动',
            description: '这里是关于软件的描述'
          },
          {
            name: 'NukeStudio',
            version: '12.1.0',
            operator: '安装',
            description: '这里是关于软件的描述'
          }
        ]
      }
    }
  }
</script>

<style scoped>
    .banner {
        margin-top: -16px;
        height: 200px;
        background-color: lightgray;
    }

    .demo-carousel {
        height: 200px;
        text-align: center;
        line-height: 200px;
    }

    .app-item-container {
        height: 60px;
        /*background-color: aquamarine;*/
        padding: 10px 20px;
        border-bottom: 1px lightgray solid;
    }

    .app-item-container:hover {
        background-color: #eaeaea;
    }

    .icon {
        float: left;
    }

    .text-container {
        display: inline-block;
        padding-left: 10px;
        float: left;
    }

    .description {
        display: inline-block;
        float: left;
    }

    .app-name {
        font-size: 16px;
        font-weight: bold;
    }

    .operator {
        float: right;
        font-size: 14px;
        letter-spacing: 1px;
    }

    .bottom-info {
        font-size: 12px;
        color: lightgray;
    }
</style>
