"use client";

import { useState } from "react";
import { signIn } from "next-auth/react";
import Link from "next/link";
import { Brain, AlertCircle, Loader2, MailCheck } from "lucide-react";

export default function RegisterPage() {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [googleLoading, setGoogleLoading] = useState(false);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!fullName || !email || !password || !confirmPassword) return;

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    if (password.length < 6) {
      setError("Password must be at least 6 characters.");
      return;
    }

    setError(null);
    setLoading(true);

    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

    try {
      const res = await fetch(`${backendUrl}/api/v1/auth/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          password,
          full_name: fullName,
        }),
      });

      if (!res.ok) {
        const errorData = await res.json().catch(() => ({}));
        throw new Error(errorData.detail || "Registration failed. Account might already exist.");
      }

      setSuccess(true);
    } catch (err: any) {
      console.error(err);
      setError(err.message || "An unexpected error occurred. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = async () => {
    setError(null);
    setGoogleLoading(true);
    try {
      await signIn("google", { callbackUrl: "/dashboard" });
    } catch (err) {
      console.error(err);
      setError("Failed to register with Google.");
      setGoogleLoading(false);
    }
  };

  if (success) {
    return (
      <div className="relative min-h-screen flex items-center justify-center bg-[#020617] px-6 overflow-hidden">
        <div className="absolute top-1/4 left-1/4 w-[400px] h-[400px] rounded-full bg-indigo-500/5 blur-[100px] pointer-events-none" />
        <div className="w-full max-w-md relative z-10 text-center">
          <div className="w-16 h-16 rounded-2xl bg-indigo-500/10 flex items-center justify-center border border-indigo-500/20 mb-6 mx-auto">
            <MailCheck className="w-8 h-8 text-indigo-400" />
          </div>
          <h2 className="font-heading text-2xl font-bold text-white mb-3">Check your inbox</h2>
          <p className="text-slate-400 text-sm leading-relaxed mb-8">
            We have sent a verification link to <span className="text-indigo-300 font-semibold">{email}</span>. 
            Please open the link to activate your account.
          </p>
          <Link
            href="/login"
            className="inline-flex items-center justify-center bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-3 px-6 rounded-lg transition"
          >
            Go to Log In
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="relative min-h-screen flex items-center justify-center bg-[#020617] px-6 py-12 overflow-hidden">
      {/* Decorative Orbs */}
      <div className="absolute top-1/4 left-1/4 w-[400px] h-[400px] rounded-full bg-indigo-500/5 blur-[100px] pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] rounded-full bg-violet-600/5 blur-[100px] pointer-events-none" />

      <div className="w-full max-w-md relative z-10">
        {/* Brand Header */}
        <div className="flex flex-col items-center mb-8">
          <div className="w-12 h-12 rounded-xl bg-indigo-500/10 flex items-center justify-center border border-indigo-500/20 mb-4">
            <Brain className="w-6 h-6 text-indigo-400" />
          </div>
          <h2 className="font-heading text-2xl font-bold text-white">Create your account</h2>
          <p className="text-slate-400 text-sm mt-2">Initialize your student cognitive OS</p>
        </div>

        {/* Card */}
        <div className="glass-panel p-8 rounded-2xl border border-white/5 shadow-2xl">
          {error && (
            <div className="mb-6 p-4 rounded-lg bg-red-500/10 border border-red-500/20 flex items-start gap-3">
              <AlertCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
              <p className="text-red-200 text-sm">{error}</p>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label htmlFor="fullName" className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
                Full Name
              </label>
              <input
                id="fullName"
                type="text"
                required
                disabled={loading || googleLoading}
                placeholder="Jane Doe"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="w-full input-field"
              />
            </div>

            <div>
              <label htmlFor="email" className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
                Email Address
              </label>
              <input
                id="email"
                type="email"
                required
                disabled={loading || googleLoading}
                placeholder="student@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full input-field"
              />
            </div>

            <div>
              <label htmlFor="password" className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
                Password
              </label>
              <input
                id="password"
                type="password"
                required
                disabled={loading || googleLoading}
                placeholder="Min. 6 characters"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full input-field"
              />
            </div>

            <div>
              <label htmlFor="confirmPassword" className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
                Confirm Password
              </label>
              <input
                id="confirmPassword"
                type="password"
                required
                disabled={loading || googleLoading}
                placeholder="Re-enter password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="w-full input-field"
              />
            </div>

            <button
              type="submit"
              disabled={loading || googleLoading}
              className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-3 px-4 rounded-lg transition shadow-md shadow-indigo-600/10 hover:shadow-indigo-600/20 active:scale-[0.99] flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50"
            >
              {loading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  <span>Registering...</span>
                </>
              ) : (
                <span>Register Account</span>
              )}
            </button>
          </form>

          {/* Divider */}
          <div className="relative my-6">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-white/5"></div>
            </div>
            <div className="relative flex justify-center text-xs uppercase">
              <span className="bg-[#020617]/90 px-3 text-slate-500 font-semibold tracking-wider">Or register with</span>
            </div>
          </div>

          {/* Google Login Button */}
          <button
            type="button"
            onClick={handleGoogleLogin}
            disabled={loading || googleLoading}
            className="w-full flex items-center justify-center gap-3 bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 font-semibold py-3 px-4 rounded-lg transition active:scale-[0.99] cursor-pointer disabled:opacity-50"
          >
            {googleLoading ? (
               <Loader2 className="w-5 h-5 animate-spin text-slate-400" />
             ) : (
               <svg className="w-5 h-5 shrink-0" viewBox="0 0 24 24">
                 <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                 <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                 <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
                 <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
               </svg>
             )}
            <span>Sign Up with Google</span>
          </button>
        </div>

        {/* Bottom Link */}
        <p className="text-center text-sm text-slate-400 mt-6">
          Already have an account?{" "}
          <Link href="/login" className="text-indigo-400 hover:text-indigo-300 font-medium transition">
            Log In
          </Link>
        </p>
      </div>
    </div>
  );
}
