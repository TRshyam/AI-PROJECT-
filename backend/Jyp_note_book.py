from admin import administration
from nbformat import v4 as nbf
from nbformat import reads
from nbformat import writes



class ipynb:
    def create_notebook(name: str):
        notebook = nbf.new_notebook()
        filename = name + ".ipynb"
        with open(filename, 'w') as f:
            f.write(writes(notebook))

    def add_markdown_cell(self,filename: str, text: str):
        with open(filename, 'r') as f:
            contents = f.read()
            notebook = reads(contents,as_version=4)
        markdown_cell = nbf.new_markdown_cell(text)
        notebook['cells'].append(markdown_cell)
        with open(filename, 'w') as f:
            f.write(writes(notebook))

    def add_code_cell(filename: str):
        with open(filename, 'r') as f:
            contents = f.read()
            notebook = reads(contents, as_version=4)
        code_cell = nbf.new_code_cell()
        notebook['cells'].append(code_cell)
        with open(filename, 'w') as f:
            f.write(writes(notebook))

    def delete_cell(filename: str, cell_index: int):
        cell_index +=1
        with open(filename, 'r') as f:
            contents = f.read()
            notebook = reads(contents, as_version=4)
            
        if cell_index < len(notebook.cells):
            notebook.cells.pop(cell_index)
            
            with open(filename, 'w') as f:
                f.write(writes(notebook))
            print(f"Cell at index {cell_index} deleted successfully.")
        else:
            print("Invalid cell index. Cell not found.")

