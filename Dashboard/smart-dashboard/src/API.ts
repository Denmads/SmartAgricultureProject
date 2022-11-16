import axios from 'axios';

async function fetchAllDroneInfo() {
    const {data} = await axios.get(process.env.REACT_APP_API_URL_BASE + "/droneinfo");
    return data
}

async function fetchAllFieldInfo() {
    const {data} = await axios.get(process.env.REACT_APP_API_URL_BASE + "/fields");
    return data
}

async function fetchAllJobInfo() {
    const {data} = await axios.get(process.env.REACT_APP_API_URL_BASE + "/jobs");
    return data
}

export {fetchAllDroneInfo, fetchAllFieldInfo, fetchAllJobInfo}