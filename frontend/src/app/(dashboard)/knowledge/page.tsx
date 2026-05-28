"use client";

import { BrainCircuit } from "lucide-react";
import { DocumentUploader } from "@/components/knowledge/DocumentUploader";
import { FlashcardDeck } from "@/components/knowledge/FlashcardDeck";
import { SummaryViewer } from "@/components/knowledge/SummaryViewer";

export default function KnowledgePage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-heading font-bold bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent flex items-center gap-3">
          <BrainCircuit className="w-8 h-8 text-emerald-400" />
          Knowledge Compression
        </h1>
        <p className="text-slate-400 mt-2">Upload materials to extract summaries and generate active recall flashcards instantly.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-1 space-y-6">
          <DocumentUploader />
          <FlashcardDeck />
        </div>
        <div className="md:col-span-2">
          <SummaryViewer />
        </div>
      </div>
    </div>
  );
}
