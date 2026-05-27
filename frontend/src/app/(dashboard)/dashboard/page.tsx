import { auth } from "@/auth";
import { Sparkles, Calendar, Zap, Layers, Activity } from "lucide-react";

export default async function DashboardPage() {
  const session = await auth();

  return (
    <div className="space-y-8 animate-fade-in">
      {/* Welcome Banner */}
      <div>
        <h1 className="font-heading text-3xl font-extrabold tracking-tight text-white mb-2">
          Welcome to your Execution OS
        </h1>
        <p className="text-slate-400 text-sm">
          Account email: <span className="text-indigo-400 font-semibold">{session?.user?.email}</span>. Status: Ready.
        </p>
      </div>

      {/* Grid Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Card 1 */}
        <div className="glass-card p-6 rounded-xl space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-heading font-bold text-sm text-slate-300 uppercase tracking-wider">
              Planning Engine
            </h3>
            <Calendar className="w-5 h-5 text-indigo-400" />
          </div>
          <p className="text-2xl font-extrabold text-white">0 Active Tasks</p>
          <div className="p-3 rounded-lg bg-indigo-500/5 border border-indigo-500/10 text-xs text-indigo-300">
            Phase 3 Adaptive Scheduling modules will activate here.
          </div>
        </div>

        {/* Card 2 */}
        <div className="glass-card p-6 rounded-xl space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-heading font-bold text-sm text-slate-300 uppercase tracking-wider">
              Knowledge Compression
            </h3>
            <Layers className="w-5 h-5 text-violet-400" />
          </div>
          <p className="text-2xl font-extrabold text-white">0 Compressed Nodes</p>
          <div className="p-3 rounded-lg bg-violet-500/5 border border-violet-500/10 text-xs text-violet-300">
            Phase 4 Document Parsing and RAG stores will activate here.
          </div>
        </div>
      </div>

      {/* Core OS Health status */}
      <div className="glass-card p-6 rounded-xl">
        <div className="flex items-center gap-3 mb-4">
          <Activity className="w-5 h-5 text-emerald-400" />
          <h3 className="font-heading font-bold text-white">System Logs & Connectivity</h3>
        </div>
        <div className="space-y-2 font-mono text-xs text-slate-400 bg-black/40 p-4 rounded-lg border border-white/5">
          <p className="text-emerald-400">[info] OS core components initialized successfully.</p>
          <p className="text-indigo-400">[info] FastAPI connection established. Auth token stored in cookie.</p>
          <p className="text-slate-500">[system] Waiting for Phase 2 contexts...</p>
        </div>
      </div>
    </div>
  );
}
