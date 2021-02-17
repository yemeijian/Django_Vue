import axiosInstance from './index'

const axios = axiosInstance

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
