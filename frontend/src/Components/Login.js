import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
const Login = () => {
  const baseURL = "http://127.0.0.1:8000";
  const [formData, setFromData] = useState({
    email: "",
    password: "",
  });

  const handleFormSubmit = () => {
    fetch(`${baseURL}/accounts/login/`, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <>
      <div className="container text-center">
        <div className="mt-3">
          <TextField
            id="email"
            type="text"
            label="email"
            variant="outlined"
            onChange={(e) =>
              setFromData({ ...formData, email: e.target.value })
            }
          />
        </div>
        <div className="mt-3">
          <TextField
            id="password"
            type="password"
            label="password"
            variant="outlined"
            onChange={(e) =>
              setFromData({ ...formData, password: e.target.value })
            }
          />
        </div>
        <div className="mt-3">
          <Button variant="contained" onClick={handleFormSubmit}>
            Submit
          </Button>
        </div>
      </div>
    </>
  );
};

export default Login;
