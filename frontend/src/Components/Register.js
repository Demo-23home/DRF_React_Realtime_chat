import React from "react";
import TextField from "@mui/material/TextField";
import { Button } from "@mui/material";
function Register() {
  return (
    <>
      <div className="container text-center">
        <div className="mt-3">
          <TextField id="email" type="text" label="email" variant="outlined" />
        </div>
        <div className="mt-3">
          <TextField id="first_name" type="text" label="first_name" variant="outlined" />
        </div>
        <div className="mt-3">
          <TextField id="last_name" type="text" label="last_name" variant="outlined" />
        </div>
        <div className="mt-3">
          <TextField id="password" type="password" label="password" variant="outlined" />
        </div>
        <div className="mt-3">
          <Button variant="contained">Saved</Button>
        </div>
      </div>
    </>
  );
}
export default Register;
