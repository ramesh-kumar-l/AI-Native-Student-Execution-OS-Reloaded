export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen flex flex-col bg-[#020617] text-slate-100 antialiased">
      {children}
    </div>
  );
}
