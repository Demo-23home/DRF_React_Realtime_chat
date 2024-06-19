import React from "react";
import Message from "./Message";
import MessageInput from "./MessageInput";
import withAuthentication from "../utils/withAuthentication";

const ChatArea = () => {
  return (
    <div className="chat-area">
      <div className="chat-header"></div>
      <div className="messages">
        <Message text="Hello there!" sent />
        <Message text="Hey" received />
      </div>
      <MessageInput />
    </div>
  );
};

export default withAuthentication(ChatArea);
