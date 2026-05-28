"use client";

import { useState } from "react";
import { User, GraduationCap, BookOpen, Save } from "lucide-react";

export default function ProfilePage() {
  const [loading, setLoading] = useState(false);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
          Student Profile
        </h1>
        <p className="text-slate-400 mt-2">Manage your academic context and learning preferences.</p>
      </div>

      <div className="glass-panel p-8 rounded-2xl border border-white/5 shadow-xl relative overflow-hidden">
        {/* Glow effect */}
        <div className="absolute top-0 right-0 w-64 h-64 bg-indigo-500/10 rounded-full blur-[80px] -mr-32 -mt-32 pointer-events-none" />

        <form className="space-y-6 relative z-10">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="text-xs font-semibold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                <GraduationCap className="w-4 h-4 text-indigo-400" />
                University
              </label>
              <input type="text" className="w-full input-field" placeholder="E.g., Stanford University" />
            </div>
            <div className="space-y-2">
              <label className="text-xs font-semibold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-violet-400" />
                Major
              </label>
              <input type="text" className="w-full input-field" placeholder="E.g., Computer Science" />
            </div>
            <div className="space-y-2 md:col-span-2">
              <label className="text-xs font-semibold uppercase tracking-wider text-slate-400 flex items-center gap-2">
                <User className="w-4 h-4 text-emerald-400" />
                Bio
              </label>
              <textarea className="w-full input-field h-24 resize-none" placeholder="Tell us about your academic journey..." />
            </div>
          </div>

          <div className="pt-4 border-t border-white/10 flex justify-end">
            <button
              type="button"
              className="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-2 px-6 rounded-lg transition shadow-md shadow-indigo-600/10 hover:shadow-indigo-600/20 active:scale-95 flex items-center gap-2"
            >
              <Save className="w-4 h-4" />
              Save Profile
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
