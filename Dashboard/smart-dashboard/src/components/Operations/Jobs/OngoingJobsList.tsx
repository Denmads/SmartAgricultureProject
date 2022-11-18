import React, {ReactElement, FC, useState} from "react";
import {Paper, Typography, Skeleton, Alert} from '@mui/material';
import {useTheme} from '@mui/material/styles';
import { Scrollbar } from 'react-scrollbars-custom';
import {useQuery} from 'react-query';
import {fetchAllJobInfo} from '../../../API';
import JobCard from './JobCard';
import {JobInfo} from '../../../models/JobInfoModel';

interface Props {
    areaName: string;
}

const OngoingJobsList: FC<Props> = (props: Props): ReactElement => {

    const theme = useTheme();

    const {isLoading, isError, error, data} = useQuery("jobInfo", fetchAllJobInfo, {refetchInterval: 2000});

    const numSkeletons = Array.from(Array(4).keys())
    const skeletonEl = (<JobCard info={{id: 1, field: "Field 1", drones: [{id: "6b086ea2-8a21-42de-bb5e-1a1c8e408d3b", status: "done"}, {id: "07421d6c-1c69-4662-a32b-bd61dbfec7d0", status: "done"}]}}></JobCard>)

    return (
        <Paper sx={{ display: 'flex', flexDirection: 'column', gap: '1rem', padding: '1rem', gridArea: props.areaName, minHeight: "450px"}}>
            <Typography variant="h4">Active Jobs</Typography>
            {isError && error instanceof Error && <Alert severity="error" sx={{width: '100%'}}>An error happened:<br/> {error.message}</Alert>}
            {!isError && <Scrollbar disableTracksWidthCompensation thumbYProps={{style:{backgroundColor: theme.palette.secondary.main}}}>
                <div style={{display: 'flex', flexDirection: 'column', gap: '1rem', paddingRight: '1rem', marginTop: '1rem'}} >
                    {isLoading && numSkeletons.map(v => <Skeleton key={v}>{skeletonEl}</Skeleton>)}
                    {!isLoading && data.map((j: JobInfo) => <JobCard key={j.id} info={j}></JobCard>)}
                </div>
            </Scrollbar>}
        </Paper>
    );
}

export default OngoingJobsList