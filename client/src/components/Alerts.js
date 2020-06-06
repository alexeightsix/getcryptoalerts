import React, { useContext, useState } from "react";
import {
  Button,
  Table,
  TableBody,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  Paper,
  Grid,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  TextField
} from "@material-ui/core/";
import SettingsIcon from "@material-ui/icons/Settings";
import Alert from '@material-ui/lab/Alert';

import { ThemeContext } from "../contexts/ThemeContext";

const Alerts = () => {

  const context = useContext(ThemeContext);
  const [resendModal, setResendModal] = useState(false);
  const [editModal, setEditModal] = useState(true);

  if (!context.logged_in)
    return "";

  const createData = (coin, rule, price, interval, protocol, enabled) => {
    return { coin, rule, price, interval, protocol, enabled };
  }

  const handleEdit = () => {
    setEditModal(true);
  }

  const handleResend = () => {
    setResendModal(true);
  };

  const handleClose = () => {
    setResendModal(false);
  };

  const alerts = [
    createData("ENJIN", ">", 0.15, 5, "SMS", "Yes"),
    createData("ENJIN", ">", 0.15, 5, "SMS", "Yes")
  ];

  return (
    <React.Fragment>

      <Dialog open={resendModal}>
        <DialogTitle id="form-dialog-title">AcSent!tivation Email Successfully Sent!</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Your activation email has been sent.
        </DialogContentText>

        </DialogContent>
        <DialogActions>

          <Button onClick={handleClose} color="primary">
            Close
    </Button>
        </DialogActions>
      </Dialog>

      <Dialog open={editModal}>
        <DialogTitle id="form-dialog-title">Edit Alert</DialogTitle>
        <DialogContent>
          <DialogContentText>
            <TextField
              label="Password"
              margin="normal"
              id="password"
              name="password"
              type="password"
              value=""
              fullWidth
              onChange=""
            />
          </DialogContentText>

        </DialogContent>
        <DialogActions>

        <Button onClick={handleClose} color="secondary">
            Cancel
    </Button>

          <Button onClick={handleClose} color="primary">
            Save
    </Button>
        </DialogActions>
      </Dialog>


      {!context.user.verified &&

        <Grid className={"verified-message"} container>
          <Grid iitem xs={9}>
            <Alert className={'error'} severity="error">Your account is not verified.</Alert>
          </Grid>
          <Grid className="align-right" item xs={3}>

            <Button onClick={handleResend} className="resend-btn" variant="outlined">Resend Activation Email</Button>

          </Grid>
        </Grid>

      }
      <TableContainer component={Paper} >
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell align="left">Coin</TableCell>
              <TableCell align="left">Rule</TableCell>
              <TableCell align="left">Price&nbsp;(USD)</TableCell>
              <TableCell align="left">Protocol</TableCell>
              <TableCell align="left">Interval&nbsp;(Minutes)</TableCell>
              <TableCell align="left">Enabled</TableCell>
              <TableCell align="left">Settings</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {alerts.map((row, index) => (
              <TableRow key={index}>
                <TableCell align="left">{row.coin}</TableCell>
                <TableCell align="left">{row.rule}</TableCell>
                <TableCell align="left">{row.price}</TableCell>
                <TableCell align="left">{row.protocol}</TableCell>
                <TableCell align="left">{row.interval}</TableCell>
                <TableCell align="left">{row.enabled}</TableCell>

                <TableCell align="left">
                  <Button className="edit-alert">
                    <SettingsIcon onClick={handleEdit} />
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer >

    </React.Fragment>

  );
}

export default Alerts;