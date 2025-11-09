"use client";

interface ChartViewProps {
  imgBase64?: string;
}

export default function ChartView({ imgBase64 }: ChartViewProps) {
  if (!imgBase64) return null;

  return (
    <div className="mt-6 bg-white p-4 rounded-lg shadow">
      <h2 className="text-lg font-bold mb-2">📊 Visualization</h2>
      <img src={`data:image/png;base64,${imgBase64}`} alt="CSV Chart" />
    </div>
  );
}
