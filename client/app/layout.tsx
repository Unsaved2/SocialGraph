import { ReactNode } from 'react';

export const metadata = {
  title: 'My Next.js 13 App',
  description: 'Using the App Router with TypeScript',
};

interface RootLayoutProps {
  children: ReactNode;
}

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body>
        <nav style={{ background: '#eee', padding: '0.5rem' }}>My Navbar</nav>
        {children}
      </body>
    </html>
  );
}
