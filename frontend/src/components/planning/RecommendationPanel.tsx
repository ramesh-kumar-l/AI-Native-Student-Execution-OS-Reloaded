"use client";

import { Lightbulb, X } from "lucide-react";

export function RecommendationPanel() {
  return (
    <div className="col-span-full glass-panel p-6 rounded-2xl border border-amber-500/20 bg-amber-500/5 relative overflow-hidden">
      <div className="absolute top-0 left-0 w-1 h-full bg-amber-500" />
      
      <div className="flex gap-4">
        <div className="w-10 h-10 rounded-full bg-amber-500/20 flex items-center justify-center shrink-0 border border-amber-500/30">
          <Lightbulb className="w-5 h-5 text-amber-400" />
        </div>
        
        <div className="flex-1">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-amber-100">Workload Alert</h3>
            <button className="text-amber-500/50 hover:text-amber-400 transition">
              <X className="w-4 h-4" />
            </button>
          </div>
          <p className="text-sm text-amber-200/80 mt-1">
            You have scheduled 6 hours of high-fatigue tasks today. Consider shifting "Read Chapter 5" to tomorrow to maintain optimal retention.
          </p>
          
          <div className="mt-3 flex gap-2">
            <button className="px-3 py-1.5 rounded border border-amber-500/30 bg-amber-500/20 text-amber-300 text-xs font-bold hover:bg-amber-500/30 transition">
              Shift Task
            </button>
            <button className="px-3 py-1.5 rounded text-amber-500/70 hover:text-amber-400 text-xs font-bold transition">
              Dismiss
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
