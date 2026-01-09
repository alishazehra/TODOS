import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Evolution of Todo",
  description: "A full-stack todo application",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
