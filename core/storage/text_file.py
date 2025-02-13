from time import time
import os
class TextSaver:

    @staticmethod
    def to_text(text:str, loc:str, filename:str):
        """
        save `text` to a file with extension .txt in location `loc`

        text: to save to file without extension
        loc: location to save to
        filename: name of textfile to save
        """
        filename_ext = f"{loc}\\{filename}.txt"
        
        try:
            with open(filename_ext, 'w') as f:
                f.write(text)
        except Exception as e:
            print("-----------\nFile write failed\n-----------")
            return False
        print("-----------\nFile successfully saved\n-----------")
        return True
    
    @staticmethod
    def to_file(text_list:list, loc:str, folder_name:str):
        """
        save to a folder a file for every element in 'text_list'

        text: to save to file without extension
        loc: location to save to
        filename: name of textfile to save
        """
        folder_direc = f"{loc}\\{folder_name}"
        if not os.path.exists(folder_direc):
            os.makedirs(folder_direc)

        for text in text_list:
            filename = f"{folder_direc}\\{text.split("\n")[0]}.txt"
            with open(filename, 'w') as f:
                try:
                    f.write(text)
                except Exception as e:
                    print(f"-----------\nFile write `{filename}` failed\n-----------")
        
        print("-----------\nFile successfully saved\n-----------")
        return True
    
