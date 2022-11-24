import React, {ReactElement, FC} from "react";
import {Card, CardContent, Typography, Stack, IconButton} from '@mui/material';
import FieldInfo from '../../../models/FieldInfoModel';
import DeleteIcon from '@mui/icons-material/Delete';
import {deleteField} from '../../../API';

interface Props {
    info: FieldInfo
}

const FieldCard: FC<Props> = (props: Props): ReactElement => {

    return (
        <Card variant="outlined">
            <CardContent>
                <div className="job-info-container">
                    <Stack direction="row" alignItems="center" justifyContent="space-between">
                        <Typography variant="h5">{props.info.name}</Typography>
                        <IconButton color="error" onClick={() => {
                            deleteField(props.info.id);
                        }}>
                            <DeleteIcon />
                        </IconButton>
                    </Stack>
                    <Stack direction="row" alignItems="center" justifyContent="flex-start" spacing={5}>
                        <Stack direction="row" spacing={1}><Typography color="grey">Width:</Typography><Typography variant="subtitle1">{props.info.width}</Typography></Stack>
                        <Stack direction="row" spacing={1}><Typography color="grey">Height:</Typography><Typography variant="subtitle1">{props.info.height}</Typography></Stack>
                    </Stack>
                </div>
            </CardContent>
        </Card>
    );
}

export default FieldCard