"use client";

import { CheckCircle2, ListTodo, Plus } from "lucide-react";

export function TaskBoard() {
  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-[400px]">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <ListTodo className="w-5 h-5 text-indigo-400" />
          <h2 className="font-bold text-lg text-white">Backlog</h2>
        </div>
        <button className="p-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition border border-white/5">
          <Plus className="w-4 h-4" />
        </button>
      </div>
      
      <div className="flex-1 overflow-y-auto space-y-3 pr-2 custom-scrollbar">
        {/* Mock Task */}
        <div className="p-4 rounded-xl bg-indigo-500/10 border border-indigo-500/20 hover:border-indigo-400/30 transition cursor-pointer group">
          <div className="flex justify-between items-start">
            <h3 className="text-sm font-semibold text-white group-hover:text-indigo-300">Finish CS50 Project</h3>
            <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-rose-500/20 text-rose-300">High Prio</span>
          </div>
          <p className="text-xs text-slate-400 mt-1 line-clamp-1">Due in 2 days. Estimated 4 hours.</p>
        </div>

        {/* Mock Task 2 */}
        <div className="p-4 rounded-xl bg-white/5 border border-white/10 hover:border-white/20 transition cursor-pointer">
          <div className="flex justify-between items-start">
            <h3 className="text-sm font-semibold text-slate-200">Read Chapter 5</h3>
          </div>
          <p className="text-xs text-slate-400 mt-1 line-clamp-1">Due next week.</p>
        </div>
      </div>
    </div>
  );
}
