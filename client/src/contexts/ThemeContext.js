import React, { createContext, useState } from 'react';
//import axios from 'axios';
//import Cookies from 'universal-cookie';
export const ThemeContext = createContext();

const ThemeContextProvider = (props) => {

    const [site_title] = useState("Get Crypto Alerts");
    const [site_url] = useState("http://getcryptoalerts.com:5000");
    const [logged_in, setLoggedIn] = useState(true);
    const [user, setUser] = useState({
        name: 'John Doe',
        email: 'testing@local.dev',
        password: 'jogl4ife',
        verified: false
    });
    const [modals, setModals] = useState({
        login: false,
        forgot: false,
        create: false,
        account: false
    })

    /*const login = async (email, password) => {
        return new Promise(async (resolve, reject) => {
            await axios.post(`${this.state.site_url}/api/user/login/`, {
                email, password
            }).then((response) => {
                resolve(response);
            }).catch((error) => {
                reject(error);
            })
        })
    }*/

    return (
        <ThemeContext.Provider value={
            {
                site_title, logged_in, user, site_url, modals,
                setLoggedIn,
                setUser,
                setModals
            }}>
            {props.children}
        </ThemeContext.Provider>
    );
}

export default ThemeContextProvider;