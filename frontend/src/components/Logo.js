import React from "react";
import "./Logo.css";
import logo from "./logo.svg";

const Logo = ({ className }) => {
  return (
    <div className={className}>
      <img src={logo} alt="логотип" />
    </div>
  );
};

export default Logo;
