import React, {ReactElement, FC} from "react";
import {Card, CardContent, Typography, Stack, Divider, IconButton} from '@mui/material';
import {JobInfo} from '../../../models/JobInfoModel';
import './JobCard.css';
import DroneItem from './DroneItem';
import LinearProgressWithLabel from '../../LinearProgressWithLabel';
import CancelIcon from '@mui/icons-material/Cancel';
import {stopJob} from '../../../API';

interface Props {
    info: JobInfo
}

const JobsCard: FC<Props> = (props: Props): ReactElement => {

    return (
        <Card variant="outlined">
            <CardContent>
                <div className="job-info-container">
                    <Stack direction="row" alignItems="center" justifyContent="space-between">
                        <Typography variant="h5">Job on {props.info.field}</Typography>
                        <IconButton color="error" onClick={() => {
                            stopJob(props.info.id)
                        }}>
                            <CancelIcon />
                        </IconButton>
                    </Stack>
                    <LinearProgressWithLabel value={45} />
                    <Typography variant="h6" sx={{textDecoration: 'underline'}}>Drones</Typography>
                    <Stack divider={<Divider flexItem />} spacing={2}>
                        {props.info.drones.map(d => <DroneItem key={d.id} info={d}/>)}
                    </Stack>
                </div>
            </CardContent>
        </Card>
    );
}

export default JobsCard