

https://github.com/user-attachments/assets/3948a27e-4efb-498a-89e1-99aca771bc3b


**Content Engine - Query and Compare PDFs**
[ML, NLP, Information Retrival, Document Search]
- This Streamlit application enables users to upload PDF documents and query their contents in a chatbot-like interface. 
- It uses FAISS for efficient similarity search and a pre-trained embedding model to generate vector embeddings for document content.

**Features**
- Upload multiple PDF files to create a searchable document index.
- Ask questions about the content of the uploaded PDFs.
- Get relevant results ranked by their similarity to the query.
- Easily clear chat history and start fresh.
- Intuitive chatbot interface with session persistence.

**How It Works**
- Loading PDFs: PDF files are preprocessed, and their contents are converted into embeddings using a pre-trained model.
- Creating FAISS Index: The embeddings are stored in a FAISS index for fast similarity search.
- Querying: User queries are embedded and compared against the FAISS index to retrieve the most relevant content.
- Interactive Interface: Results are displayed in a chatbot-like interface, and users can reset the conversation with the "Clear Chat" button.

**Retrieval-Augmented Generation (RAG)**
In this project, RAG principles are applied to allow efficient PDF querying by leveraging:
- Document Retrieval: Relevant content is retrieved using FAISS (vector similarity search) based on semantic embeddings.
- Content Display: Instead of generating new content, the system retrieves the closest matches and presents them as answers, simulating RAG-like behavior without generative modeling.

**LangChain simplifies document preprocessing for RAG by:**
- Extracting content from PDFs using PyPDFLoader.
- Splitting documents into smaller, structured chunks for easier embedding and retrieval.

**Customization**
- Embedding Model: You can replace the default embedding model with another model supported by Hugging Face by modifying preprocess.py.
- FAISS Parameters: Tune FAISS settings for better indexing and search performance in query_engine.py.
