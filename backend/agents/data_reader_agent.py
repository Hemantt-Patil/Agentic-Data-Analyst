import pandas as pd
import io

class DataReaderAgent:
    def read_csv(self, file_content: bytes):
        df = pd.read_csv(io.BytesIO(file_content))
        info = {
            "columns": df.columns.tolist(),
            "shape": df.shape,
            "head": df.head(3).to_dict(orient="records")
        }
        return df, info
