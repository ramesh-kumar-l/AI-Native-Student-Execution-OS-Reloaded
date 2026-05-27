import Link from "next/link";
import { ArrowRight, Brain, Shield, Zap, Sparkles, Cpu, Award } from "lucide-react";

export default function Home() {
  return (
    <div className="relative min-h-screen bg-[#020617] overflow-hidden flex flex-col justify-between">
      {/* Decorative Blur Background Orbs */}
      <div className="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] rounded-full bg-indigo-500/10 blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-10%] right-[-10%] w-[600px] h-[600px] rounded-full bg-violet-600/10 blur-[130px] pointer-events-none" />

      {/* Navigation Header */}
      <header className="glass-panel sticky top-0 z-50 px-6 py-4 flex items-center justify-between border-b border-white/5">
        <div className="flex items-center gap-2">
          <Brain className="w-8 h-8 text-indigo-400" />
          <span className="font-heading font-bold text-xl tracking-tight bg-gradient-to-r from-indigo-200 via-indigo-400 to-indigo-100 bg-clip-text text-transparent">
            StudentOS
          </span>
        </div>
        <div className="flex items-center gap-4">
          <Link href="/login" className="text-sm font-medium text-slate-300 hover:text-white transition">
            Sign In
          </Link>
          <Link
            href="/register"
            className="text-sm font-medium bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded-lg transition shadow-md shadow-indigo-600/20"
          >
            Get Started
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-6 py-20 flex-grow flex flex-col items-center justify-center text-center relative z-10">
        <div className="animate-slide-up flex flex-col items-center">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 text-xs font-semibold text-indigo-300 mb-8 backdrop-blur-sm">
            <Sparkles className="w-4 h-4 text-accent-violet" />
            <span>Autonomous Cognitive Framework for Ambitious Learners</span>
          </div>

          {/* Heading */}
          <h1 className="font-heading text-5xl md:text-7xl font-extrabold tracking-tight leading-[1.1] max-w-4xl mb-6">
            Transform Intent Into <br />
            <span className="text-gradient">Measurable Achievement</span>
          </h1>

          {/* Subheading */}
          <p className="text-slate-400 text-lg md:text-xl max-w-2xl mb-10 leading-relaxed">
            Students don't fail due to lack of information. They fail from fragmented execution.
            StudentOS consolidates planning, memory, learning, and action into a single persistent cognitive agent partner.
          </p>

          {/* Actions */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <Link
              href="/register"
              className="group inline-flex items-center gap-2 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-8 py-4 rounded-xl transition shadow-lg shadow-indigo-600/30 hover:scale-[1.01]"
            >
              <span>Initialize Student OS</span>
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition" />
            </Link>
            <Link
              href="/login"
              className="inline-flex items-center justify-center bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 font-semibold px-8 py-4 rounded-xl transition backdrop-blur-sm"
            >
              Access Dashboard
            </Link>
          </div>
        </div>

        {/* Feature Grid */}
        <section className="mt-32 w-full">
          <h2 className="font-heading text-3xl font-bold mb-16 text-slate-100">
            Core Operating Core Capabilities
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Card 1 */}
            <div className="glass-card p-8 rounded-2xl text-left">
              <div className="w-12 h-12 rounded-xl bg-indigo-500/10 flex items-center justify-center mb-6 border border-indigo-500/20">
                <Cpu className="w-6 h-6 text-indigo-400" />
              </div>
              <h3 className="font-heading text-lg font-bold text-white mb-3">AI Planning Infrastructure</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Adaptive scheduling, intelligent prioritization, and workload balancing customized to your cognitive capacity.
              </p>
            </div>

            {/* Card 2 */}
            <div className="glass-card p-8 rounded-2xl text-left">
              <div className="w-12 h-12 rounded-xl bg-violet-500/10 flex items-center justify-center mb-6 border border-violet-500/20">
                <Sparkles className="w-6 h-6 text-violet-400" />
              </div>
              <h3 className="font-heading text-lg font-bold text-white mb-3">Knowledge Compression</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                Upload slides, lectures, or texts to generate immediate structured study nodes, semantic summaries, and quizzes.
              </p>
            </div>

            {/* Card 3 */}
            <div className="glass-card p-8 rounded-2xl text-left">
              <div className="w-12 h-12 rounded-xl bg-blue-500/10 flex items-center justify-center mb-6 border border-blue-500/20">
                <Award className="w-6 h-6 text-blue-400" />
              </div>
              <h3 className="font-heading text-lg font-bold text-white mb-3">Persistent Memory System</h3>
              <p className="text-slate-400 text-sm leading-relaxed">
                A lifetime learning companion containing short, long-term, and episodic records of your study progress.
              </p>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-white/5 py-8 text-center text-xs text-slate-500 relative z-10">
        <p>&copy; {new Date().getFullYear()} AI-Native Student Execution OS. Built for ambitious knowledge workers.</p>
      </footer>
    </div>
  );
}
