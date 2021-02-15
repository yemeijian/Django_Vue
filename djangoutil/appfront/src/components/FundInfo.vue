<template>
  <div class="hello">
    <h1>基金监控信息</h1>
    <div class="header">
      <div class="header">
        <Button type="primary" @click="ModalBulletFrame.modal = true">添加基金监控信息</Button>
        <Modal
          v-model="ModalBulletFrame.modal"
          title="添加基金监控信息"
          :loading="ModalBulletFrame.loading"
          @on-ok="asyncOK">
          <Form ref="formValidate" :model="formFundInfo" :rules="ruleFundInfo" :label-width="100">
            <FormItem label="基金名字：" prop="formFundName">
              <Input v-model="formFundInfo.formFundName" placeholder="请输入基金名字"></Input>
            </FormItem>
            <FormItem label="基金代码：" prop="formFundCode">
              <Input v-model="formFundInfo.formFundCode" placeholder="请输入基金代码"></Input>
            </FormItem>
            <FormItem label="是否监控" prop="formIsMonitor">
              <RadioGroup v-model="formFundInfo.formIsMonitor">
                <Radio label="true">是</Radio>
                <Radio label="false">否</Radio>
              </RadioGroup>
            </FormItem>
            <FormItem>
              <Button @click="handleReset('formValidate')" style="margin-left: 8px">清空</Button>
            </FormItem>
          </Form>
        </Modal>
      </div>
      <div class="header">
        <Button @click="loadFundInfo()" type="primary" shape="circle" icon="ios-search">查询基金监控信息</Button>
      </div>
    </div>
    <Table :columns="fundInfoListText" :data="fundInfoList"></Table>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import {getFundInfo, postFundInfo} from '../api/api'

export default {
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
      formFundInfo: {
        formFundName: '',
        formFundCode: '',
        formIsMonitor: ''
      },
      ruleFundInfo: {
        formFundName: [
          {required: true, message: '基金名字不能为空', trigger: 'blur'}
        ],
        formFundCode: [
          {required: true, message: '基金代码不能为空', trigger: 'blur'}
          // {type: 'integer', message: '基金代码无效', trigger: 'blur'}
        ],
        formIsMonitor: [
          {required: true, message: '请选择是否监控', trigger: 'change'}
        ]
      },
      fundInfoList: [],
      ModalBulletFrame: {
        modal: false,
        loading: true
      }
    }
  },
  methods: {
    loadFundInfo () {
      getFundInfo().then(response => {
        console.log(response.data)
        if (response.status === 200) {
          this.fundInfoList = response.data.results
          this.$Message.success('查询成功')
        } else {
          this.$Message.error('查询失败：' + response.data)
        }
      })
    },
    asyncOK () {
      this.$refs.formValidate.validate((valid) => {
        if (valid) {
          this.$Message.success('Success!')
        } else {
          this.$Message.error('Fail!')
        }
      })
      setTimeout(() => {
        this.ModalBulletFrame.modal = false
        console.log(this.formFundInfo)
        postFundInfo(this.formFundInfo.formFundName, this.formFundInfo.formFundCode, this.formFundInfo.formIsMonitor).then(response => {
          console.log(response.data)
          this.loadFundInfo()
        })
      }, 0)
    },
    handleReset (name) {
      this.$refs[name].resetFields()
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

.header {
  display: inline;
}
</style>
