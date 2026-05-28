"use client";

import { UploadCloud, FileText } from "lucide-react";

export function DocumentUploader() {
  return (
    <div className="glass-panel p-8 rounded-2xl border border-white/5 flex flex-col items-center justify-center text-center space-y-4">
      <div className="w-16 h-16 rounded-2xl bg-indigo-500/10 flex items-center justify-center border border-indigo-500/20 mb-2">
        <UploadCloud className="w-8 h-8 text-indigo-400" />
      </div>
      <h2 className="font-bold text-lg text-white">Upload Knowledge</h2>
      <p className="text-sm text-slate-400 max-w-xs">
        Drag and drop PDFs or text files to extract key takeaways and generate flashcards instantly.
      </p>
      
      <div className="mt-4 w-full relative">
        <input 
          type="file" 
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer" 
          accept=".pdf,.txt,.md"
        />
        <div className="w-full px-4 py-3 rounded-xl border border-dashed border-indigo-500/30 bg-indigo-500/5 hover:bg-indigo-500/10 transition flex items-center justify-center gap-2">
          <FileText className="w-4 h-4 text-indigo-400" />
          <span className="text-sm font-semibold text-indigo-300">Select Files</span>
        </div>
      </div>
    </div>
  );
}
