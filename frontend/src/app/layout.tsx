import type { Metadata } from "next";
import { Inter, Outfit } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const outfit = Outfit({
  variable: "--font-outfit",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AI-Native Student Execution OS",
  description: "A persistent cognitive infrastructure that transforms student intent into measurable achievement through autonomous execution agents.",
  keywords: ["AI Student Planner", "Study Tracker", "Cognitive Agent", "Student OS"],
  authors: [{ name: "AI-Native Student OS Development Team" }],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${outfit.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col font-sans bg-[#020617] text-[#f8fafc]">
        {children}
      </body>
    </html>
  );
}
