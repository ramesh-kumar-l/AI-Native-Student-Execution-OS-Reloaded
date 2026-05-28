"use client";

import { Layers, Brain } from "lucide-react";

export function FlashcardDeck() {
  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-full min-h-[300px]">
      <div className="flex items-center gap-2 mb-6">
        <Layers className="w-5 h-5 text-emerald-400" />
        <h2 className="font-bold text-lg text-white">Flashcard Queue</h2>
      </div>

      <div className="flex-1 flex flex-col items-center justify-center">
        {/* Mock Card */}
        <div className="w-full max-w-sm aspect-[4/3] rounded-xl bg-gradient-to-br from-slate-800 to-slate-900 border border-white/10 shadow-2xl flex flex-col items-center justify-center p-8 text-center cursor-pointer hover:border-emerald-500/30 transition group relative overflow-hidden">
          
          <div className="absolute top-0 right-0 w-32 h-32 bg-emerald-500/10 blur-[50px] pointer-events-none" />
          
          <Brain className="w-8 h-8 text-emerald-400/50 mb-4 group-hover:scale-110 transition-transform" />
          <h3 className="text-lg font-semibold text-white">What is a Vector Database?</h3>
          <p className="text-xs text-slate-500 mt-4 uppercase tracking-wider font-bold">Tap to flip</p>
        </div>

        <div className="mt-6 text-sm text-slate-400">
          <span className="font-bold text-emerald-400">12</span> cards due for review today
        </div>
      </div>
    </div>
  );
}
