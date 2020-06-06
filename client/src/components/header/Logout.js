import React from "react";
import Button from "@material-ui/core/Button";
import { ThemeContext } from '../../contexts/ThemeContext';

class Logout extends React.Component {
    static contextType = ThemeContext;

    handleClick = () => {
        this.context.setLoggedIn(false);
    }

    render() {
        return (
            <Button classes={{ root: "logout" }} onClick={this.handleClick} color="inherit">
                LOGOUT
            </Button>
        );
    }
}

export default Logout;
