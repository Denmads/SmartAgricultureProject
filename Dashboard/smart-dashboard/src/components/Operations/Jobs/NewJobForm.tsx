import React, {ReactElement, FC, useState, useEffect} from "react";
import {Paper, Typography, FormControl, InputLabel, Select, Alert, Button, MenuItem, Snackbar, SelectChangeEvent, useMediaQuery, Stack, useTheme, CircularProgress, Checkbox, FormControlLabel, FormGroup} from "@mui/material";
import {useQuery} from 'react-query';
import FieldInfo from '../../../models/FieldInfoModel';
import {fetchAllFieldInfo, fetchAllDroneInfo, createJob} from '../../../API';
import Scrollbar from 'react-scrollbars-custom';
import DroneInfo from '../../../models/DroneInfoModel';
import axios from 'axios';

interface Props {
    areaName: string;
}

const NewJobForm: FC<Props> = (props: Props): ReactElement => {

    const matches = useMediaQuery('(max-width:900px)');
    const mWidth = matches ? "100%" : "33%";

    const {isLoading: isLoadingField, isError: isErrorField, error: errorField, data: fieldData} = useQuery('fieldInfo', fetchAllFieldInfo, {refetchInterval: 2000})
    const {isLoading, isError: isErrorDrone, error: errorDrone, data: droneData} = useQuery('droneInfo', fetchAllDroneInfo, {refetchInterval: 2000})

    const [fields, setFields] = useState<FieldInfo[]>([]);
    const [field, setField] = useState<FieldInfo | undefined>(undefined);
    const [selectedDrones, setSelectedDrones] = useState<DroneInfo[]>([]);
    const [snackOpen, setSnackOpen] = useState(false);
    const [snackSeverity, setSnackSeverity] = useState<"success" | "error">("success");
    const [snackMessage, setSnackMessage] = useState("");

    const snackClose = (event?: React.SyntheticEvent | Event, reason?: string) => {
        if (reason === "clickaway") return;

        setSnackOpen(false);
    }

    const theme = useTheme();

    useEffect(() => {
        if (!fieldData) return;

        setFields(fieldData);
        setField(fieldData[0]);
    }, [fieldData])

    const handleCheck = (checked: boolean, drone: DroneInfo) => {
        if (checked) {
            setSelectedDrones([...selectedDrones, drone])
        }
        else {
            setSelectedDrones(selectedDrones.filter(d => d.id !== drone.id));
        }
    }

    const displaySnack = (severity: "success" | "error", message: string) => {
        setSnackSeverity(severity);
        setSnackMessage(message);
        setSnackOpen(true);
    }

    const onClick = async () => {
        if (!field) {
            displaySnack("error", "No field selected!");
            return;
        }

        if (selectedDrones.length === 0) {
            displaySnack("error", "At least one drone must be selected!");
            return;
        }

        const {data, status, statusText} = await createJob(field, selectedDrones);

        if (status === 200) {
            displaySnack("success", "Job created!");
        }
        else {
            displaySnack("error", `Error ${status} - ${statusText}`);
            return;
        }
    }

    return (
        <Paper sx={{position: "relative", display: 'flex', flexDirection: 'column', gap: '1rem', padding: '1rem', gridArea: props.areaName}}>
            <Typography variant="h4">New Job</Typography>
            <FormControl sx={{maxWidth:mWidth}}>
                <InputLabel id="field-select-label">Field</InputLabel>
                <Select
                    labelId="field-select-label"
                    id="field-select"
                    value={field ? field.id : ''}
                    label="Field"
                    onChange={(event: SelectChangeEvent<number>) => {
                        const id = event.target.value;
                        setField(fields.find(f => f.id === id)!);
                      }}
                >
                    {!isErrorField && !isLoadingField && fields.map(f => <MenuItem key={f.id} value={f.id}>{f.name}</MenuItem>)}
                </Select>
            </FormControl>
            <Typography variant="h5">Available Drones</Typography>
            <Scrollbar disableTracksWidthCompensation thumbYProps={{style:{backgroundColor: theme.palette.secondary.main}}}>
                <Stack spacing={1} sx={{width: "fit-content"}}>
                    {isLoading && <CircularProgress />}
                    {!isLoading && droneData.filter((d: DroneInfo ) => d.status === "idle").map((d: DroneInfo) => (<FormGroup key={d.id}>
                        <FormControlLabel control={<Checkbox color="secondary" onChange={(event: React.ChangeEvent<HTMLInputElement>) => handleCheck(event.target.checked, d)}></Checkbox>} label={d.id} />
                    </FormGroup>))}
                </Stack>
            </Scrollbar>
            <Button variant="contained" sx={matches ? {width: "100%"} : {width: "35%"}} onClick={onClick}>Create Job</Button>
            <Snackbar open={snackOpen} autoHideDuration={6000} onClose={snackClose} anchorOrigin={{vertical: 'bottom', horizontal: 'right'}}>
                <Alert onClose={snackClose} severity={snackSeverity} sx={{width: '100%'}}>
                    {snackMessage}
                </Alert>
            </Snackbar>
        </Paper>
    );
};

export default NewJobForm;