
import sys

from robotsearch.robots import rct_robot


rct_clf = rct_robot.RCTRobot()


def main():
    with open(sys.argv[1]) as f:
        for line in f:
            splitted_line = line.replace("\n", "").split('\t')
            title = splitted_line[1]
            abstract = splitted_line[2]
            pred = rct_clf.predict({"title": title, "abstract": abstract, "use_ptyp": False}, filter_type="balanced", filter_class="svm_cnn")
            splitted_line.append(str(pred[0]["is_rct"]))
            print("\t".join(splitted_line))


if __name__ == "__main__":
    main()
