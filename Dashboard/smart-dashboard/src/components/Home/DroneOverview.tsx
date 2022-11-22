import React, {ReactElement, FC, useState, useEffect} from "react";
import {Box, Alert, Typography, Skeleton, IconButton, Popover, Stack, FormGroup, FormControlLabel, Switch, Autocomplete, TextField, AutocompleteChangeDetails} from "@mui/material";
import { useTheme } from '@mui/material/styles';
import './DroneOverview.css';
import { useQuery } from 'react-query'
import {fetchAllDroneInfo, fetchAllFieldInfo} from '../../API';
import { Scrollbar } from 'react-scrollbars-custom';
import DroneInfoCard from './DroneInfoCard'
import FilterAltIcon from '@mui/icons-material/FilterAlt';
import DroneInfo from '../../models/DroneInfoModel';
import FieldInfo from '../../models/FieldInfoModel';

const DroneOverview: FC<any> = (): ReactElement => {

    const {isLoading, isError: isErrorDrone, error: errorDrone, data: droneData} = useQuery('droneInfo', fetchAllDroneInfo, {refetchInterval: 2000})
    const {isError: isErrorField, error: errorField, data: fieldData} = useQuery('fieldInfo', fetchAllFieldInfo, {refetchInterval: 2000})

    const [displayDrones, setDisplayDrones] = useState<DroneInfo[]>([]);
    const [fields, setFields] = useState<FieldInfo[]>([]);

    const numSkeletons = [1, 2, 3, 4, 5, 6, 7];
    const theme = useTheme();

    //Filter Popover
    const [anchorEl, setAnchorEl] = React.useState<HTMLButtonElement | null>(null);

    const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    const open = Boolean(anchorEl);

    const [onJobFilter, setOnJobFilter] = useState(false);

    const [statusFilter, setStatusFilter] = useState<string[]>([]);
    const statusOptions = ["idle", "harvesting", "done"];

    useEffect(() => {
        if (droneData) {
            setDisplayDrones(droneData);
        }

        if (fieldData) {
            setFields(fieldData);
        }

        if (!droneData|| fields.length === 0) return;

        const allStatuses = statusFilter.length === 0;

        let filtered = droneData;
        if (onJobFilter)
            filtered = filtered.filter((d: DroneInfo) => d.field !== -1);

        if (!allStatuses)
            filtered = filtered.filter((d: DroneInfo) => statusFilter.includes(d.status))
        setDisplayDrones(filtered)
    }, [onJobFilter, statusFilter, droneData, fieldData])

    let combinedError = isErrorDrone || isErrorField;
    let combinedErrorMessage = [errorDrone && errorDrone instanceof Error ? errorDrone.message : "", errorField && errorField instanceof Error ? errorField.message : ""].join("<br/><br/>");

    if (fields.length !== 0)
        displayDrones.forEach(info => {
            if (typeof info.field === "number" && info.field !== -1)
                info.fieldName = fields.find(val => val.id === info.field)!.name
        })

    return (
        <>
            <Box display="flex" alignItems="center" gap="1rem">
                <Typography variant="h4">Drones</Typography>
                <IconButton size="large" sx={{mt: "7px"}} onClick={handleClick}>
                    <FilterAltIcon />
                </IconButton>
                <Popover 
                    open={open}
                    onClose={handleClose}
                    anchorEl={anchorEl}
                    anchorOrigin={{
                        vertical: 'center',
                        horizontal: 'center',
                    }}
                    transformOrigin={{
                        vertical: 'top',
                        horizontal: 'left',
                    }}
                    >
                    <Stack sx={{padding: "1rem", minWidth:"300px"}}>
                        <Typography variant="h6">Filter</Typography>
                        <FormGroup>
                            <FormControlLabel control={<Switch checked={onJobFilter} onChange={(event: React.ChangeEvent<HTMLInputElement>, checked: boolean) => {setOnJobFilter(checked)}} />} label="On Job" />
                        </FormGroup>
                        <Autocomplete
                            multiple
                            id="filter-status"
                            options={statusOptions}
                            getOptionLabel={(option) => option[0].toUpperCase() + option.substring(1)}
                            value={statusFilter}
                            renderInput={(params) => (
                            <TextField
                                {...params}
                                variant="standard"
                                label="Drone Status"
                                placeholder="Status..."
                            />
                            )}
                            onChange={(event: React.SyntheticEvent, value: string[], reason: string, details?: AutocompleteChangeDetails<string> | undefined) => {
                                setStatusFilter(value);
                            }}
                        />
                    </Stack>
                </Popover>
            </Box>
            {combinedError && <Alert severity="error" sx={{width: '100%'}}>An error happened:<br/> {combinedErrorMessage}</Alert>}
            {!combinedError && <Scrollbar disableTracksWidthCompensation thumbYProps={{style:{backgroundColor: theme.palette.secondary.main}}}>
                <div className="drone-list" >
                    {isLoading && numSkeletons.map(val => <Skeleton key={val} height={120} variant="rectangular"></Skeleton>)}
                    {!isLoading && displayDrones.map((info: DroneInfo) => <DroneInfoCard key={info.id} id={info.id} field={info.field} fieldName={info.fieldName} x={info.x} y={info.y} status={info.status}></DroneInfoCard>)}
                </div>
            </Scrollbar>}
        </>
    );
}

export default DroneOverview