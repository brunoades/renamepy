from distutils.core import setup
import py2exe
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import scan_base_folder
from utils.process_files import process_notidentified_pdf_files
import os
from pathlib import Path
from utils.pdf_to_lines import lines_from_pdf
from utils.process_files import process_notpdf_files
from datetime import datetime
from utils.get_cnpj import get_cnpj
from utils.process_files import process_file
import pdfplumber
import identify_file_department
import re
import mysql.connector
from db.db_config import mydb

setup(console=['renamefy.py'])