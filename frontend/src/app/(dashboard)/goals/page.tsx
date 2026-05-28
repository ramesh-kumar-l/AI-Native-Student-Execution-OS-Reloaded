"use client";

import { Sparkles, Plus, CheckCircle2, Circle } from "lucide-react";

export default function GoalsPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent flex items-center gap-3">
            <Sparkles className="w-8 h-8 text-amber-400" />
            Goals & Milestones
          </h1>
          <p className="text-slate-400 mt-2">Track your high-level objectives and break them down.</p>
        </div>
        <button className="bg-white/10 hover:bg-white/20 text-white font-medium py-2 px-4 rounded-lg transition flex items-center gap-2 border border-white/10 active:scale-95">
          <Plus className="w-4 h-4" />
          New Goal
        </button>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {/* Mock Goal Card */}
        <div className="glass-panel p-6 rounded-xl border border-white/5 transition-all hover:border-indigo-500/30 group relative overflow-hidden">
          <div className="absolute left-0 top-0 bottom-0 w-1 bg-indigo-500 rounded-l-xl" />
          
          <div className="flex items-start justify-between">
            <div className="space-y-1">
              <h3 className="text-lg font-bold text-white group-hover:text-indigo-300 transition-colors">
                Pass Advanced Algorithms
              </h3>
              <p className="text-sm text-slate-400">Master dynamic programming and graph algorithms before finals.</p>
            </div>
            <span className="text-xs font-semibold px-2 py-1 bg-indigo-500/20 text-indigo-300 rounded">In Progress</span>
          </div>

          <div className="mt-6 space-y-3">
            <div className="flex items-center gap-3 text-sm text-slate-300">
              <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
              <span className="line-through opacity-70">Complete Graph Theory assignments</span>
            </div>
            <div className="flex items-center gap-3 text-sm text-slate-300">
              <Circle className="w-5 h-5 text-slate-500 shrink-0" />
              <span>Review Dynamic Programming patterns</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
