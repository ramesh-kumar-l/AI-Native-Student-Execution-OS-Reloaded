"use client";

import { Mic, PlayCircle, Loader2 } from "lucide-react";
import { useState } from "react";

export function MockInterviewPanel() {
  const [loading, setLoading] = useState(false);
  const [active, setActive] = useState(false);

  const startInterview = () => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      setActive(true);
    }, 1500);
  };

  return (
    <div className="glass-panel p-6 rounded-2xl border border-white/5 flex flex-col h-full min-h-[300px] justify-between relative overflow-hidden">
      <div className="absolute top-0 right-0 w-32 h-32 bg-rose-500/10 blur-[50px] pointer-events-none" />

      <div>
        <div className="flex items-center gap-2 mb-2">
          <Mic className="w-5 h-5 text-rose-400" />
          <h2 className="font-bold text-lg text-white">Mock Simulator</h2>
        </div>
        <p className="text-sm text-slate-400">Generate targeted interview questions based on your resume and selected opportunity.</p>
      </div>

      <div className="flex-1 flex flex-col items-center justify-center py-6">
        {!active ? (
          <button 
            onClick={startInterview}
            className="w-16 h-16 rounded-full bg-rose-500/20 text-rose-400 flex items-center justify-center hover:bg-rose-500/30 hover:scale-105 transition-all shadow-lg shadow-rose-500/10"
          >
            {loading ? <Loader2 className="w-8 h-8 animate-spin" /> : <PlayCircle className="w-8 h-8" />}
          </button>
        ) : (
          <div className="w-full space-y-4">
            <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20">
              <p className="text-sm font-semibold text-rose-100">
                "Tell me about a time you optimized a database query as mentioned in your SWE v1 resume."
              </p>
            </div>
            <div className="flex gap-2 justify-center">
              <button className="px-4 py-2 rounded-lg bg-rose-600 text-white text-sm font-bold shadow-md">
                Answer (Mic)
              </button>
              <button onClick={() => setActive(false)} className="px-4 py-2 rounded-lg bg-white/10 text-white text-sm font-bold">
                End Session
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
