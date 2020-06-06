import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import axios from "axios"
import { withRouter } from "react-router-dom";


class UserActivation extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            code: this.props.match.params.code
        }

        axios.post('http://getcryptoalerts.com:5000/api/user/activate/', {
            code: this.state.code,
        }).then(() => {
            this.props.history.push("/?login");

        }).catch((error) => {
            this.props.history.push("/?error=invalid_code");
        })

    }
    render() {
        return ""
    }
}

export default UserActivation;
