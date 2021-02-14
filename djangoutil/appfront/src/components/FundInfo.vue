<template>
  <div class="hello">
    <h1>基金监控信息</h1>
    <Button @click="loadFundInfo" type="primary" shape="circle" icon="ios-search">查询基金信息</Button>
    <Table :columns="fundInfoListText" :data="fundInfoList"></Table>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {getFundInfo, postFundInfo} from '../api/api'

export default {
  el: '#fundinfo',
  name: 'FundInfo',
  data () {
    return {
      fundInfoListText: [
        {
          title: '基金名字',
          key: 'fundName'
        }, {
          title: '基金代码',
          key: 'fundCode'
        }, {
          title: '是否监控',
          key: 'isMonitor'
        }
      ],
      fundInfoList: []
    }
  },
  methods: {
    loadFundInfo () {
      getFundInfo().then(response => {
        console.debug(response.data)
        this.fundInfoList = response.data.results
      })
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
