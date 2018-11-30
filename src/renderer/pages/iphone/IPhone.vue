<template>

    <div class="iphone">
        <div class="iphone-top">
            <span class="camera"></span>
            <span class="sensor"></span>
            <span class="speaker"></span>
        </div>
        <div class="top-bar"></div>
        <div class="iphone-screen">
            <div class="topBar">
                <div class="header-time">{{currentTime}} - Andy</div>
            </div>
            <router-view/>
        </div>
        <div class="buttons">
            <span class="on-off"></span>
            <span class="sleep"></span>
            <span class="up"></span>
            <span class="down"></span>
        </div>
        <div class="bottom-bar"></div>
        <div class="iphone-bottom">
            <router-link to="/iphone/screen" class="home-button" tag="span"></router-link>
        </div>
    </div>
</template>

<script>
  import router from '@/router'

  export default {
    name: 'IPhone',
    data () {
      return {
        currentTime: ''
      }
    },
    mounted () {
      this.currentTime = new Date().toLocaleTimeString()
      router.push('/iphone/screen')
    },
    methods: {
      test: function () {
        console.log('clicked')
      }
    }
  }
</script>

<style scoped>
    .topBar {
        /*background-color: rgba(100, 100, 100, 0.6);*/
        /*background-color: transparent;*/
        height: 24px;
        line-height: 24px;
        width: 100%;
        text-align: center;
        color: white;
        background-color: black;
    }

    .header-time {
        text-align: center;
        padding: 2px;
        letter-spacing: 1px;
    }

    .iphone {
        box-shadow: inset 0 0 3px 0 rgba(0, 0, 0, 0.2), 0 0 0 1px #999, 0 0 30px 0px rgba(0, 0, 0, 0.7);
        border: 5px solid #d9dbdc;
        background: #f8f8f8;
        padding: 15px;
        border-radius: 50px;
        height: 877px;
        width: 423px;
        left: 20px;
        top: 20px;
        position: relative;
        /*-webkit-transform: scale(0.8);*/
        /*transform: scale(0.8);*/
    }

    .iphone-top {
        padding: 5px 110px 40px;
        position: relative;
        -webkit-app-region: drag;
    }

    .iphone-top .speaker {
        display: block;
        width: 70px;
        height: 6px;
        margin: 0 auto;
        border-radius: 6px;
        background: #292728;
    }

    .iphone-top .camera {
        display: block;
        margin: 0 auto;
        height: 8px;
        width: 8px;
        border-radius: 50%;
        margin-bottom: 13px;
        background: #333;
    }

    .iphone-top .sensor {
        display: block;
        width: 12px;
        height: 12px;
        float: left;
        background: #333;
        margin-top: -5px;
        border-radius: 50%;
    }

    .iphone .top-bar, .iphone .bottom-bar {
        display: block;
        width: 423px;
        height: 15px;
        border-left: 5px solid #BBB;
        border-right: 5px solid #BBB;
        position: absolute;
        left: -5px;
    }

    .iphone .top-bar {
        top: 65px;
    }

    .iphone .bottom-bar {
        bottom: 65px;
    }

    .iphone-screen {
        background: #eee;
        border: 1px solid #fff;
        height: 677px;
        width: 375px;
        margin: 0 auto;
        border: 2px solid rgba(0, 0, 0, 0.9);
        border-radius: 3px;
        overflow: hidden;
    }

    .iphone-screen img {
        width: 100%;
    }

    .iphone .buttons .on-off, .iphone .buttons .up, .iphone .buttons .down, .iphone .buttons .sleep {
        display: block;
        background: #CCC;
        position: absolute;
        border-radius: 2px 0px 0px 2px;
    }

    .iphone .buttons .on-off {
        height: 40px;
        width: 3px;
        top: 100px;
        left: -8px;
    }

    .iphone .buttons .up, .iphone .buttons .down, .iphone .buttons .sleep {
        height: 60px;
        width: 5px;
        left: -10px;
    }

    .iphone .buttons .up {
        top: 170px;
    }

    .iphone .buttons .down {
        top: 250px;
    }

    .iphone .buttons .sleep {
        left: auto;
        right: -10px;
        top: 170px;
        border-radius: 0px 2px 2px 0px;
    }

    .iphone-bottom {
        padding: 10px 0 0;
    }

    .iphone-bottom span {
        content: "";
        position: relative;
        display: block;
        width: 68px;
        height: 68px;
        border-radius: 50%;
        margin: 0 auto;
        background: #ccc;
        background: -webkit-linear-gradient(315deg, #303233 0%, #b5b7b9 50%, #f0f2f2 69%, #303233 100%);
        background: linear-gradient(135deg, #303233 0%, #b5b7b9 50%, #f0f2f2 69%, #303233 100%);
    }

    .iphone-bottom span:after {
        content: "";
        display: block;
        width: 60px;
        height: 60px;
        background: #fff;
        border-radius: 50%;
        position: absolute;
        left: 4px;
        top: 4px;
        margin: 0 auto;
        cursor: pointer;
    }

    .iphone-bottom span:hover {
        background-color: rgba(100, 0, 0, 0.5);
    }


</style>
