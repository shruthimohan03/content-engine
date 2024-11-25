**Content Engine - Query and Compare PDFs**
This Streamlit application enables users to upload PDF documents and query their contents in a chatbot-like interface. 
It uses FAISS for efficient similarity search and a pre-trained embedding model to generate vector embeddings for document content.

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

**Customization**
- Embedding Model: You can replace the default embedding model with another model supported by Hugging Face by modifying preprocess.py.
- FAISS Parameters: Tune FAISS settings for better indexing and search performance in query_engine.py.
