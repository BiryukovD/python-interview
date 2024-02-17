import React from "react";
import "./Button.css";

const Button = ({ className, onClick, value }) => {
  return (
    <a className={className} onClick={onClick}>
      {value}
    </a>
  );
};

export default Button;
