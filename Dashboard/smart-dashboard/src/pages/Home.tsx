import React, {ReactElement, FC} from "react";
import {Box, Paper} from "@mui/material";
import { useTheme } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';
import './Home.css';
import DroneOverview from '../components/Home/DroneOverview'
import FieldOverview from '../components/Home/FieldOverview'

const Home: FC<any> = (): ReactElement => {
    //const matches = useMediaQuery('(min-width:900px)');

    const theme = useTheme();



    return (
        <Box sx={{
            flexGrow: 1,
            backgroundColor: 'whitesmoke',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            position: 'relative'
        }}>
            <div className="grid">
                <Paper id="drone-view" className="grid-item">
                    <DroneOverview />
                </Paper>
                <Paper id="field-view" className="grid-item">
                    <FieldOverview />
                </Paper>
            </div>
        </Box>
    );
};

export default Home;