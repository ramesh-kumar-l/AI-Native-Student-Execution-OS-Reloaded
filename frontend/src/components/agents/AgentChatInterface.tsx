"use client";

import { Send, Bot, User } from "lucide-react";
import { useState } from "react";

export function AgentChatInterface({ activeAgent }: { activeAgent: string }) {
  const [input, setInput] = useState("");

  return (
    <div className="glass-panel rounded-2xl border border-white/5 flex flex-col h-[500px]">
      <div className="p-4 border-b border-white/5 flex items-center gap-3">
        <Bot className="w-5 h-5 text-slate-300" />
        <h2 className="font-bold text-white uppercase tracking-wider text-sm">Interaction Link Active</h2>
      </div>

      <div className="flex-1 overflow-y-auto p-6 space-y-4 custom-scrollbar">
        {/* Mock Agent Message */}
        <div className="flex items-start gap-3">
          <div className="w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center shrink-0 border border-white/10">
            <Bot className="w-4 h-4 text-slate-400" />
          </div>
          <div className="bg-slate-800/50 border border-white/10 p-3 rounded-2xl rounded-tl-none max-w-[80%]">
            <p className="text-sm text-slate-300">
              Hello. I am currently synching with your OS context. How can I assist you with your {activeAgent} goals today?
            </p>
          </div>
        </div>

        {/* Mock User Message */}
        <div className="flex items-start gap-3 flex-row-reverse">
          <div className="w-8 h-8 rounded-full bg-indigo-500/20 flex items-center justify-center shrink-0 border border-indigo-500/30">
            <User className="w-4 h-4 text-indigo-400" />
          </div>
          <div className="bg-indigo-600 p-3 rounded-2xl rounded-tr-none max-w-[80%] shadow-lg shadow-indigo-500/20">
            <p className="text-sm text-white">
              Can you help me break down my CS50 project?
            </p>
          </div>
        </div>
      </div>

      <div className="p-4 border-t border-white/5">
        <form className="relative" onSubmit={(e) => { e.preventDefault(); setInput(""); }}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder={`Message ${activeAgent} agent...`}
            className="w-full bg-[#020617] border border-white/10 rounded-xl pl-4 pr-12 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500/50 transition"
          />
          <button 
            type="submit"
            className="absolute right-2 top-2 p-1.5 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-white transition active:scale-95"
          >
            <Send className="w-4 h-4" />
          </button>
        </form>
      </div>
    </div>
  );
}
