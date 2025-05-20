
const team = [
  { name: 'Vibhav Darsha', role: 'Engineering Manager' },
  { name: 'Om Patki', role: 'Software Engineer' },
  { name: 'Ayaan Puri', role: 'Software Engineer' },
  { name: 'Manish Rathor', role: 'Technical Advisor' },
  { name: 'Atin Kumar Singh', role: 'Software Engineer' }
];

const Credits = () => {
  return (
    <div className="p-6 max-w-6xl mx-auto text-white">
      <h1 className="text-3xl font-bold mb-6 text-center">Credits</h1>
      <p className="mb-10 text-center text-gray-300">
        Meet the amazing team behind PitchIQ.
      </p>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {team.map((member, idx) => (
          <div
            key={idx}
            className="bg-gray-800 rounded-2xl shadow-lg p-6 flex flex-col items-center text-center"
          >
            <img
              src={""}
              alt={member.name}
              className="w-24 h-24 rounded-full mb-4"
            />
            <h2 className="text-xl font-semibold">{member.name}</h2>
            <p className="text-gray-400">{member.role}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Credits;
