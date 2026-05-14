# import os
# from dotenv import load_dotenv
# from langchain_nvidia_ai_endpoints import ChatNVIDIA







# # api_key = os.getenv("NVIDIA_API_KEY")
# # print("Loaded key:", api_key)  # sanity check
# # print("CWD:", os.getcwd())

# load_dotenv(dotenv_path="c:/Users/UNIQUE/PycharmProjects/Langgraph/.env")

# api_key = os.getenv("NVIDIA_API_KEY")

# llm= ChatNVIDIA(model="nvidia/llama-3-8b-instruct",api_key=api_key)

# llm= ChatNVIDIA(model="moonshotai/kimi-k2.6",
#     api_key=api_key)

# response= llm.invoke("hello I am Arif")
# print( response.content)



# from langchain_nvidia_ai_endpoints import list_models
# import os
# from dotenv import load_dotenv

# # Load your API key
# load_dotenv(dotenv_path="c:/Users/UNIQUE/PycharmProjects/Langgraph/.env")
# api_key = os.getenv("NVIDIA_API_KEY")

# # List all models available to your account
# models = list_models(api_key=api_key)
# print(models)

