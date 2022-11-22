import React, {ReactElement, FC, useState} from "react";
import FieldsList from './FieldsList';
import NewFieldForm from './NewFieldForm';
import '../Tab.css';

const FieldsTab: FC<any> = (): ReactElement => {

    return (
        <div className="tab">
            <FieldsList areaName="jblst" />
            <NewFieldForm areaName="jbfrm"/>
        </div>
    );
}

export default FieldsTab