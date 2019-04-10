import sys

from robotsearch.robots import rct_robot
import csv


rct_clf = rct_robot.RCTRobot()


def main():
    with open(sys.argv[1]) as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        header = next(reader)
        header.append('is_rct')
        print("\t".join(header))
        for line in reader:
            if len(line) < 3:
                continue
            title = line[1]
            abstract = line[2]
            pred = rct_clf.predict({"title": title, "abstract": abstract, "use_ptyp": False}, filter_type="balanced", filter_class="svm_cnn")
            line.append(str(pred[0]["is_rct"]))
            print(("\t".join(line).replace('\n',' ')))


if __name__ == "__main__":
    main()
