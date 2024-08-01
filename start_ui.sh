#!/usr/bin/env bash
export PYTHONPATH=`pwd`
UI_PORT=${UI_PORT:-8282}
streamlit run ui/ui_app.py --server.port "${UI_PORT}"
