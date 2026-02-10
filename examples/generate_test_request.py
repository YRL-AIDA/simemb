import json



def generate_text_only_request(filename: str = "text_req.json") -> list[str]:
    texts = [
        "What is the capital of France?",
        "Explain quantum computing in simple terms.",
        "How does photosynthesis work?",
        "What are the symptoms of the common cold?",
        "Describe the plot of 'Pride and Prejudice'.",
        "What is the Pythagorean theorem?",
        "How to bake chocolate chip cookies?",
        "What causes climate change?",
        "Who was Leonardo da Vinci?",
        "Explain the theory of relativity.",
        "What is machine learning?",
        "How do vaccines work?",
        "What is the largest planet in our solar system?",
        "Describe the water cycle.",
        "What is blockchain technology?",
        "How to tie a tie?",
        "What are the benefits of regular exercise?",
        "Explain the greenhouse effect.",
        "Who wrote 'Romeo and Juliet'?",
        "What is the speed of light?",
        "How does a car engine work?",
        "What is the Fibonacci sequence?",
        "Describe the process of mitosis.",
        "What are renewable energy sources?",
        "How to write a cover letter?",
        "What is the periodic table?",
        "Explain Newton's laws of motion.",
        "What is the human genome project?",
        "How do airplanes fly?",
        "What is artificial intelligence?",
        "Describe the French Revolution.",
        "What are the stages of sleep?",
        "How to grow tomatoes at home?",
        "What is the Big Bang theory?",
        "Explain the concept of supply and demand.",
        "What is the tallest mountain in the world?",
        "How does the internet work?",
        "What are the main types of clouds?",
        "Describe the circulatory system.",
        "What is cryptocurrency?",
        "How to meditate for beginners?",
        "What is the difference between weather and climate?",
        "Explain the process of digestion.",
        "What are the seven wonders of the ancient world?",
        "How to change a flat tire?",
        "What is the function of DNA?",
        "Describe the life cycle of a butterfly.",
        "What is the Richter scale?",
        "How do solar panels work?",
        "What is the meaning of life?"
    ]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"inputs": texts}, f, indent=2, ensure_ascii=False)
    print(f"Generated  '{filename}' with {len(texts)} text requests.")

if __name__ == "__main__":
    generate_text_only_request()
