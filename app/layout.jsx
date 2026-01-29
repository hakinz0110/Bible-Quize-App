export const metadata = {
  title: "Bible Quiz",
  description: "Bible quiz modes: classic, practice, and challenge.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
        <style jsx global>{`
          :root {
            color-scheme: light;
            --bg: #f5f7fb;
            --card: #ffffff;
            --text: #0f172a;
            --muted: #475569;
            --accent: #2563eb;
            --accent-soft: #dbeafe;
            --border: #e2e8f0;
            --good: #16a34a;
            --bad: #dc2626;
          }
          * {
            box-sizing: border-box;
          }
          body {
            margin: 0;
            font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
            background: var(--bg);
            color: var(--text);
          }
          button {
            font: inherit;
            cursor: pointer;
          }
          a {
            color: inherit;
            text-decoration: none;
          }
        `}</style>
      </body>
    </html>
  );
}
