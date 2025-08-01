#!/bin/bash
# Script para correção automática de fotos
# Uso: ./corrigir_fotos.sh [diretório_das_fotos] [diretório_de_saída]

echo "=== Corretor de Fotos Automático ==="
echo ""

# Define diretórios padrão
ENTRADA=${1:-"hackable/users"}
SAIDA=${2:-"fotos_corrigidas"}

# Verifica se o diretório de entrada existe
if [ ! -d "$ENTRADA" ]; then
    echo "Erro: Diretório '$ENTRADA' não encontrado!"
    echo "Uso: $0 [diretório_das_fotos] [diretório_de_saída]"
    exit 1
fi

echo "Processando fotos do diretório: $ENTRADA"
echo "Salvando fotos corrigidas em: $SAIDA"
echo ""

# Executa o corretor de fotos
python3 photo_corrector.py "$ENTRADA" -o "$SAIDA"

echo ""
echo "=== Processamento concluído! ==="
echo "Fotos corrigidas salvas em: $SAIDA"

# Lista as fotos processadas
if [ -d "$SAIDA" ]; then
    echo ""
    echo "Fotos corrigidas:"
    ls -la "$SAIDA"/*.jpg 2>/dev/null || echo "Nenhuma foto encontrada no diretório de saída."
fi

echo ""
echo "Para processar uma foto específica:"
echo "python3 photo_corrector.py caminho/para/foto.jpg -o foto_corrigida.jpg"
echo ""
echo "Para ajustes manuais:"
echo "python3 photo_corrector.py foto.jpg --manual -b 1.3 -c 1.2 -s 1.1"