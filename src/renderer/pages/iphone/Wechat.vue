<template>
    <div class="wechat-container">
        <div class="title-text">Nuke</div>
        <div class="app-content">
            <Row class="footer">
                <Col span="24">
                    <div class="search">
                        <Input v-model="searchValue" placeholder="搜索" style="width: 354px" class="search-input"/>
                    </div>
                </Col>
                <Col span="24" v-for="item in pluginList">
                    <div class="app-item-container">
                        <Avatar class="icon" :src="item.icon" shape="square" size="large"></Avatar>
                        <div class="text-container">
                            <div class="app-name">{{item.name | title}} {{item.version}}</div>
                            <div class="description">{{item.description}}</div>
                        </div>
                        <div>
                            <Spin size="large" fix v-show="item.showLoading && item.loading"></Spin>
                            <Button class="operator" shape="circle"
                                    @click="openApp(item)"
                                    :type="item.operator | role">{{item.operator}}
                            </Button>
                        </div>
                    </div>
                </Col>
            </Row>
        </div>
        <div class="footer-container">
            <Row class="footer">
                <Col span="8" v-for="item in footerList">
                    <div class="app-item">
                        <Badge :count="item.notice" :offset="[5,5]">
                            <Avatar class="icon" :src="item.icon" shape="square" size="small"></Avatar>
                            <p class="footer-text">{{item.name}}</p>
                        </Badge>
                    </div>
                </Col>
            </Row>
        </div>
    </div>
</template>

<script>
  import {rabbitChannel, requestQueue, guid} from '@/rabbit'

  export default {
    name: 'Wechat',
    filters: {
      title: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      },
      iconPath: function (value) {
        return 'static/images/' + value + '.png'
      },
      role: (value) => {
        let setting = {'安装': 'success', '更新': 'warning', '启动': 'primary'}
        return setting[value]
      }
    },
    data () {
      return {
        searchValue: '',
        pluginList: [
          {
            name: '高级 Blur 节点',
            version: 'v0.2',
            icon: 'static/images/blur.png',
            operator: '创建',
            description: '采用xxx算法的xxx Blur',
            request: {'url': 'nuke.create', 'body': [{'type': 'blur'}]},
            loading: false
          },
          {
            name: 'Color Temperature',
            version: 'v1.2',
            icon: 'static/images/color-temperature.png',
            operator: '创建',
            description: '色温匹配',
            request: {'url': 'nuke.create', 'body': [{'type': 'color_temperature'}]},
            loading: false
          },
          {
            name: 'Color Chart Match',
            version: 'v1.0',
            icon: 'static/images/chart.png',
            operator: '创建',
            description: '自动匹配色卡',
            request: {'url': 'nuke.create', 'body': [{'type': 'color_chart_match'}]},
            loading: false
          },
          {
            name: 'Version Up',
            version: 'v1.0',
            icon: 'static/images/update.png',
            operator: '执行',
            description: '更新工程文件中所有上游元素',
            request: {'url': 'nuke.update', 'body': [{'type': 'blur'}]},
            loading: false,
            showLoading: true
          },
          {
            name: 'Easy Slate',
            version: 'v1.0',
            icon: 'static/images/slate.png',
            operator: '创建',
            description: '花式 Slate 模板',
            request: {'url': 'nuke.create', 'body': [{'type': 'easy_slate'}]},
            loading: false
          },
          {
            name: 'Flood Fill',
            version: 'v1.0',
            icon: 'static/images/flood.png',
            operator: '创建',
            description: '洪水填充',
            request: {'url': 'nuke.create', 'body': [{'type': 'flood'}]},
            loading: false
          }
        ],
        footerList: [
          {
            name: '插件',
            icon: 'static/images/plugin.png'
          },
          {
            name: '通知',
            icon: 'static/images/info.png'
          },
          {
            name: '设置',
            icon: 'static/images/setting.png'
          }
        ]
      }
    },
    methods: {
      openApp (item) {
        item.loading = true
        return new Promise(resolve => {
          rabbitChannel.assertQueue('', {durable: false, autoDelete: true, exclusive: true}, function (err, queueObj) {
            if (err) {
              throw err
            }
            resolve(queueObj)
          })
        })
          .then(queueObj => {
            rabbitChannel.sendToQueue(requestQueue, Buffer.from(JSON.stringify(item.request)), {
              replyTo: queueObj.queue,
              correlationId: guid()
            })
            rabbitChannel.consume(queueObj.queue, (msg) => {
              this.showResultMessage(msg)
              item.loading = false
            })
          })
          .catch(err => {
            console.log(err)
            item.loading = false
          })
      },
      showResultMessage (msg) {
        this.$Message.config({
          top: 150,
          duration: 3
        })
        let dataDict = JSON.parse(msg.content.toString())
        if (dataDict.status === 'ok') {
          this.$Message.success(dataDict.message)
        } else {
          this.$Message.error(dataDict.message)
        }
      }
    }
  }
</script>

<style scoped>
    .wechat-container {
        position: absolute;
        background-color: white;
        font-family: 'PingFang SC', 'STHeitiSC-Light', 'Helvetica-Light', 'Microsoft YaHei', arial, sans-serif, 'Droid Sans Fallback';
        width: 371px;
        height: 649px;
    }

    .title-text {
        background-color: black;
        color: white;
        height: 38px;
        line-height: 38px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
    }

    .search {
        border-bottom: 1px lightgray solid;
        padding: 8px;
        background-color: #eaeaea;
    }

    .app-content {
        background-color: white;
    }

    .app-item-container {
        height: 66px;
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

    .footer-container {
        position: absolute;
        width: 100%;
        bottom: 0;
        left: 0;
        padding: 3px 20px;
        background-color: #eaeaea;
        border-top: 1px lightgray solid;
    }

    .footer {
        width: 100%;
        /*background-color: blanchedalmond;*/
    }

    .footer-text {
        text-align: center;
    }

    .app-item {
        margin: 0 35px;
        cursor: pointer;
    }

    .current-app {
        color: red;
    }
</style>
