
import "./App.css";
import "./SampleClub.css"; // New CSS file for SampleClub styling
import Navbar from "./Navbar.tsx";
import PlayerData from "./PlayerData.tsx";

interface TeamProps {
  data: any; // actual squad/team object, not just string name
}
const Sample: React.FC<TeamProps> = ({ data }) => { 
  // State to manage active tabs for the player data section
  
  if (!data) {
    return <p className="text-white">Loading squad data...</p>;
  }
  return (
    <>
      <Navbar />

      <div className="club-container">
        {/* Club Header */}
        <div className="club-header-section">
          <div className="content-box club-header-left">
            <img src={data.club_logo} alt="Club Logo" className="club-logo" />
            <h1 className="club-name">{data.club_name}</h1>
          </div>

          {/* Coach Stats Section */}
          <div className="content-box coach-stats-box">
              <h3>Coach Win Percentage</h3>
              <div className="coach-stats-content">
                {/* Dummy values for now */}
                <div className="stats-row">
                  <div className="stat-item"><div className="stat-percent">50%</div><div className="stat-label">2.0 Pts</div></div>
                  <div className="stat-item"><div className="stat-percent">50%</div><div className="stat-label">2.0 Pts</div></div>
                </div>
                <div className="stats-seasons">
                  <div className="season">22/23</div>
                  <div className="season">23/24</div>
                </div>
              </div>
          </div>

          {/* Coach image */}
          <div className="head-box club-header-right">
            <img src={data.manager_photo} alt="Coach" className="coach-image" />
          </div>
        </div>

        {/* Main Content */}
        <div className="club-content">
          <div className="club-column club-left-column">
            {/* Description Box */}
            <div className="content-box description-box">
              {data.playstyle_summaries?.length > 0 ? (
                <p>{data.playstyle_summaries[0].gpt_summary}</p>
              ) : (
                <p>No playstyle summary available for this club.</p>
              )}
            </div>

            {/* Player Data */}
            <PlayerData data={data} />
          </div>

          {/* Right Column */}
          <div className="club-column club-right-column">
            {/* Formation Visualization */}
            <div className="content-box formation-box">
              <h3>Team Formation</h3>
              <div className="formation-content">
                <div className="pitch-outline">
                  {/* 11 Player Circles */}
                  <div className="player-position" style={{top: '70%', left: '50%'}}></div>
                  <div className="player-position" style={{top: '50%', left: '30%'}}></div>
                  <div className="player-position" style={{top: '50%', left: '50%'}}></div>
                  <div className="player-position" style={{top: '50%', left: '70%'}}></div>
                  <div className="player-position" style={{top: '30%', left: '20%'}}></div>
                  <div className="player-position" style={{top: '30%', left: '40%'}}></div>
                  <div className="player-position" style={{top: '30%', left: '60%'}}></div>
                  <div className="player-position" style={{top: '30%', left: '80%'}}></div>
                  <div className="player-position" style={{top: '15%', left: '30%'}}></div>
                  <div className="player-position" style={{top: '15%', left: '70%'}}></div>
                  <div className="player-position" style={{top: '5%', left: '50%'}}></div>
                </div>
              </div>
            </div>

            {/* Heatmap Analysis */}
            <div className="content-box heatmap-box">
              <h3>Heatmap Analysis</h3>
              <img className="borderedImg" src="/assets/heatmap_placeholder.png" />
            </div>
          </div>
        </div>
      </div>

      <p className="copyright">© AI Student Collective, Davis</p>
    </>
  );
}

export default Sample;