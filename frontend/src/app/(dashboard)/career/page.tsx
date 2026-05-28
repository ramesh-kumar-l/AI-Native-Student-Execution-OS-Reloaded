"use client";

import { Target } from "lucide-react";
import { OpportunityKanban } from "@/components/career/OpportunityKanban";
import { MockInterviewPanel } from "@/components/career/MockInterviewPanel";

export default function CareerPage() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <div>
        <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-sky-400 to-indigo-400 bg-clip-text text-transparent flex items-center gap-3">
          <Target className="w-8 h-8 text-sky-400" />
          Career Mobility
        </h1>
        <p className="text-slate-400 mt-2">Track opportunities and crush your interviews with AI-generated mock sessions.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 flex-1">
        <div className="md:col-span-2 h-[600px]">
          <OpportunityKanban />
        </div>
        <div className="md:col-span-1 h-[600px]">
          <MockInterviewPanel />
        </div>
      </div>
    </div>
  );
}
