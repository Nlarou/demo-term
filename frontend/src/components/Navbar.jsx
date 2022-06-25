import { FaUser } from "react-icons/fa";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

function Navbar({ title }) {
  return (
    <nav className="navbar mb-12 shadow-lg bg-neutral">
      <div className="container mx-auto">
        <div className="flex-none px-2 mx-2">
          <h1 className="text-lg font-bold align-middle">Demo</h1>
        </div>
      </div>
    </nav>
  );
}
Navbar.defaultProps = {
  title: "Demo",
};
Navbar.propTypes = {
  title: PropTypes.string,
};
export default Navbar;
