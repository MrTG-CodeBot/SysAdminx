import docx2pdf
from docx2pdf import convert

class Docs2pdf:
  def __init__(self):
    pass
    
  def convert2pdf(self,inputpath:str,outputpath:str) -> str or None:
    try:
      return convert(inputpath, outputpath)
    except Exception as e:
      print(f"An error occured while converting to pdf: {e}")
      return None

