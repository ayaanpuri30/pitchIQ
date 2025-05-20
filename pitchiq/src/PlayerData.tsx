import React, { useState } from "react";
import PlayerList from './PlayerList';

type Player = {
  id: number;
  name: string;
  age: number;
  number: number | null;
  position: string;
  photo: string;
};

type Team = {
  id: number;
  name: string;
  logo: string;
};

type TeamData = {
  team: Team;
  players: Player[];
};

type TeamDataWrapper = {
  response: TeamData[];
};

const PlayerData: React.FC<{
  data: TeamDataWrapper
}> = ({ data }) => {
  const [localTab, setLocalTab] = useState(0);


  const switchTab = (index: number) => {
    setLocalTab(index);
  };
  const selectedPlayer = null;
  const playerTabsData = [
    {
      title: "Squad List",
      content: (
        <div className="player-data-content">
          <PlayerList
            data={data}
          />
        </div>
      ),
    },
    {
      title: "Player Stats",
      content: selectedPlayer ? (
        <div className="player-data-content">
          <h3 className="text-xl font-semibold mb-2">{selectedPlayer.name}</h3>
          <p><strong>Number:</strong> {selectedPlayer.number ?? "N/A"}</p>
          <p><strong>Position:</strong> {selectedPlayer.position}</p>
          <p><strong>Birthdate:</strong> {selectedPlayer.age}</p>
        </div>
      ) : (
        <p className="text-gray-400">No player selected.</p>
      ),
    },
  ];

  return (
    <div className="content-box player-data-box">
      <div className="tabs-header flex gap-4 mb-4">
        {playerTabsData.map((tab, index) => (
          <div
            key={index}
            className={`player-tab cursor-pointer px-4 py-2 rounded ${
              localTab === index
                ? "bg-gray-200 text-gray-800 font-semibold"
                : "bg-gray-20 text-white"
            }`}
            onClick={() => switchTab(index)}
          >
            {tab.title}
          </div>
        ))}
      </div>
      <div className="player-tabs-content">
        {playerTabsData[localTab].content}
      </div>
    </div>
  );
};

export default PlayerData;
