import React, {ReactElement, FC} from "react";
import {Card, CardContent, Chip, Typography, Divider} from '@mui/material';
import './DroneInfoCard.css';
import BatteryFullIcon from '@mui/icons-material/BatteryFull';
import DroneInfo from '../../models/DroneInfoModel'

const chipColors: { [key: string]: "info" | "warning" | "success"} = {
    "idle": "info",
    "harvesting": "warning",
    "done": "success"
}

const DroneInfoCard: FC<DroneInfo> = (props: DroneInfo): ReactElement => {

    const statusDisplay = props.status[0].toUpperCase() + props.status.substring(1);

    return (
        <Card variant="outlined">
            <CardContent>
                <div className="drone-info-container">
                    <div className="drone-info-header">
                        <BatteryFullIcon />
                        <Chip label={statusDisplay} color={chipColors[props.status]}/>
                    </div>
                    <div className="drone-info-id">
                        <Typography color="grey">ID:</Typography><Typography variant="subtitle1">{props.id}</Typography>
                    </div>
                    {props.field !== -1 && <div className="drone-info-job">
                        <Divider>Job Info</Divider>
                        <div className="drone-info-job-fields">
                            <div className="drone-info-job-field" id="id">
                                <Typography color="grey">Field:</Typography><Typography variant="subtitle1">{props.fieldName}</Typography>
                            </div>
                            <div className="drone-info-job-field" id="x">
                                <Typography color="grey">X:</Typography><Typography variant="subtitle1">{props.x}</Typography>
                            </div>
                            <div className="drone-info-job-field" id="y">
                                <Typography color="grey">Y:</Typography><Typography variant="subtitle1">{props.y}</Typography>
                            </div>
                        </div>
                    </div>}
                </div>
            </CardContent>
        </Card>
    );
}

export default DroneInfoCard