import sys

from core.config import load_settings


def main():
    # Загрузи здесь .env (load_dotenv), путь строй от __file__,
    # чтобы он находился откуда бы ни запускали программу.

    settings = load_settings()

    # Выбери здесь, что запускать, например по аргументу:
    #   python -m core gui  -> gui.app.main()
    #   python -m core web  -> web.app.main(settings)
    # Аргументы лежат в sys.argv.
    pass


if __name__ == "__main__":
    main()
