
import './Navbar.css';
import { Link } from 'react-router-dom';  // Import Link

const Navbar = () => {
  return (
    <nav className="navbar">
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/">Leagues</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/credits">Credits</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
