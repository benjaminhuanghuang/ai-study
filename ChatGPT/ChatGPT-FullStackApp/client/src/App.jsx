import { useState } from "react";
import sqlServer from "./assets/sql-server.png";
import styles from "./index.module.css";

function App() {
  // track user input
  const [userPrompt, setUserPrompt] = useState("");
  //
  const [sqlQuery, setSqlQuery] = useState("");

  const onSubmit = async (e) => {
    e.preventDefault();
    console.log("form submitted: ", userPrompt);
    // const query = await generateQuery();
    // setSqlQuery(query);
  };

  const generateQuery = async () => {
    const response = await fetch("http://localhost:3002/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ queryDescription: userPrompt }),
    });

    const data = await response.json();
    return data.sqlQuery.trim();
  };

  return (
    <main className={styles.main}>
      <img src={sqlServer} className={styles.icon} alt="SQL server" />
      <h3>Generate SQL</h3>
      <form onSubmit={onSubmit}>
        <input
          type="text"
          name="query-description"
          placeholder="Describe your query"
          value={userPrompt}
          onChange={(e) => setUserPrompt(e.target.value)}
        />
        <input type="submit" value="Generate query" />
      </form>
      <pre>{sqlQuery}</pre>
    </main>
  );
}

export default App;
