import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

class VisualizerAgent:
    def generate_chart(self, df: pd.DataFrame):
        plt.figure(figsize=(6,4))
        if df.select_dtypes(include='number').shape[1] > 0:
            df.select_dtypes(include='number').head(10).plot(kind='bar')
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return img_base64
