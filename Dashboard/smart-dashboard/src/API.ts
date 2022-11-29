import axios from 'axios';
import FieldInfo from './models/FieldInfoModel';
import DroneInfo from './models/DroneInfoModel';

let base = "http://localhost:3000"

async function fetchAllDroneInfo() {
    const {data} = await axios.get(base + "/droneinfo");
    return data
}

async function fetchAllFieldInfo() {
    const {data} = await axios.get(base + "/fields");
    return data
}

async function fetchAllJobInfo() {
    const {data} = await axios.get(base + "/jobs");
    return data
}

async function createJob (field: FieldInfo, drones: DroneInfo[]) {
    const {data, status, statusText} = await axios.post(base + "/job", {field: field.id, drones: drones.map(d => d.id)});
    return {data, status, statusText};
}

async function stopJob (id: number) {
    const {status, statusText} = await axios.delete(base + "/job?id=" + id);
    return {status, statusText};
}

async function createField (info: {name: string, width: number, height: number}) {
    const {data, status, statusText} = await axios.post(base + "/field", info);
    return {data, status, statusText};
}

async function deleteField (id: number) {
    const {status, statusText} = await axios.delete(base + "/field?id=" + id);
    return {status, statusText};
}

async function getDroneImage(id: string) {
    const {data} = await axios.get(base + "/getdroneimage?id=" + id);
    return data;
}

export {fetchAllDroneInfo, fetchAllFieldInfo, fetchAllJobInfo, createJob, createField, stopJob, deleteField, getDroneImage}