"use client";

import { BrainCircuit } from "lucide-react";
import { TaskBoard } from "@/components/planning/TaskBoard";
import { StudySchedule } from "@/components/planning/StudySchedule";
import { RecommendationPanel } from "@/components/planning/RecommendationPanel";

export default function PlanningPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-indigo-400 to-violet-400 bg-clip-text text-transparent flex items-center gap-3">
          <BrainCircuit className="w-8 h-8 text-indigo-400" />
          AI Planning Engine
        </h1>
        <p className="text-slate-400 mt-2">Let AI prioritize your tasks and balance your workload securely.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <RecommendationPanel />
        <TaskBoard />
        <StudySchedule />
      </div>
    </div>
  );
}
