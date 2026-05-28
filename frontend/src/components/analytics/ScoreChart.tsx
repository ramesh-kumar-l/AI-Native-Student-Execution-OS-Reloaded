"use client";

import { Activity } from "lucide-react";

export function ScoreChart() {
  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-full min-h-[350px]">
      <div className="flex items-center gap-2 mb-6">
        <Activity className="w-5 h-5 text-indigo-400" />
        <h2 className="font-bold text-lg text-white">Execution Quality</h2>
      </div>

      <div className="flex-1 flex items-end gap-4 px-4 pb-4 border-b border-l border-white/10 relative">
        <div className="absolute -left-8 top-0 text-xs text-slate-500">100</div>
        <div className="absolute -left-6 bottom-0 text-xs text-slate-500">0</div>
        
        {/* Mock Bars */}
        {[65, 78, 54, 89, 92, 85, 95].map((height, i) => (
          <div key={i} className="flex-1 flex flex-col items-center justify-end group">
            <div 
              style={{ height: `${height}%` }} 
              className="w-full max-w-[40px] bg-gradient-to-t from-indigo-500/20 to-indigo-500/80 rounded-t-lg hover:from-indigo-400/40 hover:to-indigo-400 transition-all cursor-pointer relative"
            >
              <div className="opacity-0 group-hover:opacity-100 absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-800 text-xs font-bold text-white px-2 py-1 rounded">
                {height}
              </div>
            </div>
            <span className="text-xs text-slate-400 mt-2">D{i+1}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
