import React, { useState, useContext } from 'react';
import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    TextField
} from '@material-ui/core/';
import { ThemeContext } from './../../contexts/ThemeContext';
//import { Redirect, BrowserRouter } from 'react-router-dom';
import Alert from '@material-ui/lab/Alert';

const Forgot = () => {
    const context = useContext(ThemeContext);

    const [values, setValues] = useState({
        'email': 'testing@local.dev',
        'password': 'tEsting@123',
    });

    const [error] = useState(false);
    //const [redirect] = useState(false);

    const handleCancel = () => {
        context.setModals({
            "login": false,
            "create": false
        });
    };

    const handleChange = (e) => {
        setValues({
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = () => {
        context.setModals({
            "login": false,
            "create": false
        });

        context.setLoggedIn(true);

    };

    return (
        <React.Fragment>
            <Dialog open={context.modals.forgot}>
                <DialogTitle id="form-dialog-title">Reset Account Password</DialogTitle>
                <DialogContent>
                    {error && <Alert className={'error'} severity="error">{error}</Alert>}
                    <TextField
                        id="email"
                        label="Email Address"
                        margin="normal"
                        onChange={handleChange}
                        type="email"
                        name="email"
                        value={values.email}
                        fullWidth
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleCancel} color="secondary">
                        Cancel
          </Button>
                    <Button onClick={handleSubmit} color="primary">
                        Submit
          </Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
};

export default Forgot;
