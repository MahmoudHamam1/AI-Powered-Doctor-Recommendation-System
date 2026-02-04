#!/bin/bash
source /workspaces/agentcore-rag-chatbot/.devcontainer/.env
npx -y @upstash/context7-mcp --api-key "$CONTEXT7_API_KEY"