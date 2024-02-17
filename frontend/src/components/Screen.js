import React from "react";
import "./Screen.css";

const Screen = ({ className, onClick, value }) => {
  return (
    <div className={className} onClick={onClick}>
      <div className="text" dangerouslySetInnerHTML={{ __html: value }}></div>
    </div>
  );
};

export default Screen;
