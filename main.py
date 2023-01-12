import sys

from os.path import exists

# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容# を逆にした新しいファイルを作成します。


def reverseCmd(contents, output):
    reversedList = list(reversed(contents))
    output.write(" ".join(reversedList))

# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。


def copyCmd(contents, output):
    output.write(contents)

# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製され# た内容を inputpath に n 回複製します。


def duplicateContents(i, contents, n):
    i.write(contents * n)


def replaceString(i, contents, needle, replacement):
    i.truncate(0)
    i.write(contents.replace(needle, replacement))


def main():
    command = sys.argv[1]
    inputpath = sys.argv[2]

    if not exists(inputpath):
        print("input file is not exist")
        sys.exit(1)

    with open(inputpath, "r+") as i:
        contents = i.read()

        if command == "reverse" or command == "copy":
            output_path = sys.argv[3]

            if inputpath == output_path:
                print("inputfile and outputfile must be different")
                sys.exit(1)

            with open(output_path, "a") as f:
                if command == "reverse":
                    # print("create outputPath")
                    reverseCmd(contents, f)
                elif command == "copy":
                    # print("copy outputPath")
                    copyCmd(contents, f)

        elif command == "duplicate-contents":
            count = int(sys.argv[3])
            duplicateContents(i, contents, count)

        elif command == "replace-string":
            substitute = sys.argv[3]
            replacement = sys.argv[4]
            replaceString(i, contents, substitute, replacement)


if __name__ == "__main__":
    main()
