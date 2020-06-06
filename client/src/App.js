import React from "react";
import Container from "@material-ui/core/Container";
import Header from "./components/header/Header"
import ThemeContextProvider from './contexts/ThemeContext';
import "./styles.css";
import Alerts from "./components/Alerts"
import Home from "./components/Home"

const App = () => {
  return (
    <ThemeContextProvider>
      <Container>
        <Header />
        <Home />
        <Alerts />
      </Container>
    </ThemeContextProvider>
  );
}

export default App;