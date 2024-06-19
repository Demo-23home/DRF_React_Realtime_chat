import React from "react";
import Register from "./Register";
import Login from "./Login";
import { Link } from "react-router-dom";


const Navigate = () => {
  return <div>
    <Link to="/register">Register</Link>
    <br/>
    <Link to="/login">Login</Link>
    <br/>
    <Link to="/chat">chat</Link>
  </div>;
};

export default Navigate;
