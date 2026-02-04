# System Architecture

```mermaid
graph TB
    subgraph "User Interface Layer"
        A[Streamlit Web App]
        A1[Text Input]
        A2[Voice Input]
        A3[Document Upload]
    end
    
    subgraph "Input Processing Layer"
        B[Document Processor]
        C[Speech Recognition]
        D[Text Preprocessor]
    end
    
    subgraph "AI Analysis Layer"
        E[Medical Analyzer]
        E1[Gemma 2 2B Model]
        E2[Rule-Based Engine]
    end
    
    subgraph "Matching Layer"
        F[Doctor Matcher]
        G[Doctors Database]
    end
    
    subgraph "Output Layer"
        H[Results Display]
        H1[Specialty Detection]
        H2[Doctor Recommendations]
        H3[Urgency Assessment]
    end
    
    A1 --> D
    A2 --> C
    A3 --> B
    
    B --> D
    C --> D
    D --> E
    
    E --> E1
    E --> E2
    E1 -.Fallback.-> E2
    
    E --> F
    F --> G
    
    F --> H
    H --> H1
    H --> H2
    H --> H3
    
    style E1 fill:#90EE90
    style E2 fill:#87CEEB
    style G fill:#FFD700
    style A fill:#FF6B6B
