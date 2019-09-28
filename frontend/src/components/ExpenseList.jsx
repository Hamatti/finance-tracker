import React from "react";

const ExpenseDetail = ({ expense: { description, cost, store } }) => {
  return (
    <div>
      {description} for {cost} at {store}
    </div>
  );
};

const ExpenseList = ({ expenses }) => {
  return (
    <ul>
      {expenses.map(expense => (
        <li key={expense.id}>
          <ExpenseDetail expense={expense} />
        </li>
      ))}
    </ul>
  );
};

export default ExpenseList;
