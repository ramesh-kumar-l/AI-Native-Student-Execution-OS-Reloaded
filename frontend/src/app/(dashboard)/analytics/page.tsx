"use client";

import { LineChart } from "lucide-react";
import { ScoreChart } from "@/components/analytics/ScoreChart";
import { ReflectionPanel } from "@/components/analytics/ReflectionPanel";

export default function AnalyticsPage() {
  return (
    <div className="space-y-6 h-full flex flex-col">
      <div>
        <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-indigo-400 to-fuchsia-400 bg-clip-text text-transparent flex items-center gap-3">
          <LineChart className="w-8 h-8 text-indigo-400" />
          Analytics & Reflection
        </h1>
        <p className="text-slate-400 mt-2">Visualize your execution momentum and review AI-driven weekly insights.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 flex-1">
        <div className="h-full">
          <ScoreChart />
        </div>
        <div className="h-full">
          <ReflectionPanel />
        </div>
      </div>
    </div>
  );
}
