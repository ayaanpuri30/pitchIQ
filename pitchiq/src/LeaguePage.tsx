import { useEffect, useState } from 'react';
import "./App.css";
import leagues from "./teams.ts";
import Navbar from "./Navbar.tsx";
import { supabase } from './supabaseClient';
import { useNavigate } from 'react-router-dom';

interface LeaguePageProps {
    setClubData: (data: any) => void;
  }

function LeaguePage({ setClubData } : LeaguePageProps) {
    const navigate = useNavigate();
    const [selectedClub, setSelectedClub] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchClubData = async () => {
            if (!selectedClub) return;

            setLoading(true);

            const { data: club, error: clubError } = await supabase
                .from('clubs')
                .select('*')
                .eq('club_name', selectedClub)
                .single();

            if (clubError || !club) {
                console.error('Error fetching club:', clubError);
                setClubData(null);
                setLoading(false);
                return;
            }

            const { data: squad, error: squadError } = await supabase
                .from('players')
                .select('*')
                .eq('club_name', selectedClub)
                .order('player_id', { ascending: true });
            
            const { data: summaries, error: summariesError } = await supabase
                .from('playstyle_summaries')
                .select('*')
                .eq('team_name', selectedClub);

            if (squadError || summariesError) {
                console.error('Error fetching squad/summaries:', squadError, summariesError);
                setClubData(null);
                setLoading(false);
                return;
            }

            
            setClubData({
                ...club,
                squad: squad,
                playstyle_summaries: summaries,
            });
            navigate("/atl"); 
            setLoading(false);
        };

        fetchClubData();
    }, [selectedClub]);


    if (loading) return <p className="text-white">Loading...</p>;
    return (
        <>
            <Navbar />
            <div className="tables-wrapper">
                <div>
                    <h1 className="aboves">
                        Welcome to <span className="highlight">PitchIQ!</span>
                    </h1>
                    <h3 className="aboves">Choose a club to learn about their playstyle.</h3>
                </div>

                {leagues.map((league, index) => (
                    <div className="card" key={index}>
                        <div className="table-container">
                            <table className="table">
                                <thead className="rounded-l-md">
                                    <tr className="">
                                        <th colSpan={3}>
                                            <div className="relative h-10">
                                                <div className="flex items-center space-x-2 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                                                    <img src={league.logo} className="" />
                                                    <h2 className="text-2xl">{league.name}</h2>
                                                </div>
                                            </div>

                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {league.teams.map((team, idx) => (
                                        <tr
                                            key={idx}
                                            className="cursor-pointer"
                                            onClick={() => setSelectedClub(team.name)}
                                        >
                                            <td className=""><img src={team.logo} /></td>
                                            <td><h2 className="text-lg font-normal">{team.name}</h2></td>
                                            <td className=" p-4"><img src={team.coach} /></td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}
export default LeaguePage;