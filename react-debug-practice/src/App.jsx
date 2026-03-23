import { useState } from "react";

function SlowList({ count }) {
  const items = [];
  for (let i = 0; i < 5000; i++) {
    items.push(
      <li key={i}>
        Item {i} - Count {count}
      </li>,
    );
  }
  return <ul>{items}</ul>;
}

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>React Profiler Practice</h1>
      <button onClick={() => setCount(count + 1)}>Increase</button>
      <p>Count: {count}</p>
      <SlowList count={count} />
    </div>
  );
}

export default App;
