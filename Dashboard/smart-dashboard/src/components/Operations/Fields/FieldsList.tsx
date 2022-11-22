import React, {ReactElement, FC, useState} from "react";
import {Paper, Typography, Skeleton, Alert} from '@mui/material';
import {useTheme} from '@mui/material/styles';
import { Scrollbar } from 'react-scrollbars-custom';
import {useQuery} from 'react-query';
import {fetchAllFieldInfo} from '../../../API';
import FieldCard from './FieldCard';
import FieldInfo from '../../../models/FieldInfoModel';

interface Props {
    areaName: string;
}

const FieldsList: FC<Props> = (props: Props): ReactElement => {

    const theme = useTheme();

    const {isLoading, isError, error, data} = useQuery("fieldInfo", fetchAllFieldInfo, {refetchInterval: 2000});

    const numSkeletons = Array.from(Array(4).keys())
    const skeletonEl = (<FieldCard info={{id: 1, name: "Field 1", width: 450, height:300}}></FieldCard>)

    return (
        <Paper sx={{ display: 'flex', flexDirection: 'column', gap: '1rem', padding: '1rem', gridArea: props.areaName, minHeight: "450px"}}>
            <Typography variant="h4">Active Jobs</Typography>
            {isError && error instanceof Error && <Alert severity="error" sx={{width: '100%'}}>An error happened:<br/> {error.message}</Alert>}
            {!isError && <Scrollbar disableTracksWidthCompensation thumbYProps={{style:{backgroundColor: theme.palette.secondary.main}}}>
                <div style={{display: 'flex', flexDirection: 'column', gap: '1rem', paddingRight: '1rem', marginTop: '1rem'}} >
                    {isLoading && numSkeletons.map(v => <Skeleton key={v}>{skeletonEl}</Skeleton>)}
                    {!isLoading && data.map((j: FieldInfo) => <FieldCard key={j.id} info={j}></FieldCard>)}
                </div>
            </Scrollbar>}
        </Paper>
    );
}

export default FieldsList