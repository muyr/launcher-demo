<template>
    <div class="layout">
        <Layout>
            <creative-header></creative-header>
        </Layout>
        <Layout class="content-layout">
            <Content>
                <Tabs value="name1" class="test">
                    <TabPane label="Apps" name="name1">
                        <apps></apps>
                    </TabPane>
                    <TabPane label="资源" name="name3">插件 | 动作 | 贴图</TabPane>
                    <TabPane label="学习" name="name2">
                        <learning></learning>
                    </TabPane>
                    <TabPane label="工作" name="name4">Stock</TabPane>
                    <TabPane label="Behance" name="name5">展示作品</TabPane>
                </Tabs>
            </Content>
        </Layout>
    </div>
</template>

<script>
  import CreativeHeader from './components/CreativeHeader'
  import Apps from './components/Apps'
  import Learning from './components/Learning'

  export default {
    name: 'Creative',
    components: {
      CreativeHeader,
      Apps,
      Learning
    }
  }
</script>

<style scoped>
</style>
