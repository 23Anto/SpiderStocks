import React from "react";

import {MyChart} from "./componets/stockgraph.jsx";
import {StickyNavbar} from "./componets/navbar.jsx"


function MyButton({ title }: { title: string }) {
  return (
    <button>{title}</button>
  );
}

export default function App() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <StickyNavbar />
    </div>
  );
}
