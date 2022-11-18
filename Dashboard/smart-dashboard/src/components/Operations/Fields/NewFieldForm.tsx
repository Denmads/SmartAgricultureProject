import React, {ReactElement, FC, useState} from "react";
import {Paper, Typography, Alert, Button, Snackbar, useMediaQuery, TextField} from "@mui/material";
import {createField} from '../../../API';

interface Props {
    areaName: string;
}

interface NewFieldInfo {
    name: string,
    width: number,
    height: number
}

const NewFieldForm: FC<Props> = (props: Props): ReactElement => {

    const matches = useMediaQuery('(max-width:900px)');

    const [nameError, setNameError] = useState<string | undefined>(undefined);
    const [widthError, setWidthError] = useState<string | undefined>(undefined);
    const [heightError, setHeightError] = useState<string | undefined>(undefined);

    const [newInfo, setNewInfo] = useState<NewFieldInfo>({name: "", width: 0, height: 0});
    const [snackOpen, setSnackOpen] = useState(false);
    const [snackSeverity, setSnackSeverity] = useState<"success" | "error">("success");
    const [snackMessage, setSnackMessage] = useState("");

    const snackClose = (event?: React.SyntheticEvent | Event, reason?: string) => {
        if (reason === "clickaway") return;

        setSnackOpen(false);
    }

    const displaySnack = (severity: "success" | "error", message: string) => {
        setSnackSeverity(severity);
        setSnackMessage(message);
        setSnackOpen(true);
    }

    const nameChanged = (event: React.ChangeEvent<HTMLInputElement>) => {
        let name: string = event.target.value;

        if (name.length === 0) {
            setNameError("Name can't be empty");
            return;
        }

        setNameError(undefined);
        setNewInfo({...newInfo, name: name});
    }

    const widthChanged = (event: React.ChangeEvent<HTMLInputElement>) => {
        let width: number = event.target.value === "" ? -1 : Math.floor(parseFloat(event.target.value));

        if (width <= 0) {
            setWidthError("Width must be greater than zero");
            return;
        }

        setWidthError(undefined);
        setNewInfo({...newInfo, width: width});
    }

    const heightChanged = (event: React.ChangeEvent<HTMLInputElement>) => {
        let height: number = event.target.value === "" ? -1 : Math.floor(parseFloat(event.target.value));

        if (height <= 0) {
            setHeightError("Width must be greater than zero");
            return;
        }

        setHeightError(undefined);
        setNewInfo({...newInfo, height: height});
    }

    const onClick = async () => {
        if (nameError || widthError || heightError) {
            displaySnack("error", "Resolve errors!");
            return;
        }

        if (newInfo.name === "" || newInfo.width <= 0 || newInfo.height <= 0) {
            displaySnack("error", "Fields cannot be empty!");
            return;
        }

        const {data, status, statusText} = await createField(newInfo);

        if (status !== 200) {
            displaySnack("success", "Field created!");
        }
        else {
            displaySnack("error", `Error ${status} - ${statusText}`);
            return;
        }
    }

    return (
        <Paper sx={{position: "relative", display: 'flex', flexDirection: 'column', gap: '1rem', padding: '1rem', gridArea: props.areaName}}>
            <Typography variant="h4">New Field</Typography>
            <TextField label="Name" variant="outlined" onChange={nameChanged} error={nameError !== undefined} helperText={nameError ? nameError : ""}/>
            <TextField label="Width" variant="outlined" type="number" onChange={widthChanged} error={widthError !== undefined} helperText={widthError ? widthError : ""}/>
            <TextField label="Height" variant="outlined" type="number" onChange={heightChanged} error={heightError !== undefined} helperText={heightError ? heightError : ""}/>
            <Button variant="contained" sx={matches ? {width: "100%"} : {width: "35%"}} onClick={onClick}>Create Job</Button>
            <Snackbar open={snackOpen} autoHideDuration={6000} onClose={snackClose} anchorOrigin={{vertical: 'bottom', horizontal: 'right'}}>
                <Alert onClose={snackClose} severity={snackSeverity} sx={{width: '100%'}}>
                    {snackMessage}
                </Alert>
            </Snackbar>
        </Paper>
    );
};

export default NewFieldForm;