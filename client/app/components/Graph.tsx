"use client";

import { useEffect, useRef } from 'react';
import { Network, Data, Options } from 'vis-network/standalone';

interface GraphProps {
  data: Data;
}

export default function Graph({ data }: GraphProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (data && containerRef.current) {
      console.log("Graph data:", data);

      const options: Options = {
        layout: {
          improvedLayout: false, // Turn off the heavier layout algorithm
        },
        physics: {
          // Either reduce or disable physics for faster rendering
          enabled: true,
          stabilization: {
            iterations: 200, // Lower number => faster, less precise layout
          },
        },
        nodes: {
          shape: 'dot',
          size: 16,
          font: { size: 14 },
        },
        edges: {
          width: 2,
        },
      };

      new Network(containerRef.current, data, options);
    }
  }, [data]);

  return <div ref={containerRef} style={{ height: '500px' }} />;
}
