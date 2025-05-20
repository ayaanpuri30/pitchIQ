// Navbar.tsx
import React from 'react';
import './Navbar.css';  
import "./Results.css";
const Results = () => {
  return (
    <table className="table results">
                {
                  <thead>
                    <th colSpan={3}>
                    </th>
                  </thead>
                }
                <tbody>
                  {/*league.teams.map((team, index) => (
                    <tr key={index}>
                      <td>
                        <img src={team.logo}></img>
                      </td>
                      <td>{team.name}</td>
                      <td>
                        <img src={team.coach} />
                      </td>
                    </tr>
                  ))*/}
                </tbody>
              </table>
  );
};

export default Results;