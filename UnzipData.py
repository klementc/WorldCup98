import os
import fnmatch


def main():

    print("Start to unzip file")

    pattern = '*.gz'
    root_path = './input'
    tool_path = './ita_public_tools/'

    print("make tools")
    os.system("cd "+tool_path+" && make")
    print("tools built")

    list_dirs = os.walk(root_path)
    for root, dirs, files in list_dirs:
        for f in fnmatch.filter(files, pattern):
            cmd = 'gzip -dc '+root_path+'/'+f + ' | ' + tool_path +'bin/recreate ' + tool_path + 'state/object_mappings.sort > '+tool_path+'output/' + f[:-3] + '.log'
            print(cmd)
            os.system(cmd)


if __name__ == "__main__":
    main()
