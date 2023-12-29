function_list = [
    {
        "name": "ask_knowledge",
        "description": "This function is called when user asks medical knowledge",
        "parameters": {
            "type": "object",
            "properties": {
            },
        "required": [],
        },
    },
    {
        "name": "unfamiliar_question",
        "description": "This function is called when user's question is not related to medical assistant.",
        "parameters": {
            "type": "object",
            "properties": {
            },
        "required": [],
        },
    }
]

# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "get_knowledge",
#             "description": "This function is called when user asks medical knowledge from knowledge base.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {

#                 },
#                 "required": []
#             },
#         }
#     },
#     {
#         "type": "function",
#         "function": {
#             "name": "unfamiliar_question",
#             "description": "This function is called when user's question is not related to medical assistant",
#             "parameters": {
#                 "type": "object",
#                 "properties": {

#                 },
#                 "required": []
#             },
#         }
#     },
#     # {
#     #     "name": "ask_summarization",
#     #     "description": "This function is called when user asks summarization.",
#     #     "parameters": {
#     #         "type": "object",
#     #         "properties": {

#     #         },
#     #         "required": []
#     #     },
#     # }
# ]