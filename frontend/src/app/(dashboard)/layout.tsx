import { auth, signOut } from "@/auth";
import { redirect } from "next/navigation";
import Link from "next/link";
import { Brain, LayoutDashboard, Calendar, Library, Sparkles, Settings, LogOut, User, Target, LineChart } from "lucide-react";

export default async function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await auth();
  if (!session) {
    redirect("/login");
  }

  // Define Server Action to sign out user
  async function handleSignOut() {
    "use server";
    await signOut({ redirectTo: "/" });
  }

  const navItems = [
    { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
    { name: "Planning", href: "/dashboard/planning", icon: Calendar, badge: "AI" },
    { name: "Knowledge", href: "/dashboard/knowledge", icon: Library, badge: "RAG" },
    { name: "Agents", href: "/dashboard/agents", icon: Sparkles, badge: "AI" },
    { name: "Career", href: "/dashboard/career", icon: Target, badge: "AI" },
    { name: "Analytics", href: "/dashboard/analytics", icon: LineChart },
    { name: "Profile", href: "/dashboard/profile", icon: User },
    { name: "Goals", href: "/dashboard/goals", icon: Sparkles },
    { name: "Calendar", href: "/dashboard/calendar", icon: Calendar },
    { name: "Settings", href: "/dashboard/settings", icon: Settings },
  ];

  return (
    <div className="flex h-screen bg-[#020617] overflow-hidden text-slate-100 font-sans">
      {/* Sidebar */}
      <aside className="w-64 glass-panel border-r border-white/5 flex flex-col justify-between shrink-0">
        <div>
          {/* Logo */}
          <div className="p-6 border-b border-white/5 flex items-center gap-2">
            <Brain className="w-7 h-7 text-indigo-400" />
            <span className="font-heading font-bold text-lg tracking-tight bg-gradient-to-r from-indigo-200 to-indigo-400 bg-clip-text text-transparent">
              StudentOS
            </span>
          </div>

          {/* Navigation Links */}
          <nav className="p-4 space-y-1">
            {navItems.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className={`flex items-center justify-between p-3 rounded-lg text-sm font-medium transition cursor-pointer ${
                  item.href === "/dashboard"
                    ? "bg-indigo-600/20 border border-indigo-600/30 text-white"
                    : "text-slate-400 hover:bg-white/5 hover:text-white border border-transparent"
                }`}
              >
                <div className="flex items-center gap-3">
                  <item.icon className="w-5 h-5 shrink-0" />
                  <span>{item.name}</span>
                </div>
                {item.badge && (
                  <span className="text-[10px] font-bold uppercase px-1.5 py-0.5 rounded bg-white/5 text-slate-400 scale-90">
                    {item.badge}
                  </span>
                )}
              </Link>
            ))}
          </nav>
        </div>

        {/* User profile footer */}
        <div className="p-4 border-t border-white/5 space-y-3">
          <div className="flex items-center gap-3 px-2">
            <div className="w-9 h-9 rounded-full bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center">
              <User className="w-5 h-5 text-indigo-400" />
            </div>
            <div className="overflow-hidden">
              <p className="text-xs font-semibold text-slate-200 truncate">
                {session.user?.email || "Student Account"}
              </p>
              <p className="text-[10px] text-slate-500 uppercase tracking-wider font-bold">
                Student
              </p>
            </div>
          </div>

          <form action={handleSignOut}>
            <button
              type="submit"
              className="w-full flex items-center gap-3 p-3 rounded-lg text-sm font-medium text-slate-400 hover:bg-red-500/10 hover:text-red-400 transition cursor-pointer border border-transparent"
            >
              <LogOut className="w-5 h-5 shrink-0" />
              <span>Log Out</span>
            </button>
          </form>
        </div>
      </aside>

      {/* Main Viewport Content Area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top Header */}
        <header className="glass-panel h-16 border-b border-white/5 px-8 flex items-center justify-between shrink-0">
          <h2 className="font-heading font-bold text-lg text-white">Execution OS Platform</h2>
          <div className="text-xs text-indigo-300 font-semibold px-3 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/20 backdrop-blur-sm">
            Phase 1 Core Running
          </div>
        </header>

        {/* Content View */}
        <main className="flex-1 overflow-y-auto p-8 relative">
          <div className="max-w-4xl mx-auto">{children}</div>
        </main>
      </div>
    </div>
  );
}
