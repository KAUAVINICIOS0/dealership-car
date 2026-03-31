# Dealership Car

Projeto de aprendizado com Django. Nada gráfico foi feito — está completamente cru, sem estilização, sem frontend elaborado. O objetivo é apenas praticar os conceitos básicos do Django com duas entidades relacionadas.

## Sobre o projeto

O projeto possui duas entidades principais com relacionamento **one-to-many**:

- **Brand** (Marca) — uma marca pode ter vários carros
- **Car** (Carro) — cada carro pertence a uma marca

### Modelos

**Brand**
| Campo | Tipo |
|-------|------|
| name | CharField(100) |
| created_at | DateTimeField (auto) |
| updated_at | DateTimeField (auto) |

**Car**
| Campo | Tipo |
|-------|------|
| name | CharField(100) |
| year | IntegerField (opcional) |
| color | CharField(50) (opcional) |
| brand | ForeignKey → Brand (CASCADE) |
| data_created | DateTimeField (auto) |
| data_updated | DateTimeField (auto) |

### Rotas disponíveis

**Brands** (`/brands/`)
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/brands/` | Lista todas as marcas |
| POST | `/brands/create/` | Cria uma nova marca |
| POST | `/brands/delete/<id>` | Deleta uma marca |
| POST | `/brands/update/<id>` | Atualiza uma marca |

**Cars** (`/cars/`)
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/cars/` | Lista todos os carros |
| POST | `/cars/create/` | Cria um novo carro |
| POST | `/cars/delete/<id>` | Deleta um carro |
| POST | `/cars/update/<id>` | Atualiza um carro |

## Como rodar

O projeto usa [uv](https://docs.astral.sh/uv/) como gerenciador de pacotes e ambiente virtual.

### Pré-requisitos

- Python 3.13+
- uv instalado (`pip install uv` ou via script oficial)

### Passos

```bash
# Clonar o repositório
git clone <url-do-repo>
cd dealership

# Instalar dependências
uv sync

# Aplicar as migrations
uv run python manage.py migrate

# Rodar o servidor de desenvolvimento
uv run python manage.py runserver
```

Acesse em `http://127.0.0.1:8000`.

### Criar superusuário (opcional)

```bash
uv run python manage.py createsuperuser
```


