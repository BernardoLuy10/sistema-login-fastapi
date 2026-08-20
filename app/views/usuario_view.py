from fastapi import APIRouter, HTTPException, status
from app.controllers.usuario_controller import(
    EmailJaCadastradoError, cadastrar_novo_usuario
)
from app.schemas.usuario_schema import CadastroUsuario

router = APIRouter( #Cria um roteador para agrupar as rotas relacionadas a usuários, facilitando a organização e manutenção do código.
    prefix="/usuarios",#Define um prefixo para todas as rotas deste roteador, ou seja, todas as rotas definidas aqui começarão com "/usuarios".
    tags=["Usuários"]#identifica o grupo de rotas relacionadas a usuários na documentação automática do FastAPI.
)

@router.post("", status_code=status.HTTP_201_CREATED)
def cadastrar_usuario(usuario: CadastroUsuario):
    try:
        return cadastrar_novo_usuario(
            nome=usuario.nome,
            email=str(usuario.nome),
            senha=usuario.senha
        )
    except EmailJaCadastradoError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-mail já cadastrado."
        )

