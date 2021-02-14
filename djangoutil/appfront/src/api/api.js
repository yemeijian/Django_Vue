import axiosInstance from './index'

const axios = axiosInstance

export const getFundInfo = () => {
  return axios.get(`http://localhost:8000/api/fundinfo/`)
}

export const postFundInfo = (fundName, fundCode, isMonitor) => {
  return axios.post(`http://localhost:8000/api/fundinfo/`, {
    'fundName': fundName,
    'fundCode': fundCode,
    'isMonitor': isMonitor
  })
}
