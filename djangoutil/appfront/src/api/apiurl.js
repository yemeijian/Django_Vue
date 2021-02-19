// 公共路径和请求地址配置

// 全局域名
const domain = 'https://localhost'

// 各个接口url
const apiList = {
  fundInfo: '/api/fundinfo'
}

// 域名和接口拼接api url
// eslint-disable-next-line camelcase
const domain_url = function () {
  let api = {}
  for (let i in apiList) {
    api[i] = domain + apiList[i]
  }
  return api
}

// 导出
export default {
  domain_url
}
