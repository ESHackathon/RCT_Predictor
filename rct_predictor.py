import sys

from robotsearch.robots import rct_robot
import csv


rct_clf = rct_robot.RCTRobot()


def main():
    result = []
    with open(sys.argv[1],'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        header = next(reader)
        header.append('is_rct')
        result.append(header)
        for line in reader:
            if len(line) < 3:
                continue
            title = line[1]
            abstract = line[2]
            pred = rct_clf.predict({"title": title, "abstract": abstract, "use_ptyp": False}, filter_type="balanced", filter_class="svm_cnn")
            line.append(str(pred[0]["is_rct"]))
            line = [x.replace('\n',' ') for x in line]
            result.append(line)
    with open(sys.argv[2],'w+') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        for r in result:
            writer.writerow(r)


if __name__ == "__main__":
    main()
