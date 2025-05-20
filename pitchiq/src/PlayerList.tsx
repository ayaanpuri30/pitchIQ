import React, {useState} from 'react';

interface Player {
  id: number;
  name: string;
  age: number;
  number: number | null;
  position: string;
  photo: string;
}
 interface Props{
  data :any
 }

const PlayerList: React.FC<Props> = ({ data }) => {
  const [selectedPlayerId, setSelectedPlayerId] = useState<number | null>(null);

  return (
    <div className="p-4 text-white">
      <h2 className="text-2xl font-bold mt-2 mb-6 text-center">{data.club_name} Squad</h2>

      <div className="max-h-[400px] overflow-y-auto overflow-x-auto rounded border border-gray-700">
        <table className="min-w-full table-auto border-collapse">
          <thead>
            <tr className="bg-gray-800 text-left">
              <th className="px-4 py-2 border-b border-gray-700">#</th>
              <th className="px-4 py-2 border-b border-gray-700">Name</th>
              <th className="px-4 py-2 border-b border-gray-700">Position</th>
              <th className="px-4 py-2 border-b border-gray-700">Birthdate</th>
            </tr>
          </thead>
          <tbody>
            {data.squad.map((player : Player) => (
                <tr
                key={player.id}
                className={`transition duration-150 cursor-pointer ${
                  selectedPlayerId === player.id ? 'bg-blue-700' : 'hover:bg-gray-800'
                }`}
                onClick={() => {
                    setSelectedPlayerId(player.id);
                    //if (onPlayerClick) onPlayerClick(player);
                  }}
                >
                <td className="px-4 py-2 border-b border-gray-700">{player.number ?? '—'}</td>
                <td className="px-4 py-2 border-b border-gray-700 font-medium">{player.name}</td>
                <td className="px-4 py-2 border-b border-gray-700">{player.position}</td>
                <td className="px-4 py-2 border-b border-gray-700">{player.age}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default PlayerList;
