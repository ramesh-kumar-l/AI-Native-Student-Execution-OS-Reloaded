"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { Brain, AlertCircle, Loader2, CheckCircle2 } from "lucide-react";

export default function VerifyEmailPage() {
  const searchParams = useSearchParams();
  const token = searchParams.get("token");

  const [loading, setLoading] = useState(true);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!token) {
      setError("Verification token is missing.");
      setLoading(false);
      return;
    }

    const verify = async () => {
      const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";
      try {
        const res = await fetch(`${backendUrl}/api/v1/auth/verify-email?token=${token}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.detail || "Email verification failed.");
        }

        setSuccess(true);
      } catch (err: any) {
        console.error(err);
        setError(err.message || "Invalid or expired token.");
      } finally {
        setLoading(false);
      }
    };

    verify();
  }, [token]);

  return (
    <div className="relative min-h-screen flex items-center justify-center bg-[#020617] px-6 overflow-hidden">
      <div className="absolute top-1/4 left-1/4 w-[400px] h-[400px] rounded-full bg-indigo-500/5 blur-[100px] pointer-events-none" />

      <div className="w-full max-w-md relative z-10 text-center">
        {/* Brand Header */}
        <div className="flex flex-col items-center mb-8">
          <div className="w-12 h-12 rounded-xl bg-indigo-500/10 flex items-center justify-center border border-indigo-500/20 mb-4">
            <Brain className="w-6 h-6 text-indigo-400" />
          </div>
          <h2 className="font-heading text-2xl font-bold text-white">Email Verification</h2>
        </div>

        {/* Card */}
        <div className="glass-panel p-8 rounded-2xl border border-white/5 shadow-2xl">
          {loading && (
            <div className="flex flex-col items-center py-6">
              <Loader2 className="w-10 h-10 animate-spin text-indigo-400 mb-4" />
              <p className="text-slate-300 text-sm">Verifying your email address, please wait...</p>
            </div>
          )}

          {!loading && success && (
            <div className="flex flex-col items-center py-6">
              <CheckCircle2 className="w-12 h-12 text-emerald-400 mb-4" />
              <h3 className="text-lg font-semibold text-white mb-2">Email Verified!</h3>
              <p className="text-slate-400 text-sm mb-8">
                Your email has been verified successfully. You can now access the platform.
              </p>
              <Link
                href="/login"
                className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-3 px-4 rounded-lg transition"
              >
                Continue to Log In
              </Link>
            </div>
          )}

          {!loading && error && (
            <div className="flex flex-col items-center py-6">
              <AlertCircle className="w-12 h-12 text-red-400 mb-4" />
              <h3 className="text-lg font-semibold text-white mb-2">Verification Failed</h3>
              <p className="text-red-200 text-sm mb-8">{error}</p>
              <Link
                href="/register"
                className="w-full bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 font-semibold py-3 px-4 rounded-lg transition mb-3"
              >
                Try Registering Again
              </Link>
              <Link
                href="/login"
                className="text-xs text-slate-400 hover:text-slate-300 font-medium transition"
              >
                Back to Sign In
              </Link>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
