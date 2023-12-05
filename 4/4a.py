from absl import app

def main(argv):
    filename = argv[1]
    print(filename)


if __name__ == '__main__':
    app.run(main)