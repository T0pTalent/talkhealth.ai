function_list = [
    {
        "name": "ask_knowledge",
        "description": "This function is called when a user asks for specific medical knowledge, such as symptoms of a disease or treatment options.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The user's medical question to be answered."
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "normal_chat",
        "description": "This function is called when the user wants to engage in a casual conversation about medical topics or has general medical inquiries or general information about the services provided by the medical assistant",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The user's message to initiate a normal chat."
                }
            },
            "required": ["message"]
        }
    },
    {
        "name": "unfamiliar_question",
        "description": "This function is called when the user's question is outside the scope of medical assistance, such as personal questions or unrelated topics.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The user's question that is not related to medical assistance."
                }
            },
            "required": ["question"]
        }
    }
]