import React, {ReactElement, FC} from "react";
import {Box, Typography, Grid} from "@mui/material";
import useMediaQuery from '@mui/material/useMediaQuery';


const Home: FC<any> = (): ReactElement => {
    const matches = useMediaQuery('(min-width:900px)');

    return (
        <Box sx={{
            flexGrow: 1,
            backgroundColor: 'whitesmoke',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center'
        }}>
            <Grid container spacing={2} direction={matches ? 'row' : 'column-reverse'}>
                <Grid item xs={12} md={4}>
                    <Typography>Hello</Typography>
                </Grid>
                <Grid item xs={12} md={8}>
                    <Typography>Other</Typography>
                </Grid>
            </Grid>
        </Box>
    );
};

export default Home;