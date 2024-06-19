import React, { useState } from "react";

const MessageInput = () => {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSendMessage = () => {
    console.log("MESSAGE SEND");
  };

  return (
    <div className="message-input">
      <textarea
        placeholder="Type you message here"
        value={inputValue}
        onChange={handleInputChange}
      />
      <button onClick={handleSendMessage}>Send</button>
    </div>
  );
};

export default MessageInput;
