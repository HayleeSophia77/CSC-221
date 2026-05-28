import os
import sys
import streamlit.web.cli as stcli

def main():
    # Disable development mode so it uses the normal 8501 server
    os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"

    # When bundled by PyInstaller, sys._MEIPASS points to the temp folder
    if getattr(sys, "frozen", False):
        base_dir = sys._MEIPASS  # type: ignore[attr-defined]
    else:
        base_dir = os.path.dirname(__file__)

    script_path = os.path.join(base_dir, "main.py")
    script_path = os.path.abspath(script_path)

    # Run: streamlit run main.py
    sys.argv = [
        "streamlit",
        "run",
        script_path,
    ]

    stcli.main()

if __name__ == "__main__":
    main()