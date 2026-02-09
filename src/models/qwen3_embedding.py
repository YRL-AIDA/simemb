import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel



class Qwen3Embedder:
    def __init__(self, model_name: str, device: str):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, 
            trust_remote_code=True
        )
        # TODO: Flash Attention
        self.model = AutoModel.from_pretrained(
            model_name,
            trust_remote_code=True,
            device_map="auto" if torch.cuda.is_available() else None,
            dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        ).to(device).eval()
        self.device = device

    def last_token_pool(self, last_hidden_states: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
        if left_padding:
            return last_hidden_states[:, -1]
        else:
            sequence_lengths = attention_mask.sum(dim=1) - 1
            batch_size = last_hidden_states.shape[0]
            return last_hidden_states[torch.arange(
                batch_size, 
                device=last_hidden_states.device
                ), sequence_lengths
            ]

    @torch.no_grad()
    def process(self, queries: list[str], normalize: bool = True) -> torch.Tensor:
        batch_dict = self.tokenizer(
            queries,
            padding=True,
            truncation=True,
            return_tensors="pt",
            # max_length=,
        )
        batch_dict.to(self.model.device)

        outputs = self.model(**batch_dict)
        embeddings = self.last_token_pool(
            outputs.last_hidden_state,
            batch_dict['attention_mask']
        )

        if normalize:
            return F.normalize(embeddings, p=2, dim=1)#.cpu().numpy()
        return embeddings
