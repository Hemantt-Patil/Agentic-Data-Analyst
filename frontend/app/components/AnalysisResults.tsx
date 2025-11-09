"use client";

interface AnalysisResultsProps {
  result: any;
}

export default function AnalysisResults({ result }: AnalysisResultsProps) {
  if (!result) return null;

  return (
    <div className="bg-white p-4 rounded-lg shadow space-y-6">
      <section>
        <h2 className="text-lg font-bold mb-2">🧠 Technical Analysis</h2>
        <pre className="whitespace-pre-wrap text-sm">{result.analysis}</pre>
      </section>

      <section>
        <h2 className="text-lg font-bold mb-2">💡 Business Insights</h2>
        <pre className="whitespace-pre-wrap text-sm">{result.insights}</pre>
      </section>

      <section>
        <h2 className="text-lg font-bold mb-2">📋 Summary Report</h2>
        <pre className="whitespace-pre-wrap text-sm">{result.summary}</pre>
      </section>
    </div>
  );
}
