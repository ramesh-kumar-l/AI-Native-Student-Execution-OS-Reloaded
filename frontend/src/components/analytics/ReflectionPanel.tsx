"use client";

import { Sparkles, PenLine } from "lucide-react";

export function ReflectionPanel() {
  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-full min-h-[350px]">
      <div className="flex items-center gap-2 mb-6">
        <Sparkles className="w-5 h-5 text-fuchsia-400" />
        <h2 className="font-bold text-lg text-white">Weekly AI Reflection</h2>
      </div>

      <div className="space-y-6">
        <div className="p-4 rounded-xl bg-fuchsia-500/10 border border-fuchsia-500/20">
          <p className="text-sm text-fuchsia-100 leading-relaxed">
            "Your execution score peaked on Thursday with an impressive 92% task completion rate. 
            However, your weekend retention scores dropped by 15%. Focus on clearing your Flashcard queue earlier in the day to maintain your streak."
          </p>
        </div>

        <div>
          <div className="flex items-center gap-2 mb-3">
            <PenLine className="w-4 h-4 text-slate-400" />
            <h3 className="text-sm font-bold text-slate-300">Your Lessons Learned</h3>
          </div>
          <textarea 
            placeholder="What went well? What could be improved?"
            className="w-full h-32 bg-[#020617]/50 border border-white/10 rounded-xl p-4 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-fuchsia-500/50 transition resize-none custom-scrollbar"
          />
          <div className="flex justify-end mt-2">
            <button className="px-4 py-2 bg-fuchsia-600 hover:bg-fuchsia-500 text-white rounded-lg text-sm font-bold shadow-lg transition">
              Save Notes
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
