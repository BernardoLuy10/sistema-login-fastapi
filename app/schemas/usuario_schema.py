
from pydantic import BaseModel, ConfigDict, EmailStr, Field
class CadastroUsuario(BaseModel):
    model_config = ConfigDict(extra="forbid") #Regra de validação para impedir que campos extras sejam enviados na requisição.
    nome: str = Field(min_length = 3, max_length = 50) #Regra de validação para o campo nome, que deve ter no mínimo 3 e no máximo 50 caracteres.
    email: EmailStr #Regra de validação para o campo email, que deve ser um email válido.
    senha: str = Field(min_length = 4, max_length = 12) #Regra de validação para o campo senha, que deve ter no mínimo 4 e no máximo 12 caracteres.