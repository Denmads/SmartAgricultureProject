import React, {ReactElement, FC, useState} from "react";
import OngoingJobsList from './OngoingJobsList';
import NewJobForm from './NewJobForm';
import '../Tab.css';

const JobsTab: FC<any> = (): ReactElement => {

    return (
        <div className="tab">
            <OngoingJobsList areaName="jblst" />
            <NewJobForm areaName="jbfrm"/>
        </div>
    );
}

export default JobsTab