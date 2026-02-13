from typing import Dict, List

from pydantic import BaseModel



class EmbedRequest(BaseModel):
    documents: List[Dict]
