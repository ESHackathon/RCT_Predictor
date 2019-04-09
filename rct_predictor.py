import sys

from robotsearch.robots import rct_robot


rct_clf = rct_robot.RCTRobot()


def main():
    for index, line in enumerate(open(sys.argv[1], mode='rt', encoding='utf-8')):
        splitted_line = line.rstrip("\r\n").split('\t')
        # skip blank lines
        if len(splitted_line) < 2:
            continue
        if index == 0:
            splitted_line.append("is_rct")
            print(("\t".join(splitted_line)))
        else:
            try:
                title = splitted_line[1]
                abstract = splitted_line[2]
                pred = rct_clf.predict({"title": title, "abstract": abstract, "use_ptyp": False}, filter_type="balanced", filter_class="svm_cnn")
                splitted_line.append(str(pred[0]["is_rct"]))
                print(("\t".join(splitted_line)))
            except:
                raise Exception("There's been a problem")


if __name__ == "__main__":
    main()
