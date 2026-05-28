"use client";

import { FileSearch, Sparkles } from "lucide-react";

export function SummaryViewer() {
  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-[400px]">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <FileSearch className="w-5 h-5 text-violet-400" />
          <h2 className="font-bold text-lg text-white">Semantic Search & Summaries</h2>
        </div>
      </div>

      <div className="relative mb-6">
        <input 
          type="text" 
          placeholder="Ask your knowledge base..." 
          className="w-full bg-[#020617]/50 border border-white/10 rounded-lg px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-violet-500/50 transition"
        />
        <Sparkles className="w-4 h-4 text-violet-400 absolute right-4 top-3.5" />
      </div>

      <div className="flex-1 overflow-y-auto space-y-4 pr-2 custom-scrollbar">
        {/* Mock Summary Block */}
        <div className="p-4 rounded-xl bg-violet-500/5 border border-violet-500/20">
          <h3 className="text-sm font-bold text-violet-300 mb-2">Key Takeaways: Intro to Algorithms</h3>
          <ul className="space-y-2 text-sm text-slate-300 list-disc pl-4">
            <li>Dynamic programming breaks complex problems down into simpler subproblems.</li>
            <li>Greedy algorithms make the optimal choice at each step locally.</li>
            <li>Dijkstra's finds the shortest path but cannot handle negative weights.</li>
          </ul>
        </div>
      </div>
    </div>
  );
}
