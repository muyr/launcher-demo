<template>
    <div class="screen-container">
        <div class="content-container">
            <Row>
                <Col span="6" v-for="item in dataList">
                    <div class="app-item">
                        <Badge :count="item.notice" :offset="[5,5]">
                            <img class="item-icon" :src="item.icon"/>
                        </Badge>
                        <div class="item-text">{{item.text}}</div>
                    </div>
                </Col>
            </Row>
        </div>
        <div class="footer-container">
            <Row class="footer">
                <Col span="6" v-for="item in footerList">
                    <router-link to="/iphone/wechat">
                        <div class="app-item">
                            <Badge :count="item.notice" :offset="[5,5]">
                                <img class="item-icon" :src="item.icon"/>
                            </Badge>
                        </div>
                    </router-link>
                </Col>
            </Row>
        </div>
    </div>
</template>

<script>
  const remote = require('electron').remote
  export default {
    name: 'Screen',
    methods: {
      closeApp () {
        remote.app.quit()
      },
      minimize () {
        remote.BrowserWindow.getFocusedWindow().minimize()
      }
    },
    data () {
      return {
        currentTime: '',
        dataList: [
          {
            text: 'Mari',
            icon: 'static/images/app-mari.png',
            notice: 0
          },
          {
            text: 'Katana',
            icon: 'static/images/app-katana.png'
          },
          {
            text: 'Modo',
            icon: 'static/images/app-modo.png'
          },
          {
            text: 'Hiero',
            icon: 'static/images/app-hiero.png'
          },
          {
            text: 'Shotgun',
            icon: 'static/images/app-shotgun.png',
            notice: 2
          }
        ],
        footerList: [
          {
            text: 'Nuke',
            icon: 'static/images/app-nuke.png'
          },
          {
            text: 'Maya',
            icon: 'static/images/app-maya.png'
          },
          {
            text: 'Houdini',
            icon: 'static/images/app-houdini.png'
          },
          {
            text: '任务',
            icon: 'static/images/reminders.png',
            notice: 999
          }
        ]
      }
    }
  }
</script>

<style scoped>
    .screen-container {
        position: absolute;
        background: url('~@/assets/images/background.png');
        width: 371px;
        height: 649px;
        font-family: 'PingFang SC', 'STHeitiSC-Light', 'Helvetica-Light', 'Microsoft YaHei', arial, sans-serif, 'Droid Sans Fallback'
        /*padding: 0 10px;*/
        /*background-color: #076c62;*/
    }

    .app-item {
        display: inline-block;
        padding: 16px;
        cursor: pointer;
    }

    .app-item:hover {
        background-color: rgba(200, 0, 0, 0.1);
    }

    .item-icon {
        width: 100%;
        border-radius: 18px;
    }

    .item-text {
        text-align: center;
        color: #eaeaea;
        padding: 2px 2px;
        font-size: 13px;
        font-family: "Microsoft YaHei UI";
    }

    .content-container {
        padding: 0;
    }

    .footer-container {
        /*padding: 0;*/
        position: absolute;
        width: 100%;
        bottom: 0;
        left: 0;
        padding: 0 10px;
        background-color: rgba(200, 200, 200, 0.6);
    }
</style>
