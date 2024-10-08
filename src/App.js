
import theme from './theme';
import React from "react";
import Nav from "./nav";
import {
    HashRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import {Home} from "./pages/home";
import Simulation from "./pages/simulation"
import {ThemeProvider} from "@mui/material";
import { LanguageProvider } from './components/LanguageContext';


function App() {
    return (
        <>
            <ThemeProvider theme={theme}>
                <LanguageProvider>
                    <Router>
                        <Nav/>
                        <Routes>
                                <Route path="/" element={<Home />} />
                                <Route path="/simulation" element={<Simulation />} />
                        </Routes>
                    </Router>
                </LanguageProvider>
            </ThemeProvider>
        </>
    );
}

export default App;