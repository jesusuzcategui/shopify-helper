import src.load as carga
import src.menu.render as menu

if __name__ == '__main__':
    try:
        carga.init_load()
    except KeyboardInterrupt:
        pass
    finally:
        menu.render()