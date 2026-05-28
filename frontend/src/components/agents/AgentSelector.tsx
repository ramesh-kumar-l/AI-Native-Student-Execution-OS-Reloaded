"use client";

import { Bot, Calendar, Brain, Flame } from "lucide-react";

export function AgentSelector({ activeAgent, setActiveAgent }: { activeAgent: string, setActiveAgent: (agent: string) => void }) {
  const agents = [
    { id: "planner", name: "The Planner", icon: Calendar, color: "text-indigo-400", bg: "bg-indigo-500/10", border: "border-indigo-500/20", activeBg: "bg-indigo-500/20 border-indigo-500/40" },
    { id: "revision", name: "Revision Master", icon: Brain, color: "text-emerald-400", bg: "bg-emerald-500/10", border: "border-emerald-500/20", activeBg: "bg-emerald-500/20 border-emerald-500/40" },
    { id: "accountability", name: "The Coach", icon: Flame, color: "text-rose-400", bg: "bg-rose-500/10", border: "border-rose-500/20", activeBg: "bg-rose-500/20 border-rose-500/40" },
  ];

  return (
    <div className="flex flex-col gap-3">
      {agents.map((agent) => (
        <button
          key={agent.id}
          onClick={() => setActiveAgent(agent.id)}
          className={`flex items-center gap-4 p-4 rounded-xl border transition-all text-left group
            ${activeAgent === agent.id ? agent.activeBg : `bg-white/5 border-white/5 hover:${agent.bg} hover:${agent.border}`}
          `}
        >
          <div className={`w-10 h-10 rounded-lg flex items-center justify-center shrink-0 ${agent.bg} ${agent.border} border`}>
            <agent.icon className={`w-5 h-5 ${agent.color}`} />
          </div>
          <div>
            <h3 className="font-bold text-white text-sm group-hover:text-slate-200">{agent.name}</h3>
            <p className="text-xs text-slate-400">Autonomous Execution Persona</p>
          </div>
        </button>
      ))}
    </div>
  );
}
