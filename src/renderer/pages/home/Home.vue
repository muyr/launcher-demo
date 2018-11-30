<template>
    <div class="layout">
        <Layout>
            <Header>
                <home-header/>
            </Header>
        </Layout>
        <Layout class="content-layout">
            <Sider hide-trigger
                   width="240" :style="{position: 'fixed', height: '100vh',background: '#fff', overflow: 'auto'}">
                <home-toolbar :dataList="toolSectionList" @menu-item-clicked="handleToolClicked"/>
            </Sider>
            <Layout :style="{marginLeft: '240px', padding: '24px'}">
                <Content>
                    <Tabs type="card" closable :before-remove="handleTabRemoved" v-model="currentTab">
                        <TabPane v-for="(item, index) in tabList"
                                 :label="item.name"
                                 :icon="item.icon"
                                 :name="item.name"
                                 :closable="item.closeable">
                            <router-view name="item.component"></router-view>
                            <div>{{item.component}}</div>
                        </TabPane>
                    </Tabs>
                </Content>
            </Layout>
        </Layout>
        <Layout>
            <Footer>
                <div>Footer</div>
            </Footer>
        </Layout>
    </div>
</template>

<script>
  import HomeHeader from './components/HomeHeader'
  import HomeToolbar from './components/HomeToolbar'

  export default {
    name: 'Home',
    components: {HomeToolbar, HomeHeader},
    data () {
      return {
        recentFileList: [
          {file_name: 'pl_0010_ani_master.ma', created_at: new Date().toLocaleString(), software: 'maya'},
          {file_name: 'pl_0010_comp_master.ma', created_at: new Date().toLocaleString(), software: 'nuke'},
          {file_name: 'pl_0010_efx_master.ma', created_at: new Date().toLocaleString(), software: 'houdini'},
          {file_name: 'pl_0010_mm_master.ma', created_at: new Date().toLocaleString(), software: 'maya'}
        ],
        recentFileHeaderList: [
          {
            title: 'Software',
            key: 'software',
            width: 120,
            sortable: true,
            render: (h, params) => {
              return h('Avatar', {
                props: {
                  shape: 'square',
                  src: '/static/images/app-' + params.row.software + '.png'
                }
              })
            }
          }, {
            title: 'File Name',
            key: 'file_name',
            sortable: true,
            width: 250
          }, {
            title: 'Create At',
            key: 'created_at',
            sortable: true
          }, {
            title: 'Action',
            key: 'action',
            align: 'center',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      console.log(params)
                    }
                  }
                }, 'Open')
              ])
            }
          }
        ],
        recentToolList: [
          {
            icon: '/static/images/app-maya.png',
            content: {
              name: 'Maya 2018'
            }
          },
          {
            icon: '/static/images/app-nuke.png',
            content: {
              name: 'Nuke 11.2v2'
            }
          },
          {
            icon: '/static/images/app-houdini.png',
            content: {
              name: 'Houdini 16.5.4496'
            }
          }
        ],
        toolSectionList: [
          {
            title: '修改节点属性类',
            data: [
              {
                'icon': '/static/images/replace.png',
                'name': '路径查找 & 替换'
              },
              {
                'icon': '/static/images/app-nuke.png',
                'name': 'OutBox'
              }
            ]
          },
          {
            title: '模板类',
            data: [
              {
                'icon': '/static/images/curve.png',
                'name': 'ROTO 模板'
              }, {
                'icon': '/static/images/colorboard.png',
                'name': '色卡'
              }, {
                'icon': '/static/images/watermark.png',
                'name': 'Easy Slate'
              }
            ]
          },
          {
            title: '效果类',
            data: [
              {
                'icon': '/static/images/fill.png',
                'name': '洪水填充'
              }, {
                'icon': '/static/images/icon-view.png',
                'name': 'Animation'
              }
            ]
          },
          {
            title: '工具类',
            data: [
              {
                'icon': '/static/images/icon-view.png',
                'name': '色彩空间转换'
              }, {
                'icon': '/static/images/icon-view.png',
                'name': 'Animation-From Coco'
              }
            ]
          },
          {
            title: 'My Filters',
            data: [
              {
                'icon': '/static/images/icon-search.png',
                'name': '今天的 Dailies'
              }, {
                'icon': '/static/images/icon-search.png',
                'name': '发包 Plate'
              }
            ]
          }
        ],
        tabList: [
          {
            name: 'Welcome',
            closeable: false,
            component: 'welcome'
          }
        ],
        currentTab: null
      }
    },
    comments: {
      HomeHeader,
      HomeToolbar
    },
    methods: {
      handleToolClicked (tabName) {
        for (var index in this.tabList) {
          if (this.tabList[index].name === tabName) {
            this.currentTab = tabName
            return
          }
        }
        this.tabList.push({
          name: tabName,
          closeable: true,
          component: tabName.toLowerCase()
        })
        this.currentTab = tabName
      },
      handleTabRemoved (index) {
        this.tabList.splice(index, 1)
        return new Promise(function (resolve, reject) {
          // resolve('删除');
          // reject('不删除');//这里是传递一个错误，可以不写，同样不删除
        })
      }
    }
  }
</script>

<style scoped>
    .layout {
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }

    .content-layout {
        height: auto;
    }
</style>
