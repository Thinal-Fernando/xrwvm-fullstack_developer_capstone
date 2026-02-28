import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";
import Register from "./components/Register/Register";
import Dealer from "./components/Dealers/Dealer"
import Dealers from './components/Dealers/Dealers';




function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dealer/:id" element={<Dealer/>} />
      <Route path="/dealers" element={<Dealers/>} />



    </Routes>
  );
}
export default App;
