import torch
import transformers
from transformers import LlamaTokenizer, LlamaForCausalLM

def generate_prompt(text):
    return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{text}

### Response:"""

checkpoint="DUOMO-Lab/TransGPT-v0"
tokenizer = LlamaTokenizer.from_pretrained(checkpoint)
model = LlamaForCausalLM.from_pretrained(checkpoint).half().cuda()
model.eval()

text = '我想了解如何申请和更新驾驶证？'
prompt = generate_prompt(text)
input_ids = tokenizer.encode(prompt, return_tensors='pt').to('cuda')


with torch.no_grad():
    output_ids = model.generate(
        input_ids=input_ids,
        max_new_tokens=1024,
        temperature=1,
        top_k=20,
        top_p=0.9,
        repetition_penalty=1.15
    ).cuda()


output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output.replace(text, '').strip())
