import sys

from robotsearch.robots import rct_robot
import json


rct_clf = rct_robot.RCTRobot()


def predict(infile, outfile):
    with open(infile,'r') as jsonfile:
        in_data = json.load(jsonfile)
    for j in in_data:
        if 'title' not in j or 'abstract' not in j:
            j['is_rct'] = 'missing title and/or abstract'
            continue
        pred = rct_clf.predict({"title": j['title'], "abstract": j['abstract'], "use_ptyp": False}, filter_type="balanced", filter_class="svm_cnn")
        j['is_rct'] = str(pred[0]["is_rct"])
    with open(outfile,'w+') as out:
       json.dump(in_data,out)



if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    predict(infile,outfile)
