import AtleticoMadridData from './Atlético_Madrid.tsx';
import FCBarcelonaData from './FC_Barcelona.tsx';
import LiverpoolData from './Liverpool.tsx';
import LOSCLilleData from './LOSC_Lille.tsx';
import ManchesterCityData from './Manchester_City.tsx';
import ManchesterUnitedData from './Manchester_United.tsx';
import OlympiqueMarseilleData from './Olympique_Marseille.tsx';
import ParisSaintGermainData from './Paris_Saint_Germain.tsx';
import RealMadridData from './Real_Madrid.tsx';

const teamMap: Record<string, any> = {
  "Atlético Madrid": AtleticoMadridData,
  "FC Barcelona": FCBarcelonaData,
  "Liverpool": LiverpoolData,
  "LOSC Lille": LOSCLilleData,
  "Manchester City": ManchesterCityData,
  "Manchester United": ManchesterUnitedData,
  "Olympique Marseille": OlympiqueMarseilleData,
  "Paris Saint Germain": ParisSaintGermainData,
  "Real Madrid": RealMadridData,
};

export default teamMap;