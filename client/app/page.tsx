"use client";

import { useEffect, useState } from 'react';
import Graph from './components/Graph';
import { Data } from 'vis-network/standalone';

export default function HomePage() {
  const [graphData, setGraphData] = useState<Data | null>(null);

  useEffect(() => {
    // Adjust the URL if your backend is hosted somewhere else
    fetch('http://localhost:8000/graph')
      .then((response) => response.json())
      .then((data: Data) => setGraphData(data))
      .catch((error) => console.error('Error fetching graph:', error));
  }, []);

  return (
    <main style={{ padding: '1rem' }}>
      <h1>Graph Visualization</h1>
      {graphData ? <Graph data={graphData} /> : <p>Loading graph...</p>}
    </main>
  );
}
