import ChatArea from "./Components/ChatArea";
import Login from "./Components/Login";
import Navigate from "./Components/Navigate";
import Register from "./Components/Register";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import SideBar from "./Components/SideBar";
import './app.css'


function App() {
  return (
    <>
    <div className="chat-container">
    <SideBar/>
    <ChatArea/>
    </div>
    </>
    // <BrowserRouter>
    //   <Navigate />
    //   <Routes>
    //     <Route path="/login" element={<Login />} />
    //     <Route path="/register" element={<Register />} />
    //   </Routes>
    // </BrowserRouter>
  );
}

export default App;
