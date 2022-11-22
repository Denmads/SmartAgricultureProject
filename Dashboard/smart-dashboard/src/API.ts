import axios from 'axios';
import FieldInfo from './models/FieldInfoModel';
import DroneInfo from './models/DroneInfoModel';

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

async function createJob (field: FieldInfo, drones: DroneInfo[]) {
    const {data, status, statusText} = await axios.post(process.env.REACT_APP_API_URL_BASE + "/job", {field: field.id, drones: drones.map(d => d.id)});
    return {data, status, statusText};
}

async function stopJob (id: number) {
    const {status, statusText} = await axios.delete(process.env.REACT_APP_API_URL_BASE + "/job?id=" + id);
    return {status, statusText};
}

async function createField (info: {name: string, width: number, height: number}) {
    const {data, status, statusText} = await axios.post(process.env.REACT_APP_API_URL_BASE + "/field", info);
    return {data, status, statusText};
}

async function deleteField (id: number) {
    const {status, statusText} = await axios.delete(process.env.REACT_APP_API_URL_BASE + "/field?id=" + id);
    return {status, statusText};
}

export {fetchAllDroneInfo, fetchAllFieldInfo, fetchAllJobInfo, createJob, createField, stopJob, deleteField}