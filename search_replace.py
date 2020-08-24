from sys import argv
import os

def search_replace(replace, path):
    """Replace search with replace in all filenames
    and file contents in directory path.
    @type   search: string
    @param  search: The old string.
    @type   replace: string
    @param  replace: The new string.
    @type   path: string
    @param  path: The path in which files area.
    @rtype: boolean
    @returns: True or False. Also print a msg to the console.
    """
    # dirs and files to exculded
    exclude = set(['.git', 'data', '__init__.py', '.coveragerc', '.gitignore', 'Jenkinsfile', 'MANIFEST.in', 'setup.cfg', 'setup.py'])
    
    if not os.path.exists(path):
        print ('Path does not exist')
        return False
    for dirpath, dirs, files in os.walk(path):
        # exclude dirs/files
        dirs[:] = list(filter(lambda x: not x in exclude, dirs))
        files = list(filter(lambda x: not x in exclude, files))

        for filename in files:
            # replace contents
            indata = open(os.path.join(dirpath, filename)).read()
            search = 'placeholder'
            if search in indata:
                new = indata.replace(search, replace)
                output = open(os.path.join(dirpath, filename), "w", encoding='utf-8')
                output.write(new)
                
            # replace in filename
            if search in filename:
                os.rename(
                    os.path.join(dirpath, filename),
                    os.path.join(dirpath, filename.replace(search, replace))
                )
    return True

script, replace, src_path = argv

search_replace(replace, src_path)
