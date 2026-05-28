"use client";

import { Calendar as CalendarIcon, Link as LinkIcon, RefreshCw } from "lucide-react";

export default function CalendarPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent flex items-center gap-3">
            <CalendarIcon className="w-8 h-8 text-rose-400" />
            Calendar Sources
          </h1>
          <p className="text-slate-400 mt-2">Connect iCal feeds from your university or personal calendar.</p>
        </div>
        <button className="bg-rose-600 hover:bg-rose-500 text-white font-medium py-2 px-4 rounded-lg transition shadow-md shadow-rose-600/10 hover:shadow-rose-600/20 active:scale-95 flex items-center gap-2">
          <LinkIcon className="w-4 h-4" />
          Add Source
        </button>
      </div>

      <div className="glass-panel p-8 rounded-2xl border border-white/5 flex flex-col items-center justify-center text-center space-y-4 py-16">
        <div className="w-16 h-16 rounded-2xl bg-rose-500/10 flex items-center justify-center border border-rose-500/20">
          <CalendarIcon className="w-8 h-8 text-rose-400" />
        </div>
        <h3 className="text-xl font-bold text-white">No Calendars Connected</h3>
        <p className="text-slate-400 max-w-sm">
          Link an iCal (.ics) URL to automatically ingest your classes, exams, and personal events.
        </p>
      </div>
    </div>
  );
}
