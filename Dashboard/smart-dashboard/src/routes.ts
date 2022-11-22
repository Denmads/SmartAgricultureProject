import Home from './pages/Home';
import Operations from './pages/Operations';

import {FC} from 'react';

//interface
interface Route {
    key: string,
    title: string,
    path: string,
    enabled: boolean,
    component: FC<{}>
}

export const routes: Array<Route> = [
    {
        key: "home-route",
        title: "Home",
        path: "/",
        enabled: true,
        component: Home
    },
    {
        key: "operations-route",
        title: "Operations",
        path: "/operations",
        enabled: true,
        component: Operations
    }
]