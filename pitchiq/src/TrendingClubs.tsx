// Navbar.tsx
import React from 'react';
import './Navbar.css';  // Optionally add styling for your navbar
import "./TrendingClubs.css";
import trends from './trends';
const TrendingClubs = () => {
  return (
    <table className="trending">
                {
                  <thead>
                    <th colSpan={3}>
                    </th>
                  </thead>
                }
                <tbody>
                  {trends.map((team, index) => (
                    <tr key={index}>
                      <td>
                        <img src={team.logo}></img>
                      </td>
                      <td>{team.name}</td>
                      <td>
                        <img src={team.coach} />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
  );
};

export default TrendingClubs;