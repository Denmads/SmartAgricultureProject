interface DroneJobInfo {
    id: string,
    status: string
}

interface JobInfo {
    id: number,
    field: string,
    drones: DroneJobInfo[]
}

export type {DroneJobInfo, JobInfo};