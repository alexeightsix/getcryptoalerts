import React, { useState, useContext } from 'react';
import {
  Button,
  Dialog,
  Link,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  TextField
} from '@material-ui/core/';
import { ThemeContext } from './../../contexts/ThemeContext';
//import { Redirect, BrowserRouter } from 'react-router-dom';
import Alert from '@material-ui/lab/Alert';

const Login = () => {
  const context = useContext(ThemeContext);

  const [values, setValues] = useState({
    email: 'testing@local.dev',
    password: 'tEsting@123',
  });

  const [error] = useState(false);
  //const [redirect] = useState(false);

  const handleOpen = () => {
    context.setModals({
      ...context.modals,
      login: true,
    });
  };
  const handleCancel = () => {
    context.setModals({
      ...context.modals,
      login: false,
    });
  };

  const handleChange = (e) => {
    setValues({
      [e.target.name]: e.target.value,
    });
  };

  const handleCreate = (e) => {
    e.preventDefault();
    context.setModals({
      login: false,
      create: true
    });
  };

  const handleForgot = (e) => {
    e.preventDefault();
    context.setModals({
      ...context.modals,
      login: false,
      forgot: true
    });
  };

  const handleSubmit = () => {
    context.setModals({
      "login": false,
      "create": false
    });

    context.setUser({
      name: 'John Doe',
      email: 'testing@local.dev',
      password: 'jogl4ife',
      verified: false
    });
    
    context.setLoggedIn(true);

  };

  return (
    <React.Fragment>
      <Button className={'login'} onClick={handleOpen} color="inherit">
        LOGIN
      </Button>
      <Dialog open={context.modals.login}>
        <DialogTitle id="form-dialog-title">Login</DialogTitle>
        <DialogContent>
          {error && <Alert className={'error'} severity="error">{error}</Alert>}

          <DialogContentText><Link onClick={handleCreate} href="#">Create Account</Link></DialogContentText>
          <DialogContentText><Link onClick={handleForgot} href="#">Forgot your password?</Link></DialogContentText>
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

export default Login;
