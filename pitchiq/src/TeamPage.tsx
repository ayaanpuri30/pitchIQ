
import { useParams } from 'react-router-dom';

const TeamPage = () => {
  const { teamName } = useParams();  // Grabbing team name from URL
  
  return (
    <div>
      <h1>{teamName} Stats</h1>
      <p>Here are the stats for {teamName}...</p>
      {/* Fetch and display team-specific data here */}
    </div>
  );
};

export default TeamPage;