# Corretor de Fotos Automático

Uma ferramenta completa para correção e aprimoramento automático de fotos com diversos filtros e ajustes.

## 📋 Funcionalidades

- **Correção Automática**: Aplica automaticamente melhorias em brilho, contraste, saturação, nitidez e redução de ruído
- **Ajustes Manuais**: Permite controle preciso sobre cada parâmetro
- **Processamento em Lote**: Processa múltiplas fotos de uma vez
- **Formatos Suportados**: JPG, JPEG, PNG, BMP, TIFF, GIF

## 🚀 Como Usar

### Método Simples (Script em Português)

```bash
# Processar todas as fotos do diretório padrão
./corrigir_fotos.sh

# Especificar diretórios personalizados
./corrigir_fotos.sh diretorio_origem diretorio_destino
```

### Método Avançado (Python)

#### Correção Automática

```bash
# Processar um diretório inteiro
python3 photo_corrector.py hackable/users/ -o fotos_corrigidas

# Processar uma foto específica
python3 photo_corrector.py foto.jpg -o foto_corrigida.jpg

# Ajustar intensidade da correção (0.0 a 1.0)
python3 photo_corrector.py foto.jpg --intensity 0.5
```

#### Ajustes Manuais

```bash
# Ajustes específicos
python3 photo_corrector.py foto.jpg --manual -b 1.3 -c 1.2 -s 1.1 --sharpen 1.4

# Parâmetros:
# -b: Brilho (padrão: 1.2)
# -c: Contraste (padrão: 1.2) 
# -s: Saturação (padrão: 1.2)
# --sharpen: Nitidez (padrão: 1.5)
```

## 📊 Exemplos de Uso

### Exemplo 1: Correção Automática de Todas as Fotos
```bash
./corrigir_fotos.sh
```

### Exemplo 2: Fotos Muito Escuras
```bash
python3 photo_corrector.py foto_escura.jpg --manual -b 1.5 -c 1.3
```

### Exemplo 3: Fotos Desbotadas
```bash
python3 photo_corrector.py foto_desbotada.jpg --manual -s 1.4 -c 1.2
```

### Exemplo 4: Fotos Borradas
```bash
python3 photo_corrector.py foto_borrada.jpg --manual --sharpen 2.0
```

## 📁 Estrutura de Arquivos

```
workspace/
├── photo_corrector.py       # Ferramenta principal de correção
├── corrigir_fotos.sh       # Script simplificado em português
├── hackable/users/         # Fotos originais
│   ├── admin.jpg
│   ├── pablo.jpg
│   ├── smithy.jpg
│   ├── 1337.jpg
│   └── gordonb.jpg
├── fotos_corrigidas/       # Fotos processadas automaticamente
└── corrected_photos/       # Fotos processadas manualmente
```

## ⚙️ Configurações Avançadas

### Parâmetros de Correção Automática

A correção automática aplica os seguintes ajustes baseados na intensidade:

- **Brilho**: 1.0 + intensidade × 0.1
- **Contraste**: 1.0 + intensidade × 0.2
- **Saturação**: 1.0 + intensidade × 0.15
- **Nitidez**: 1.0 + intensidade × 0.25
- **Redução de Ruído**: Filtro gaussiano + máscara de nitidez
- **Auto-contraste**: Melhoria automática do alcance dinâmico

### Dicas de Uso

1. **Para fotos antigas ou escaneadas**: Use intensidade baixa (0.3-0.5)
2. **Para fotos digitais modernas**: Use intensidade média (0.6-0.8)
3. **Para correções extremas**: Use ajustes manuais específicos

## 🔧 Requisitos

- Python 3.x
- PIL/Pillow
- NumPy

## 📝 Exemplos de Resultados

As fotos processadas terão:
- ✅ Melhor brilho e contraste
- ✅ Cores mais vibrantes
- ✅ Maior nitidez
- ✅ Redução de ruído
- ✅ Melhor alcance dinâmico

## 🆘 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'PIL'"
```bash
sudo apt update && sudo apt install -y python3-pil python3-numpy
```

### Erro: "Permission denied"
```bash
chmod +x photo_corrector.py
chmod +x corrigir_fotos.sh
```

### Para ver todas as opções disponíveis:
```bash
python3 photo_corrector.py --help
```

---

**Nota**: Este corretor foi desenvolvido para melhorar automaticamente a qualidade visual das suas fotos. Para melhores resultados, experimente diferentes configurações baseadas no tipo e condição das suas imagens.