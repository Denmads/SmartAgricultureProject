import React, {ReactElement, FC, useState, useEffect} from "react";
import {Typography, FormControl, InputLabel, Select, MenuItem, SelectChangeEvent} from "@mui/material";
import FieldInfo from "../../models/FieldInfoModel";
import {useQuery} from 'react-query';
import {fetchAllFieldInfo, fetchAllDroneInfo} from '../../API';
import useMediaQuery from '@mui/material/useMediaQuery';
import FieldView from './FieldView';
import DroneInfo from "../../models/DroneInfoModel";

const FieldOverview: FC<any> = (): ReactElement => {

    const matches = useMediaQuery('(max-width:900px)');
    const mWidth = matches ? "100%" : "33%";

    const {isLoading: isLoadingField, isError: isErrorField, error: errorField, data: fieldData} = useQuery('fieldInfo', fetchAllFieldInfo)
    const {isLoading: isLoadingDrone, isError: isErrorDrone, error: errorDrone, data: droneData} = useQuery('droneInfo', fetchAllDroneInfo, {
                                                                                                                                            refetchInterval: 2000
                                                                                                                                        })

    const [fields, setFields] = useState<FieldInfo[]>([])
    const [field, setField] = useState<FieldInfo | undefined>(undefined)                                                                                                                             
    
    useEffect(() => {
        if (!fieldData) return;

        setFields(fieldData)
        setField(fieldData[0])
    }, [fieldData])

    return (
        <>
            <Typography variant="h4">Field View</Typography>
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
            <FieldView info={field} drones={droneData && field ? droneData.filter((d: DroneInfo) => d.field === field.id): []}/>
        </>
    )
}

export default FieldOverview