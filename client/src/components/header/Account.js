import React, { useContext, useState } from "react";
import Button from "@material-ui/core/Button";
import { ThemeContext } from "./../../contexts/ThemeContext"
import { Dialog, DialogTitle, DialogActions, DialogContent, TextField } from "@material-ui/core/";
import Alert from '@material-ui/lab/Alert';
//import { isEmail, isPassword } from '../../lib/Validation';


const Account = () => {

    const context = useContext(ThemeContext);
    const [error] = useState(false);
    const [values, setValues] = useState(context.user);

    const handleCancel = () => {
        context.setModals({
            ...context.modals,
            "account": false
        });

        setValues(context.user);
    }

    const handleSubmit = () => {
        // context.setUser(context.values);
        context.setModals({
            ...context.modals,
            "account": false
        });
    }

    const handleOpen = () => {
        context.setModals({
            ...context.modals,
            "account": true
        });
    }

    const handleChange = (e) => {
        setValues({
            ...values,
            [e.target.name]: e.target.value,
        });
    }

    return (
        <React.Fragment>
            <Button className={'account'} onClick={handleOpen} color="inherit">
                ACCOUNT
        </Button>
            <Dialog open={context.modals.account}>
                <DialogTitle id="form-dialog-title">Edit Account</DialogTitle>
                <DialogContent>
                    {error && <Alert className={'error'} severity="error">{error}</Alert>}
                    <TextField
                        id="name"
                        label="Name"
                        margin="normal"
                        onChange={handleChange}
                        type="name"
                        name="name"
                        value={values.name}
                        fullWidth
                    />
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
                    <TextField
                        label="Password"
                        margin="normal"
                        id="password"
                        name="password"
                        type="password"
                        value={values.password}
                        fullWidth
                        onChange={handleChange}
                    />
                    <TextField
                        label="Password Confirm"
                        margin="normal"
                        id="password_confirm"
                        name="password_confirm"
                        type="password"
                        value={values.password_confirm}
                        fullWidth
                        onChange={handleChange}
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
}

export default Account;