from logging.config import fileConfig
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import engine_from_config
from sqlalchemy import pool, MetaData

from alembic import context
from sqlmodel import create_engine, SQLModel

# 載入環境變數
load_dotenv()

# 匯入配置系統
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.shared.config.config import get_settings

# 添加專案根目錄到 Python 路徑
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

# 導入所有模型以確保 Alembic 能偵測到它們
from src.auth.models import Account, EmailVerification, User, UserWord
from src.course.models import (
    Situation, Chapter, Sentence
)
from src.practice.models import *
from src.therapist.models import TherapistProfile, TherapistClient
from src.pairing.models import PairingToken
from src.verification.models import TherapistApplication, UploadedDocument
from src.chat.models import ChatMessage
from src.ai_analysis.models import AIAnalysisTask, AIAnalysisResult, TaskStatus

# 設置命名約定
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# 應用命名約定到 metadata
target_metadata = SQLModel.metadata
target_metadata.naming_convention = convention

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    """Get the database URL from configuration system."""
    # Ensure the database URL is correctly fetched from environment variables
    settings = get_settings()
    result = settings.database_url
    print(f"Using database URL: {result}")
    return result

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # connectable = engine_from_config(
    #     config.get_section(config.config_ini_section, {}),
    #     prefix="sqlalchemy.",
    #     poolclass=pool.NullPool,
    # )

    connectable = create_engine(get_url())

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
