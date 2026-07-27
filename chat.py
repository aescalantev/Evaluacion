{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtZECqz4sG8ZjTya6zC8ZJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aescalantev/Evaluacion/blob/main/chat.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Desinstalar todas las librerías de LangChain y relacionadas.\n",
        "!pip uninstall -y langchain langchain-community langchain-core langchain-google-genai langgraph langchain-text-splitters google-generativeai\n",
        "\n",
        "# 2. Limpiar el caché de pip para asegurar que las nuevas instalaciones no usen paquetes corruptos.\n",
        "!pip cache purge"
      ],
      "metadata": {
        "id": "5JSPNRgZHykx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "_U5XkpBRF-SG",
        "outputId": "11143716-0194-4d71-bcab-6ef62fa9ddef"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found existing installation: langchain 1.3.13\n",
            "Uninstalling langchain-1.3.13:\n",
            "  Would remove:\n",
            "    /usr/local/lib/python3.12/dist-packages/langchain-1.3.13.dist-info/*\n",
            "    /usr/local/lib/python3.12/dist-packages/langchain/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled langchain-1.3.13\n",
            "Found existing installation: langchain-openai 1.4.1\n",
            "Uninstalling langchain-openai-1.4.1:\n",
            "  Would remove:\n",
            "    /usr/local/lib/python3.12/dist-packages/langchain_openai-1.4.1.dist-info/*\n",
            "    /usr/local/lib/python3.12/dist-packages/langchain_openai/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled langchain-openai-1.4.1\n",
            "Found existing installation: langchain-community 0.4.2\n",
            "Uninstalling langchain-community-0.4.2:\n",
            "  Would remove:\n",
            "    /usr/local/lib/python3.12/dist-packages/langchain_community-0.4.2.dist-info/*\n",
            "    /usr/local/lib/python3.12/dist-packages/langchain_community/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled langchain-community-0.4.2\n",
            "Found existing installation: faiss-cpu 1.14.3\n",
            "Uninstalling faiss-cpu-1.14.3:\n",
            "  Would remove:\n",
            "    /usr/local/lib/python3.12/dist-packages/faiss/*\n",
            "    /usr/local/lib/python3.12/dist-packages/faiss_cpu-1.14.3.dist-info/*\n",
            "    /usr/local/lib/python3.12/dist-packages/faiss_cpu.libs/libgfortran-83c28eba.so.5.0.0\n",
            "    /usr/local/lib/python3.12/dist-packages/faiss_cpu.libs/libgomp-e985bcbb.so.1.0.0\n",
            "    /usr/local/lib/python3.12/dist-packages/faiss_cpu.libs/libopenblaso-r0-d77a1985.3.15.so\n",
            "    /usr/local/lib/python3.12/dist-packages/faiss_cpu.libs/libquadmath-2284e583.so.0.0.0\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled faiss-cpu-1.14.3\n",
            "Found existing installation: pypdf 6.14.2\n",
            "Uninstalling pypdf-6.14.2:\n",
            "  Would remove:\n",
            "    /usr/local/lib/python3.12/dist-packages/pypdf-6.14.2.dist-info/*\n",
            "    /usr/local/lib/python3.12/dist-packages/pypdf/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled pypdf-6.14.2\n",
            "Found existing installation: python-docx 1.2.0\n",
            "Uninstalling python-docx-1.2.0:\n",
            "  Would remove:\n",
            "    /usr/local/lib/python3.12/dist-packages/docx/*\n",
            "    /usr/local/lib/python3.12/dist-packages/python_docx-1.2.0.dist-info/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled python-docx-1.2.0\n",
            "Found existing installation: streamlit 1.60.0\n",
            "Uninstalling streamlit-1.60.0:\n",
            "  Would remove:\n",
            "    /usr/local/bin/streamlit\n",
            "    /usr/local/lib/python3.12/dist-packages/streamlit-1.60.0.dist-info/*\n",
            "    /usr/local/lib/python3.12/dist-packages/streamlit/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled streamlit-1.60.0\n",
            "Found existing installation: python-dotenv 1.2.2\n",
            "Uninstalling python-dotenv-1.2.2:\n",
            "  Would remove:\n",
            "    /usr/local/bin/dotenv\n",
            "    /usr/local/lib/python3.12/dist-packages/dotenv/*\n",
            "    /usr/local/lib/python3.12/dist-packages/python_dotenv-1.2.2.dist-info/*\n",
            "Proceed (Y/n)? Y\n",
            "  Successfully uninstalled python-dotenv-1.2.2\n"
          ]
        }
      ],
      "source": [
        "!pip uninstall -y langchain langchain-openai langchain-community faiss-cpu pypdf python-docx  streamlit python-dotenv"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip cache purge"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ARbhgdlTJaGu",
        "outputId": "3595cac3-9d9a-48e8-b338-2054171c96e0"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Files removed: 78\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q \\\n",
        "    langchain --no-cache-dir \\\n",
        "    langchain-google-genai \\\n",
        "    google-generativeai \\\n",
        "    langchain_community \\\n",
        "    faiss-cpu \\\n",
        "    langchain-text-splitters \\\n",
        "    pymupdf \\\n",
        "    langgraph"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C7EFkZ2jH0zW",
        "outputId": "b2149219-038e-4d6d-c328-81e46b2d315b"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/139.6 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m139.6/139.6 kB\u001b[0m \u001b[31m8.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/72.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m72.2/72.2 kB\u001b[0m \u001b[31m280.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.4/2.4 MB\u001b[0m \u001b[31m52.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m18.5/18.5 MB\u001b[0m \u001b[31m188.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m25.7/25.7 MB\u001b[0m \u001b[31m276.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pathlib import Path\n",
        "from langchain_community.document_loaders import PyMuPDFLoader\n",
        "\n",
        "docs = []\n",
        "\n",
        "for documento in Path(\"/content/\").glob(\"*.pdf\"):\n",
        "    try:\n",
        "        loader = PyMuPDFLoader(str(documento))\n",
        "        docs.extend(loader.load())\n",
        "        print(f\"Archivo cargado: {documento.name}\")\n",
        "    except Exception as e:\n",
        "        print(f\"Error cargando archivo: {documento.name}: {e}\")\n",
        "\n",
        "print(f\"Total de documentos cargados: {len(docs)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eacfuImDGkMB",
        "outputId": "dbedb09a-c766-485a-8fcb-d56104d74fe8"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_7307/3183474.py:2: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.\n",
            "  from langchain_community.document_loaders import PyMuPDFLoader\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archivo cargado: Política de Teletrabajo (Home Office).pdf\n",
            "Archivo cargado: Política de Uso de Correo Electrónico y Seguridad de la Información.pdf\n",
            "Archivo cargado: Política de Reembolsos (Viajes y Gastos).pdf\n",
            "Total de documentos cargados: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(len(docs))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TJenIcxkHFLN",
        "outputId": "b5b62a46-6580-40c1-8b4f-ac7efccd0ba7"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Dividir el texto**"
      ],
      "metadata": {
        "id": "f72T5bnwKAns"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
        "\n",
        "splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)\n",
        "docs_splits = splitter.split_documents(docs)"
      ],
      "metadata": {
        "id": "k7CWKZnAOmZp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Crear Embeddings**"
      ],
      "metadata": {
        "id": "kNq1NtNkKU_h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import userdata\n",
        "\n",
        "GEMINI_API_KEY=userdata.get(\"GEMINI_API_KEY\")"
      ],
      "metadata": {
        "id": "ROPwuEGFLRi4"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_google_genai import GoogleGenerativeAIEmbeddings\n",
        "\n",
        "modelo_embeddings = GoogleGenerativeAIEmbeddings(\n",
        "    model = \"models/gemini-embedding-001\",\n",
        "    google_api_key=GEMINI_API_KEY\n",
        ")"
      ],
      "metadata": {
        "id": "NdcERBc3KP-5"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.vectorstores import FAISS\n",
        "\n",
        "vectorstore = FAISS.from_documents(docs_splits, modelo_embeddings)\n",
        "\n",
        "retriever = vectorstore.as_retriever(\n",
        "    search_type=\"similarity_score_threshold\",\n",
        "    search_kwargs={\"score_threshold\": 0.3, \"k\": 4}\n",
        ")\n",
        "\n",
        "vectorstore.save_local(\"vectorstore\")"
      ],
      "metadata": {
        "id": "kGlzAb2jOVNf"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.vectorstores import FAISS\n",
        "\n",
        "vectorstore = FAISS.from_documents(docs_splits, modelo_embeddings)\n",
        "\n",
        "retriever = vectorstore.as_retriever(\n",
        "    search_type=\"similarity_score_threshold\",\n",
        "    search_kwargs={\"score_threshold\": 0.3, \"k\": 4}\n",
        ")"
      ],
      "metadata": {
        "id": "Z4CveiZkLIU7"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_google_genai import ChatGoogleGenerativeAI\n",
        "\n",
        "llm = ChatGoogleGenerativeAI(\n",
        "    model=\"gemini-2.5-flash\",\n",
        "    temperature=0.2,\n",
        "    google_api_key=GEMINI_API_KEY\n",
        ")"
      ],
      "metadata": {
        "id": "LwrEWhduQr7u"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "from langchain_core.runnables import RunnablePassthrough\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "\n",
        "prompt_rag = ChatPromptTemplate(\n",
        "    [\n",
        "        (\"system\",\n",
        "            \"\"\"Eres el especialista en RR.HH. de la empresa Excelence Desarrollo de Software.\n",
        "            Responde siempre utilizando los conocimientos del contexto que te fue pasado a ti.\n",
        "            Si no hay informacion sobre la pregunta en los datos, responde solo 'No lo se'.\n",
        "            \"\"\"\n",
        "        ),\n",
        "        (\"human\", \"Contexto: {context}\\nPregunta del empleado: {input}\")\n",
        "    ]\n",
        ")\n",
        "\n",
        "# Helper function to format documents for stuffing into the prompt\n",
        "def format_docs(docs):\n",
        "    return \"\\n\\n\".join(doc.page_content for doc in docs)\n",
        "\n",
        "# Re-implement create_stuff_documents_chain functionality using LCEL\n",
        "document_chain = (\n",
        "    {\n",
        "        \"context\": lambda x: format_docs(x[\"context\"]), # Takes list of docs, formats to string\n",
        "        \"input\": RunnablePassthrough() # Passes the original 'input' through\n",
        "    }\n",
        "    | prompt_rag\n",
        "    | llm\n",
        "    | StrOutputParser()\n",
        ")"
      ],
      "metadata": {
        "id": "Ik6SBWqHLv3Y"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def consultar(pregunta):\n",
        "\n",
        "    documentos = retriever.invoke(pregunta)\n",
        "\n",
        "    contexto = \"\\n\\n\".join(\n",
        "        [d.page_content for d in documentos]\n",
        "    )\n",
        "\n",
        "    mensajes = prompt_rag.format_messages(\n",
        "        context=contexto,\n",
        "        input=pregunta\n",
        "    )\n",
        "\n",
        "    respuesta = llm.invoke(mensajes)\n",
        "\n",
        "    return respuesta.content"
      ],
      "metadata": {
        "id": "vOQY8-UvRDsb"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while True:\n",
        "\n",
        "    p = input(\"Pregunta: \")\n",
        "\n",
        "    if p==\"salir\":\n",
        "        break\n",
        "\n",
        "    print(consultar(p))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O1WaGpbqRa49",
        "outputId": "70131460-ec97-4dac-a426-9e236cb19540"
      },
      "execution_count": 19,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Pregunta: Como informar las vacaciones?\n",
            "Las ausencias, incluyendo las solicitudes de vacaciones, deben gestionarse de la misma manera que si estuvieras trabajando en la oficina.\n",
            "Pregunta: Como informar los gastos reembolsables?\n",
            "Todos los gastos reembolsables deben ser presentados a través del sistema \"Gestión de Gastos\" antes del día 5 del mes siguiente. Es obligatorio adjuntar recibos o facturas legibles para todos los gastos, excepto la dieta diaria de viaje.\n",
            "Pregunta: salir\n"
          ]
        }
      ]
    }
  ]
}