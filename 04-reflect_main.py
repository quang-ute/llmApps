from reflection_agent import ReflectionAgent

def main():
    print("Hello from agents!")
    agent = ReflectionAgent()
    generation_system_prompt = "You are a Python programmer tasked with generating high quality Python code"

    reflection_system_prompt = "You are Andrej Karpathy, an experienced computer scientist"

    user_msg = "Generate a Python implementation of the Quick Sort algorithm"
    final_response = agent.run(
            user_msg=user_msg,
            generation_system_prompt=generation_system_prompt,
            reflection_system_prompt=reflection_system_prompt,
            n_steps=10,
            verbose=1,
        )

if __name__ == "__main__":
    main()
