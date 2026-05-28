"use client";

import { Briefcase, MoreHorizontal, Plus } from "lucide-react";

export function OpportunityKanban() {
  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-full min-h-[400px]">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-2">
          <Briefcase className="w-5 h-5 text-sky-400" />
          <h2 className="font-bold text-lg text-white">Opportunity Tracker</h2>
        </div>
        <button className="p-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 transition border border-white/5">
          <Plus className="w-4 h-4" />
        </button>
      </div>

      <div className="flex-1 grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Wishlist Column */}
        <div className="bg-[#020617]/50 rounded-xl border border-white/5 p-4 flex flex-col gap-3">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
            Wishlist <span className="bg-white/10 px-2 py-0.5 rounded text-white">1</span>
          </h3>
          
          {/* Card */}
          <div className="p-4 rounded-xl bg-slate-800/50 border border-white/10 hover:border-sky-500/30 transition cursor-grab">
            <div className="flex justify-between items-start mb-2">
              <h4 className="text-sm font-bold text-white">Google</h4>
              <MoreHorizontal className="w-4 h-4 text-slate-500" />
            </div>
            <p className="text-xs text-sky-300">Software Engineer Intern</p>
          </div>
        </div>

        {/* Applied Column */}
        <div className="bg-[#020617]/50 rounded-xl border border-white/5 p-4 flex flex-col gap-3">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
            Applied <span className="bg-white/10 px-2 py-0.5 rounded text-white">0</span>
          </h3>
          <div className="flex-1 border-2 border-dashed border-white/5 rounded-xl flex items-center justify-center">
            <span className="text-xs text-slate-500">Drop here</span>
          </div>
        </div>

        {/* Interviewing Column */}
        <div className="bg-[#020617]/50 rounded-xl border border-white/5 p-4 flex flex-col gap-3">
          <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
            Interviewing <span className="bg-white/10 px-2 py-0.5 rounded text-white">0</span>
          </h3>
          <div className="flex-1 border-2 border-dashed border-white/5 rounded-xl flex items-center justify-center">
            <span className="text-xs text-slate-500">Drop here</span>
          </div>
        </div>
      </div>
    </div>
  );
}
