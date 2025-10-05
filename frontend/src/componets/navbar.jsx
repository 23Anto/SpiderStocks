import React from "react";

 
export function StickyNavbar() {
  return (
    <div className="fixed top-0 bg-gray-800 p-4 flex gap-4 w-full">
      <a href="#home" className="text-white hover:underline sticky top-0">
        Home
      </a>
    </div>
  );
}