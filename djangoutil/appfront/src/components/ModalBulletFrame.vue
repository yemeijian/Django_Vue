// @author: 某小健
// @file: ModalBulletFrame.vue
// @time: 2021/2/15 15:42
// @desc:
<template>
  <div>
    <Button type="primary" @click="modal1 = true">添加</Button>
    <Modal
          v-model="modal1"
          title="Common Modal dialog box title"
          @on-ok="ok"
          @on-cancel="cancel">
          <p>Content of dialog</p>
          <p>Content of dialog</p>
          <p>Content of dialog</p>
      </Modal>
  </div>
</template>

<script>
export default {
  name: 'ModalBulletFrame',
  data () {
    return {
      modal1: false
    }
  },
  methods: {
    ok () {
      this.$Message.info('Clicked ok')
    },
    cancel () {
      this.$Message.info('Clicked cancel')
    }
  }
}
</script>

<style scoped>

</style>
