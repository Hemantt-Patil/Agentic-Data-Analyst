"use client";

import { useState } from "react";
import FileUploader from "./components/FileUploader";
import AnalysisResults from "./components/AnalysisResults";
import ChartView from "./components/ChartView";

export default function HomePage() {
  const [result, setResult] = useState<any>(null);

  return (
    <main className="max-w-5xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">🤖 Agentic Data Analyst</h1>

      {/* CSV Upload */}
      <FileUploader onResult={setResult} />

      {/* Analysis Results */}
      {result && (
        <div className="mt-6 space-y-6">
          <AnalysisResults result={result} />
          <ChartView imgBase64={result?.chart} />
        </div>
      )}
    </main>
  );
}
