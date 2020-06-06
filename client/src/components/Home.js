import React, { useContext } from 'react';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Register from './Register';
import { ThemeContext } from '../contexts/ThemeContext';

const Home = () => {

    const context = useContext(ThemeContext);

    if (context.logged_in)
        return "";

    return (<Grid className={'home'} container spacing={0}>
        <Grid className={'header'} item xs={12}>
            <Typography variant="h2" component="h2">
                Send me an email as soon as BTC goes above the price of 0.11 USD
    </Typography>
            <Register />
        </Grid>
    </Grid >
    )
}

export default Home;