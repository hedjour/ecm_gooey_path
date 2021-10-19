#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Main module to run the right script with the given options
"""

import argparse
from os import path as ptah
import yaml
from gooey import Gooey, GooeyParser

BOOM = r"""
     _.-^^---....,,--
 _--                  --_
<                        >
|                        |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
______.,-#%&$@%#&#~,._____
    KAA-BOOOOOOM -
Oops your data have disappeared
    OH good news 
You missed to give me your data
"""
data = ptah.dirname(ptah.realpath(__file__))

@Gooey( program_name= "med_to_csv",
        image_dir=f'{data}/img/',
        monospace_display=True,
        default_size=(900,650),
        header_show_title = False,
        header_height=100,
        menu=[{
            'name': 'Help',
            'items': [{
                    'type': 'Link',
                    'menuTitle': 'Documentation',
                    'url': 'https://www.readthedocs.com/foo'
                }]
        }]
    )
def main() :
    """main function, to display a select file/directory window"""
    parser = GooeyParser(prog="med_to_csv", 
                         formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                         description = """This software is just a simple soft to repeat an error
""")
    parser.add_argument("option1", type=str, 
                        help= """Path to option config file.""", widget="FileChooser")
    parser.add_argument("output", type=str,   
                        help= """Path output of the csv file""", widget="FileSaver")
    parser.add_argument("-p","--path", type=str,
                        help="""
Option to indicate a path to the group directory which contains data files from : Medassociate
                        """, widget="DirChooser")
    parser.add_argument("-f", "--file", type=str,
                        help="""Option to indicate a unique file and not a directory.""",
                        widget="FileChooser", 
                        gooey_options={ 'validator': {
                            'test': 'user_input is None and args.path is None',
                            'message': 'Choose a file or a directory'
                            } })
    # parser.add_argument("-v","--verbose", type=str, help= """Verbose mode""")

    args = parser.parse_args()
    #load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    if args.file is not None:
        df_res = file.read_path(args.path, opt_dic)
        df_res.to_csv(args.file, index=False)
    elif args.path is not None :
        print(f"expe.main(path={args.path}, output_file = {args.output}, opt=opt_dic)")
    else:
        raise Exception(BOOM)

if __name__ == "__main__":
    main()
