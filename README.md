
# Word to PDF

Transforme seus arquivos Word em PDF com uma interface simples e direta.

---

## 🧾 Visão geral

Este projeto converte documentos do Microsoft Word (como `.docx`) para o formato PDF. É ideal para quem precisa automatizar a transformação de documentos editáveis em arquivos estáticos para distribuição ou arquivamento.

Atualmente, o repositório contém um arquivo principal: `WordToPDF.py`. :contentReference[oaicite:0]{index=0}

---

## Funcionalidades

- Conversão de documento Word para PDF.  
- Simplicidade: poucas dependências, uso direto.  
- Código em Python (100 % da base) :contentReference[oaicite:1]{index=1}  
- Sem interface gráfica complexa — fácil adaptação para scripts ou integração.  

---

## Requisitos

- Python (versão compatível — idealmente Python 3.x)  
- Bibliotecas necessárias (dependendo da implementação de `WordToPDF.py`; por exemplo, `python-docx`, `reportlab` ou outras)  
- Ambiente operacional com suporte a manipulação de arquivos  

> ⚠️ *Se o script depender de ferramentas externas (como LibreOffice, `docx2pdf`, ou outros utilitários), inclua essas dependências no seu ambiente.*

---

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/GiPalotta/word-to-pdf.git
   cd word-to-pdf


2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # no Linux/macOS
   venv\Scripts\activate      # no Windows
   ```

3. Instale as dependências (caso haja um `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

Supondo que o script principal seja `WordToPDF.py`, um exemplo de execução:

```bash
python WordToPDF.py input.docx output.pdf
```

Ou, se implementado como função dentro de outro script:

```python
from WordToPDF import convert

convert("entrada.docx", "saida.pdf")
```

Adapte conforme a assinatura real da função no código.

---

## Exemplos

| Entrada                             | Saída                               |
| ----------------------------------- | ----------------------------------- |
| `documento_exemplo.docx`            | `documento_exemplo.pdf`             |
| Documento com imagens, tabelas etc. | PDF renderizado mantendo formatação |

Você pode também incluir um ou mais arquivos de exemplo dentro do repositório (ex: `examples/`) para demonstração.

---

## Limitações e melhorias

* A conversão pode não replicar **100 %** todos os estilos (margens, fontes especiais, layouts complexos).
* Dependendo da biblioteca usada, pode haver limitação com arquivos `.doc` antigos ou funcionalidades avançadas do Word.
* Não há (ainda) suporte a processamento em lote ou interface Web (a menos que você adicione).
* Melhorias possíveis:

  * Suporte a múltiplos arquivos com um único comando
  * Interface gráfica ou web
  * Integração com serviços de nuvem

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

* Abrir **issues** relatando bugs ou sugerindo melhorias
* Enviar **pull requests** com correções ou novas funcionalidades
* Comentar no código, documentar casos de uso ou criar exemplos

Antes de submeter alterações, sugiro seguir:

* Rodar testes (se tiver)
* Manter consistência de estilo de código
* Atualizar a documentação conforme necessário

---

Se quiser, posso gerar para você uma versão em inglês ou já com badges (stars, build, licença), ou até sugerir melhorias no próprio `WordToPDF.py`. Você quer que eu envie isso também?
