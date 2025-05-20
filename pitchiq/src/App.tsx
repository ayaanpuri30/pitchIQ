import "./App.css";
import Navbar from "./Navbar.tsx";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LeaguePage from "./LeaguePage.tsx";
import Sample from "./SampleClub.tsx";
import About from "./About.tsx";
import Credits from "./Credits.tsx"
import { useState } from 'react';

function App() {
  const [clubData, setClubData] = useState<any>(null);
  return (
    <Router>
      <div className="app">
        <Navbar />
        <div className="content">
          <Routes>
            <Route path="/" element={<LeaguePage setClubData={setClubData} />} />
            <Route path="/atl" element={<Sample data={clubData} />} />
            <Route path="/about" element={<About />} />
            <Route path="/credits" element={<Credits />} />
          </Routes>
        </div>
      </div>
    </Router>
  );  
}

export default App;
