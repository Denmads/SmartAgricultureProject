import axios from 'axios';
import DroneInfo from './models/DroneInfoModel';

async function fetchAllDroneInfo() {
    const {data} = await axios.get(process.env.REACT_APP_API_URL_BASE + "/droneinfo");
    return data
}

async function fetchAllFieldInfo() {
    const {data} = await axios.get(process.env.REACT_APP_API_URL_BASE + "/fields");
    return data
}

async function fetchDroneInfo(ids: number[]) {
    const droneInfo: DroneInfo[] = [];

    for (let id in ids) {
        const {data} = await axios.get(process.env.REACT_APP_API_URL_BASE + `/droneinfo/${id}`);
        droneInfo.push(data);
    }

    return droneInfo;
}

export {fetchAllDroneInfo, fetchAllFieldInfo, fetchDroneInfo}