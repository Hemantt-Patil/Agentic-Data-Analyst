"use client";

import { useState } from "react";
import axios from "axios";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

interface FileUploaderProps {
  onResult: (data: any) => void;
}

export default function FileUploader({ onResult }: FileUploaderProps) {
  const [loading, setLoading] = useState(false);

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;

    console.log("Uploading file:", file.name);
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(`${BACKEND_URL}/analyze/`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
        timeout: 120000, // 2 minutes in case processing is slow
      });
      console.log("Response received:", res.data);
      onResult(res.data);
    } catch (err: any) {
      console.error("Error during upload:", err);
      if (err.response) {
        alert(`Backend Error: ${err.response.data.detail || err.response.statusText}`);
      } else {
        alert("Network or timeout error. Check backend is running.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-4 border rounded-lg bg-white shadow text-center">
      <input
        type="file"
        accept=".csv"
        onChange={handleUpload}
        className="mb-2"
      />
      {loading && <p className="text-gray-500 mt-2">Analyzing your CSV...</p>}
    </div>
  );
}

