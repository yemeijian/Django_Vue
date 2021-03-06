import axiosInstance from './index'

const axios = axiosInstance

// 获取菜单
export const getMenu = () => {
  try {
    return axios.get('http://localhost:8000/admin/api/menu/')
  } catch (e) {
    console.log(e)
  }
}
export const getFundInfo = () => {
  try {
    return axios.get('../api/fundinfo/')
  } catch (e) {
    console.log(e)
  }
}

export const postFundInfo = (fundName, fundCode, isMonitor) => {
  return axios.post('../api/fundinfo/', {
    'fundName': fundName,
    'fundCode': fundCode,
    'isMonitor': isMonitor
  })
}
