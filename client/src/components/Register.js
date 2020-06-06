import React, { useContext, useState } from "react";
import {
  Button,
  TextField,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle
} from "@material-ui/core/";
import Alert from '@material-ui/lab/Alert';
import { ThemeContext } from '../contexts/ThemeContext';
import { isEmail, isPassword } from '../lib/Validation';


const Register = () => {

  const context = useContext(ThemeContext);
  const [error, setError] = useState(false);
  const [values, setValues] = useState({
    'name': 'John Doe',
    'email': 'jon@local.dev',
    'password': 'joHN1@2!',
    'password_confirm': 'joHN1@2!',

  });

  const handleOpen = () => {
    context.setModals({
      ...context.modals,
      "create": true,
    });
  }

  const handleCancel = () => {
    context.setModals({
      ...context.modals,
      "create": false,
    });
  }

  const handleChange = (e) => {
    setValues({
      ...values,
      [e.target.name]: e.target.value,
    });
  }

  /*const handleSuccess = () => {
    context.setLoggedIn(true);
    context.setModals({
      ...context.modals,
      "create": false,
    });
  }
  */

  const handleSubmit = () => {

    let error;

    if (!values.name) {
      error = "Name field is missing."
    } else if (!isEmail(values.email)) {
      error = "Email field is missing or invalid."
    } else if (!isPassword(values.password)) {
      error = "Password field is missing or invalid. Passwords must be atleast 6 characters long."
    } else if (!values.password_confirm) {
      error = "Confirm Password field is missing."
    } else if (values.password !== values.password_confirm) {
      error = "Passwords do not match."
    }

    if (error) {
      setError(error)
    } else {

      context.setModals({
        ...context.modals,
        "create": false,
      });

      context.setUser({
        name: 'John Doe',
        email: 'testing@local.dev',
        password: 'jogl4ife',
        verified: false
      });

      context.setLoggedIn(true);



      //context.setModals
      // close modal
      // set user
      // set logged in

    }
  }

  return (
    <React.Fragment>
      <Button onClick={handleOpen} variant="contained" color="secondary">CREATE NEW ALERT (FREE)</Button>
      <Dialog open={context.modals.create}>
        <DialogTitle id="form-dialog-title">Account Registration</DialogTitle>
        <DialogContent>
          {error && <Alert className={'error'} severity="error">{error}</Alert>}
          <DialogContentText>
            To register to this website, please enter your email address and
            password here. We will send a confirmation email upon submission
            of this form.
        </DialogContentText>
          <TextField
            autoFocus
            margin="normal"
            id="name"
            label="Name"
            type="name"
            name="name"
            value={values.name}
            fullWidth
            onChange={handleChange}
          />
          <TextField
            margin="normal"
            id="email"
            label="Email Address"
            type="email"
            name="email"
            value={values.email}
            fullWidth
            onChange={handleChange}
          />
          <TextField
            margin="normal"
            id="password"
            label="Password"
            type="password"
            onChange={handleChange}
            name="password"
            value={values.password}
            fullWidth
          />
          <TextField
            margin="normal"
            id="password_confirm"
            label="Confirm Password"
            type="password"
            name="password_confirm"
            value={values.password_confirm}
            onChange={handleChange}
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

export default Register;