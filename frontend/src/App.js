import ReactDOM from "react-dom";
import React, { useState } from "react";

import Button from "./components/Button";
import Screen from "./components/Screen";
import Logo from "./components/Logo";

const App = ({ className, onClick, value }) => {
  const [question, setQuesion] = useState("Начать");
  const [answer, setAnswer] = useState("Answer");
  const [material, setMateril] = useState("material");
  const [state, setState] = useState("question");

  const click_next_question = () => {
    fetch("http://45.9.40.200:7777/question")
      .then((response) => response.json())
      .then((json) => {
        console.log(json.question);
        setQuesion(json.question);
        setAnswer(json.answer);
        setMateril(json.additional - material);

        setState("question");

        // setAnswer(json.answer)
        // setMateril(json.material)
      })
      .catch((err) => alert(err));
  };

  const change_state = () => {
    if (question !== "Начать") {
      if (state === "question") {
        setState("answer");
      }
    } else {
      click_next_question();
    }
  };

  return (
    <div className="main">
      <div className="container">
        <Logo className="logo" />
        <div className="window">
          <Screen
            className={state === "question" ? "question" : "answer"}
            onClick={() => change_state()}
            value={state === "question" ? question : answer}
          />
          <div className="buttons">
            <Button
              className="btn-answer"
              onClick={() => change_state()}
              value="Узнать ответ"
            />

            <Button
              className="btn-next-question"
              onClick={() => click_next_question()}
              value="Следующий вопрос"
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
