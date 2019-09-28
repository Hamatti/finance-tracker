import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

import ExpenseList from "./components/ExpenseList";
import ENDPOINTS from "./endpoints";

const getExpenses = setExpenses => {
  axios.get(ENDPOINTS.expenses.list).then(response => {
    setExpenses(response.data);
  });
};

function App() {
  const [expenses, setExpenses] = useState([]);
  useEffect(() => getExpenses(setExpenses), []);
  return (
    <div className="App">
      <header>Finance Tracker Home Page</header>
      <main>
        <ExpenseList expenses={expenses} />
      </main>
    </div>
  );
}

export default App;
