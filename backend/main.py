from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from agents.data_reader_agent import DataReaderAgent
from agents.analyst_agent import AnalystAgent
from agents.insight_agent import InsightAgent
from agents.summary_agent import SummaryAgent
from agents.visualizer_agent import VisualizerAgent
from utils.logger import log_event

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_reader = DataReaderAgent()
analyst = AnalystAgent()
insight = InsightAgent()
summary = SummaryAgent()
visualizer = VisualizerAgent()

@app.post("/analyze/")
async def analyze_csv(file: UploadFile = File(...)):
    log_event(f"Received file: {file.filename}")
    content = await file.read()
    df, meta = data_reader.read_csv(content)

    analysis_task = asyncio.create_task(analyst.analyze(df))
    insight_task = asyncio.create_task(insight.derive_insights(df))

    analysis, insights = await asyncio.gather(analysis_task, insight_task)
    report = await summary.summarize(analysis, insights)
    chart = visualizer.generate_chart(df)

    return {
        "metadata": meta,
        "analysis": analysis,
        "insights": insights,
        "summary": report,
        "chart": chart
    }
