# ┌─────────────┐
# │ Vorx Engine │
# │─────────────│
# │ Classes +   │
# │ Console CLI │
# └─────────────┘

try:
    from vorx.cli import main
except ImportError:
    from .cli import main
except Exception as e:
    print(f"Error importing cli: {e}")

main()