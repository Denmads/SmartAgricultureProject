import React, {ReactElement, FC, useState} from "react";
import {Box, Tab} from "@mui/material";
import {TabContext, TabList, TabPanel} from '@mui/lab';
import JobsTab from '../components/Operations/Jobs/JobsTab'
import FieldsTab from '../components/Operations/Fields/FieldsTab'

const Operations: FC<any> = (): ReactElement => {
    const [tabValue, setTabValue] = useState('1');

    const handleChange = (event: React.SyntheticEvent, newValue: string) => {
        setTabValue(newValue);
    };

    return (
        <Box sx={{
            flexGrow: 1,
            backgroundColor: 'whitesmoke',
            display: 'flex',
            flexDirection: 'column'
        }}>
            <TabContext value={tabValue}>
                <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <TabList textColor="secondary" indicatorColor="secondary" onChange={handleChange} >
                        <Tab label="Jobs" value="1" />
                        <Tab label="Fields" value="2" />
                    </TabList>
                </Box>
                <TabPanel value="1" sx={{height: '100%', padding: '0'}}><JobsTab /></TabPanel>
                <TabPanel value="2" sx={{height: '100%', padding: '0'}}><FieldsTab /></TabPanel>
            </TabContext>
        </Box>
    );
};

export default Operations;