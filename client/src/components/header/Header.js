import React, { useContext } from "react";
import { Grid, Toolbar, Typography } from "@material-ui/core/";
import { ThemeContext } from "./../../contexts/ThemeContext"
import AnnouncementOutlinedIcon from "@material-ui/icons/AnnouncementOutlined";
import Account from "./Account"
import Login from "./Login";
import Logout from "./Logout"
import Forgot from "./Forgot"


const Header = () => {

  const context = useContext(ThemeContext);

  return (
    <div>
      <Toolbar>
        <Grid container spacing={0}>
          <Grid item xs={6}>
            <Typography variant="h5" className="upper" component="h5">
              {context.site_title}
              <AnnouncementOutlinedIcon className={"announcement"} />
            </Typography>
          </Grid>
          <Grid className={'navigation'} item xs={6}>
            {
              context.logged_in ?
                <React.Fragment>
                  <Account />
                  <Logout />
                </React.Fragment>
                :
                <React.Fragment>
                  <Forgot />
                  <Login />
                </React.Fragment>
            }
          </Grid>
        </Grid>
      </Toolbar>
    </div>
  )
}

export default Header;