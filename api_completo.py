from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from produtos import lista_produtos

app = FastAPI()

# Modelo para validação de dados
class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    estoque: int

# 🔍 Ler todos os produtos
@app.get("/")
def listar_produtos():
    return {"lista_produtos": lista_produtos}

# 📌 Adicionar um novo produto
@app.post("/produtos/")
def adicionar_produto(produto: Produto):
    for p in lista_produtos["produtos"]:
        if p["id"] == produto.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    
    lista_produtos["produtos"].append(produto.dict())
    return {"mensagem": "Produto adicionado com sucesso"}

# 📝 Atualizar um produto
@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto: Produto):
    for index, p in enumerate(lista_produtos["produtos"]):
        if p["id"] == produto_id:
            lista_produtos["produtos"][index] = produto.dict()
            return {"mensagem": "Produto atualizado com sucesso"}
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

# ❌ Remover um produto
@app.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int):
    for index, p in enumerate(lista_produtos["produtos"]):
        if p["id"] == produto_id:
            del lista_produtos["produtos"][index]
            return {"mensagem": "Produto removido com sucesso"}
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
