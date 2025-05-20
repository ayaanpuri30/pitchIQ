

const About = () => {
  return (
    <div className="p-6 max-w-4xl mx-auto text-white">
      <h1 className="text-3xl font-bold mb-4">About PitchIQ</h1>

      <p className="mb-4">
        <strong>PitchIQ</strong> is an interactive football intelligence platform designed to help fans, analysts, and players explore club-specific playing styles, tactical tendencies, and squad characteristics.
      </p>

      <p className="mb-4">
        By combining structured data with clean visual summaries, PitchIQ offers insights into how teams operate on the pitch — from their defensive shape to midfield control and attacking buildup.
      </p>

      <p className="mb-4">
        Data is sourced directly from structured club and player datasets, stored in a Supabase PostgreSQL backend and rendered dynamically through a responsive React frontend.
      </p>

      <p className="mb-4">
        This project is built with a love for both football and technology — aiming to make advanced football intelligence accessible to everyone.
      </p>

      <p className="text-sm text-gray-400">Built by AI Student Collective @ UC Davis</p>
    </div>
  );
};

export default About;
