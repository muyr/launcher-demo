<template>
    <div class="learning-container">
        <div class="title">学习新技术。</div>
        <div class="search">
            <Input search enter-button placeholder="搜索教程"/>
            <div class="hot-topic-container">热门:
                <ul class="hot-topic">
                    <li class="hot-topic">
                        <a>色彩科学</a>
                    </li>
                    <li class="hot-topic">
                        <a>Hiero导表插件</a>
                    </li>
                </ul>
            </div>
        </div>
        <Tabs value="name1" class="test">
            <TabPane label="文章" name="name1">
                <ul>
                    <li class="text-item">
                        <Icon size="18" type="ios-paper"/>
                        <a>十分钟色彩科学：我们为什么能感觉到颜色(上)</a></li>
                    <li class="text-item">
                        <Icon size="18" type="ios-paper"/>
                        <a>十分钟色彩科学：我们为什么能感觉到颜色(下)</a></li>
                </ul>
                <!--<html-panel :url="testUrl"></html-panel>-->
            </TabPane>
            <TabPane label="视频" name="name2">
                <ul>
                    <li>十分钟色彩科学</li>
                </ul>
            </TabPane>
        </Tabs>
    </div>
</template>

<script>
  import HtmlPanel from 'common/HtmlPanel'

  export default {
    name: 'Learning',
    components: {
      HtmlPanel
    },
    data () {
      return {
        testUrl: 'https://mp.weixin.qq.com/s?__biz=MzIxMzc3NTQ5OA==&mid=2247483701&idx=1&sn=54f8d48053bfed6baf231e4823911868&chksm=97b0e4d0a0c76dc6b907821039e09a143becf232a8712a71085dbee79b599d559936c201e70b&scene=21#wechat_redirect',
        tagList:
          [
            {
              name: '分类',
              tags: ['全部', 'Maya', 'Houdini', 'Nuke', 'Mari', 'Hiero', 'Nuke Studio']
            },
            {
              name: '难度',
              tags: ['全部', '入门', '初级', '中级', '高级']
            }
          ]
      }
    }
  }
</script>

<style scoped>
    .learning-container {
        background-color: white;
        margin-top: -16px;
    }

    .title {
        padding-top: 20px;
        font-size: 24px;
        text-align: center;
        letter-spacing: 2px;
    }

    .search {
        padding: 20px 60px;
    }

    .hot-topic-container {
        margin: 5px 0;
    }

    .hot-topic {
        display: inline-block;
        padding: 0 2px;
    }

    .tag-container {
        margin: 8px 20px;
    }

    .text-item {
        font-size: 14px;
        padding: 10px;
        border-bottom: 1px lightgray solid;
    }
</style>
