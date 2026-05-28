"use client";

import { Sparkles } from "lucide-react";
import { useState } from "react";
import { AgentSelector } from "@/components/agents/AgentSelector";
import { AgentChatInterface } from "@/components/agents/AgentChatInterface";

export default function AgentsPage() {
  const [activeAgent, setActiveAgent] = useState("planner");

  return (
    <div className="space-y-6 h-full flex flex-col">
      <div>
        <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-rose-400 to-orange-400 bg-clip-text text-transparent flex items-center gap-3">
          <Sparkles className="w-8 h-8 text-rose-400" />
          Execution Agents
        </h1>
        <p className="text-slate-400 mt-2">Interact with autonomous personas dedicated to keeping your momentum high.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 flex-1">
        <div className="md:col-span-1">
          <AgentSelector activeAgent={activeAgent} setActiveAgent={setActiveAgent} />
        </div>
        <div className="md:col-span-2">
          <AgentChatInterface activeAgent={activeAgent} />
        </div>
      </div>
    </div>
  );
}
